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
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, c):
		frame = self.frames[c]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		StartPageButton0 = tk.Button(self, width=20, height=5, text="Repair Programs", fg="black", bg="orange", command=lambda: controller.show_frame(DiagnosticRepairProgs))
		StartPageButton1 = tk.Button(self, width=20, height=5, text="AutOptimizer", fg="black", bg="orange", command=lambda: controller.show_frame(AutOptimizer))
		StartPageButton2 = tk.Button(self, width=20, height=5, text="Hardware Tester", fg="black", bg="orange", command=lambda: controller.show_frame(HardwareTester))

		StartPageButton0.grid(row=0, column=2, padx=10, pady=10)
		StartPageButton1.grid(row=4, column=1, padx=10, pady=116)
		StartPageButton2.grid(row=4, column=3, padx=10, pady=116)

class DiagnosticRepairProgs(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		BackButton0 = tk.Button(self, width =20, height = 5, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageOneButton1 = tk.Button(self, width=20, height=5, text="Function1", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton2 = tk.Button(self, width=20, height=5, text="Function2", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton3 = tk.Button(self, width=20, height=5, text="Function3", command=lambda: subprocess.Popen('', shell=True))

		PageOneButton4 = tk.Button(self, width=20, height=5, text="Function4", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton5 = tk.Button(self, width=20, height=5, text="Function5", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton6 = tk.Button(self, width=20, height=5, text="Function6", command=lambda: subprocess.Popen('', shell=True))

		PageOneButton7 = tk.Button(self, width=20, height=5, text="Function7", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton8 = tk.Button(self, width=20, height=5, text="Function8", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton9 = tk.Button(self, width=20, height=5, text="Function9", command=lambda: subprocess.Popen('', shell=True))

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

		PageTwoButton1 = tk.Button(self, width=20, height=5, text="Startup Porgams", command=lambda: subprocess.Popen('%CD%/ProgFiles/whatinstartup/whatinstartup.exe && taskmgr /0 /startup', shell=True))
		PageTwoButton2 = tk.Button(self, width=20, height=5, text="Scheduled Tasks", command=lambda: subprocess.Popen('taskschd.msc', shell=True))
		PageTwoButton3 = tk.Button(self, width=20, height=5, text="Services", command=lambda: subprocess.Popen('services.msc', shell=True))

		PageTwoButton4 = tk.Button(self, width=20, height=5, text="Bulk Uninstall", command=lambda: subprocess.Popen('%CD%/ProgFiles/myuninst/myuninst.exe', shell=True))
		PageTwoButton5 = tk.Button(self, width=20, height=5, text="Windows Directory\nStatistics", command=lambda: subprocess.Popen('%CD%/ProgFiles/windirstat/WinDirStatPortable.exe', shell=True))
		PageTwoButton6 = tk.Button(self, width=20, height=5, text="Backup and\nRestore Drivers", command=lambda: subprocess.Popen('%CD%/ProgFiles/doubledriver/dd.exe', shell=True))

		PageTwoButton7 = tk.Button(self, width=20, height=5, text="Tweaking's\n Windows Repair", command=lambda: subprocess.Popen('%CD%/ProgFiles/tweaking/Repair_Windows.exe', shell=True))
		PageTwoButton8 = tk.Button(self, width=20, height=5, text="Rkill (Silent, Wait for Log)", command=lambda: subprocess.Popen('%CD%/ProgFiles/rkill.exe', shell=True))
		PageTwoButton9 = tk.Button(self, width=20, height=5, text="Rootkit Scanner", command=lambda: subprocess.Popen('%CD%/ProgFiles/aswMBR.exe', shell=True))

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

		PageThreeButton1 = tk.Button(self, width=20, height=5, text="Battery Health", command=lambda: subprocess.Popen('%CD%/ProgFiles/batteryinfoview/BatteryInfoView.exe', shell=True))
		PageThreeButton2 = tk.Button(self, width=20, height=5, text="Keyboard", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton3 = tk.Button(self, width=20, height=5, text="WebCam", command=lambda: subprocess.Popen('%CD%/ProgFiles/Camera.exe', shell=True))

		PageThreeButton4 = tk.Button(self, width=20, height=5, text="Left Speaker", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton5 = tk.Button(self, width=20, height=5, text="Stress Tester", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton6 = tk.Button(self, width=20, height=5, text="Right Speaker", command=lambda: subprocess.Popen('', shell=True))

		PageThreeButton7 = tk.Button(self, width=20, height=5, text="WiFi Import/Export", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton8 = tk.Button(self, width=20, height=5, text="Shutdown into\nRefresh or Reset", command=lambda: subprocess.Popen('shutdown -r -t 1 -f', shell=True))
		PageThreeButton9 = tk.Button(self, width=20, height=5, text="Activation", command=lambda: subprocess.Popen('slmgr /xpr', shell=True))

		# USB EJECT
		# CHECK DRIVERS
		# "Keyboard" gets it's own Class so as to load Keyboard input window within same window as other classes

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