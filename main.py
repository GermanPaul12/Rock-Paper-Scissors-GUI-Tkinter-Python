from tkinter import *
from tkinter import messagebox 
import customtkinter
from PIL import ImageTk, Image
from game import Game
import re

root = customtkinter.CTk()

root.title('Rock-Paper-Scissors')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.iconbitmap('/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Monopoly/favicon.ico')
root.geometry("1000x500")
root.configure(bg='black')


rounds_won = 0
rounds_lost = 0

def send_msg():
    global rounds_won
    global rounds_lost
    player_choice = combobox.get()
    bot_choice = Game()
    opponents_choice.configure(text=f"{bot_choice}")
    if bot_choice == player_choice:
        game_title.configure(text=f"It's a draw😐")
    if bot_choice == 'Paper' and player_choice == 'Scissors':
        game_title.configure(text=f"You won!😎")   
        rounds_won += 1
        won_label.configure(text=f"Rounds Won: {rounds_won}")
    elif bot_choice == 'Rock' and player_choice == 'Paper':
        game_title.configure(text=f"You won!😎")   
        rounds_won += 1
        won_label.configure(text=f"Rounds Won: {rounds_won}")  
    elif bot_choice == 'Scissors' and player_choice == 'Rock':
        game_title.configure(text=f"You won!😎")   
        rounds_won += 1
        won_label.configure(text=f"Rounds Won: {rounds_won}")    
    else:
        game_title.configure(text=f"You lost!😱")   
        rounds_lost += 1
        lost_label.configure(text=f"Rounds Lost: {rounds_lost}")         
         
    


game_frame = customtkinter.CTkFrame(master=root,
                               width=1000,
                               height=500,
                               corner_radius=10,
                               bg='black',
                               fg_color='#FEB139',
                               border_width=2, border_color="white")

game_title = customtkinter.CTkLabel(root, text="Rock-Paper-Scissors Game", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 28),
                               bg_color='#FEB139')

won_label = customtkinter.CTkLabel(root, text=f"Rounds Won: {rounds_won}", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='#FEB139')

lost_label = customtkinter.CTkLabel(root, text=f"Rounds Lost: {rounds_lost}", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='#FEB139')


your_choice_label = customtkinter.CTkLabel(root, text=f"Your choice:", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='#FEB139')

opponents_choice_label = customtkinter.CTkLabel(root, text=f"Opponents choice:", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='#FEB139')

opponents_choice = customtkinter.CTkLabel(root, text=f"", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='#FEB139',
                               anchor="w")

play_button = customtkinter.CTkButton(root, command=send_msg, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Play",
                                 fg_color='#0F3D3E',
                                 text_font=('Times New Roman', 26),
                               bg_color='#FEB139',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white"
                                 )


combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=["Rock", "Paper", "Scissors"], 
                                       width=80,
                                        height=40,
                                        fg_color=("white", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='#FEB139',
                                        text_color='white',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )
combobox.grid(row=2, column=2, sticky='ew', padx=10, columnspan=2)
combobox.set("Your Choice")  # set initial value




#Packing them on the screen

game_frame.grid(row=0, column=0, columnspan=4, rowspan=6, sticky='news')
game_title.grid(row=0, column=0, sticky='ew', padx=10, columnspan=4)
your_choice_label.grid(row=2, column=0, sticky='ew', padx=10, columnspan=2)
won_label.grid(row=1, column=0, sticky='ew', padx=10, columnspan=2)
lost_label.grid(row=1, column=2, sticky='ew', padx=10, columnspan=2)
opponents_choice_label.grid(row=3, column=0, sticky='ew', padx=10, columnspan=2)
opponents_choice.grid(row=3, column=2, sticky='ew', padx=10, columnspan=2)
play_button.grid(row=5, column=0, columnspan=4, sticky='ew', padx=10)




root.mainloop()