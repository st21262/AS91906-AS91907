from tkinter import *
from tkinter import StringVar


root = Tk()
root.geometry('500x500')

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
                       bg='grey', fg='#fff', font=('Verdana, 20'), wraplength=500)
question_label.pack()

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)


option1 = Radiobutton(frame, bg='#fff', variable=v1, font=(
    'Verdana', 20))
option2 = Radiobutton(frame, bg='#fff', variable=v1, font=(
    'Verdana', 20))
option3 = Radiobutton(frame, bg='#fff', variable=v1, font=(
    'Verdana', 20))
option4 = Radiobutton(frame, bg='#fff', variable=v1, font=(
    'Verdana', 20))

button_next = Button(frame, text='Next')

frame.pack(fill="both", expand=True)
question_label.grid(row=0, column=0)

option1.grid(sticky='W', row=1, column=0)
option2.grid(sticky='W', row=2, column=0)
option3.grid(sticky='W', row=3, column=0)
option4.grid(sticky='W', row=4, column=0)

button_next.grid(row=6, column=0)

index = 0
correct = 0

# create a function to disable the radiobuttons


def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

# create a function to check the selected answer


def checkAnswer(radio):
    global correct, index

    if radio['text'] == options[index][0]:
        correct += 1

    index += 1
    if index < len(options):
        displayNextQuestion()
    else:
        displayResults()


def displayNextQuestion():
    global index, correct

    if index == len(options):
        displayResults()
        return


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart?':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
        question_label['text'] = str(correct) + " / " + str(len(options))
        button_next['text'] = 'Restart?'
        if correct >= len(options)/2:
            question_label['bg'] = 'green'
        else:
            question_label['bg'] = 'red'


question_label['text'] = questions[index]

opts = options[index]
option1['text'] = opts[0]
option2['text'] = opts[1]
option3['text'] = opts[2]
option4['text'] = opts[3]
v1.set(opts[0])
v2.set(opts[1])
v3.set(opts[2])
v4.set(opts[3])
disableButtons('active')


def displayResults():
    global correct
    question_label['text'] = str(correct) + " / " + str(len(options))
    button_next['text'] = 'Restart?'
    if correct >= len(options) / 2:
        question_label['bg'] = 'green'
    else:
        question_label['bg'] = 'red'
    disableButtons('disable')


if index == len(options) - 1:
    button_next['text'] = 'Check your Results'


displayNextQuestion()


root.mainloop()
