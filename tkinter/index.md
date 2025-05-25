# Tkinter Tutorial: A Comprehensive Overview

**Tkinter** is the standard GUI (Graphical User Interface) toolkit for Python. It provides a simple way to create desktop applications with various widgets like buttons, labels, text boxes, and more.

## Getting Started

To use Tkinter, you first need to import it:

```python
import tkinter as tk
```

## Creating Your First Window

Here's how to create a basic window:

```python
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My Tkinter App")
root.geometry("300x200")

# Start the main event loop
root.mainloop()
```

## Adding Widgets

## 1. Labels

### Synatx:
```
label = tk.Label(root, options)
```

### Tkinter Label Options
- `anchor`: This option is used to control the positioning of the text if the widget has more space than required for the text. The default is anchor=CENTER, which centers the text in the available space.
- `bg`: This option is used to set the normal background color displayed behind the label and indicator.
height:This option is used to set the vertical dimension of the new frame.
width:Width of the label in characters (not pixels!). If this option is not set, the label will be sized to fit its contents.
- `bd`:This option is used to set the size of the border around the indicator. Default bd value is set on 2 pixels.
- `font`:If you are displaying text in the label (with the text or textvariable option), the font option is used to specify in what font that text in the label will be displayed.
cursor:It is used to specify what cursor to show when the mouse is moved over the label. The default is to use the - standard cursor.
- `textvariable`: As the name suggests it is associated with a Tkinter variable (usually a StringVar) with the label. If the variable is changed, the label text is updated.
- `bitmap`:It is used to set the bitmap to the graphical object specified so that, the label can represent the graphics instead of text.
- `fg`:The label clior, used for text and bitmap labels. The default is system specific. If you are displaying a bitmap, this is the clior that will appear at the position of the 1-bits in the bitmap.
- `image`: This option is used to display a static image in the label widget.
- `padx`:This option is used to add extra spaces between left and right of the text within the label.The default value for this option is 1.
- `pady`:This option is used to add extra spaces between top and bottom of the text within the label.The default value for this option is 1.
- `justify`:This option is used to define how to align multiple lines of text. Use LEFT, RIGHT, or CENTER as its values. Note that to position the text inside the widget, use the anchor option. Default value for justify is CENTER.
- `relief`: This option is used to specify appearance of a decorative border around the label. The default value for this option is FLAT.
- `underline`:This
- `wraplength`:Instead of having only one line as the label text it can be broken into to the number of lines where each line has the number of characters specified to this option.

### Example
```python
import tkinter as tk

root = tk.Tk()
root.title("Label Example")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()
```
### ttk example 
```py
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter.Ttk Widgets Example")

# Create a label widget
label = ttk.Label(root, text="Hello, Tkinter.Ttk")
label.pack()

```

## 2. Buttons

Buttons trigger actions when clicked.

### Syntax:
```
button = tk.Button(root, options)
button = ttk.Button(root, options)
```

### Tkinter Button Options

- `activebackground`: Background color when the button is under the cursor.
- `activeforeground`: Foreground color when the button is under the cursor.
- `anchor`: Width of the border around the outside of the button
- `bd` or `borderwidth`: Width of the border around the outside of the button
- `bg` or `background`: Normal background color.
- `command`: Function or method to be called when the button is clicked.
- `cursor`: Selects the cursor to be shown when the mouse is over the button.
- `text`: Text displayed on the button.
- `disabledforeground`: Foreground color is used when the button is disabled.
- `fg` or `foreground`: Normal foreground (text) color.
- `font`: Text font to be used for the button’s label.
- `height`: Height of the button in text lines
- `highlightbackground`: Color of the focus highlight when the widget does not have focus.
- `highlightcolor`: The color of the focus highlight when the widget has focus.
- `highlightthickness`: Thickness of the focus highlight.
- `image`: Image to be displayed on the button (instead of text).
- `justify`: tk.LEFT to left-justify each line; tk.CENTER to center them; or tk.RIGHT to right-justify.
- `overrelief`: The relief style to be used while the mouse is on the button; default relief is tk.RAISED.
- `padx`, `pady`: padding left and right of the text. / padding above and below the text.
- `width`: Width of the button in letters (if displaying text) or pixels (if displaying an image).
- `underline`: Default is -1, underline=1 would underline the second character of the button’s text.
- `width`: Width of the button in letters
- `wraplength`: If this value is set to a positive number, the text lines will be wrapped to fit within this length.

