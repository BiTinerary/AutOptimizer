import os
import subprocess
import Tkinter as tk
from PIL import ImageTk

global icondirectory
icondirectory = "./ProgFiles/Icons/" # As guessed, static directory where all icons are stored.

class MainApp(tk.Tk):

	def __init__(self, *args, **kwargs): # Container is where the Windows are stacked on top of each other. As one Winodow is selected/executed, it is raised above the others.
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.grid(column=5, row=15)
		container.grid_rowconfigure(0)
		container.grid_columnconfigure(0)

		self.frames = {} # Put pages into the same location and the selected one is made visible.
		for F in (StartPage, DiagnosticRepairProgs, AutOptimizer, HardwareTester, ChocolateyAndInstall):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nswe")

		self.show_frame(StartPage)

	def show_frame(self, c):
		frame = self.frames[c]
		frame.tkraise()

class StartPage(tk.Frame): # First initial frame. Which contains primary classes/functions.

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		def AllHardwareTesterButtons(): # Sequentially run hardware diagnostic programs.
			BATTERY = '"%CD%/ProgFiles/batteryinfoview/batteryinfoview.exe"'
			CAMERA = '"%CD%/ProgFiles/Camera.exe"'
			LEFTSPKR = '"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Left.mp3"'
			RIGHTSPKR = '"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Right.mp3"'
			HDDSMART = '"%CD%/ProgFiles/crystaldiskinfo/DiskInfo.exe"'
			IMPORTWIFI = 'cd "%CD%/ProgFiles/wirelesskeyview" && WirelessKeyView.exe /import "%CD%/ProgFiles/wirelesskeyview/WiFiKeysBackup.txt"'
			ACTIVATION = 'slmgr /xpr'

			HardwareTestingCommands = [IMPORTWIFI, LEFTSPKR, RIGHTSPKR, ACTIVATION, HDDSMART, BATTERY, CAMERA] #Above commands stored in list
			
			KeyboardTester() # Call the keyboard class
			for Command in HardwareTestingCommands: # Sequentially execute each variable stored in HardwareTestingCommands list.
				#print Command
				subprocess.call(Command, shell=True) #subprocess.check_call((command), shell=True)

		def AllAutOptimizerButtons(): # Sequentially run hardware diagnostic programs.
			TASKMGR = 'taskmgr /0 /startup'
			SERVICES = 'services.msc'
			TASKSCHD = 'taskschd.msc'
			TREESIZEFREE = '"%CD%/ProgFiles/treesizefree/treesizefree.exe"'
			BULKUNINST = '"%CD%/ProgFiles/myuninstaller/myuninst.exe"'
			JUNKREMTOOL = '"%CD%/ProgFiles/JRT.exe"'
			CLEANMGR = 'cleanmgr /sageset99 && cleanmgr /sagerun99'

			AutOptCommands = [TASKMGR, JUNKREMTOOL, BULKUNINST, TREESIZEFREE, TASKSCHD, CLEANMGR, SERVICES]
			
			for Command in AutOptCommands: # Sequentially execute each variable stored in AutOptCommands list.
				#print Command
				subprocess.call(Command, shell=True) #subprocess.check_call((command), shell=True)

		TopAutOptimizerButton0 = tk.Button(self, width=15, height=2, text="Quick Start AutOptimizer", command=lambda: AllAutOptimizerButtons()) # Auto All button
		TopAutoHardwareButton1 = tk.Button(self, width=15, height=2, text="Quick Start Hardware Tester", command=lambda: AllHardwareTesterButtons()) # Auto All button

		TopAutOptimizerButton0.grid(row=0, columnspan=3, ipadx=50, padx=(0,60), pady=0)
		TopAutoHardwareButton1.grid(row=0, column=2, columnspan=2, ipadx=50, padx=(60,0), pady=0)

		StartPageLabel1 = tk.Label(self, width=1, height=2)
		StartPageLabel1.grid(row=2, column=2, padx=0, pady=60)

		self.StartImage0 = ImageTk.PhotoImage(file=icondirectory + 'removedrive.png') # More icons tied to specific buttons.
		self.StartImage1 = ImageTk.PhotoImage(file=icondirectory + 'closeall.png') #
		self.StartImage2 = ImageTk.PhotoImage(file=icondirectory + 'optimize.png') #
		self.StartImage3 = ImageTk.PhotoImage(file=icondirectory + 'repairprogs.png') #
		self.StartImage4 = ImageTk.PhotoImage(file=icondirectory + 'hardware.png') #
		self.StartImage5 = ImageTk.PhotoImage(file=icondirectory + 'install.png') #

		StartPageButton0 = tk.Button(self, compound="top", image=self.StartImage0, text="Eject USB", fg="black", command=lambda: subprocess.Popen('"%CD%/ProgFiles/RemoveDrive.exe" . -l -b -e', shell=True))
		StartPageButton1 = tk.Button(self, compound="top", image=self.StartImage1, text="Close All Windows", fg="black", command=lambda: subprocess.Popen('"%CD%/ProgFiles/CloseAll.exe"', shell=True))
		StartPageButton2 = tk.Button(self, compound="top", image=self.StartImage2, text="AutOptimizer", fg="black", command=lambda: controller.show_frame(AutOptimizer))
		StartPageButton3 = tk.Button(self, compound="top", image=self.StartImage3, text="Repair Programs", fg="black", command=lambda: controller.show_frame(DiagnosticRepairProgs))
		StartPageButton4 = tk.Button(self, compound="top", image=self.StartImage4, text="Hardware Tester", fg="black", command=lambda: controller.show_frame(HardwareTester))
		StartPageButton5 = tk.Button(self, compound="top", image=self.StartImage5, text="Misc. Install", fg="black", command=lambda: controller.show_frame(ChocolateyAndInstall))

		StartPageButton0.grid(row=1, column=1, padx=20, pady=10) #
		StartPageButton1.grid(row=1, column=3, padx=20, pady=10) #
		StartPageButton2.grid(row=3, column=1, padx=20, pady=10) #
		StartPageButton3.grid(row=2, column=2, padx=20, pady=10) # .Grid() function which easily places buttons symetrically as opposed to .pack()
		StartPageButton4.grid(row=3, column=3, padx=20, pady=10) #
		StartPageButton5.grid(row=3, column=2, padx=20, pady=10) #

