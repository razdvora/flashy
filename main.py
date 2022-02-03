from tkinter import *
import pandas
BACKGROUND_COLOR= "#B1DDC6"
import random
curr_card ={}
to_learn={}
try:
    data = pandas.read_csv("word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:


    to_learn = data.to_dict(orient="records")


def next_card():
    global  curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    curr_card["French"]
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word, text=curr_card["French"])
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def right():
    to_learn.remove(curr_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("word_to_learn.csv", index=False)


    next_card()


def flip_card():
    canvas.itemconfig(card_title,text= "English")
    canvas.itemconfig(card_word,text=curr_card["English"])
    canvas.itemconfig(card_background,image=card_backimg)
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)

card_front_img =PhotoImage(file="card_front.png")
canvas =Canvas(width=800,height=526)
card_backimg=PhotoImage(file="card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=1,columnspan=2)
card_title = canvas.create_text(400,150 ,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))
wrong_img=PhotoImage(file="wrong.png")
wrong_btn = Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_btn.grid(row=2,column=1)
right_img = PhotoImage(file="right.png")
right_btn =Button(image=right_img,highlightthickness=0,command=right)
right_btn.grid(row=2,column=2)


next_card()
print(curr_card)
window.mainloop()