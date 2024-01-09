import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, font

root = tk.Tk()
root.geometry('350x500') #Window size
root.configure(bg="#80BCBD") #Bakcground-color
custom_font = font.Font(family="Arial",size=15) #RadioButton's Font

#-------------------------------------------------option 1---------------------------------------------#
#It calls al the clase "Guess_num"
def create_guess_num():
    limit_num = simpledialog.askinteger("Create the number", "Enter the number limit:")
    if limit_num is not None:   #It verifies if the camp was succesfully completed 
        user = Guess_num(limit_num)
        user.attempts()

# Class "Guess_num" for The option Guess a number
class Guess_num:
    def __init__(self, limit_num):
        self.limit_num = limit_num
        self.attempts_left = 3
        self.num_created = self.random_number()  #It brings the "num_created" from "random_number"

    #Create a random number with "limit_num"
    def random_number(self):  #"num_Created" cannot be here, due to random library
        num_created = random.randrange(1, self.limit_num + 1)
        return num_created

    #Create the user interactions
    def attempts(self):
       #it will be checking if the user has attempts
        while self.attempts_left > 0:
            user_num = simpledialog.askinteger("Guess the Number", "Enter a number:")
            if user_num == self.num_created:
                messagebox.showinfo("Congratulations!", "Congratulations! It was the number")
                break  # if the number is guessed, it will end up
            else:
                self.attempts_left -= 1
                messagebox.showinfo("Incorrect", f"You have {self.attempts_left} attempts left")
        else:
            messagebox.showinfo("Game Over", f"Sorry. You've not guessed the number.\n \n The number was {self.num_created}")
            
#----------------------------------------------------option 2---------------------------------------#
#It calls al the clase "Password"
def create_password():
    len_password= simpledialog.askinteger("Lenght", "Enter the lenght password: ")
    symbols_question = simpledialog.askstring("Symbols","Do you want symbols? (yes/no): ")
    if len_password is not None and symbols_question is not None:   #verifica si el campo esta lleno 
        user = Password(len_password,symbols_question)
        user.generate()

# Class "Password" for The option Passowrd       
class Password:
    def __init__(self,len_password,symbols_question):
        self.len_password = len_password
        self.symbols_question = symbols_question
        #variables from the respective functions
        self.symbols_generator = self.symbols()
        self.letters_generator = self.letters()
        self.numbers_generator = self.numbers()
        self.capital_letters_generator = self.cap_letters()
        
    #symbols
    def symbols(self):
        symbols_generator = ['!','/','#','$','%','&','=','?']
        return symbols_generator
    
    #lower letters
    def letters(self):
        letters_generator = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
        return letters_generator
    
    #capital letters: It makes a loop for changing "lower" to "upper" letters
    def cap_letters(self):
        capital_letters_generator = [] #capital letters will be stored here
        for i in self.letters_generator:
            i = i.upper()
            capital_letters_generator.append(i)
        return capital_letters_generator
    
    #numbers
    def numbers(self):
        numbers_generator = ['0','1','2','3','4','5','6','7','8','9']
        return numbers_generator
    
    #create a random password
    def generate(self):
        final_password=[] #here will be stored the final password
        if self.symbols_question.lower() == 'yes':
            #It makes a loop for create the password if the user wants symbols with the lenght he set
            for password in range(self.len_password):
                    var = random.randrange(1,4+1)
                    match var:
                        case 1:
                            final_password.append(random.choice(self.symbols_generator))
                        case 2:
                            final_password.append(random.choice(self.letters_generator))
                        case 3:
                            final_password.append(random.choice(self.numbers_generator))
                        case 4:
                            final_password.append(random.choice(self.capital_letters_generator))
                    
        elif self.symbols_question.lower() == 'no':
            for password in range(self.len_password):
                    var = random.randrange(2,4+1)
                    match var:
                        case 2:
                            final_password.append(random.choice(self.letters_generator))
                        case 3:
                            final_password.append(random.choice(self.numbers_generator))
                        case 4:
                            final_password.append(random.choice(self.capital_letters_generator))
                            
        string_password = "".join(final_password) #Convert "final_password" Array to Str
        messagebox.showinfo("Password",f"Your password is:  {string_password}")
        return final_password