### Methods
- `flash()`: Causes the button to flash several times between active and normal colors. Leaves the button in the state it was in originally. Ignored if the button is disabled.
- `invoke()`: Calls the button’s command callback, and returns what that function returns. Has no effect if the button is disabled or there is no callback.


### Example:
```python
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Button Example")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()
```

### ttk Example
```py
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter.Ttk Widgets Example")

# Create a button widget
button = ttk.Button(root, text="Click Me")
button.pack()

# Run the application
root.mainloop()
```

### Example Using Options:
```py
import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()

# Creating a button with specified options
button = tk.Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()
```



## 3. Entry Widgets

Entry widgets allow users to input text.

### Synatx:
```
entry = tk.Entry(root, options)
```

### Tkinter LabEntry Options
- `bg` : The normal background color displayed behind the label and indicator. 
- `bd` : The size of the border around the indicator. Default is 2 pixels. 
- `font` : The font used for the text. 
- `fg` : The color used to render the text. 
- `justify` : If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT. 
- `relief` : With the default value, relief=FLAT. You may set this option to any of the other styles like : SUNKEN, RIGID, RAISED, GROOVE 
- `show` : Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each character as an asterisk, set show=”*”. 
- `textvariable` : In order to be able to retrieve the current text from your entry widget, you must set this option to an instance of the StringVar class.

### Methods: The various methods provided by the entry widget are: 

- `get()` : Returns the entry’s current text as a string. 
- `delete()` : Deletes characters from the widget 
- `insert ( index, 'name') `: Inserts string ‘name’ before the character at the given index. 


### Example:

```python
import tkinter as tk

def show_entry():
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")

root = tk.Tk()
root.title("Entry Example")

label = tk.Label(root, text="Enter something:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=show_entry)
button.pack()

root.mainloop()
```

### ttk example
```py
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter.Ttk Widgets Example")

# Create an entry widget
entry = ttk.Entry(root)
entry.pack()

# Run the application
root.mainloop()
```

## 4. Checkbuttons

Checkbuttons allow users to select multiple options.

### Synatx:
```
check1 = tk.Checkbutton(root, options)
```

### Tkinter Checkbutton Options
The following are commonly used Options that can be used with this widget:

- `activebackground`: This option used to represent the background color when the checkbutton is under the cursor.
- `activeforeground`: This option used to represent the foreground color when the checkbutton is under the cursor.
- `bg`: This option used to represent the normal background color displayed behind the label and indicator.
- `bitmap`: This option used to display a monochrome image on a button.
- `bd`: This option used to represent the size of the border around the indicator and the default value is 2 pixels.
- `command`: This option is associated with a function to be called when the state of the checkbutton is changed.
- `cursor`: By using this option, the mouse cursor will change to that pattern when it is over the checkbutton.
disabledforeground: The foreground color used to render the text of a disabled checkbutton. The default is a stippled version of the default foreground color.
- `font`: This option used to represent the font used for the text.
- `fg`: This option used to represent the color used to render the text.
- `height`: This option used to represent the number of lines of text on the checkbutton and it’s default value is 1.
- `highlightcolor`: This option used to represent the color of the focus highlight when the checkbutton has the focus.
- `image`: This option used to display a graphic image on the button.
- `justify`: This option used to control how the text is justified: CENTER, LEFT, or RIGHT.
- `offvalue`: The associated control variable is set to 0 by default if the button is unchecked. We can change the state of an unchecked variable to some other one.
- `onvalue`: The associated control variable is set to 1 by default if the button is checked. We can change the state of the checked variable to some other one.
- `padx`: This option used to represent how much space to leave to the left and right of the checkbutton and text. It’s default value is 1 pixel.
- `pady`: This option used to represent how much space to leave above and below the checkbutton and text. It’s default value is 1 pixel.
- `relief`: The type of the border of the checkbutton. It’s default value is set to FLAT.
selectcolor: This option used to represent the color of the checkbutton when it is set. The Default is selectcolor=”red”.
- `selectimage`: The image is shown on the checkbutton when it is set.
- `state`: It represents the state of the checkbutton. By default, it is set to normal. We can change it to DISABLED to make the checkbutton unresponsive. The state of the checkbutton is ACTIVE when it is under focus.
- `text`: This option used use newlines (“\n”) to display multiple lines of text.
underline: This option used to represent the index of the character in the text which is to be underlined. The indexing - `starts` with zero in the text.
- `variable`: This option used to represents the associated variable that tracks the state of the checkbutton.
- `width`: This option used to represents the width of the checkbutton. and also represented in the number of characters that are represented in the form of texts.
- `wraplength`: This option will be broken text into the number of pieces.

