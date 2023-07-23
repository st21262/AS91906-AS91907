from tkinter import *
from tkinter import StringVar


root = Tk()
root.geometry('1000x600')

questions = ["What is a group of crows called?",
             "How many dots appear on a pair of dice?",
             "Which is the only body part that is fully grown from birth?",
             "What planet is closest to the sun?",
             "Where did sushi originate?",]

options = [['A murder', 'A pack', 'A school', 'A group,'], ['10', '42', '45', '40'],
           ['Ear', 'Arm', 'Nose', 'Eyes'], [
    'Mercury', 'Moon', 'Pluto', 'Saturn'],
    ['Japan', 'Vietnam', 'Germany', 'China']]


frame = Frame(root)
frame.pack(pady=20)

question_label = Label(frame, height=5, width=28,
                       bg='#ddd', font=('Verdana, 20'), wraplength=500,
                       textvariable=questions)
question_label.pack()

option1 = Radiobutton(frame, bg="#fff")
option2 = Radiobutton(frame, bg="#fff")
option3 = Radiobutton(frame, bg="#fff")
option4 = Radiobutton(frame, bg="#fff")

button_next = Button(frame, text='Next')

frame.pack(fill="both", expand=True)
question_label.grid(row=0, column=0)

option1.grid(row=1, column=0)
option2.grid(row=2, column=0)
option3.grid(row=3, column=0)
option4.grid(row=4, column=0)

button_next.grid(row=6, column=0)

root.mainloop()