#-------------------------------------------------option 3-------------------------------------------#
user_dsc_list = [] #User options will be strored here
machine_dsc_list = [] #Machine options will be strored here
user_wins = 0 #User victories
machine_wins = 0 #Machine victories

def create_rock_paper_scissors():
    user_object_dsc = simpledialog.askinteger("Options", "Choose one option (number): \n\n1.Rock \n2.Paper \n3.Scissors\n")
    if user_object_dsc is not None: #If the user choosed one option, the program will be executed
        user = Traditionalgame_rps(user_object_dsc)
        user.play()
        
        #The code ever will execute the class "Traditionalgame_rps" and the user desicion brings the respective object
        match user_object_dsc:  
            case 1:
                rock = Rock()
                rock.win_rock(user_object_dsc)
            case 2:
                paper = Paper()
                paper.win_paper(user_object_dsc)
            case 3:
                scissors = Scissors()
                scissors.win_scissors(user_object_dsc)
        user.rock_paper_scissors_again()    #The program ever will ask to user if he wants to play again
        
class Traditionalgame_rps:
    def __init__(self, user_object_dsc):
        self.user_object_dsc = user_object_dsc
        self.final_option_machine = self.computer_dsc()
        
    def computer_dsc(self):
        options_list = ["Rock", "Paper", "Scissors"]
        machine_dsc_list.append(random.choice(options_list))    #It will store in "machine_dsc_list" one random option from "Option_list"

    #The program will be execute
    def play(self):
        match self.user_object_dsc: #It converts the user_object_decision (Int) to string
            case 1:
                user_object_dsc_converted = "Rock"
            case 2:
                user_object_dsc_converted = "Paper"
            case 3:
                user_object_dsc_converted = "Scissors"
        user_dsc_list.append(user_object_dsc_converted) #It will store in "user_dsc_list" the "user_object_dsc_converted"
        
        #It shows the result message (user desicion and machine desicion)
        messagebox.showinfo("Result", f"You: {user_object_dsc_converted}\nMachine: {machine_dsc_list[-1]}")
        return user_object_dsc_converted
    
    #The user decision if the user wants to play again
    def rock_paper_scissors_again(self):
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            create_rock_paper_scissors()
        return play_again

#win message against the machine
def win_message(user_wins,machine_wins):
    messagebox.showinfo("win", f"You have won \n\n Victrories: {user_wins} \n Defeats: {machine_wins}")

#lose message against the machine
def lose_message(user_wins,machine_wins):
    messagebox.showinfo("Lose", f"You have lost \n\n Victrories: {user_wins} \n Defeats: {machine_wins}")
    
def draw_message(user_wins,machine_wins):
    messagebox.showinfo("Draw", f"You have Drawn \n\n Victrories: {user_wins} \n Defeats: {machine_wins}")

# It contains all about the object Rock 
class Rock:
    def __init__(self):
        pass
    
    #If the rock wins
    def win_rock(self,user_object_dsc):
        global user_wins,machine_wins
        
        #The user decision and the last machine desicion 
        if user_object_dsc == 1 and machine_dsc_list[-1] == "Scissors":
            user_wins += 1
            win_message(user_wins,machine_wins)
        elif user_object_dsc == 1 and machine_dsc_list[-1] == "Rock":
            draw_message(user_wins,machine_wins)
        else:
            machine_wins += 1
            lose_message(user_wins,machine_wins)
            
#It contains all abou the object Paper 
class Paper:
    def __init__(self):
        pass
    
    #if the paper wins
    def win_paper(self,user_object_dsc):
        global user_wins,machine_wins
        #The user decision and the last machine desicion
        if user_object_dsc == 2 and machine_dsc_list[-1] == "Rock":
            user_wins += 1
            win_message(user_wins,machine_wins)
        elif user_object_dsc == 2 and machine_dsc_list[-1] == "Paper":
            draw_message(user_wins,machine_wins)
        else:
            machine_wins += 1
            lose_message(user_wins,machine_wins)
    
#It contains all abou the object Scissors  
class Scissors:
    def __init__(self):
        pass
    
    #if the scissors wins
    def win_scissors(self,user_object_dsc):
        global user_wins,machine_wins
        
        #The user decision and the last machine desicion
        if user_object_dsc == 3 and machine_dsc_list[-1] == "Paper":
            user_wins += 1  
            win_message(user_wins,machine_wins)
        elif user_object_dsc == 3 and machine_dsc_list[-1] == "Scissors":
            draw_message(user_wins,machine_wins)
        else:
            machine_wins += 1
            lose_message(user_wins,machine_wins)
            
