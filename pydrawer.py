__author__ = "Essam Mohamed"

xes = list()
yes = list()
colors = list()
widths = list()



def about():
    tkinter.messagebox.showinfo("About", "I have been created by Essam Mohamed")


def color():
    selected_color = tkinter.colorchooser.askcolor()
    colors.append(selected_color[1])


class Application(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("PyFrame")
        self.root.maxsize(600, 600)
        self.root.minsize(600, 600)

        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=Application)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.settings = Menu(self.menu_bar, tearoff=0)
        self.settings.add_command(label="Frame BG color", command=self.bg_frame)
        self.settings.add_command(label="PenWidth", command=PenWidth)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings)
        self.delete_menu = Menu(self.menu_bar, tearoff=0)
        self.delete_menu.add_command(label="Clear", command=self.clear)
        self.menu_bar.add_cascade(label="Procedures", menu=self.delete_menu)
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.root.config(menu=self.menu_bar)

        # self.scroll = Scrollbar(self.root)
        # self.scroll.pack(side=RIGHT, fill=Y)

        self.frame = Frame(self.root, width=590, height=500)
        self.frame.pack()
        self.interact_frame = Frame(self.root)
        self.interact_frame.pack()
        self.can = Canvas(self.frame, width=590, height=500, bg="dark green")
        self.can.pack()
        self.can.bind("<Button-1>", self.event)
        self.lbl = Label(self.interact_frame, fg="dark green")
        self.lbl.grid(row=1, column=1)
        self.lin = Button(self.interact_frame, relief=FLAT, text="CreateLine", fg="white", bg="royal blue", command=self.create_line)
        self.lin.grid(row=2, column=0, padx=60)
        self.ovl = Button(self.interact_frame, relief=FLAT, text="CreateOval", fg="white", bg="royal blue", command=self.create_oval)
        self.ovl.grid(row=2, column=1, padx=60)
        self.color = Button(self.interact_frame, relief=FLAT, fg="white", bg="royal blue", text="ShapeColor", command=color)
        self.color.grid(row=2, column=2, padx=60)
        self.pol = Button(self.interact_frame, relief=FLAT, text="CreatePoly", fg="white", bg="royal blue", command=self.create_poly)
        self.pol.grid(row=3, column=0, padx=60, pady=3)
        self.arc = Button(self.interact_frame, relief=FLAT, text="Create_Arc", fg="white", bg="royal blue", command=self.create_arc)
        self.arc.grid(row=3, column=1, padx=60, pady=3)
        self.rec = Button(self.interact_frame, relief=FLAT, text="CreateRect", fg="white", bg="royal blue", command=self.create_rec)
        self.rec.grid(row=3, column=2, padx=60, pady=3)
        self.root.mainloop()

    def clear(self):
        self.can.create_rectangle(0, 0, 591, 501, fill="dark green")

    def bg_frame(self):
        bg_color = tkinter.colorchooser.askcolor()
        self.can.configure(bg=bg_color[1])

    def event(self, event):

        self.lbl.configure(text="X of the click was " + str(event.x) + " Y of the click was " + str(event.y))

        try:

            xes.append(event.x)
            yes.append(event.y)
            global x1
            x1 = xes[len(xes) - 2]
            global x2
            x2 = xes[len(xes) - 1]
            global x3
            x3 = xes[len(xes) - 3]
            global y1
            y1 = yes[len(yes) - 2]
            global y2
            y2 = yes[len(yes) - 1]
            global y3
            y3 = yes[len(yes) - 3]

        except IndexError:
            pass

    def create_line(self):
        try:
            self.can.create_line(x1, y1, x2, y2, width=widths[len(widths) - 1], fill=colors[len(colors) - 1])
        except IndexError:
            tkinter.messagebox.showwarning("", "Color hasn't been chosen or width hasn't been given a value")

    def create_oval(self):
        try:
            self.can.create_oval(x1, y1, x2, y2, width=widths[len(widths) - 1], fill=colors[len(colors) - 1])
        except IndexError:
            tkinter.messagebox.showwarning("", "Color hasn't been chosen or width hasn't been given a value")

    def create_poly(self):
        try:
            self.can.create_polygon(x1, y1, x2, y2, x3, y3, width=widths[len(widths) - 1], fill=colors[len(colors) - 1])
        except IndexError:
            tkinter.messagebox.showwarning("", "Color hasn't been chosen or width hasn't been given a value")

    def create_arc(self):
        try:
            self.can.create_arc(x1, y1, x2, y2, width=widths[len(widths) - 1], fill=colors[len(colors) - 1])
        except IndexError:
            tkinter.messagebox.showwarning("", "Color hasn't been chosen or width hasn't been given a value")

    def create_rec(self):
        try:
            self.can.create_rectangle(x1, y1, x2, y2, width=widths[len(widths) - 1], fill=colors[len(colors) - 1])
        except IndexError:
            tkinter.messagebox.showwarning("", "Color hasn't been chosen or width hasn't been given a value")


class PenWidth:
    def __init__(self):
        self.root = Tk()
        self.root.title("Width")
        self.root.maxsize(180, 70)
        self.root.minsize(180, 70)
        self.lbl = Label(self.root, text="Enter pen's width in pxs...")
        self.lbl.pack()
        self.w = Entry(self.root, text="2")
        self.w.pack()
        self.b = Button(self.root, text="Set", bg="royal blue", fg="white", command=self.set_width)
        self.b.pack()
        self.root.mainloop()

    def set_width(self):
        widths.append(self.w.get())

if __name__ == '__main__':
    from tkinter import *
    import tkinter.messagebox
    import tkinter.colorchooser
    app = Application()
