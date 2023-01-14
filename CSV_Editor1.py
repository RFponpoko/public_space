# -*- coding: utf-8 -*-

import os
import csv
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

G_DEBUG = False

class CsvEditor:
    
    def __init__(self):
        
        self.root = None      # root window
        self.data = []        # data of csv file loaded
        self.tree = None      # ttk.Treeview table for csv data loaded

    def start(self):

        self.call_root_window()
        self.call_csv_widget()
        self.call_treeview_widget()
        self.call_command_widget()
        self.root.mainloop()

    def call_root_window(self):
        """
        create root window
        """
        self.root = tk.Tk()
        self.root.geometry('1200x800')
        self.root.title('CsvEditor')

    def call_csv_widget(self):
        """
        a widget for reading a csv file
        """
        # creating a frame for the widget
        self.csv_frame = tk.Frame(self.root, relief="ridge", bd=3)
        self.csv_frame.pack(fill=tk.BOTH, padx=5, pady=5)

        # making a label
        self.file_name = tk.Label(self.csv_frame, text='file name')
        self.file_name.pack(side=tk.LEFT)
        
        # creating an input field to identify the file-path of the csv file you want to read
        self.entry_field = tk.Entry(self.csv_frame)
        self.entry_field.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # file dialog button
        self.file_path_bottom = tk.Button(self.csv_frame, text='...', command=lambda: self.set_path(self.entry_field))
        self.file_path_bottom.pack(side=tk.LEFT)

        # read the csv file and generate data for Treeview
        self.file_read_bottom = tk.Button(self.csv_frame, text='read', command=lambda: self.read_csv(self.entry_field.get()))
        self.file_read_bottom.pack(side=tk.LEFT)
        
        self.save_bottom  = tk.Button(self.csv_frame, text='save', command=self.save_csv)
        self.save_bottom.pack(side=tk.LEFT)
        
    def call_treeview_widget(self):
        """
        call ttk.Treeview
        """
        # widget, generate a frame
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.tree_frame.columnconfigure(0, weight=1)
        self.tree_frame.rowconfigure(0, weight=1)

        # generate a treeview for a CSV file
        self.tree = ttk.Treeview(self.tree_frame, show='headings')
        self.tree.column('#0', width=50, stretch=tk.NO, anchor=tk.E)
        self.tree.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        
        # command binding
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # scrollbar for x axis
        hscrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=lambda f, l: hscrollbar.set(f, l))
        hscrollbar.grid(row=1, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

        # scrollbar for y axis
        vscrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vscrollbar.set)
        vscrollbar.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)

    # for editing the table (current implementation is just selecting a row and show data of the row)
    def on_tree_select(self, event):
        for item in self.tree.selection():
            item_value = self.tree.item(item,'values')
            _ = list(item_value)
            
            if(G_DEBUG):
                print(f'_ = {_}')
            
            for i, data in enumerate(_):
                if(G_DEBUG):
                    print(f'i = {i}')
                    print(f'type(i) = {type(i)}')
                    print(f'data = {data}')
                    print(f'type(data) = {type(data)}')
                # self.edit_entry[i].delete(0, tk.END)
                # self.edit_entry[i].insert(0, data)
                print(f'i & data = {i} and {data}')
                self.entry_var[i].set(data)
                
    def set_path(self, entry_field):
        # clear the content of tk.Entry
        entry_field.delete(0, tk.END)

        # get the absolute path of the current python module
        abs_path = os.path.abspath(os.path.dirname(__file__))

        # call the function of file dialog using the absolute path
        file_path = filedialog.askopenfilename(
            title="Open CSV file",
            filetypes=[("CSV file", ".csv")],
            initialdir=abs_path
            )

        # insert the selected data into tk.Entry
        entry_field.insert(tk.END, str(file_path))

    def read_csv(self, file_path):
        """
        read csv data and store it in self.data
        """
        # read csv file and put the content to self.data
        with open(file_path) as fp:
            _ = csv.reader(fp)
            self.data = [row for row in _]
        
        self.show_csv()

    def show_csv(self):
        """
        to apply content of the csv loaded into ttk.Treeview
        """
        # clear the current content of the Treeview
        for _ in self.tree.get_children():
            self.tree.delete(_)
        
        # to add column number to the Treeview
        self.tree['column'] = np.arange(np.array(self.data).shape[1]).tolist()

        # update column header information
        for i in self.tree['column']:
            self.tree.column(i, width=100, anchor=tk.E)
            self.tree.heading(i, text=str(i))
        
        # show the content of the csv and row numbers
        for i, row in enumerate(self.data, 0):
            self.tree.insert('', 'end', text=i, values=row)

        column_list = self.tree['column']

        for x in self.edit_name_frame.winfo_children():
            x.destroy()
        
        for x in self.edit_frame.winfo_children():
            x.destroy()
        
        self.call_command_widget(False)
        
        self.edit_label = []
        self.edit_entry = []
        
        if (G_DEBUG):
            print(f'self.edit_label = {self.edit_label}')
            print(f'self.edit_entry = {self.edit_entry}')
        
        # add labels for editting on edit_name_frame
        for i in range(len(column_list)):
            self.edit_label.append('')
            self.edit_entry.append('')
            
        for i, data in enumerate(column_list):
            self.edit_label[i] = tk.Label(self.edit_name_frame, text=data)
            self.edit_label[i].pack(side=tk.LEFT, expand=True)

        self.entry_var = []
        
        for i in range(len(column_list)):
            self.entry_var.append(tk.StringVar(self.edit_frame))
            self.edit_entry[i] = tk.Entry(self.edit_frame, textvariable=self.entry_var[i])
            self.edit_entry[i].pack(side=tk.LEFT, expand=True)
            
            self.entry_var[i].trace_add('write', self.entry_monitor_callback)
    
    def entry_monitor_callback(self, *args):
        self.for_update_tree_list = []
        
        for _ in self.edit_entry:
            self.for_update_tree_list.append(_.get())
            
        print(f'for_update_tree_list data = {self.for_update_tree_list}')
        
        # for item in self.tree.selection():
        #     item_value = self.tree.item(item,'values')
        #     _ = list(item_value)
        
        # print(f'tree data = {_}')
        
        selected = self.tree.focus()
        self.tree.item(selected, text='', values=self.for_update_tree_list)
    
    def call_command_widget(self, make_frame_flag=True):
        # for initial creation
        if (make_frame_flag == True):
            self.edit_name_frame = tk.Frame(self.root)
            self.edit_frame = tk.Frame(self.root, relief="ridge", bd=3)
            
        self.edit_name_frame.pack(fill=tk.BOTH, padx=5, pady=5)
        self.edit_frame.pack(fill=tk.BOTH, padx=5, pady=5)
        
    def save_csv(self):
        data_to_write = []

        for line in self.tree.get_children():
            # for value in mytree.item(line)['values']:
            #     print(value)
            data_to_write.append(self.tree.item(line)['values'])
    
        print(data_to_write)
        self.save_process(data_to_write)
        
    def save_process(self, data):
        pd_data = pd.DataFrame(data)
        file_path = filedialog.asksaveasfile(initialfile = 'Untitled.csv', defaultextension=".csv", filetypes=[("csv","*.csv"), ("All Files","*.*")])
        pd_data.to_csv(file_path, sep = ",", header=False, index=False)
        
if __name__ == '__main__':
    viewer = CsvEditor()
    viewer.start()