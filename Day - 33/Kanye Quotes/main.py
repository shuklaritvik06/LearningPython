# Module impots

import requests
from tkinter import *


#  Quote Function
def change_quote():
    data= requests.get(url="https://api.kanye.rest")
    data = data.json()
    canvas.itemconfig(quote,text=data["quote"])

#  UI
BACKGROUND_COLOR = "white"
root = Tk()
root.config(bg=BACKGROUND_COLOR)
root.title("Kanye Says...",)
myimage = PhotoImage(file="background.png")
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img,bg=BACKGROUND_COLOR,borderwidth=0,command=change_quote)
canvas =  Canvas(width= 500,height= 500,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.create_image(250,250,image=myimage)
quote= canvas.create_text(250,250,text="",width=120,font=("Open Sans",10,"bold"),fill=BACKGROUND_COLOR)
canvas.pack()
kanye_button.pack()
root.mainloop()