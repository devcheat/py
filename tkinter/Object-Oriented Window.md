Tkinter Object-Oriented Window
===

## Defining a Tkinter object-oriented window
The following simple program creates a root window and displays it on the screen:
```py
import tkinter as tk
root = tk.Tk()
root.mainloop()
```

When the program is getting more complex, you can use an object-oriented programming approach to make the code more organized.

he following program achieves the same result as the program above, but use a `class` instead:
```py
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = App()
    app.mainloop()
```
### How it works.

- First, define an `App` class that inherits from the `tk.Tk` class. Inside the `__init__()` method, call the `__init__()` method of the `tk.Tk` class.
- Second, create a new instance of the `App` class and call the `mainloop()` method to display the root window.

## Another example of an object-oriented window in Tkinter
The following class represents a window that consists of a label and a button. When you click the button, the program displays a message box:
```py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('My Awesome App')
    self.geometry('300x50')

    # label
    self.label = ttk.Label(self, text='Hello, Tkinter!')
    self.label.pack()

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
  app = App()
  app.mainloop()
```
### How it works.

- First, create a label and button in the `__init__()` method of App class.
- Second, assign the `button_clicked()` method to the command option of the button. Inside the `button_clicked()` method, display a message box.
- Third, move the application bootstrapping to the `if __name__ = "main"` block.

## Summary
- Use an object-oriented programming approach to make the code more organized.
- Define a class that inherits from the tk.Tk class. Always, call the `super().__init__()` from the parent class in the child class.


Tkinter Object-Oriented Frames
===

To inherit the ttk.Frame class, you use the following syntax:
```py
class MainFrame(ttk.Frame):
    pass
```
Since a Frame needs a container, you need to add an argument to its __init__() method and call the __init__() method of the ttk.Frame class like this:
```py
class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)   
```
The following shows the complete MainFrame class that has a label and a button. When you click the button, it shows a message box:
```py
class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack(**options)

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack(**options)

        # show the frame on the container
        self.pack(**options)

    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')
```
The following defines an App class that inherits from the Tk class:
```py
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x100')
```
And you can bootstrap the application via the if __name__ == "__main__" block.
```py
if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
```

In this code:
- First, create a new instance of the App class.
- Second, create a new instance of the MainFrame class and set its container to the app instance.
- Third, start the application by calling the app(). It’ll execute the __call__() method that will invoke the mainloop() of the root window.

Put it all together:
```py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack(**options)

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack(**options)

        # show the frame on the container
        self.pack(**options)

    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x100')


if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
```

Output:

<img src="data:image/png;base64,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">

## Summary
- Subclass the `ttk.Frame` and initialize the widgets on the frame.
- Use the subclass of the `ttk.Frame` in a root window.
