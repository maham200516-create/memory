import tkinter as tk
import time
from tkinter import messagebox
import random

m=tk.Tk()                                   #main window
m.geometry("700x650")
m.title("Flipping Cards-Memory Game")
m.configure(padx=10,pady=20,background="light pink")
title_frame=tk.Frame(m,width=600,height=500)
title_frame.pack(side="top", fill="x", pady=10)
game_title= tk.Label(title_frame,text="Flipping Cards-Memory Game",font=("Arial",35,"bold"),background="light pink",foreground="purple")
game_title.pack(anchor="center",fill="x")
card_frame=tk.Frame(m,width=650,height=600,padx=10,pady=10)
card_frame.pack(side="left")
lives_text="❤❤❤❤❤\n❤❤❤❤❤"
lives=tk.Label(m,text=lives_text,font=("Arial",20),pady=50,bg="light pink")
lives.place(x=500,y=100)
score_label=tk.Label(m,text="Score:",font=("Arial",20,"bold"),bg="light pink")
score_label.place(x=500, y=300)
score=0
game_score=tk.Label(m,text=score,font=("Arial",20,"bold"),bg="light pink")
game_score.place(x=600,y=300)

def h_t_play():                         #function explaining the game
    m1=tk.Tk()                          #new window
    m1.geometry("700x250")
    m1.title("Rules")

    rule1=tk.Label(m1,text="1)You have total of three lives.",font=("Arial",15))
    rule1.place(x=0,y=0)
    rule2=tk.Label(m1,text="2)Select two cards.",font=("Arial",15))
    rule2.place(x=0,y=30)
    rule3=tk.Label(m1,text="3)If both cards have the same number, game continues.",font=("Arial",15))
    rule3.place(x=0,y=60)
    rule4=tk.Label(m1,text="4)If both cards do not have the same number,\n you lose 1 life.",font=("Arial",15))
    rule4.place(x=0,y=120)
    rule5 = tk.Label(m1,text="5)If all lives are gone, you lose.",font=("Arial", 15))
    rule5.place(x=0,y=180)

h_t_p=tk.Button(m,text="Rules",font=("Arial",20,"bold"),relief="flat",bg="light pink",activebackground="grey",cursor="hand2",command=h_t_play)
h_t_p.place(x=500,y=500)

buttons=[]         #cards
lst=[]             #input
clicked=[]         #card tracking

class Cards:
    def __init__(self,value,j,i):                   #function to make buttons
        self.value=value
        self.button=tk.Button(card_frame,text="X",font=("Arial",20,"bold"),height=2,width=5,bg="white",activebackground="grey",foreground="purple",borderwidth=1.5,relief="sunken",command=self.click,cursor="hand2")
        self.button.grid(row=j,column=i)
        buttons.append(self.button)

    def click(self):                        #function inputs numbers and checks them for validity
        global lst, score,lives_text,clicked
        if len(lst)==2:                     #corectly matched cards stay flipped
            return
        self.button.configure(text=self.value,bg="grey",state="disabled")   #flips cards
        lst.append(self.value)                                                 #inputs numbers
        clicked.append(self.button)                                             #tracks cards
        if len(lst)==2:
            m.update()
            time.sleep(0.5)
            if lst[0] == lst[1]:                  #checks if both numbers are same
                score=score+1
                game_score.configure(text=score)
                for button in clicked:             #makes cards unavailable
                        button.configure(state="disabled")
            else:
                if len(lives_text)>1:                 #checks if lives are available and removes one for wrong selection
                    lives_text = lives_text[:len(lives_text)-1]
                    lives.configure(text=lives_text)                #updating lives
                else:
                    lives_text = lives_text[:len(lives_text) - 1]
                    lives.configure(text=lives_text)
                    messagebox.showerror("You lose!",lives_text)
                    m.destroy()
                    return                  #ends game
                for button in clicked:                          #if unmatched makes cards available
                    button.configure(text="X",bg="white",state="normal",foreground="black")
            clicked=[]                  #empties the button tracking list
            lst=[]                      #empties input taking list
button_value=[3, 2, 4, 3, 6, 6, 5, 2, 5, 4]*3                        #cards
random.shuffle(button_value)                                         #makes cards random
a=0
for j in range(6):
    for i in range(5):
        x=Cards(button_value[a],j,i)
        a+=1
        m.update()
m.mainloop()

