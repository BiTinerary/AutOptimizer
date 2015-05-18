import Tkinter as tk
import subprocess
from PIL import ImageTk

global icondirectory
icondirectory = "./ProgFiles/Icons/"

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

		self.StartImage0 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.StartImage1 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.StartImage2 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.StartImage3 = ImageTk.PhotoImage(file=icondirectory + 'diskejectorz.png')
		self.StartImage4 = ImageTk.PhotoImage(file=icondirectory + 'closeallz.png')

		StartPageLabel0 = tk.Label(self, width=1, height=2)
		StartPageLabel1 = tk.Label(self, width=1, height=2)

		StartPageButton0 = tk.Button(self, compound="top", image=self.StartImage0, text="Repair Programs", fg="black", bg="orange", command=lambda: controller.show_frame(DiagnosticRepairProgs)) # width=20, height=5,
		StartPageButton1 = tk.Button(self, compound="top", image=self.StartImage1, text="AutOptimizer", fg="black", command=lambda: controller.show_frame(AutOptimizer))
		StartPageButton2 = tk.Button(self, compound="top", image=self.StartImage2, text="Hardware Tester", fg="black", command=lambda: controller.show_frame(HardwareTester))
		StartPageButton3 = tk.Button(self, compound="top", image=self.StartImage3, text="Eject USB", fg="black", command=lambda: subprocess.Popen('"%CD%/ProgFiles/USBDiskEject.exe" /NOSAVE /REMOVETHIS', shell=True))
		StartPageButton4 = tk.Button(self, compound="top", image=self.StartImage4, text="Close All Windows", fg="black", command=lambda: subprocess.Popen('"%CD%/ProgFiles/CloseAll.exe"', shell=True))

		StartPageLabel0.grid(row=0, column=2, padx=0, pady=3)
		StartPageLabel1.grid(row=2, column=2, padx=0, pady=58)

		StartPageButton0.grid(row=3, column=2, padx=20, pady=10)
		StartPageButton1.grid(row=3, column=1, padx=20, pady=10)
		StartPageButton2.grid(row=3, column=3, padx=20, pady=10)
		StartPageButton3.grid(row=1, column=1, padx=20, pady=10)
		StartPageButton4.grid(row=1, column=3, padx=20, pady=10)