### Methods
Methods used in this widgets are as follows:

- `deselect()`: This method is called to turn off the checkbutton.
- `flash()`: The checkbutton is flashed between the active and normal colors.
- `invoke()`: This method will invoke the method associated with the checkbutton.
- `select()`: This method is called to turn on the checkbutton.
- `toggle()`: This method is used to toggle between the different Checkbuttons.

### Example
```python
import tkinter as tk

def show_selection():
    selections = []
    if var1.get():
        selections.append("Option 1")
    if var2.get():
        selections.append("Option 2")
    label.config(text=", ".join(selections))

root = tk.Tk()
root.title("Checkbutton Example")

var1 = tk.IntVar()
var2 = tk.IntVar()

check1 = tk.Checkbutton(root, text="Option 1", variable=var1, command=show_selection)
check1.pack()

check2 = tk.Checkbutton(root, text="Option 2", variable=var2, command=show_selection)
check2.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
```

### ttk example
```py
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter.Ttk Widgets Example")

chkbtn1 = ttk.Checkbutton(root, text ='Checkbutton1',takefocus = 0)
.place(x = 140, y = 40)
chkbtn2 = ttk.Checkbutton(root, text ='Checkbutton2',takefocus = 0)
.place(x = 140, y = 60)

# Run the application
root.mainloop()                
```

## 5. Radio Buttons

Radio buttons allow users to select one option from multiple choices.

```python
import tkinter as tk

def show_choice():
    label.config(text=f"You selected: {var.get()}")

root = tk.Tk()
root.title("Radiobutton Example")

var = tk.StringVar(value="Option 1")

radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=show_choice)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=show_choice)
radio2.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
```

## 6. Listbox

Listboxes allow users to select from a list of options.

### Synbatx:
```
listbox = Listbox(root, bg, fg, bd, height, width, font, ..) 
```

### Optional parameters

- `root` – root window.
- `bg` – background colour
- `fg` – foreground colour
- `bd` – border
- `height` – height of the widget.
- `width` – width of the widget.
- `font` – Font type of the text.
- `highlightcolor` – The colour of the list items when focused.
- `yscrollcommand` – for scrolling vertically.
- `xscrollcommand` – for scrolling horizontally.
- `cursor` – The cursor on the widget which can be an arrow, a dot etc.

### Common methods

- `yview` – allows the widget to be vertically scrollable.
- `xview` – allows the widget to be horizontally scrollable.
- `get()` – to get the list items in a given range.
- `activate(index)` – to select the lines with a specified index.
- `size()` – return the number of lines present.
- `delete(start, last)` – delete lines in the specified range.
- `nearest(y)` – returns the index of the nearest line.
- `curseselection()` – returns a tuple for all the line numbers that are being selected.


### Example:
```python
import tkinter as tk

def show_selection():
    selected = listbox.curselection()
    label.config(text=f"You selected: {listbox.get(selected)}")

root = tk.Tk()
root.title("Listbox Example")

listbox = tk.Listbox(root)
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")
listbox.pack()

button = tk.Button(root, text="Show Selected", command=show_selection)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
```

## 7. Scrollbar
It refers to the slide controller which will be used to implement listed widgets. The general syntax is:
```
w = Scrollbar(root, option=value)
```

There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas.
```py
from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
    
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()
```

## 8. Menu
It is used to create all kinds of menus used by the application. The general syntax is:
```
w = Menu(master, option=value)
```
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of this widget.
```py
from tkinter import *

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()
```

## 9. Combobox
Combobox widget is created using the ttk.Combobox class from the tkinter.ttk module. The values for the Combobox are specified using the values parameter.

The default value is set using the set method. An event handler function on_select is bound to the Combobox using the bind method, which updates a label with the selected item whenever an item is selected.
```py
import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

# Create a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo_box.pack(pady=5)

# Set default value
combo_box.set("Option 1")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", on_select)

root.mainloop()
```