class DiagnosticRepairProgs(tk.Frame): # secondary frame.

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.PageOneImage1 = ImageTk.PhotoImage(file=icondirectory + 'MalwareBytes.png') # More icons tied to specific buttons.
		self.PageOneImage2 = ImageTk.PhotoImage(file=icondirectory + 'aswMBR.png') #
		self.PageOneImage3 = ImageTk.PhotoImage(file=icondirectory + 'SuperAntiSpyware.png') #
		self.PageOneImage4 = ImageTk.PhotoImage(file=icondirectory + 'Rkill.png') #
		self.PageOneImage5 = ImageTk.PhotoImage(file=icondirectory + 'TweakingsWindowsRepair.png') #
		self.PageOneImage6 = ImageTk.PhotoImage(file=icondirectory + 'ShadowExplorer.png') #
		self.PageOneImage7 = ImageTk.PhotoImage(file=icondirectory + 'DoubleDriver.png') #
		self.PageOneImage8 = ImageTk.PhotoImage(file=icondirectory + 'devmgmt.png') #
		self.PageOneImage9 = ImageTk.PhotoImage(file=icondirectory + 'PCI-Z.png') #

		BackButton0 = tk.Button(self, width=60, height=2, text="Go Back", command=lambda: controller.show_frame(StartPage)) # Back button allowing for seemless navigation between frames.

		PageOneButton1 = tk.Button(self, compound="top", image=self.PageOneImage1, text="MalwareBytes", command=lambda: subprocess.Popen('"%CD%/ProgFiles/Malwarebytes.cameyo.exe" -SafeMode', shell=True)) # More buttons specifying programs, flags, icons and position.
		PageOneButton2 = tk.Button(self, compound="top", image=self.PageOneImage2, text="Rootkit Scanner", command=lambda: subprocess.Popen('"%CD%/ProgFiles/aswMBR.exe"', shell=True)) #
		PageOneButton3 = tk.Button(self, compound="top", image=self.PageOneImage3, text="SuperAntiSpyware", command=lambda: subprocess.Popen('"%CD%/ProgFiles/superantispyware/superantispyware.exe"', shell=True)) #

		PageOneButton4 = tk.Button(self, compound="top", image=self.PageOneImage4, text="Rkill (Wait for Log)", command=lambda: subprocess.Popen('"%CD%/ProgFiles/rkill.exe" -w "%CD%/ProgFiles/batch/whitelist.txt"', shell=True)) #
		PageOneButton5 = tk.Button(self, compound="top", image=self.PageOneImage5, text="AIO Windows Repair", command=lambda: subprocess.Popen('"%CD%/ProgFiles/tweaking/Repair_Windows.exe"', shell=True)) #
		PageOneButton6 = tk.Button(self, compound="top", image=self.PageOneImage6, text="Shadow Explorer", command=lambda: subprocess.Popen('"%CD%/ProgFiles/shadowexplorer/ShadowExplorerPortable.exe"', shell=True)) #

		PageOneButton7 = tk.Button(self, compound="top", image=self.PageOneImage7, text="Backup Drivers", command=lambda: subprocess.Popen('"%CD%/ProgFiles/doubledriver/dd.exe"', shell=True)) #
		PageOneButton8 = tk.Button(self, compound="top", image=self.PageOneImage8, text="Device Management", command=lambda: subprocess.Popen('"devmgmt.msc"', shell=True)) #
		PageOneButton9 = tk.Button(self, compound="top", image=self.PageOneImage9, text="PCI-Z Driver Lookup", command=lambda: subprocess.Popen('"%CD%/ProgFiles/PCI-Z.exe"', shell=True)) #

		BackButton0.grid(row=0, column=0, columnspan=4) # positioning buttons for frame 2

		PageOneButton1.grid(row=1, column=1, padx=20, pady=10) #
		PageOneButton2.grid(row=1, column=2, padx=20, pady=10) #
		PageOneButton3.grid(row=1, column=3, padx=20, pady=10) #

		PageOneButton4.grid(row=2, column=1, padx=20, pady=10) #
		PageOneButton5.grid(row=2, column=2, padx=20, pady=10) #
		PageOneButton6.grid(row=2, column=3, padx=20, pady=10) #

		PageOneButton7.grid(row=3, column=1, padx=20, pady=10) #
		PageOneButton8.grid(row=3, column=2, padx=20, pady=10) #
		PageOneButton9.grid(row=3, column=3, padx=20, pady=10) #

