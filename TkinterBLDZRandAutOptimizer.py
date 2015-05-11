# -*- coding: utf-8 -*-
import Tkinter as tk
import subprocess
############################################################## Secondary Window Being Predefined ##########################################################################
class AutOptimizer(tk.Frame):
	
	def start_optimizer_gui(self,ok = True):
		
		if ok:
			self.mainloop()
		else:
			self.master.destroy()

	def createOptimizerWidgets(self):
		#Create the set of initial widgets.
		# Create the label

		self.title = tk.Label(self, width = 100)
		self.title.grid(row=0, column=0,columnspan=3, sticky = tk.E+tk.W )

		# Create the buttons

		self.zero = tk.Button(self, width = 30, height = 5)
		self.zero["text"] = "Run All Progs"
		self.zero.grid(row=1, column=1)

		self.title = tk.Label(self, width = 10)
		self.title.grid(row=2, column=0,columnspan=2, sticky = tk.E+tk.W )

		self.one = tk.Button(self, width = 20, height = 5)
		self.one["text"] = "Startup\nPrograms"
		self.one.grid(row=3, column=0)

		self.two = tk.Button(self, width = 20, height = 5)
		self.two["text"] = "Scheduled Tasks"
		self.two.grid(row=4, column=0)

		self.three = tk.Button(self, width = 20, height = 5)
		self.three["text"] = "Services"
		self.three.grid(row=5, column=0)
	 
		self.four = tk.Button(self, width = 20, height = 5)
		self.four["text"] = "Bulk Uninstall"
		self.four.grid(row=3, column=1)

		self.five = tk.Button(self, width = 20, height = 5)
		self.five["text"] = "Windows Directory\nStatistics"
		self.five.grid(row=4, column=1)

		self.six = tk.Button(self, width = 20, height = 5)
		self.six["text"] = "Remove Toolbars"
		self.six.grid(row=5, column=1)

		self.seven = tk.Button(self, width = 20, height = 5)
		self.seven["text"] = "Tweaking's\n Windows Repair"
		self.seven.grid(row=3, column=2)

		self.eight = tk.Button(self, width = 20, height = 5)
		self.eight["text"] = "Rkill and TDSSKiller"
		self.eight.grid(row=4, column=2)

		self.nine = tk.Button(self, width = 20, height = 5)
		self.nine["text"] = "Backup and\nRestore Drivers"
		self.nine.grid(row=5, column=2)

		self.title = tk.Label(self, width = 100)
		self.title.grid(row=6, column=0,columnspan=3, sticky = tk.E+tk.W )

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		# option is needed to put the main label in the window
		self.createOptimizerWidgets()

######################################################################## Secondary Window Being Predefined ###########################################################
class AutOptimizerController(object):

	def winzero(self):
		os.system('')

	def winone(self):
		#os.system('%CD%/ProgFiles/whatinstartup/whatinstartup.exe')
		subprocess.Popen('%CD%/ProgFiles/whatinstartup/whatinstartup.exe', shell=True)
		
	def wintwo(self):
		subprocess.Popen('taskschd.msc', shell=True)
		
	def winthree(self):
		subprocess.Popen('services.msc', shell=True)

	def winfour(self):
		subprocess.Popen('%CD%/ProgFiles/myuninst/myuninst.exe', shell=True)
		
	def winfive(self):
		subprocess.Popen('%CD%/ProgFiles/windirstat/WinDirStatPortable.exe', shell=True)
		
	def winsix(self):
		subprocess.Popen('slmgr/xpr', shell=True)
		
	def winseven(self):
		subprocess.Popen('%CD%/ProgFiles/tweaking/Repair_Windows.exe', shell=True)
	
	def wineight(self):
		subprocess.Popen('%CD%/ProgFiles/rkill/rkill.exe && %CD%/ProgFiles/tdsskiller/tdsskiller.exe', shell=True)

	def winnine(self):
		subprocess.Popen('%CD%/ProgFiles/doubledriver/dd.exe', shell=True)

	def init_view(self,root):

		self.view = AutOptimizer(master=root)   
	
		# Bind buttons with callback methods
		self.view.zero["command"] = self.winzero
		self.view.one["command"] = self.winone
		self.view.two["command"] = self.wintwo
		self.view.three["command"] = self.winthree
		self.view.four["command"] = self.winfour
		self.view.five["command"] = self.winfive
		self.view.six["command"] = self.winsix
		self.view.seven["command"] = self.winseven
		self.view.eight["command"] = self.wineight
		self.view.nine["command"] = self.winnine

		# Start the gui 
		self.view.start_optimizer_gui()

def AutOptimizerMain():

	AutoController = AutOptimizerController()

	# Build Gui and start it
	root = tk.Tk()
	root.title('Auto Optimizer')

	AutoController.init_view(root)

###################################### Main Window GUI, First to be executed ################
class MainWindow(tk.Frame):
	
	def start_mainwindow_gui(self,ok = True):
		
		if ok:
			self.mainloop()
		else:
			self.master.destroy()

	def createMainWindowWidgets(self):
		# Create set of Main Window widgets.
		# Create labels

		self.title = tk.Label(self, width=80)
		self.title.grid(row=0, column=0,columnspan=6, sticky = tk.E+tk.W )

		# Create the buttons

		self.mainzero = tk.Button(self, width = 17, height = 5)
		self.mainzero["text"] = "AutOptimizer"
		self.mainzero.grid(row=0, column=3)

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		# option is needed to put the main label in the window
		self.createMainWindowWidgets()

class MainWindowController(object):

	def mainzero(self): # First Window, First Button > Executing Secondary (AutOptimizer/HWTester/DiagProg) Window.
		if __name__ == "__main__":
			AutOptimizerMain()

	def init_view(self,root):

		self.view = MainWindow(master=root)   
	
		# Bind buttons with callback methods
		self.view.mainzero["command"] = self.mainzero

		#start the GUI
		self.view.start_mainwindow_gui()

def MainWindowMain():

	MainController = MainWindowController()

	# Building Main Window GUI
	root = tk.Tk()
	root.title('B.L.D.Z.R')

	MainController.init_view(root)

if __name__ == "__main__":
	MainWindowMain()