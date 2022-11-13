# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class CsvEditor:

    def __init__(self):

        self.root = None      # root window
        self.data = []        # data of csv file loaded
        self.tree = None      # ttk.Treeview table for csv data loaded

    def start(self):

        self.call_root_window()
        self.call_csv_reader_widget()
        self.call_treeview_widget()
        self.root.mainloop()

    def call_root_window(self):
        """
        create root window
        """
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('CsvEditor')

    def call_csv_reader_widget(self):
        """
        a widget for reading a csv file
        """
        # creating a frame for the widget
        frame = tk.Frame(self.root, relief="ridge", bd=3)
        frame.pack(fill=tk.BOTH, padx=5, pady=5)

        # making a label
        tk.Label(frame, text='file name').pack(side=tk.LEFT)
        
        # creating an input field to identify the file-path of the csv file you want to read
        entry_field = tk.Entry(frame)
        entry_field.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # file dialog button
        tk.Button(frame, text='...', command=lambda: self.set_path(entry_field)).pack(side=tk.LEFT)

        # read the csv file and generate data for Treeview
        tk.Button(frame, text='read', command=lambda: self.read_csv(entry_field.get())).pack(side=tk.LEFT)
    

    def call_treeview_widget(self):
        """
        call ttk.Treeview
        """
        # widget, generate a frame
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        # generate a treeview for a CSV file
        self.tree = ttk.Treeview(frame)
        self.tree.column('#0', width=50, stretch=tk.NO, anchor=tk.E)
        self.tree.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # scrollbar for x axis
        hscrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=lambda f, l: hscrollbar.set(f, l))
        hscrollbar.grid(row=1, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

        # scrollbar for y axis
        vscrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vscrollbar.set)
        vscrollbar.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)

    # for editing the table
    def on_tree_select(self, event):
        print("selected items:")
        for item in self.tree.selection():
            item_text = self.tree.item(item,'text')
            item_value = self.tree.item(item,'values')
            _ = list(item_value)
            _[0] = str(item_text)
            update_item_value = _
            print(update_item_value)

    def set_path(self, entry_field):
        # clear the content of tk.Entry
        entry_field.delete(0, tk.END)

        # get the absolute path of the current python module
        abs_path = os.path.abspath(os.path.dirname(__file__))

        # call the function of file dialog using the absolute path
        file_path = filedialog.askopenfilename(
            title = "Open CSV file",
            filetypes = [("CSV file", ".csv")],
            initialdir=abs_path)

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


if __name__ == '__main__':
    viewer = CsvEditor()
    viewer.start()