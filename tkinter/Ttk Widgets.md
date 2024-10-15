Ttk Widgets
===

## Introduction to Tk themed widgets
Tkinter has two generations of widgets:

The old classic tk widgets. Tkinter introduced them in 1991.
The newer themed ttk widgets added in 2007 with Tk 8.5. The newer Tk themed widgets replace many (but not all) classic widgets.
Note that ttk stands for Tk themed. Therefore, Tk themed widgets are the same as ttk widgets

The tkinter.ttk module contains all the new ttk widgets. It’s a good practice to always use themed widgets whenever they’re available.

The following statements import the classic and the new Tk themed widgets:
```py
import tkinter as tk
from tkinter import ttk
```
And the following program illustrates how to create classic and themed labels:
```py
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

root.mainloop()
```
Output:

<img src="data:image/png;base64,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">

They look similar. However, their appearances depend on the platform on which the program runs.

## Advantages of using Tk themed widgets
By using the Tk themed widgets, you gain the following advantages:

- Separating the widget’s behavior and appearance – the ttk widgets attempt to separate the code that implements the widgets’ behaviors from their appearance through the styling system.
- Native look & feel – the ttk widgets have the native look and feel of the platform on which the program runs.
- Simplify the state-specific widget behaviors – the ttk widgets simplify and generalize the state-specific widget behavior.

## The ttk widgets
The following ttk widgets replace the Tkinkter widgets with the same names:

- Button
- Checkbutton
- Entry
- Frame
- Label
- LabelFrame
- Menubutton
- PanedWindow
- Radiobutton
- Scale
- Scrollbar
- Spinbox

And the following widgets are new and specific to ttk:

- Combobox
- Notebook
- Progressbar
- Separator
- Sizegrip
- Treeview
