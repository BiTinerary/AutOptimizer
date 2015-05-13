import Tkinter as tk
import subprocess


TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (StartPage, AutOptimizer, HardwareTester, RepairProgs):
			frame = F(container, self)
			self.frames[F] = frame
			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, c):
		'''Show a frame for the given class'''
		frame = self.frames[c]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="B.L.D.Z.R", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10, padx=250)

		StartPageButton1 = tk.Button(self, width=20, height=5, text="AutOptimizer", command=lambda: controller.show_frame(AutOptimizer))
		StartPageButton2 = tk.Button(self, width=20, height=5, text="HardwareTester", command=lambda: controller.show_frame(HardwareTester))
		StartPageButton3 = tk.Button(self, width=20, height=5, text="Diagnostic and\nRepair Progs", command=lambda: controller.show_frame(RepairProgs))
		
		StartPageButton1.pack(side="right", padx=25, pady=25)
		StartPageButton2.pack(side="left", padx=25, pady=25)
		StartPageButton3.pack(side="top", padx=25, pady=25)


class AutOptimizer(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame(StartPage))

		button2 = tk.Button(self, width =30, height = 5, text="subprocess", command=lambda: subprocess.Popen('taskschd.msc', shell=True))

		button3 = tk.Button(self, width =30, height = 5, text="subprocess", command=lambda: subprocess.Popen('services.msc', shell=True))

		button.pack()
		button2.pack()
		button3.pack()


class HardwareTester(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page",
						   command=lambda: controller.show_frame(StartPage))
		button.pack()

class RepairProgs(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page",
						   command=lambda: controller.show_frame(StartPage))
		button.pack()


if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()