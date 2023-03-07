import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pylab as pl

class Aplikation(tk.Tk):
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl=tk.Label(self, text="Vyber soubor")
        self.lbl.pack()
        self.chooseBtn = tk.Button(self, text="...", command=self.choose )
        self.chooseBtn.pack()
        self.showBtn = tk.Button(self, text="Show", command=self.show )
        self.showBtn.pack()
        self.quitBtn = tk.Button(self, text="Quit", command=self.quit )
        self.quitBtn.pack()

    def choose(self):
        self.filename = filedialog.askopenfilename()
        self.lbl.config(text=self.filename)

    def show(self):
        if not self.filename:
            return
        axisx = []
        axisy = []
        with open(self.filename, "r") as f:
            while line := f.readline():
                x, y = line.split()
                axisx.append(float(x))
                axisy.append(float(y))
            pl.plot(axisx, axisy)
            pl.show()
    
    def quit(self, event=None):
        super().quit()


app = Aplikation()
app.mainloop()

