# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:00:13 2022

@author: Hiroaki.Kato
"""

from pathlib import Path
import os

class find_files:

    def __init__(self, folder, extension):

        if folder == "":
            self.folder = os.getcwd()
        else:
            self.folder = folder

        self.extension = self._check_extension(extension)
        self.list_data = []

    @staticmethod
    def get_current_folder():
        return os.getcwd()

    def _check_extension(self, be_checked_str):
        if be_checked_str.startswith('.') == False:
            be_checked_str = '.' + be_checked_str

        print("the target extension is :", be_checked_str)
        return be_checked_str

    def search_current_folder(self):

        my_str = "*" + self.extension
        print("seraching of ", my_str)

        self.mypath = Path(self.folder)
        self.list_data = list(self.mypath.glob(my_str))

    def search_current_with_subfolder_folder(self):

        my_str = "**/*" + self.extension
        print(my_str)

        self.mypath = Path(self.folder)
        self.list_data = list(self.mypath.glob(my_str))

    def show_parent(self):

        tmp = []
        for _ in self.list_data:
            # print('Parent:', _.parent)
            tmp.append(_.parent)
        return tmp

    def show_name(self):

        tmp = []
        for _ in self.list_data:
            # print('Filename:', _.name)
            tmp.append(_.name)
        return tmp

    def show_suffix(self):

        tmp = []
        for _ in self.list_data:
            # print('Extension:', _.suffix)
            tmp.append(_.suffix)
        return tmp

if __name__ == '__main__':

    current_path = find_files.get_current_folder()
    file_obj = find_files(current_path, ".csv")
    file_obj.search_current_folder()
    file_name_list = file_obj.show_name()
    
    print(file_name_list)
