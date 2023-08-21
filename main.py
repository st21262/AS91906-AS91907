import tkinter as tk
from tkinter import *
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x600')
        self.root.title('My Quiz Academy')

        self.questions = [
            "What is a group of crows called?",
            "How many dots appear on a pair of dice?",
            "Which is the only body part that is fully grown from birth?",
            "What planet is closest to the sun?",
            "Where did sushi originate?"
        ]

        self.options = [
            ['A murder', 'A pack', 'A school', 'A group'],
            ['10', '42', '45', '40'],
            ['Ear', 'Arm', 'Nose', 'Eyes'],
            ['Mercury', 'Moon', 'Pluto', 'Saturn'],
            ['Japan', 'Vietnam', 'Germany', 'China']
        ]

        # Index of the correct option for each question
        self.answers = [0, 1, 3, 0, 3]

        self.score = 0
        self.current_question = -1

        self.question_label = Label(
            self.root, text=self.questions[0], font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_var = IntVar()
        self.option_buttons = []
        for i, option in enumerate(self.options[0]):
            option_button = Radiobutton(
                self.root, text=option, variable=self.answer_var, value=i)
            option_button.pack(anchor=W, padx=20)
            self.option_buttons.append(option_button)

        self.next_button = Button(
            self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            selected_option = self.answer_var.get()
            if selected_option == self.answers[self.current_question] and self.score < 5:
                self.score += 1

            self.current_question += 1
            if self.current_question < len(self.questions):
                self.question_label.config(
                    text=self.questions[self.current_question])
                for i, option in enumerate(self.options[self.current_question]):
                    self.option_buttons[i].config(text=option)
            else:
                self.show_result()

    def show_result(self):
        result = f"You scored {self.score} out of {len(self.questions)}"
        messagebox.showinfo("Quiz Result", result)
        self.root.destroy()


def open_quiz():
    quiz_root = tk.Toplevel()
    quiz_app = QuizApp(quiz_root)


def open_settings():
    settings_root = tk.Toplevel()


# start page window
second_root = tk.Toplevel()
second_root.geometry('1000x600')
second_root.title('My Quiz Academy')

second_label = Label(second_root, text='My Quiz Academy')
second_label.pack(pady=20)

quiz_button = Button(second_root, text='Start Game', command=open_quiz)
quiz_button.pack()

settings_button = Button(second_root, text='Settings', command=open_settings)
settings_button.pack()

quit_button = Button(second_root, text='Quit', command=second_root.destroy)
quit_button.pack()

second_root.mainloop()
