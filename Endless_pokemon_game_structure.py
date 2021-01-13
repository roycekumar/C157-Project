from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("Endless Dice Game")
root.geometry("700x500")
root.configure(background="orange")
img=ImageTk.PhotoImage(Image.open ("button.jpg"))
pokemon_list=["Pikachu", "Bulbasor","Abra","Bulbasaur","Charmender","Iyvasour","Jigglypuff","Kadabra","Nidoking"]
Power_pokemon=[200, 60,30,60,50,100,70,70,90]
player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)

player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor =  CENTER)

random_poke_label = Label(root, fg = "black",bg="yellow")
random_poke_label.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)
player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,8)
    random_poke_label["text"] = ""
    player1_score = player1_score + Power_pokemon[random_no]
    player_1_score_label["text"] = str( player1_score)
    
player_1_btn = Button(root, image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)
    
player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(0,8)
    random_poke_label["text"] = ""
    player2_score = player2_score + Power_pokemon[random_no2]
    player_2_score_label["text"] = str( player2_score)
    

player_2_btn = Button(root, image = img, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor =  CENTER)
root.mainloop()