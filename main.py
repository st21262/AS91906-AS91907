from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('1000x600')
root.title('Quiz Program')

questions = [
    "What is a group of crows called?",
    "How many dots appear on a pair of dice?",
    "Which is the only body part that is fully grown from birth?",
    "What planet is closest to the sun?",
    "Where did sushi originate?"
]

options = [
    ['A murder', 'A pack', 'A school', 'A group'],
    ['10', '42', '45', '40'],
    ['Ear', 'Arm', 'Nose', 'Eyes'],
    ['Mercury', 'Moon', 'Pluto', 'Saturn'],
    ['Japan', 'Vietnam', 'Germany', 'China']
]

answers = [0, 1, 1, 0, 0]  # Index of the correct option for each question

score = 0
current_question = -1


def next_question():
    global current_question, score

    if current_question < len(questions):
        selected_option = answer_var.get()
        if selected_option == answers[current_question] and score < 5:
            score += 1

        current_question += 1
        if current_question < len(questions):
            question_label.config(text=questions[current_question])
            for i, option in enumerate(options[current_question]):
                option_buttons[i].config(text=option)
        else:
            show_result()


def show_result():
    result = f"You scored {score} out of {len(questions)}"
    messagebox.showinfo("Quiz Result", result)
    root.destroy()


question_label = Label(root, text=questions[0], font=("Arial", 16))
question_label.pack(pady=20)

answer_var = IntVar()
option_buttons = []
for i, option in enumerate(options[0]):
    option_button = Radiobutton(
        root, text=option, variable=answer_var, value=i)
    option_button.pack(anchor=W, padx=20)
    option_buttons.append(option_button)

next_button = Button(root, text="Next", command=next_question)
next_button.pack(pady=20)

next_question()

root.mainloop()
