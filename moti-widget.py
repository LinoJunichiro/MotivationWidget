import tkinter as tk # import the tkinter library for GUI
import random # import random module
import datetime # import datetime module
import os # import os module

quotes = [ # list of motivational quotes
    "You are smart and lazy enough to find easier ways to do things.",
    "Start slow until no one can keep up.",
    "Gotta work for that dream life.",
    "You are the smartest person in the room. Use that to your advantage.",
    "You'll never know you can fly until you take the leap.",
    "You miss 100% of the shots you don't take.",
    "Greatness doesn't come from potential, it comes from action.",
    "People think that the sky is the limit until they saw the stars.",
    "Clock is ticking. Are you becoming the person you want to be?"
]

today = datetime.date.today() # get today's date
random.seed(today.toordinal()) # different quote each day
quote = random.choice(quotes) # randomly select a quote

root = tk.Tk() # create the main window
root.title("Lino Daily Motivation") # set the window title

root.geometry("420x160") # set the window size
root.configure(bg="#444aaa") # set the background color

label = tk.Label( # create a label to display the quote
    root,
    text=quote,
    wraplength=380,
    justify="center",
    font=("AKIRA Expanded", 12, "italic"),
    fg="white",
    bg="#444aaa",
    padx=20,
    pady=20
)
label.pack(expand=True) # add the label to the window and center it

button = tk.Button(
    root,
    text="Got it",
    command=root.destroy,
    font=("AKIRA Expanded", 10, "bold"),
    bg="#2e2e2e",
    fg="white",
    relief="flat"
)
button.pack(pady=5)

root.mainloop()