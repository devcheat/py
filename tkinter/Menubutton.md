Tkinter Menubutton
===

## Introduction to the Menubutton widget
A Menubutton widget is a combination of a Button and a Menu widget.

When you click the Menubutton, it shows a menu with choices. For example:

<img src="data:image/png;base64,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VKW0ZUn/+7w8RyXlq2r/etWt6b3tca3mVBEJx+cqJhGv18t6XBHwer3q7OzUzJkzlZOTo5kzZ2r8+PFKS0uLeZ+J/jRpPlcxOsy4AJhDuACYQ7gAmEO4AJhDuACYwx9ZA+JVPWuYcQEwh3ABMIdwATCHcKWiAetuZSqzoEYJXokZiArhSjUdNSpwr7vl82n/gnNqT/S4gCjwqmJK6VDN472LApa5lmrOr6pK3JCAGDDjSiUdh3Wweb2Kwi6z1fsJPh5PQf/SzREs59x/u/8TgGo8faehBYn+OCB8KxGuVJObozn+f+2oKfAHxv1xY806k7NLPl+V8odczjnU7b0/v+VcUd+nCDVv2WnyU4SQ3AhXqmnuv56VVXZEPt/+oPW1crU68OkZQy3nHOp2/89XBtZ5zi/Sep1RG5MuxBnhSiVZ2VoQdUjCLefMMs9IHMKVUvwrni6J8ENgh1rOOdTtwBghXCkmq+yIfPulNX0X1tfoTOWuAa8y9htiOeeQtwNjg6WbkwhLN0dmNJZuhi3MuACYQ7gAmEO4AJhDuACYQ7gAmEO4AJhDuACYQ7gAmEO4AJhDuFLKUXncSzZnZqr/L3X8a2nx54cwgHClnFxVBtbROlWpM2si/INrIIkQrlQW0zI3QOIRrlR2tEF168tDrAwRfNoY9H245ZyBMUK4Uo575VJpf9QLAA61bDMwNghXynFf48rRjmgvyA+5bDMwNvh4slSWtVKrc7foXLukkAsJhrNe+31VYrFmJAozrlTWcVgHm3OVMyf4jjnKyW1W30TqaIPqAnexbDOSAOFKOa7TvCUHtfrUkRAX57NUVr5edWv82zXI9UlALNuMxGPp5iTC0s2RYelmMOMCYA7hAmAO4QJgDuECYA7hAmAO4QJgDu+cTzJerzfRQwCSHuFKIqHew3Xt2jVdunRJ7e3tunz5srq6unTr1q0EjC65TJgwQRkZGUpPT5fjOHIcJ9FDwhgiXEkuPT1d48eP19SpUyVJN27cUE8P7xnOyMjQ1KlTeeNpiiJcSS4tLU0TJ07UzJkzNWXKFN28eTPRQ0oKgaBPnDixb9aF1EG4klxaWlrfKdGkSZOYbfk5jqP09HSlpaUx40pBhCvJuZ+gkgiXX2CGFfxPpAbCleR4YgKD8T4uAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOYQLgDmEC4A5hAuAOb8P+8R5t1qAdWaAAAAAElFTkSuQmCC">


To create a Menubutton widget, you follow these steps:

First, create a MenuButton widget:
```py
menu_button = ttk.Menubutton(container, **options)
```

Second, create a new instance of the Menu class:
```py
menu = tk.Menu(menu_button, tearoff=False)
```
Third, add one or more menu items to the menu instance. And you can add Checkbutton or Radiobutton widgets to the menu.

Finally, assign the Menu to the MenuButton instance:
```py
menu_button["menu"] = menu
```

## Tkinter Menubutton widget example
The following program illustrates how to use Menubutton widget. When you click the MenuButton, it’ll display a menu that consists of three choices: red, green, and blue.

The background color of the main window will change based on the selected menu item of the Menubutton:

```py
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x250')
        self.title('Menubutton Demo')

        # Menubutton variable
        self.selected_color = tk.StringVar()
        self.selected_color.trace("w", self.menu_item_selected)

        # create the menu button
        self.create_menu_button()

    def menu_item_selected(self, *args):
        """ handle menu selected event """
        self.config(bg=self.selected_color.get())

    def create_menu_button(self):
        """ create a menu button """
        # menu variable
        colors = ('Red', 'Green', 'Blue')

        # create the Menubutton
        menu_button = ttk.Menubutton(
            self,
            text='Select a color')

        # create a new menu instance
        menu = tk.Menu(menu_button, tearoff=0)

        for color in colors:
            menu.add_radiobutton(
                label=color,
                value=color,
                variable=self.selected_color)

        # associate menu with the Menubutton
        menu_button["menu"] = menu

        menu_button.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
```

### How it works.

In the `__init__()` method, we define a variable that tracks the selected value of the menu:
```py
self.selected_color = tk.StringVar()
self.selected_color.trace("w", self.menu_item_selected)
```
If the value of the selected_color is changed, the method menu_item_selected will be executed.

The create_menu_button() method creates the MenuButton:

First, create a Menubutton:
```py
menu_button = ttk.Menubutton(
    self,
    text='Select a color')
```
Then create a new menu and add three Radiobutton widgets derived from the colors tuple to the menu:
```py
# create a new menu instance
menu = tk.Menu(menu_button, tearoff=0)

for color in colors:
    menu.add_radiobutton(
        label=color,
        value=color,
        variable=self.selected_color)
```
When you select a menu item, the value of the self.selected_color variable changes to the value of the selected menu item.

Finally, associate menu with the Menubutton:
```py
menu_button["menu"] = menu
```

## Summary
- Use Tkinter Menubutton widget to create a menu associated with a button.