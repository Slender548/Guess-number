import random
import tkinter as tk


def show_tutorial():
    tutorial = tk.Tk()
    tutorial.title("Tutorial")
    tutorial_text = """
    Welcome to the Guess Number Game Tutorial!
    
    In this game, you will be trying to guess a randomly generated number.
    
    Instructions:
    1. Enter a number in the input field.
    2. Click the 'Enter' button to check your guess.
    3. You will receive hints about whether the target number is higher or lower.
    4. Keep guessing until you find the correct number.
    
    There are different game modes to choose from:
    - Basic game (1-10)
    - Advanced game (1-50)
    - Hard game (1-100)
    - Skill game (1-500)
    - Crazy game! (1-200)
    
    In "Crazy" mode, the target number changes with every guess!
    
    Good luck and have fun playing the game!
    """

    tutorial_label = tk.Label(tutorial, text=tutorial_text, fg='black', bg='white', font=30, width=70, height=20)
    tutorial_label.pack()
    tutorial.mainloop()

def play_crazy(max_value):
    def check():
        guess_number = random.randint(1, max_value)
        user_input = guess_input.get()
        if user_input.strip():  # Check if the input is not empty after stripping whitespace
            try:
                user_input = int(user_input)
                if user_input == guess_number:
                    guess_hint.configure(text="Yeah! You did it!")
            except ValueError:
                guess_hint.configure(text="Hint: Only numbers are allowed")
        else:
            guess_hint.configure(text="Hint: Please enter a number.")
    guess = tk.Tk()
    guess.title("Guessing the number")
    guess_main = tk.Label(guess, text=f"""Let's try to guess a number between 1 and {max_value}. 
    Warning! In this mode will be a generating 
    random number in every click to enter!""", fg='black', bg='white', font=40, width=50, height=10)
    guess_hint = tk.Label(guess, text="Hint: There`s no clue", fg='black', bg='white', font=30, width=50, height=5)
    guess_input = tk.Entry(guess, background='white', foreground='black', width=77, justify='center')
    guess_enter = tk.Button(guess, bg='white', fg='black', text='Enter', font=10, command=lambda: check())
    guess_main.pack()
    guess_hint.pack(fill=tk.BOTH)
    guess_input.pack(side='left')
    guess_enter.pack(side='right')
    guess.mainloop()

def play(max_value):
    def check():
        user_input = guess_input.get()
        if user_input.strip():  # Check if the input is not empty after stripping whitespace
            try:
                user_input = int(user_input)
                if user_input < guess_number:
                    guess_hint.configure(text=f"Hint: Number is larger than {user_input}")
                elif user_input > guess_number:
                    guess_hint.configure(text=f"Hint: Number is less than {user_input}")
                else:
                    guess_hint.configure(text="Yeah! You did it!")
            except ValueError:
                guess_hint.configure(text="Hint: Only numbers are allowed")
        else:
            guess_hint.configure(text="Hint: Please enter a number")

    guess = tk.Tk()
    guess.title("Guessing the number")
    guess_number = random.randint(1, max_value)
    guess_main = tk.Label(guess, text=f"Let's try to guess a number between 1 and {max_value}", fg='black', bg='white', font=40, width=50, height=10)
    guess_hint = tk.Label(guess, text="Hint: ...", fg='black', bg='white', font=30, width=50, height=5)
    guess_input = tk.Entry(guess, background='white', foreground='black', width=77, justify='center')
    guess_enter = tk.Button(guess, bg='white', fg='black', text='Enter', font=10, command=lambda: check())
    guess_main.pack()
    guess_hint.pack(fill=tk.BOTH)
    guess_input.pack(side='left')
    guess_enter.pack(side='right')
    guess.mainloop()

def show_mainmenu():
    main_menu = tk.Tk()
    main_menu.title("Main-Menu")
    main = tk.Label(main_menu, text='What you`re interested in?', fg='black', bg='white', pady=5, width=40, height=5,font=30)
    button_tutorial = tk.Button(main_menu, text='Tutorial', fg='black', bg='white', width=40, height=5, font=30, command=lambda: show_tutorial())
    button1 = tk.Button(main_menu, text='Basic game (10)', fg='black', bg='white', width=19, height=5,font=30, command=lambda: play(10))
    button2 = tk.Button(main_menu, text='Advanced game(50)', fg='black', bg='white', width=19, height=5,font=30, command=lambda: play(50))
    button3 = tk.Button(main_menu, text='Hard game(100)', fg='black', bg='white', width=19, height=5,font=30, command=lambda: play(100))
    button4 = tk.Button(main_menu, text='Skill game(500)', fg='black', bg='white', width=19, height=5,font=30, command=lambda: play(500))
    button5 = tk.Button(main_menu, text='Crazy game!(200)', fg='black',bg='white',width=38,height=5,font=30,command=lambda: play_crazy(200))
    main.pack(fill=tk.X)
    button_tutorial.pack(side='top',fill=tk.X)
    button1.pack(side='left',fill=tk.Y)
    button3.pack(side='right',fill=tk.Y)
    button4.pack(side='bottom',fill=tk.X)
    button2.pack(side='top',fill=tk.X)
    button5.pack(anchor='s')

    main_menu.mainloop()


windows = tk.Tk()


def but(TK: tk.Tk):
    TK.destroy()
    show_mainmenu()


label = tk.Label(text="Hello. This is a guess number game!", fg='black', bg='white', width=40, height=10, font=30)
button1 = tk.Button(text="I`m deeping in!", fg='white', bg='black', width=40, height=5, font=25,
                    command=lambda: but(windows))
button2 = tk.Button(text="No. I`m leaving.", fg='white', bg='black', width=40, height=5, font=25,
                    command=lambda: quit())
windows.title("Starting!")
label.pack()
button1.pack()
button2.pack()
windows.mainloop()
show_mainmenu()
