#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import webbrowser
import os

class MainAppView(tk.Frame):
    
    def start_gui(self,ok = True):
        
        if ok:
            self.mainloop()
        else:
            self.master.destroy()

    def createWidgets(self):
        #Create the set of initial widgets.
        # Create the label

        self.title = tk.Label(self, width = 80)
        self.title.grid(row=0, column=0,columnspan=6, sticky = tk.E+tk.W )

        # Create the buttons

        self.one = tk.Button(self, width = 17, height = 5)
        self.one["text"] = "Run All Progs"
        self.one.grid(row=1, column=2)

        self.title = tk.Label(self, width = 80)
        self.title.grid(row=2, column=0,columnspan=6, sticky = tk.E+tk.W )

        self.two = tk.Button(self, width = 17, height = 5)
        self.two["text"] = "Edit Startup\nPrograms"
        self.two.grid(row=3, column=1)
     
        self.three = tk.Button(self, width = 17, height = 5)
        self.three["text"] = "Bulk Uninstall"
        self.three.grid(row=3, column=2)

        self.four = tk.Button(self, width = 17, height = 5)
        self.four["text"] = "Backup or\nRestore Drivers"
        self.four.grid(row=3, column=3)

        self.five = tk.Button(self, width = 17, height = 5)
        self.five["text"] = "Google Ext"
        self.five.grid(row=4, column=1)

        self.six = tk.Button(self, width = 17, height = 5)
        self.six["text"] = "Battery Info"
        self.six.grid(row=4, column=2)

        self.seven = tk.Button(self, width = 17, height = 5)
        self.seven["text"] = "6"
        self.seven.grid(row=4, column=3)

        self.eight = tk.Button(self, width = 17, height = 5)
        self.eight["text"] = "7"
        self.eight.grid(row=5, column=1)

        self.nine = tk.Button(self, width = 17, height = 5)
        self.nine["text"] = "8"
        self.nine.grid(row=5, column=2)

        self.ten = tk.Button(self, width = 17, height = 5)
        self.ten["text"] = "9"
        self.ten.grid(row=5, column=3)

        self.title = tk.Label(self, width = 80)
        self.title.grid(row=6, column=0,columnspan=6, sticky = tk.E+tk.W )

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.createWidgets()

class MainAppController(object):

    def winone(self):
        os.system('')

    def wintwo(self):
        os.system('%CD%/ProgFiles/whatinstartup/whatinstartup.exe')

    def winthree(self):
        os.system('%CD%/ProgFiles/myuninst/myuninst.exe')

    def winfour(self):
        os.system('%CD%/ProgFiles/doubledriver/dd.exe')

    def winfive(self):
        os.system('cd %programfiles(x86)%/google/chrome/application/ && chrome chrome//extensions/')

    def winsix(self):
        os.system('%CD%/ProgFiles/batteryinfoview/batteryinfoview.exe /sverhtml %CD%/batteryinfoview.html && cd "%programfiles%/internet explorer/" && iexplore %CD%/batteryinfoview.html')

    def winseven(self):
        os.system('')

    def wineight(self):
        os.system('')

    def winnine(self):
        os.system('')

    def winten(self):
        os.system('')

    def init_view(self,root):

        self.view = MainAppView(master=root)   
    
        # Bind buttons with callback methods
        self.view.one["command"] = self.winone
        self.view.two["command"] = self.wintwo
        self.view.three["command"] = self.winthree
        self.view.four["command"] = self.winfour
        self.view.five["command"] = self.winfive
        self.view.six["command"] = self.winsix
        self.view.seven["command"] = self.winseven
        self.view.eight["command"] = self.wineight
        self.view.nine["command"] = self.winnine
        self.view.ten["command"] = self.winten

        # Start the gui 
        self.view.start_gui()

def main():

    controller = MainAppController()

    # Build Gui and start it
    root = tk.Tk()
    root.title('Auto Optimizer')

    controller.init_view(root)

if __name__ == "__main__":
    main()