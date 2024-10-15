Tkinter Entry
===

## Introduction to Tkinter Entry widget
The Entry widget allows you to enter a single-line text. In Tkinter, to create a textbox, you use the Entry widget:

```py
textbox = ttk.Entry(master, **options)
```
In this syntax:

- The master is the parent frame or window. on which you want to place the widget.
- The options is one or more keyword arguments used to configure the Entry widget.

> Note that if you want to enter multi-line text, you can use the Text widget.

To get the current text of a Entry widget as a string, you use the `get()` method:
```py
textbox.get()
```

Typically, you associate the current value of the textbox with a StringVar object like this:
```py
text = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)
```

In this syntax:
- First, create a new instance of the `StringVar` class. The text will be the value holder for a string variable.
- Second, assign the text variable to the `textvariable` of the `Entry` widget.

In this case, you can use call the `get()` method of the `StringVar()` object to get the current value of the entry widget:
```py
text.get()
```

## Setting the focus to the Tkinter Entry widget
To provide a better user experience, you can move the focus to the first Entry widget after the window appears. Once the Entry widget has focus, it’s ready to accept the user input.

To do it, you use the focus() method of the Entry widget like this:
```py
textbox.focus()
```
## Showing a Tkinter password entry
To hide sensitive information on the Entry widget e.g., a password, you can use the show option.

The following creates a password entry. When you enter a password, it doesn’t show the actual characters but the asterisks (*) specified in the show option:
```py
password = tk.StringVar()
password_entry = ttk.Entry(
    root,
    textvariable=password,
    show='*'
)
password_entry.pack()
```

## Tkinter Entry widget example
The following program shows how to use the Entry widgets to create a sign-in form:
```py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(
        title='Information',
        message=msg
    )


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)


root.mainloop()
```
Output:

<img src="data:image/png;base64,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">

### How it works.

First, create two string variables to hold the current text of the email and password Entry widgets:
```py
# store email address and password
email = tk.StringVar()
password = tk.StringVar()
```
Second, create an email Entry widget and associate it with the email variable:
```py
email_entry = ttk.Entry(signin, textvariable=email)
```
The following sets focus on the email entry:
```py
email_entry.focus()
```
Third, create the password entry widget and assign the password variable to its textvariable:
```py
password_entry = ttk.Entry(signin, textvariable=password, show="*")
```
Finally, display a message box that shows the entered email and password if the login button is clicked.

## Summary
- Use the `ttk.Entry` widget to create a textbox.
- Use an instance of the `StringVar()` class to associate the current text of the Entry widget with a string variable.
- Use the show option to create a password entry.