## 10. Scale
It is used to provide a graphical slider that allows to select any value from that scale. The general syntax is:

### Syntax:
```
w = Scale(root, option=value)
```
### Example
```py
from tkinter import *

master = Tk()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()
```

## 11. TopLevel
This widget is directly controlled by the window manager. It don’t need any parent window to work on.The general syntax is:

### Synatx:
```
w = TopLevel(master, option=value)
```

### Example:
```py
from tkinter import *

root = Tk()
root.title('killercodes')
top = Toplevel()
top.title('Python3.9')
top.mainloop()
```

## 12. Message
It refers to the multi-line and non-editable text. It works same as that of Label. The general syntax is:
### Synatx:
```
w = Message(root, option=value)
```
### Example:
```py
from tkinter import *

main = Tk()
ourMessage = 'This is Matrix'
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop()
```

## 13. MenuButton
It is a part of top-down menu which stays on the window all the time. Every menubutton has its own functionality. The general syntax is:

### Syntax:
```
w = MenuButton(master, option=value)
```

### Syntax:
```py
from tkinter import *

top = Tk() 
mb = Menubutton ( top, text = "Killercodes") 
mb.grid() 

mb.menu = Menu ( mb, tearoff = 0 ) 
mb["menu"] = mb.menu

cVar = IntVar() 
aVar = IntVar() 
mb.menu.add_checkbutton ( label ='Contact', variable = cVar ) 
mb.menu.add_checkbutton ( label = 'About', variable = aVar ) 

mb.pack() 
top.mainloop() 
```

## 14. Progressbar
Tkinter application with a Progressbar widget and a button to start the progress. When the button is clicked, the progressbar fills up to 100% over a short period, simulating a task that takes time to complete.

### Example:
```py
import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.05)  
        progress['value'] = i
        # Update the GUI
        root.update_idletasks()  
    progress.stop()

root = tk.Tk()
root.title("Progressbar Example")

# Create a progressbar widget
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# Button to start progress
start_button = tk.Button(root, text="Start Progress", command=start_progress)
start_button.pack(pady=10)

root.mainloop()
```

## 15. SpinBox
It is an entry of ‘Entry’ widget. Here, value can be input by selecting a fixed value of numbers.The general syntax is:

### Syntax:
```
w = SpinBox(master, option=value)
```

### Example:
```py
from tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=10)
w.pack()

mainloop()
```

## 16. Text
To edit a multi-line text and format the way it has to be displayed. The general syntax is:

### Synatx:
```
w  =Text(root, option=value)
```

### Example:
```py
from tkinter import *

root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'Killer \nCODES\n')

mainloop()
```

## 17. Canvas
It is used to draw pictures and other complex layout like graphics, text and widgets. The general syntax is:

### Syntax:
```
w = Canvas(root, option=value)
```

### Example:
```py
from tkinter import *

root = Tk()

w = Canvas(root, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )

mainloop()
```

## 18. PannedWindow
It is a container widget which is used to handle number of panes arranged in it. The general syntax is:

### Syntax:
```
w = PannedWindow(master, option=value)
```

### Example:
```py
from tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = Entry(m1, bd=5)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
top = Scale(m2, orient=HORIZONTAL)
m2.add(top)

mainloop()
```

## 19. Frame 

A frame is a rectangular region on the screen. A frame can also be used as a foundation class to implement complex widgets. It is used to organize a group of widgets.

### Syntax:
```
Syntax:  w = frame(root, options)
```


### Tkinter Frame Options
The following are commonly used Options that can be used with this widget:

- `bg`: This option used to represent the normal background color displayed behind the label and indicator.
- `bd`: This option used to represent the size of the border around the indicator and the default value is 2 pixels.
- `cursor`: By using this option, the mouse cursor will change to that pattern when it is over the frame.
- `height`: The vertical dimension of the new frame.
- `highlightcolor`: This option used to represent the color of the focus highlight when the frame has the focus.
- `highlightthickness`: This option used to represent the color of the focus highlight when the frame does not have focus.
- `highlightbackground`: This option used to represent the thickness of the focus highlight..
- `relief`: The type of the border of the frame. It’s default value is set to FLAT.
- `width`: This option used to represents the width of the frame.

