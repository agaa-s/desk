from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Frame Test')

frame1 = ttk.Frame(
    root,
    height=200,
    width=300,
    relief='flat',
    borderwidth=5)
frame1.grid()

# 別の書き方
#frame1 = ttk.Frame(root)
#frame1['height'] = 200
#frame1['width'] = 300
#frame1['relief'] = 'sunken'  # flat (既定)、raised、 groove、ridge
#frame1['borderwidth'] = 5
#frame1.grid()


root.mainloop()


# http://python.keicode.com/advanced/tkinter-widget-frame.php
