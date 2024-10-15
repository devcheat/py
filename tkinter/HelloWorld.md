Tkinter Hello, World!
===

## Creating a window
The following program shows how to display a window on the screen:
```py
import tkinter as tk

root = tk.Tk()
root.mainloop()
```

### How it works.

First, import the tkinter module as tk to the program:
```py
import tkinter as tk
```
Second, create an instance of the tk.Tk class that will create the application window:
```py
root = tk.Tk()
```
By convention, the main window in Tkinter is called root. But you can use any other name like main.

Third, call the mainloop() method of the main window object:
```py
root.mainloop()
```
The ```mainloop()``` method ensures the main window remains visible on the screen.

If you don’t call the ```mainloop()``` method, the main window will display and disappear almost instantly – too quickly to perceive its appearance.

Additionally, the ```mainloop()``` method ensures the main window continues to display and run until you close it.

Typically, in a Tkinter program, you place the call to the ```mainloop()``` method as the last statement after creating the widgets.

## Troubleshooting
The tkinter module is a built-in Python module. But sometimes, it is not the case. For example, on Ubuntu, you may encounter the following error:
```
ImportError: No module named Tkinter
```

In this case, you need to install tkinter module using the following command line:
```bash
sudo apt-get install python3-tk
```

## Displaying a label
Now, let’s place a component on the window. In Tkinter, these components are referred to as widgets.

The following code adds a label widget to the root window:
```py
import tkinter as tk

root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window displaying
root.mainloop()
```