class AutOptimizer(tk.Frame): # frame 3

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.PageTwoImage1 = ImageTk.PhotoImage(file=icondirectory + 'TaskManager.png')
		self.PageTwoImage2 = ImageTk.PhotoImage(file=icondirectory + 'TaskScheduler.png')
		self.PageTwoImage3 = ImageTk.PhotoImage(file=icondirectory + 'Services.png')
		self.PageTwoImage4 = ImageTk.PhotoImage(file=icondirectory + 'bleachbit.png')
		self.PageTwoImage5 = ImageTk.PhotoImage(file=icondirectory + 'cleanmgr.png')
		self.PageTwoImage6 = ImageTk.PhotoImage(file=icondirectory + 'nirsoft.png')
		self.PageTwoImage7 = ImageTk.PhotoImage(file=icondirectory + 'JRT.png')
		self.PageTwoImage8 = ImageTk.PhotoImage(file=icondirectory + 'treesizefree.png')
		self.PageTwoImage9 = ImageTk.PhotoImage(file=icondirectory + 'synergy.png')

		BackButton0 = tk.Button(self, width=60, height=2, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageTwoButton1 = tk.Button(self, compound="top", image=self.PageTwoImage1, text="Startup Progams", command=lambda: subprocess.Popen('taskmgr /0 /startup', shell=True)) # "%CD%/ProgFiles/whatinstartup/whatinstartup.exe" && taskmgr /0 /startup
		PageTwoButton2 = tk.Button(self, compound="top", image=self.PageTwoImage2, text="Scheduled Tasks", command=lambda: subprocess.Popen('"taskschd.msc"', shell=True))
		PageTwoButton3 = tk.Button(self, compound="top", image=self.PageTwoImage3, text="Services", command=lambda: subprocess.Popen('"services.msc"', shell=True))

		PageTwoButton4 = tk.Button(self, compound="top", image=self.PageTwoImage4, text="BleachBit", command=lambda: subprocess.Popen('"%CD%/ProgFiles/bleachbit/BleachBit.exe"', shell=True))
		PageTwoButton5 = tk.Button(self, compound="top", image=self.PageTwoImage5, text="CleanMgr", command=lambda: subprocess.Popen('cleanmgr /sageset99 && cleanmgr /sagerun99' , shell=True))
		PageTwoButton6 = tk.Button(self, compound="top", image=self.PageTwoImage6, text="Bulk Uninstaller", command=lambda: subprocess.Popen('"%CD%/ProgFiles/myuninstaller/myuninst.exe"', shell=True))

		PageTwoButton7 = tk.Button(self, compound="top", image=self.PageTwoImage7, text="Junkware Removal", command=lambda: subprocess.Popen('"%CD%/ProgFiles/JRT.exe"', shell=True))
		PageTwoButton8 = tk.Button(self, compound="top", image=self.PageTwoImage8, text="TreeSizeFree", command=lambda: subprocess.Popen('"%CD%/ProgFiles/treesizefree/treesizefree.exe"', shell=True))
		PageTwoButton9 = tk.Button(self, compound="top", image=self.PageTwoImage9, text="Synergy", command=lambda: subprocess.Popen('"%CD%/ProgFiles/Synergy.cameyo.exe"', shell=True))

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

		self.PageThreeImage1 = ImageTk.PhotoImage(file=icondirectory + 'BatteryInfoView.png')
		self.PageThreeImage2 = ImageTk.PhotoImage(file=icondirectory + 'keyboard.png')
		self.PageThreeImage3 = ImageTk.PhotoImage(file=icondirectory + 'Camera.png')
		self.PageThreeImage4 = ImageTk.PhotoImage(file=icondirectory + 'SpeakerIconLeft.png')
		self.PageThreeImage5 = ImageTk.PhotoImage(file=icondirectory + 'CrystalDiskInfo.png')
		self.PageThreeImage6 = ImageTk.PhotoImage(file=icondirectory + 'SpeakerIconRight.png')
		self.PageThreeImage7A = ImageTk.PhotoImage(file=icondirectory + 'wifitophalf.png')
		self.PageThreeImage7 = ImageTk.PhotoImage(file=icondirectory + 'wifibottomhalf.png')
		self.PageThreeImage8 = ImageTk.PhotoImage(file=icondirectory + 'Folding@Home.png')
		self.PageThreeImage9 = ImageTk.PhotoImage(file=icondirectory + 'activation.png')

		BackButton0 = tk.Button(self, width=60, height=2, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageThreeButton1 = tk.Button(self, compound="top", image=self.PageThreeImage1, text="Battery Health", command=lambda: subprocess.Popen('"%CD%/ProgFiles/batteryinfoview/batteryinfoview.exe"', shell=True))
		PageThreeButton2 = tk.Button(self, compound="top", image=self.PageThreeImage2, text="Keyboard", command=lambda: KeyboardTester())
		PageThreeButton3 = tk.Button(self, compound="top", image=self.PageThreeImage3, text="WebCam", command=lambda: subprocess.Popen('cd "%CD%/ProgFiles/commandcam" && "commandcam.exe" && image.bmp', shell=True))

		PageThreeButton4 = tk.Button(self, compound="top", image=self.PageThreeImage4, text="Left Speaker", command=lambda: subprocess.Popen('"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Left.mp3"', shell=True))
		PageThreeButton5 = tk.Button(self, compound="top", image=self.PageThreeImage5, text="S.M.A.R.T Tester", command=lambda: subprocess.Popen('"%CD%/ProgFiles/crystaldiskinfo/DiskInfo.exe"', shell=True))
		PageThreeButton6 = tk.Button(self, compound="top", image=self.PageThreeImage6, text="Right Speaker", command=lambda: subprocess.Popen('"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Right.mp3"', shell=True))

		PageThreeButton7 = tk.Button(self, compound="top", image=self.PageThreeImage7, text="WiFi Export", command=lambda: subprocess.Popen('cd "%CD%/ProgFiles/wirelesskeyview" && WirelessKeyView.exe /export "%CD%/ProgFiles/wirelesskeyview/WiFiKeysBackup.txt"', shell=True))
		PageThreeButton7A = tk.Button(self, compound="bottom", image=self.PageThreeImage7A, text="WiFi Import", command=lambda: subprocess.Popen('cd "%CD%/ProgFiles/wirelesskeyview" && WirelessKeyView.exe /import "%CD%/ProgFiles/wirelesskeyview/WiFiKeysBackup.txt"', shell=True))
		PageThreeButton8 = tk.Button(self, compound="top", image=self.PageThreeImage8, text="Stress Tester", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton9 = tk.Button(self, compound="top", image=self.PageThreeImage9, text="Activation", command=lambda: subprocess.Popen('slmgr /xpr', shell=True))

		BackButton0.grid(row=0, column=0, columnspan=4)

		PageThreeButton1.grid(row=1, column=1, padx=20, pady=10)
		PageThreeButton2.grid(row=1, column=2, padx=20, pady=10)
		PageThreeButton3.grid(row=1, column=3, padx=20, pady=10)

		PageThreeButton4.grid(row=2, column=1, padx=20, pady=10)
		PageThreeButton5.grid(row=2, column=2, padx=20, pady=10)
		PageThreeButton6.grid(row=2, column=3, padx=20, pady=10)

		PageThreeButton8.grid(row=3, column=1, padx=20, pady=10)
		PageThreeButton7.grid(row=3, column=2, padx=20, pady=(65,5))
		PageThreeButton7A.grid(row=3, column=2, padx=20, pady=(5,65))
		PageThreeButton9.grid(row=3, column=3, padx=20, pady=10)

class ChocolateyAndInstall(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.PageThreeImage1 = ImageTk.PhotoImage(file=icondirectory + 'python.png')
		self.PageThreeImage2 = ImageTk.PhotoImage(file=icondirectory + 'chocolatey.png')
		self.PageThreeImage3 = ImageTk.PhotoImage(file=icondirectory + 'chocolatey.png')
		self.PageThreeImage4 = ImageTk.PhotoImage(file=icondirectory + 'chocolatey.png')
		self.PageThreeImage5 = ImageTk.PhotoImage(file=icondirectory + 'chocolatey.png')
		self.PageThreeImage6 = ImageTk.PhotoImage(file=icondirectory + 'chocolatey.png')
		self.PageThreeImage7 = ImageTk.PhotoImage(file=icondirectory + 'chocolatey.png')
		self.PageThreeImage8 = ImageTk.PhotoImage(file=icondirectory + 'chocolatey.png')
		self.PageThreeImage9 = ImageTk.PhotoImage(file=icondirectory + 'chocolatey.png')

		BackButton0 = tk.Button(self, width=60, height=2, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageThreeButton1 = tk.Button(self, compound="top", image=self.PageThreeImage1, text="Python EnVars", command=lambda: os.system("%CD%/ProgFiles/batch/addpythonvars.bat"))
		PageThreeButton2 = tk.Button(self, compound="top", image=self.PageThreeImage2, text="Chocolatey", command=lambda: subprocess.Popen("@powershell -NoProfile -ExecutionPolicy Bypass -Command " + "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" + "&& SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin", shell=True))
		PageThreeButton3 = tk.Button(self, compound="top", image=self.PageThreeImage3, text="Choco Script", command=lambda: os.system('%CD%/ProgFiles/batch/chocoinstall.bat'))

		PageThreeButton4 = tk.Button(self, compound="top", image=self.PageThreeImage4, text="Vbox Guest", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton5 = tk.Button(self, compound="top", image=self.PageThreeImage5, text="VirtualBox", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton6 = tk.Button(self, compound="top", image=self.PageThreeImage6, text="VirtualBox", command=lambda: subprocess.Popen('', shell=True))

		PageThreeButton7 = tk.Button(self, compound="top", image=self.PageThreeImage7, text="VirtualBox", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton8 = tk.Button(self, compound="top", image=self.PageThreeImage8, text="VirtualBox", command=lambda: subprocess.Popen('', shell=True))
		PageThreeButton9 = tk.Button(self, compound="top", image=self.PageThreeImage9, text="VirtualBox", command=lambda: subprocess.Popen('', shell=True))

		BackButton0.grid(row=0, column=0, columnspan=4)

		PageThreeButton1.grid(row=1, column=1, padx=20, pady=10)
		PageThreeButton2.grid(row=1, column=2, padx=20, pady=10)
		PageThreeButton3.grid(row=1, column=3, padx=20, pady=10)

		PageThreeButton4.grid(row=2, column=1, padx=20, pady=10)
		PageThreeButton5.grid(row=2, column=2, padx=20, pady=10)
		PageThreeButton6.grid(row=2, column=3, padx=20, pady=10)

		PageThreeButton7.grid(row=3, column=2, padx=20, pady=10)
		PageThreeButton8.grid(row=3, column=1, padx=20, pady=10)
		PageThreeButton9.grid(row=3, column=3, padx=20, pady=10)

class KeyboardTester(tk.Tk): # Custom keyboard tester.
	def __init__(self):
		tk.Tk.__init__(self)

		self.title("KeyBoard Testing")

		LABEL1 = tk.Label(self, compound="left", text="Test the keyboard using the four main rows of ASCII characters 0-9 and a-z.")
		LABEL1.grid(row=0, column=0, columnspan=3)

		LABEL2 = tk.Label(self, compound="left", text="ie: 1234567890qwertyuiopasdfghjklzxcvbnm                               ")
		LABEL2.grid(row=1, column=0, columnspan=2)

		INPUTRETURN = tk.Entry(self, bd=5, width=58) # create GUI prompt for end user/character input
		INPUTRETURN.grid(row=2, column=0, columnspan=3) # create ^ and store in a grid

		def ButtonPressVerification(input):
			VERIFICATION = INPUTRETURN.get() # grabs whatever input provided by enduser and assigns it as "VERIFICATION" variable
			qwertyuiop = "1234567890qwertyuiopasdfghjklzxcvbnm" # dynamic/hardcoded string for cross referencing enduser input.

			if VERIFICATION.lower() == qwertyuiop: # decapitalize all characters in VERIFICATION string (end user input) and `IF` it's exactly equal to `qwertyuiop` string...
				#print "VERIFIED"
				self.destroy() #.... allow the end user access to initial window by "destroying" keyboard tester window. Similar to the exit() command but for individual child/GUI windows.

			else:
				#print "TRY AGAIN!!"
				self.destroy() #... destroy current keyboard tester window (for visual notification)
				KeyboardTester() #.... and restart the entire function.

		BUTTON = tk.Button(self, width=50, height=2, text="Click or Press Enter", command=lambda: ButtonPressVerification()) # button for Enduser to "submit" characters to `VERIFICATION` variable
		BUTTON.grid(row=3, column=0, columnspan=3) # creates this button and assigns to grid placement

		self.bind('<Return>',(lambda event: ButtonPressVerification(INPUTRETURN.get()))) # connect/BIND the "Return" (aka enter) key with the previously mentioned button. 
		self.mainloop

def center(toplevel): # Function for centering all windows upon execution
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth() #function for finding resolution
    h = toplevel.winfo_screenheight() #function for finding resolution
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2 # find the middle of current resolution
    y = h/2 - size[1]/2 # find the middle of current resolution
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

if __name__ == "__main__": # Executes the main app (which then executes the other classes) and ties everyting together.
	app = MainApp()
	app.title("B.L.D.Z.R                                                                         ") # Title seen in top bar
	app.iconbitmap(icondirectory + 'BLDZR.ico') # icon seen in top left hand corner of prog window
	center(app) # Call Center all windows function
	app.mainloop() # ties all GUI windows/classes together


	#TODO#
	
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
		#Comodo (rm proc hacker)