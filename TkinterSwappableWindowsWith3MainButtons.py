import Tkinter as tk
import subprocess

TITLE_FONT = ("Helvetica", 18, "bold")

class MainApp(tk.Tk):

	def __init__(self, *args, **kwargs): # the container is where we'll stack a bunch of frames on top of each other, then the one we want visible will be raised above the others
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.grid(column=5, row=15)
		#container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0)
		container.grid_columnconfigure(0)

		self.frames = {} # put all of the pages in the same location; the one on the top of the stacking order will be the one that is visible
		for F in (StartPage, PageOne, PageTwo, PageThree):
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

		#label = tk.Label(self)
		#label.grid(column=9, row=2)

		StartPageButton1 = tk.Button(self, width=20, height=5, text="Page One", fg="blue", bg="orange", command=lambda: controller.show_frame(PageOne))
		StartPageButton2 = tk.Button(self, width=20, height=5, text="Page Two", command=lambda: controller.show_frame(PageTwo))
		StartPageButton3 = tk.Button(self, width=20, height=5, text="Page Three", command=lambda: controller.show_frame(PageThree))

		StartPageButton1.grid(row=1, column=2, padx=10, pady=10)
		StartPageButton2.grid(row=3, column=1, padx=10, pady=10)
		StartPageButton3.grid(row=3, column=3, padx=10, pady=10)

class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		BackButton0 = tk.Button(self, width =20, height = 5, text="Go Back", command=lambda: controller.show_frame(StartPage))

		PageOneButton1 = tk.Button(self, width=20, height=5, text="Function1", fg="white", bg="blue", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton2 = tk.Button(self, width=20, height=5, text="Function2", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton3 = tk.Button(self, width=20, height=5, text="Function3", command=lambda: subprocess.Popen('', shell=True))

		PageOneButton4 = tk.Button(self, width=20, height=5, text="Function4", fg="white", bg="blue", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton5 = tk.Button(self, width=20, height=5, text="Function5", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton6 = tk.Button(self, width=20, height=5, text="Function6", command=lambda: subprocess.Popen('', shell=True))

		PageOneButton7 = tk.Button(self, width=20, height=5, text="Function7", fg="white", bg="blue", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton8 = tk.Button(self, width=20, height=5, text="Function8", command=lambda: subprocess.Popen('', shell=True))
		PageOneButton9 = tk.Button(self, width=20, height=5, text="Function9", command=lambda: subprocess.Popen('', shell=True))

		BackButton0.grid(row=0, column=2, padx=10, pady=10)

		PageOneButton1.grid(row=1, column=1, padx=10, pady=10)
		PageOneButton2.grid(row=1, column=2, padx=10, pady=10)
		PageOneButton3.grid(row=1, column=3, padx=10, pady=10)

		PageOneButton4.grid(row=2, column=1, padx=10, pady=10)
		PageOneButton5.grid(row=2, column=2, padx=10, pady=10)
		PageOneButton6.grid(row=2, column=3, padx=10, pady=10)

		PageOneButton7.grid(row=3, column=1, padx=10, pady=10)
		PageOneButton8.grid(row=3, column=2, padx=10, pady=10)
		PageOneButton9.grid(row=3, column=3, padx=10, pady=10)

		#label = tk.Label(self, text="Page 1", font=TITLE_FONT)
		#label.pack(side="top", fill="x", pady=10)

		#button = tk.Button(self, width =20, height = 5, text="Go Back", command=lambda: controller.show_frame(StartPage))
		#button.pack()

class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text="Page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		
		button = tk.Button(self, width =20, height = 5, text="Go Back", command=lambda: controller.show_frame(StartPage))
		button2 = tk.Button(self, width =20, height = 5, text="Command One", command=lambda: subprocess.Popen('', shell=True))

		button.pack()
		button2.pack()

class PageThree(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page 3", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)

		button = tk.Button(self, width =20, height = 5, text="Go Back", command=lambda: controller.show_frame(StartPage))
		button2 = tk.Button(self, width =20, height = 5, text="Command One", command=lambda: subprocess.Popen('', shell=True))
		
		button.pack()
		button2.pack()

if __name__ == "__main__":
	app = MainApp()
	app.title("Main App                                                                                                         ")
	app.mainloop()