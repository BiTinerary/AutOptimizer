import Tkinter as tk
import subprocess

TITLE_FONT = ("Helvetica", 18, "bold")

class MainApp(tk.Tk):

	def __init__(self, *args, **kwargs): # Container is where the Windows are stacked on top of each other. As one Winodow is selected/executed, it is raised above the others.
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.grid(column=5, row=15)
		container.grid_rowconfigure(0)
		container.grid_columnconfigure(0)

		self.frames = {} # Put pages into the same location (where you can open it on center screen?) and the selected one is made visible.
		for F in (StartPage, DiagnosticRepairProgs, AutOptimizer, HardwareTester):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nswe")

		self.show_frame(StartPage)

	def show_frame(self, c):
		frame = self.frames[c]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.photoz = tk.PhotoImage(file='adbicontestgif.gif')

		StartPageButton0 = tk.Button(self, compound="left", image=self.photoz, text="Repair Programs", fg="black", bg="orange", command=lambda: controller.show_frame(DiagnosticRepairProgs)) # width=20, height=5,
		StartPageButton1 = tk.Button(self, width=20, height=5, text="AutOptimizer", fg="black", bg="orange", command=lambda: controller.show_frame(AutOptimizer))
		StartPageButton2 = tk.Button(self, width=20, height=5, text="Hardware Tester", fg="black", bg="orange", command=lambda: controller.show_frame(HardwareTester))
		StartPageButton3 = tk.Button(self, width=20, height=5, text="Eject USB", fg="black", bg="orange", command=lambda: subprocess.Popen('"%CD%/ProgFiles/USBDiskEject.exe" /NOSAVE /REMOVETHIS', shell=True))
		StartPageButton4 = tk.Button(self, width=20, height=5, text="Close All Windows", fg="black", bg="orange", command=lambda: subprocess.Popen('"%CD%/ProgFiles/CloseAll.exe"', shell=True))

		StartPageLabel0 = tk.Label(self, width=20, height=5)
		StartPageLabel0.grid(row=1, column=2, padx=10, pady=10)
		StartPageLabel1 = tk.Label(self, width=20, height=5)
		StartPageLabel1.grid(row=2, column=2, padx=10, pady=10)

		StartPageButton0.grid(row=0, column=2, padx=10, pady=10)
		StartPageButton1.grid(row=0, column=1, padx=10, pady=10) #116
		StartPageButton2.grid(row=0, column=3, padx=10, pady=10)
		StartPageButton3.grid(row=3, column=1, padx=10, pady=10)
		StartPageButton4.grid(row=3, column=3, padx=10, pady=10)

