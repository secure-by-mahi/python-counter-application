import tkinter as tk#this beginner took me 2 hours to build 1 hours of playing tag of war with chatgpt

window = tk.Tk()#this is the core app here
window.config(bg="black")# to set the windows colour

window.geometry("500x400") # this is for to set the window size
check = tk.Label(window, text="my hacking tools",bg="black",fg="green")
check.pack() # THIS is for to set my label or windows ui name

clicks = 0

def button_clicked(): # the system or blueprint for my button that will help it work
    global clicks
    clicks = clicks + 1
    messege.config(text=f"clicks : {clicks}")

    if clicks == 10:
        window.config(bg="red")

        check.pack_forget()
        messege.pack_forget()
        re_set_Label.pack_forget()
        my_button.pack_forget()
        my_neg_Button.pack_forget()
        multiply_button.pack_forget()

        messege.config(
            text="SYSTEM IS HACKED!!!",
            bg='red',
            fg='white',
            font=('Arial', 24 ,'bold'),
        )

        messege.pack()


my_button = tk.Button(window, text="click me", command=button_clicked,bg="black",fg="green")
my_button.pack(pady=5)

messege = tk.Label(window,text="clicks : 0",bg="black",fg="green",font=("Arial",24,"bold"))
messege.pack(pady=5)

def re_set_clicked():
    global clicks
    clicks = 0

    window.config(bg="black")
    check.pack()
    messege.pack(pady=10)
    re_set_Label.pack(pady=5)
    my_button.pack(pady=5)
    my_neg_Button.pack(pady=5)
    multiply_button.pack(pady=5)

    messege.config(text=f"clicks : {clicks}",bg="black",fg="green")


re_set_Label = tk.Label(window,text=f"clicks reseted{check}",bg="black",fg="green")
re_set_Label.pack(pady=10)

reset_button = tk.Button(window,text="TAP HERE TO RESET CLICKS!",command=re_set_clicked,bg="black",fg="green")
reset_button.pack(pady=5)

messege.pack(pady=10)

def negetive_clicks():
    global clicks
    clicks = clicks - 1
    messege.config(text=f"clicks : {clicks}")

    if clicks == -10:
        window.config(bg="red")
        my_neg_Button.pack_forget()
        my_button.pack_forget()
        re_set_Label.pack_forget()
        check.pack_forget()
        multiply_button.pack_forget()

        messege.config(
            text="UR SYSTEM IN DANGER!!!",
            bg="red",
            fg="white",
            font=("Arial",24,"bold"),
        )
        messege.pack()


my_neg_Button = tk.Button(
    window,
    text="TAP HERE TO DECREASE UR NUMBERS",
    command=negetive_clicks,
    bg="black",
    fg="green"
)

my_neg_Button.pack()

def multiply_clicks():
    global clicks
    clicks = clicks * 2
    messege.config(text=f"clicks : {clicks}")

    if clicks >= 70000:
        window.config(bg="yellow")

        check.pack_forget()
        my_button.pack_forget()
        my_neg_Button.pack_forget()
        multiply_button.pack_forget()
        re_set_Label.pack_forget()

        messege.config(
            text="HACKING IS NOT REAL!!!",
            bg="yellow",
            fg="black",
            font=("Arial",24,"bold"),
        )

        messege.pack()


multiply_button = tk.Button(
    window,
    text="TAP HERE TO MULTIPLY UR NUMBER!",
    command=multiply_clicks,
    bg="black",
    fg="green"
)

multiply_button.pack(pady=5)

window.mainloop()