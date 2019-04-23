    # -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox


# 由于tkinter中没有ToolTip功能，所以自定义这个功能如下
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


# ===================================================================
def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# Create instance
win = tk.Tk()

# Add a title
win.title("Python 图形用户界面")

# Disable resizing the GUI
win.resizable(0, 0)

# Tab Control introduced here --------------------------------------
tabControl = ttk.Notebook(win)  # Create Tab Control

tab1 = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab1, text='第一页')  # Add the tab

tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2, text='第二页')  # Make second tab visible

tab3 = ttk.Frame(tabControl)  # Add a third tab
tabControl.add(tab3, text='第三页')  # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ~ Tab Control introduced here -----------------------------------------

# ---------------Tab1控件介绍------------------#
# We are creating a container tab3 to hold all other widgets
monty = ttk.LabelFrame(tab1, text='控件示范区1')
monty.grid(column=0, row=0, padx=8, pady=4)


# Modified Button Click Function
def clickMe():
    action.configure(text='Hello\n ' + puls())
    action.configure(state='disabled')  # Disable the Button Widget


# Changing our Label
ttk.Label(monty, text="输入文字:").grid(column=0, row=0, sticky='W')

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='W')

# Adding a Button
action = ttk.Button(monty, text="点击之后\n按钮失效", width=10, command=clickMe)
action.grid(column=2, row=1, rowspan=2, ipady=7)

ttk.Label(monty, text="请选择一本书:").grid(column=1, row=0, sticky='W')

# Adding a Combobox
book = tk.StringVar()
bookChosen = ttk.Combobox(monty, width=12, textvariable=book)
bookChosen['values'] = ('平凡的世界', '亲爱的安德烈', '看见', '白夜行')
bookChosen.grid(column=1, row=1)
bookChosen.current(0)  # 设置初始显示值，值为元组['values']的下标
bookChosen.config(state='readonly')  # 设为只读模式


# Spinbox callback
def _spin():
    value = spin.get()
    # print(value)
    scr.insert(tk.INSERT, value + '\n')


def _spin2():
    value = spin2.get()
    # print(value)
    scr.insert(tk.INSERT, value + '\n')

def puls():
    ad=1+int(name.get())
    ad=str(ad)
    return ad
    # print(ad)

# Adding 2 Spinbox widget using a set of values
spin = Spinbox(monty, from_=10, to=25, width=5, bd=8, command=_spin)
spin.grid(column=0, row=2)

spin2 = Spinbox(monty, values=('Python3入门', 'C语言', 'C++', 'Java', 'OpenCV'), width=13, bd=3, command=_spin2)
spin2.grid(column=1, row=2, sticky='W')

# Using a scrolled Text control
scrolW = 30;
scrolH = 5
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, row=3, sticky='WE', columnspan=3)

# Add Tooltip
createToolTip(spin, '这是一个Spinbox.')
createToolTip(spin2, '这是一个Spinbox.')
createToolTip(action, '这是一个Button.')
createToolTip(nameEntered, '这是一个Entry.')
createToolTip(bookChosen, '这是一个Combobox.')
createToolTip(scr, '这是一个ScrolledText.')

# 一次性控制各控件之间的距离
for child in monty.winfo_children():
    child.grid_configure(padx=3, pady=1)
# 单独控制个别控件之间的距离

# Place cursor into name Entry
nameEntered.focus()
#======================
# Start GUI
#======================
win.mainloop()
