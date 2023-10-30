import random
import tkinter as tk


def BaseGame():
    print("There will be a random number between 1 and 10. Try to guess!")
    guess_number = random.randint(1,10)
    get = int(input("Answer: "))
    while get!=guess_number:
        if get<guess_number:
            print(f"Number is larger than {get}")
        else:
            print(f"Number is less than {get}")
        get = int(input("Answer: "))
    print("Yeah! You did it!")

windows = tk.Tk()
label = tk.Label(text="Hello. This is a guess number game!", fg='black', bg='white', width=40, height=10,font=30)
button1 = tk.Button(text="I`m deeping in!",fg='white',bg='black',width=40,height=5, font=25,command=lambda: windows.quit())
button2 = tk.Button(text="No. I`m leaving.",fg='white',bg='black',width=40,height=5,font=25,command=lambda: quit())
windows.title("Starting!")
label.pack()
button1.pack()
button2.pack()
windows.mainloop()
def show_mainmenu():
    main_menu = tk.Tk()
    main_menu.title("Main-Menu")
    main = tk.Label(text='What you`re interested in?', fg)