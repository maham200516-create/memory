import tkinter as tk
import time

m=tk.Tk()
m.geometry("710x630")
m.title("Flipping Cards-Memory Game")
m.configure(padx=10, pady=20,
            background="light blue")
title_frame=tk.Frame(m,
                     width=680,
                     height=560)
title_frame.pack(side="top",
                 fill="x",
                 pady=10)
game_title= tk.Label(title_frame,
                     text="Flipping Cards-Memory Game",
                     font=("Arial",35,"bold"),
                     background="light blue")
game_title.pack(anchor="center",
                fill="x")
card_frame=tk.Frame(m,
                    width=480,
                    height=560,
                    padx=10,
                    pady=10,
                    background="yellow")
card_frame.pack(side="left")
lives_text="❤❤❤"
lives=tk.Label(m,
               text=lives_text,
               font=("Arial",20),
               bg="light blue",
               pady=50)
lives.place(x=480,
            y=100)
score_label=tk.Label(m,
                     text="Score:",
                     font=("Helvetica",24),
                     bg="light blue")
score_label.place(x=480,
                  y=300)

score=0
game_score=tk.Label(m,
                    text=score,
                    font=("Arial",24),
                    bg="light blue")
game_score.place(x=600,
                 y=300)
def h_t_play():
    m2=tk.Tk()
    m2.geometry("700x200")
    m2.title("Rules")

    rule1=tk.Label(m2,
                   text="1)You have total of three lives",
                   font=("Arial",15))
    rule1.place(x=0,
                y=0)
    rule2=tk.Label(m2,
                   text="2)For odd selection:select any Card ",
                   font=("Arial",15))
    rule2.place(x=0,
                y=30)
    rule3=tk.Label(m2,
                   text="3)For even selection: selected card should have same number as\nprevious odd card  ",
                   font=("Arial",15))
    rule3.place(x=0,
                y=60)
    rule4=tk.Label(m2,
                   text="4)on even selection if number didnt match with previous odd selection\nyou lose ",
                   font=("Arial",15))
    rule4.place(x=0,
                y=120)

h_t_p=tk.Button(m,
                text="How To Play?👀",
                font=("Arial",17,"bold"),
                relief="flat",
                bg="light blue",
                activebackground="light blue",
                cursor="hand2",
                command=h_t_play)
h_t_p.place(x=480,y=500)

buttons=[]
lst=[]
class Cards:
    def __init__(self,value,j,i):
        self.button=tk.Button(card_frame,
                              text=value,
                              font=("Arial",19,"bold"),
                              height=2,
                              width=5,
                              bg="white",
                              activebackground="white",
                              foreground="black",
                              borderwidth=1.5,
                              relief="sunken")
        self.button.grid(row=j+200,
                         column=i)
        self.value=value
        buttons.append(self.button)
def rotate(self):
    self.button.configure(text="X")

    def click(self):
        global lst, score,lives_text
        self.button.configure(text=self.value,bg="#D3D3D3",state="disabled")
        lst.append(self.value)
        if len(lst)==2:
            m.update()
            time.sleep(0.5)
            if lst[0] == lst[1]:
                score=score+1
                game_score.configure(text=score)
                for button in buttons:
                    if button.cget("state") == "disabled":
                        button.configure(state="disabled")
                        card_frame.update()
                        m.update()
            else:
                if len(lives_text)>2:
                    lives_text = lives_text[:len(lives_text)-2]
                    lives.configure(text=lives_text)
                else:
                    pass
                score = 0
                game_score.configure(text=score)
                for button in buttons:
                    if button.cget("state")=="disabled":
                        button.configure(text="X",bg="white",foreground="black")
                        card_frame.update()
                        m.update()
            lst=[]
but_value=[3, 2, 4, 3, 6, 6, 5, 2, 5, 4]
for i in range(6):
    for j in range(5):
        if j%2==0:
            x=Cards(but_value[i],j,i)
        else:
            x=Cards(but_value[5+i],j,i)
        m.update()
        time.sleep(0.1)
        x.rotate()
        m.update()






m.mainloop()