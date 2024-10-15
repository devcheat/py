Tkinter Frame
===


## Introduction to Tkinter Frame widget
A frame is a widget that displays as a simple rectangle. Typically, you use a frame to organize other widgets both visually and at the coding level.

To create a frame, you use the ttk.Frame class:
```
frame = ttk.Frame(master, **options)
```
A frame has various configuration objects which determine its appearance.

Object|Description
--|--
borderwidth	| Specify the border width of the frame. It defaults to zero
class_	|Set widget class name
cursor	|Change the cursor appearance when the mouse cursor is over the frame
height	|Set the height of the frame.
padding	|To create padding inside the frame and outside of the contained widgets.
relief	|Specify the relief style for the border. To make it effective, you also need to set the borderwidth.
style	|Specify custom widget custom style name
takefocus	|A boolean value specifies whether the frame is visited during focus traversal. By default, it is False. So the frame widget does not accept focus.
width	|Set the width of the frame.

## Frame size
The size of a frame is determined by the size and layout of the widgets it contains. Also, you can explicitly specify the height and width of the frame when creating it:

```py
frame = ttk.Frame(master, height, width)
```

## Padding
The padding allows you to add extra space inside the frame and outside of the contained widgets. Paddings are in pixels.

To specify padding for each side of the frame separately, you use the following:
```py
frame['padding'] = (left, top, right, bottom)
```
For example:
```py
frame['padding'] = (5,10,5,10)
```

Or you can specify paddings for the left, right and top, bottom as follows:
```py
frame['padding'] = (5, 10)
```

In this example, the left and right paddings are 5 and the top and bottom paddings are 10. If the paddings of all sides are the same, you can specify the padding like this:
```py
frame['padding'] = 5
```

## Frame borders
By default, the border width of a frame is zero. In other words, the frame has no border.

To set a border for a frame, you need to set both border’s width and style.

The border’s width of a frame is in pixels. The border’s style of a frame can be flat, groove, raised, ridge, solid, or sunken. The default border style of a frame is flat.

The following example sets the border width of the frame to 5 pixels and the border style of the frame to sunken.
```py
frame['borderwidth'] = 5
frame['relief'] = 'sunken'
```

## Tkinter Frame example
We’re going to create the following Replace window that is quite common in text editors like Notepad:
<img src="data:image/png;base64,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">

To make the widgets more organized, you can divide the window into two frames:

- The left frame consists of Label, Entry, and Checkbox widgets. The left frame will use the grid geometry manager that has two columns and four rows.
- The right frame consists of the Button widgets. The right frame will also use the grid geometry manager that has four rows and one column.

To place the left and right frames on the window, you can use the grid geometry manager that has one row and two columns:


<img src="data:image/png;base64,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21+KJT0plkUyF4olACNp+0uxpCfFskjmQrEEYCRtfymW9KRYFslcKJYAjKTtL8WSnhTLIpkLxRKAkbT9pVjSk2JZJHOhWAIwkra/FEt6UiyLZC4USwBG0vaXYklPimWRzIViCcBI2v5SLOlJsSySuVAsARhJ21+KJT0plkUyF4olACNp+0uxpCfFskjmQrEEYCRtfymW9KRYFslcKJYAjKTtL8WSnhTLIpkLxRKAkbT9pVjSk2JZJHOhWAIwkra/FEt6UiyLZC4USwBG0vaXYklPimWRzIViCcBI2v5SLOlJsSySuVAsARhJ21+KJT0plkUyF4olACNp+0uxpCfFskjmQrEEYCRtfymW9KRYFslcKJYAjKTtL8WSnhTLIpkLxRKAkbT9pVjSk2JZJHOhWAIwkra/FEt6UiyLZC7yfxQAjKLtr68pllOvC5V8/yiWJ5I5ABjVlxZL+BqK5YlkFgBG9SXFcup14FxL8uaKpYiIiIi8TBRLEREREVkliqWIiIiIrBLFUkRERERWiWIpIiIiIqtEsRQRERGRVaJYioiIiMgqUSxFREREZJUoliIiIiKyShRLEREREVkliqWIiIiIrBLFUkRERERWiWIpIiIiIqtEsRQRERGRVXJRxTL/CwDAt3MxxRIAgG9v6GKZ264AALweS/PqiqWIiIiIjBnFUkRERERWiWIpIiIiIqtEsRQRERGRVaJYioiIiMgqUSxFREREZJUoliIiIiKyShRLEREREVkliqWIiIiIrBLFUkRERERWiWIpIiIiIqtEsRQRERGRVaJYioiIiMgqUSxFREREZJUoliIiIiKyShRLEREREVkliqWIiIiIrBLFUkRERERWyGbzfxRyLVso9iPMAAAAAElFTkSuQmCC">

The following program illustrates how to create the Replace window above:
```py
import tkinter as tk
from tkinter import TclError, ttk


def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    # Replace with:
    ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_main_window():
    root = tk.Tk()
    root.title('Replace')
    root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
```

### How it works.

- First, import the tkinter module and tkinter.ttk submodule:
    ```py

    import tkinter as tk
    from tkinter import ttk
    ```
- Second, create the left frame in the `create_input_frame()` function. The following code adds paddings to all widgets within the input_frame:

    ```py
    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)
    ```
- Third, create the right frame in the create_button_frame() function.

- Fourth, create the root window in the create_main_window() function. The following code removes the minimize/maximize buttons from the window:
    ```py
    root.attributes('-toolwindow', True)
    ```
Note that this code only works on Windows.

In the `create_main_window()` function, we also create the left frame, and right frame, and use the grid geometry manager to arrange them on the root window.

Finally, call the `create_main_window()` function on the `if __name__ == "__main__":` block.

## Summary
- A `ttk.Frame` is a simple rectangle widget that can hold other widgets.
- Tkinter frames are used to organize user interfaces visually and at the coding level.