class DiagnosticRepairProgs(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		BackButton0 = tk.Button(self, width=20, height=5, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageOneButton1 = tk.Button(self, width=20, height=5, text="MalwareBytes", command=lambda: subprocess.Popen('"%CD%/ProgFiles/Malwarebytes.cameyo.exe" -SafeMode', shell=True))
		PageOneButton2 = tk.Button(self, width=20, height=5, text="Rootkit Scanner", command=lambda: subprocess.Popen('"%CD%/ProgFiles/aswMBR.exe"', shell=True))
		PageOneButton3 = tk.Button(self, width=20, height=5, text="SuperAntiSpyware", command=lambda: subprocess.Popen('"%CD%/ProgFiles/SuperAntiSpyware.cameyo.exe" -SafeMode', shell=True))

		PageOneButton4 = tk.Button(self, width=20, height=5, text="Rkill (Silent, Wait for Log)", command=lambda: subprocess.Popen('"%CD%/ProgFiles/rkill.exe"', shell=True))
		PageOneButton5 = tk.Button(self, width=20, height=5, text="Tweaking's\n Windows Repair", command=lambda: subprocess.Popen('"%CD%/ProgFiles/tweaking/Repair_Windows.exe"', shell=True))
		PageOneButton6 = tk.Button(self, width=20, height=5, text="Shadow Explorer", command=lambda: subprocess.Popen('"%CD%/ProgFiles/shadowexplorer/ShadowExplorerPortable.exe"', shell=True))

		PageOneButton7 = tk.Button(self, width=20, height=5, text="Driver Identifier", command=lambda: subprocess.Popen('"%CD%/ProgFiles/driveridentifierportable.exe"', shell=True))
		PageOneButton8 = tk.Button(self, width=20, height=5, text="Backup and\nRestore Drivers", command=lambda: subprocess.Popen('"%CD%/ProgFiles/doubledriver/dd.exe"', shell=True))
		PageOneButton9 = tk.Button(self, width=20, height=5, text="PCI-Z Driver Lookup", command=lambda: subprocess.Popen('"%CD%/ProgFiles/PCI-Z.exe"', shell=True))

		BackButton0.grid(row=3, column=2, padx=10, pady=10)

		PageOneButton1.grid(row=0, column=1, padx=10, pady=10)
		PageOneButton2.grid(row=0, column=2, padx=10, pady=10)
		PageOneButton3.grid(row=0, column=3, padx=10, pady=10)

		PageOneButton4.grid(row=1, column=1, padx=10, pady=10)
		PageOneButton5.grid(row=1, column=2, padx=10, pady=10)
		PageOneButton6.grid(row=1, column=3, padx=10, pady=10)

		PageOneButton7.grid(row=2, column=1, padx=10, pady=10)
		PageOneButton8.grid(row=2, column=2, padx=10, pady=10)
		PageOneButton9.grid(row=2, column=3, padx=10, pady=10)

class AutOptimizer(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text="Page 2", bg="orange", font=TITLE_FONT)
		
		BackButton0 = tk.Button(self, width =20, height = 5, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageTwoButton1 = tk.Button(self, width=20, height=5, text="Startup Progams", command=lambda: subprocess.Popen('taskmgr /0 /startup', shell=True)) # "%CD%/ProgFiles/whatinstartup/whatinstartup.exe" && taskmgr /0 /startup
		PageTwoButton2 = tk.Button(self, width=20, height=5, text="Scheduled Tasks", command=lambda: subprocess.Popen('"taskschd.msc"', shell=True))
		PageTwoButton3 = tk.Button(self, width=20, height=5, text="Services", command=lambda: subprocess.Popen('"services.msc"', shell=True))

		PageTwoButton4 = tk.Button(self, width=20, height=5, text="Bulk Uninstall", command=lambda: subprocess.Popen('"%CD%/ProgFiles/myuninst/myuninst.exe"', shell=True))
		PageTwoButton5 = tk.Button(self, width=20, height=5, text="Windows Directory\nStatistics", command=lambda: subprocess.Popen('"%CD%/ProgFiles/WinDirStat.cameyo.exe" -SafeMode', shell=True))
		PageTwoButton6 = tk.Button(self, width=20, height=5, text="EMPTY", command=lambda: subprocess.Popen('""', shell=True))

		PageTwoButton7 = tk.Button(self, width=20, height=5, text="Cleanup All\nBrowser Add-Ons", command=lambda: subprocess.Popen('"%CD%/ProgFiles/avastbrowsercleanup.exe"', shell=True))
		PageTwoButton8 = tk.Button(self, width=20, height=5, text="EMPTY", command=lambda: subprocess.Popen('""', shell=True))
		PageTwoButton9 = tk.Button(self, width=20, height=5, text="EMPTY", command=lambda: subprocess.Popen('""', shell=True))

		BackButton0.grid(row=3, column=2, padx=10, pady=10)

		PageTwoButton1.grid(row=0, column=1, padx=10, pady=10)
		PageTwoButton2.grid(row=0, column=2, padx=10, pady=10)
		PageTwoButton3.grid(row=0, column=3, padx=10, pady=10)

		PageTwoButton4.grid(row=1, column=1, padx=10, pady=10)
		PageTwoButton5.grid(row=1, column=2, padx=10, pady=10)
		PageTwoButton6.grid(row=1, column=3, padx=10, pady=10)

		PageTwoButton7.grid(row=2, column=1, padx=10, pady=10)
		PageTwoButton8.grid(row=2, column=2, padx=10, pady=10)
		PageTwoButton9.grid(row=2, column=3, padx=10, pady=10)

class HardwareTester(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page 3", font=TITLE_FONT)

		BackButton0 = tk.Button(self, width=20, height = 5, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageThreeButton1 = tk.Button(self, width=20, height=5, text="Battery Health", command=lambda: subprocess.Popen('"%CD%/ProgFiles/batteryinfoview/BatteryInfoView.exe"', shell=True))
		PageThreeButton2 = tk.Button(self, width=20, height=5, text="Keyboard", command=lambda: subprocess.Popen('""', shell=True))
		PageThreeButton3 = tk.Button(self, width=20, height=5, text="WebCam", command=lambda: subprocess.Popen('"%CD%/ProgFiles/Camera.exe"', shell=True))

		PageThreeButton4 = tk.Button(self, width=20, height=5, text="Left Speaker", command=lambda: subprocess.Popen('"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Left.mp3"', shell=True))
		PageThreeButton5 = tk.Button(self, width=20, height=5, text="Stress Tester", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton6 = tk.Button(self, width=20, height=5, text="Right Speaker", command=lambda: subprocess.Popen('"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Right.mp3"', shell=True))

		PageThreeButton7 = tk.Button(self, width=20, height=5, text="WiFi Import/Export", command=lambda: subprocess.Popen('""', shell=True))
		PageThreeButton8 = tk.Button(self, width=20, height=5, text="Shutdown into\nRefresh or Reset", command=lambda: subprocess.Popen('"shutdown -r -t 1 -f"', shell=True))
		PageThreeButton9 = tk.Button(self, width=20, height=5, text="Activation", command=lambda: subprocess.Popen('slmgr /xpr', shell=True))

		# CHECK DRIVERS
		# "Keyboard" gets it's own Class so as to load Keyboard input window within same window as other classes
		#Close all (main screen)
		#Synergy
		#Process Hacker
		#Portable VirtualBox
		#Disk2VHD, VHD 2Disk
		#HttRack
		#Flow Chart
		#Chocolatey
		#Unhide
		#AntiVirusProg Removal

		BackButton0.grid(row=3, column=2, padx=5, pady=5)

		PageThreeButton1.grid(row=0, column=1, padx=10, pady=10)
		PageThreeButton2.grid(row=0, column=2, padx=10, pady=10)
		PageThreeButton3.grid(row=0, column=3, padx=10, pady=10)

		PageThreeButton4.grid(row=1, column=1, padx=10, pady=10)
		PageThreeButton5.grid(row=1, column=2, padx=10, pady=10)
		PageThreeButton6.grid(row=1, column=3, padx=10, pady=10)

		PageThreeButton7.grid(row=2, column=1, padx=10, pady=10)
		PageThreeButton8.grid(row=2, column=2, padx=10, pady=10)
		PageThreeButton9.grid(row=2, column=3, padx=10, pady=10)

if __name__ == "__main__":
	app = MainApp()
	app.title("B.L.D.Z.R                                                                                ")
	app.mainloop()
