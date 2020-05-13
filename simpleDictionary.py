from tkinter import *
from PIL import Image, ImageTk
import json
from difflib import get_close_matches

data = json.load(open("/home/soumyo/PycharmProjects/Simple Dictonary/data.json"))


# Creating Functions

# Creating Search Function


def search(word):
    if word in data:
        output_text.delete(1.0, END)
        output_text.config(fg='white')
        output_text.insert(END, data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        output_text.config(fg='red')
        output_text.delete(1.0, END)
        output_text.insert(END, "Did you mean {} to mean : {} ".format(get_close_matches(word, data.keys())[0], data[get_close_matches(word, data.keys())[0]]))
        output = get_close_matches(word, data.keys())


root = Tk()
root.title("Simple Dictionary")
root.resizable(width=False, height=False)
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/Simple Dictonary/icon.png"))

# Creating Background
bg_img = Image.open("/home/soumyo/PycharmProjects/Simple Dictonary/images/WebDevelopemnt.png")
bg_img = bg_img.resize((960, 540), Image.ANTIALIAS)
BG_IMG = ImageTk.PhotoImage(bg_img)
img_label = Label(root, image=BG_IMG)
img_label.pack()

# Creating Input EntryBox
input_text = StringVar()
entry_box1 = Entry(root, textvariable=input_text, bg="#FFFD38", fg="black", justify=CENTER, font=('Courier New', 20, 'bold'))
entry_box1.place(relx=.185, rely=0.67, relwidth=.63, relheight=.082)

# Creating Search Button
search_btn = Button(root, text="Search", command=lambda: search(input_text.get()), relief=FLAT, bg="green", fg="white", font=('TSCu_Comic', 25, 'bold'))
search_btn.place(relx=.40, rely=0.82, relwidth=.2, relheight=.065)

# Creating OutputBox for Word Definition
output_text = Text(root, fg="white", relief=FLAT, bg="#444444", font=('courier', 15, 'bold'))
output_text.place(relx=.185, rely=.05, relwidth=.63, relheight=.28)

root.mainloop()