class DiagnosticRepairProgs(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.PageOneImage1 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageOneImage2 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageOneImage3 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageOneImage4 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageOneImage5 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageOneImage6 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageOneImage7 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageOneImage8 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageOneImage9 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')

		BackButton0 = tk.Button(self, width=55, height=2, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageOneButton1 = tk.Button(self, compound="top", image=self.PageOneImage1, text="MalwareBytes", command=lambda: subprocess.Popen('"%CD%/ProgFiles/Malwarebytes.cameyo.exe" -SafeMode', shell=True))
		PageOneButton2 = tk.Button(self, compound="top", image=self.PageOneImage2, text="Rootkit Scanner", command=lambda: subprocess.Popen('"%CD%/ProgFiles/aswMBR.exe"', shell=True))
		PageOneButton3 = tk.Button(self, compound="top", image=self.PageOneImage3, text="SuperAntiSpyware", command=lambda: subprocess.Popen('"%CD%/ProgFiles/SuperAntiSpyware.cameyo.exe" -SafeMode', shell=True))

		PageOneButton4 = tk.Button(self, compound="top", image=self.PageOneImage4, text="Rkill (Wait for Log)", command=lambda: subprocess.Popen('"%CD%/ProgFiles/rkill.exe"', shell=True))
		PageOneButton5 = tk.Button(self, compound="top", image=self.PageOneImage5, text="AIO Windows Repair", command=lambda: subprocess.Popen('"%CD%/ProgFiles/tweaking/Repair_Windows.exe"', shell=True))
		PageOneButton6 = tk.Button(self, compound="top", image=self.PageOneImage6, text="Shadow Explorer", command=lambda: subprocess.Popen('"%CD%/ProgFiles/shadowexplorer/ShadowExplorerPortable.exe"', shell=True))

		PageOneButton7 = tk.Button(self, compound="top", image=self.PageOneImage7, text="Driver Identifier", command=lambda: subprocess.Popen('"%CD%/ProgFiles/driveridentifierportable.exe"', shell=True))
		PageOneButton8 = tk.Button(self, compound="top", image=self.PageOneImage8, text="Backup Drivers", command=lambda: subprocess.Popen('"%CD%/ProgFiles/doubledriver/dd.exe"', shell=True))
		PageOneButton9 = tk.Button(self, compound="top", image=self.PageOneImage9, text="PCI-Z Driver Lookup", command=lambda: subprocess.Popen('"%CD%/ProgFiles/PCI-Z.exe"', shell=True))

		BackButton0.grid(row=0, column=0, columnspan=4)

		PageOneButton1.grid(row=1, column=1, padx=20, pady=10)
		PageOneButton2.grid(row=1, column=2, padx=20, pady=10)
		PageOneButton3.grid(row=1, column=3, padx=20, pady=10)

		PageOneButton4.grid(row=2, column=1, padx=20, pady=10)
		PageOneButton5.grid(row=2, column=2, padx=20, pady=10)
		PageOneButton6.grid(row=2, column=3, padx=20, pady=10)

		PageOneButton7.grid(row=3, column=1, padx=20, pady=10)
		PageOneButton8.grid(row=3, column=2, padx=20, pady=10)
		PageOneButton9.grid(row=3, column=3, padx=20, pady=10)

class AutOptimizer(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.PageTwoImage1 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageTwoImage2 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageTwoImage3 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageTwoImage4 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageTwoImage5 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageTwoImage6 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageTwoImage7 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageTwoImage8 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageTwoImage9 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')

		label = tk.Label(self, text="Page 2", bg="orange", font=TITLE_FONT)

		BackButton0 = tk.Button(self, width=55, height=2, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageTwoButton1 = tk.Button(self, compound="top", image=self.PageTwoImage1, text="Startup Progams", command=lambda: subprocess.Popen('taskmgr /0 /startup', shell=True)) # "%CD%/ProgFiles/whatinstartup/whatinstartup.exe" && taskmgr /0 /startup
		PageTwoButton2 = tk.Button(self, compound="top", image=self.PageTwoImage2, text="Scheduled Tasks", command=lambda: subprocess.Popen('"taskschd.msc"', shell=True))
		PageTwoButton3 = tk.Button(self, compound="top", image=self.PageTwoImage3, text="Services", command=lambda: subprocess.Popen('"services.msc"', shell=True))

		PageTwoButton4 = tk.Button(self, compound="top", image=self.PageTwoImage4, text="Bulk Uninstall", command=lambda: subprocess.Popen('"%CD%/ProgFiles/myuninst/myuninst.exe"', shell=True))
		PageTwoButton5 = tk.Button(self, compound="top", image=self.PageTwoImage5, text="WinDirStat", command=lambda: subprocess.Popen('"%CD%/ProgFiles/WinDirStat.cameyo.exe" -SafeMode', shell=True))
		PageTwoButton6 = tk.Button(self, compound="top", image=self.PageTwoImage6, text="EMPTY", command=lambda: subprocess.Popen('""', shell=True))

		PageTwoButton7 = tk.Button(self, compound="top", image=self.PageTwoImage7, text="Browser Addons", command=lambda: subprocess.Popen('"%CD%/ProgFiles/avastbrowsercleanup.exe"', shell=True))
		PageTwoButton8 = tk.Button(self, compound="top", image=self.PageTwoImage8, text="EMPTY", command=lambda: subprocess.Popen('""', shell=True))
		PageTwoButton9 = tk.Button(self, compound="top", image=self.PageTwoImage9, text="EMPTY", command=lambda: subprocess.Popen('""', shell=True))

		BackButton0.grid(row=0, column=0, columnspan=4)

		PageTwoButton1.grid(row=1, column=1, padx=20, pady=10)
		PageTwoButton2.grid(row=1, column=2, padx=20, pady=10)
		PageTwoButton3.grid(row=1, column=3, padx=20, pady=10)

		PageTwoButton4.grid(row=2, column=1, padx=20, pady=10)
		PageTwoButton5.grid(row=2, column=2, padx=20, pady=10)
		PageTwoButton6.grid(row=2, column=3, padx=20, pady=10)

		PageTwoButton7.grid(row=3, column=1, padx=20, pady=10)
		PageTwoButton8.grid(row=3, column=2, padx=20, pady=10)
		PageTwoButton9.grid(row=3, column=3, padx=20, pady=10)

class HardwareTester(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page 3", font=TITLE_FONT)

		self.PageThreeImage1 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageThreeImage2 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageThreeImage3 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageThreeImage4 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageThreeImage5 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageThreeImage6 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageThreeImage7 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageThreeImage8 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')
		self.PageThreeImage9 = ImageTk.PhotoImage(file=icondirectory + 'emptybutton.png')

		BackButton0 = tk.Button(self, width=55, height=2, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageThreeButton1 = tk.Button(self, compound="top", image=self.PageThreeImage1, text="Battery Health", command=lambda: subprocess.Popen('"%CD%/ProgFiles/batteryinfoview/BatteryInfoView.exe"', shell=True))
		PageThreeButton2 = tk.Button(self, compound="top", image=self.PageThreeImage2, text="Keyboard", command=lambda: subprocess.Popen('""', shell=True))
		PageThreeButton3 = tk.Button(self, compound="top", image=self.PageThreeImage3, text="WebCam", command=lambda: subprocess.Popen('"%CD%/ProgFiles/Camera.exe"', shell=True))

		PageThreeButton4 = tk.Button(self, compound="top", image=self.PageThreeImage4, text="Left Speaker", command=lambda: subprocess.Popen('"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Left.mp3"', shell=True))
		PageThreeButton5 = tk.Button(self, compound="top", image=self.PageThreeImage5, text="Stress Tester", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton6 = tk.Button(self, compound="top", image=self.PageThreeImage6, text="Right Speaker", command=lambda: subprocess.Popen('"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Right.mp3"', shell=True))

		PageThreeButton7 = tk.Button(self, compound="top", image=self.PageThreeImage7, text="WiFi Import/Export", command=lambda: subprocess.Popen('""', shell=True))
		PageThreeButton8 = tk.Button(self, compound="top", image=self.PageThreeImage8, text="Reboot to Refresh", command=lambda: subprocess.Popen('"shutdown -r -t 1 -f"', shell=True))
		PageThreeButton9 = tk.Button(self, compound="top", image=self.PageThreeImage9, text="Activation", command=lambda: subprocess.Popen('slmgr /xpr', shell=True))

		BackButton0.grid(row=0, column=0, columnspan=4)

		PageThreeButton1.grid(row=1, column=1, padx=20, pady=10)
		PageThreeButton2.grid(row=1, column=2, padx=20, pady=10)
		PageThreeButton3.grid(row=1, column=3, padx=20, pady=10)

		PageThreeButton4.grid(row=2, column=1, padx=20, pady=10)
		PageThreeButton5.grid(row=2, column=2, padx=20, pady=10)
		PageThreeButton6.grid(row=2, column=3, padx=20, pady=10)

		PageThreeButton7.grid(row=3, column=1, padx=20, pady=10)
		PageThreeButton8.grid(row=3, column=2, padx=20, pady=10)
		PageThreeButton9.grid(row=3, column=3, padx=20, pady=10)

		# CHECK DRIVERS
		# "Keyboard" gets it's own Class so as to load Keyboard input window within same window as other classes
		#Synergy
		#Process Hacker
		#Portable VirtualBox
		#Disk2VHD, VHD 2Disk
		#HttRack
		#Flow Chart
		#Chocolatey
		#Unhide
		#AntiVirusProg Removal

if __name__ == "__main__":
	app = MainApp()
	app.title("B.L.D.Z.R                                                                                ")
	app.mainloop()