#---------------------------------------Option 4-------------------------------------------#

def create_hangman_game():
    user_word = simpledialog.askstring("User", "\nYou have 4 Attempts left\n\n___ ___ ___ ___ ___ \n\nEnter a word (5 letters): ")
    if user_word is not None:
        user = Hangman_game(user_word)
        user.game(user_word)
    return user_word

class Hangman_game:
    def __init__(self,user_word):
        self.user_attempts = 3
        self.user_word = user_word
        self.current_word_user = ""
        self.final_word = self.words_machine()

    def words_machine(self):
        words_list = ['pizza', 'crazy', 'field', 'joker','japan']
        final_word = random.choice(words_list)
        print(final_word)
        return final_word

    def game(self,user_word):
        print("current word:", self.current_word_user)
        if not self.current_word_user:
            self.current_word_user += "___ " * len(self.final_word)
        else:
            pass
            
        user_word = simpledialog.askstring("User", f"\nYou have {self.user_attempts} attempts left\n\n{self.current_word_user}\n\nEnter a word (5 letters): ")
        if len(self.final_word) != len(user_word):
            messagebox.showerror("Error","The lenght must be same")
        else:
            new_current_word = ""
            for i in range(len(self.final_word)):
                if self.final_word[i].lower() == user_word[i].lower():
                    new_current_word += user_word[i].lower() + " "
                else:
                    new_current_word += self.current_word_user[2*i:2*i+2]
            self.current_word_user = new_current_word.strip()
        self.attempts(user_word)
        
    def attempts(self,user_word):

        while self.user_attempts >= 0:
            if self.user_attempts == 0:
                messagebox.showinfo("Sorry", "You have lost the game")
                break
            elif user_word.replace(" ", "") == self.final_word:
                messagebox.showinfo("Congrats", "You have won the game")
                self.user_attempts = -1
                break
            
            else:
                self.user_attempts -= 1
                self.game(user_word)

#-------------------------------------------------menu options---------------------------------------
menu = Label(root, text='Choose one option:', font=("Times New Roman",25))
menu.pack(pady=10)
menu.config(bg="#80BCBD",fg="white")

#When the mouse is over a menu option
def on_enter(event):
    event.widget.config(bg="#4caf50", fg="white")
#When the mouse isn't over a menu option
def on_leave(event):
    event.widget.config(bg="#80BCBD", fg="black")
    
#Radiobuttons 
def menu_options():
    #guess the number
    option1 = tk.Radiobutton(root, text="Guess the number", value="option1", command=create_guess_num, font=custom_font, borderwidth=8)
    option1.pack(pady=10, anchor="w", padx=10, in_=root, side="top")
    option1.config(bg="#80BCBD",cursor="cross")
    option1.bind("<Enter>", on_enter)
    option1.bind("<Leave>", on_leave)

    #create a random password
    option2 = tk.Radiobutton(root, text="Create a random password", value="option2", command=create_password, font=custom_font, borderwidth=8)
    option2.pack(pady=10, anchor="w", padx=10, in_=root, side="top")
    option2.config(bg="#80BCBD",cursor="cross")
    option2.bind("<Enter>", on_enter)
    option2.bind("<Leave>", on_leave)

    #rock,paper or scissors
    option3 = tk.Radiobutton(root, text="rock,paper or scissors", value="option3", command=create_rock_paper_scissors)
    option3.pack(pady=10, anchor="w", padx=10, in_=root, side="top")
    option3.config(bg="#80BCBD", font=custom_font, borderwidth=8,cursor="cross")
    option3.bind("<Enter>", on_enter)
    option3.bind("<Leave>", on_leave)
    
    #
    option4 = tk.Radiobutton(root, text="Hangman game", value="option4", command=create_hangman_game)
    option4.pack(pady=10, anchor="w", padx=10, in_=root, side="top")
    option4.config(bg="#80BCBD", font=custom_font, borderwidth=8,cursor="cross")
    option4.bind("<Enter>", on_enter)
    option4.bind("<Leave>", on_leave)
menu_options()

root.mainloop()