### Example:
```py
from tkinter import *

root = Tk()

frame = tk.Frame(root,bg='lightblue', bd=3, cursor='hand2', height=100,highlightcolor='red', highlightthickness=2, highlightbackground='black', relief=tk.RAISED, width=20)
frame.pack(padx=20, pady=20)

# Create a label
label = tk.Label(frame, text="Hello, Tkinter!")
label.pack()

window.mainloop()

```

## 20. Label Frame

### Synatx:
```
labelframe = ttk.LabelFrame(root, options) 
```

### Example:
```py
import tkinter as tk 
import tkinter.ttk as ttk 
  
# initialize the tkinter window 
root = tk.Tk()  
  
# provide some width and height 
root.geometry("300x300")  
  
# created a label frame with title "Group" 
labelframe = ttk.LabelFrame(root, text = "Label frame") 
  
# provide padding  
labelframe.pack(padx=30, pady=30)  
  
# created the text label inside the the labelframe 
left = tk.Label(labelframe, text="Label inside Labelframe")  
left.pack() 
  
root.mainloop()
```

## 21. Treeview

### Synatx
```
treev = ttk.Treeview(root, options)
```

### Example
```py
from tkinter import ttk
import tkinter as tk
 
# Creating tkinter window
window = tk.Tk()
window.resizable(width = 1, height = 1)
 
# Using treeview widget
treev = ttk.Treeview(window, selectmode ='browse')
 
# Calling pack method w.r.to treeview
treev.pack(side ='right')
 
# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(window, 
                           orient ="vertical", 
                           command = treev.yview)
 
# Calling pack method w.r.to vertical 
# scrollbar
verscrlbar.pack(side ='right', fill ='x')
 
# Configuring treeview
treev.configure(xscrollcommand = verscrlbar.set)
 
# Defining number of columns
treev["columns"] = ("1", "2", "3")
 
# Defining heading
treev['show'] = 'headings'
 
# Assigning the width and anchor to  the
# respective columns
treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')
 
# Assigning the heading names to the 
# respective columns
treev.heading("1", text ="Name")
treev.heading("2", text ="Sex")
treev.heading("3", text ="Age")
 
# Inserting the items and their features to the 
# columns built
treev.insert("", 'end', text ="L1", 
             values =("Nidhi", "F", "25"))
treev.insert("", 'end', text ="L2",
             values =("Nisha", "F", "23"))
treev.insert("", 'end', text ="L3",
             values =("Preeti", "F", "27"))
treev.insert("", 'end', text ="L4",
             values =("Rahul", "M", "20"))
treev.insert("", 'end', text ="L5", 
             values =("Sonu", "F", "18"))
treev.insert("", 'end', text ="L6",
             values =("Rohit", "M", "19"))
treev.insert("", 'end', text ="L7", 
             values =("Geeta", "F", "25"))
treev.insert("", 'end', text ="L8", 
             values =("Ankit", "M", "22"))
treev.insert("", 'end', text ="L10", 
             values =("Mukul", "F", "25"))
treev.insert("", 'end', text ="L11",
             values =("Mohit", "M", "16"))
treev.insert("", 'end', text ="L12",
             values =("Vivek", "M", "22"))
treev.insert("", 'end', text ="L13",
             values =("Suman", "F", "30"))
 
# Calling mainloop
window.mainloop()
```


---
## Layout Management

### 1. Pack

The `pack()` method organizes widgets in blocks before placing them in the parent widget.

```python
# Example with pack
label1 = tk.Label(root, text="Label 1")
label1.pack(side=tk.TOP)

label2 = tk.Label(root, text="Label 2")
label2.pack(side=tk.BOTTOM)
```

### 2. Grid

The `grid()` method organizes widgets in a table-like structure.

```python
# Example with grid
label1 = tk.Label(root, text="Row 0, Column 0")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Row 0, Column 1")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Row 1, Column 0")
label3.grid(row=1, column=0)
```

### 3. Place

The `place()` method places widgets at an exact position you specify.

```python
# Example with place
label = tk.Label(root, text="I am placed at (50, 50)")
label.place(x=50, y=50)
```



## Conclusion

Tkinter provides a wide array of widgets and layout options for creating user-friendly desktop applications. This tutorial covers the basics, allowing you to build upon these examples to create more complex applications as needed! Feel free to experiment by combining different widgets and layout managers.
