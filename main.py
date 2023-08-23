import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Form the quiz game


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
            self.root, text=self.questions[0], font=("Comic Sans MS", 16))
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

    # Functions
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
        open_start_page()


class QuizSettings:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x600')
        self.root.title('My Quiz Academy')
        quiz_back = Button(root, text='Go Back', command=open_start_page)
        quiz_back.pack()


def open_quiz():
    clear_window()
    quiz_app = QuizApp(root)


def open_settings():
    clear_window()
    quiz_app = QuizSettings(root)


def open_start_page():
    clear_window()

    root.configure(bg="#18141D")

    title_label = Label(root, bg="#18141D", font=(
        "Comic Sans MS", 24), fg="white")
    title_label.pack(anchor="nw", padx=20, pady=10)

    title_text = "My Quiz Academy"
    parts = title_text.split()

    for part in parts:
        if part == "Quiz":
            label = Label(title_label, text=part, bg="#18141D",
                          font=("Comic Sans MS", 50), fg="#ED3A50")
        else:
            label = Label(title_label, text=part, bg="#18141D",
                          font=("Comic Sans MS", 50), fg="white")
        label.pack(side="left")


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# start page window
root = tk.Tk()
root.geometry('1000x600')
root.title('My Quiz Academy')

open_start_page()

quiz_button = Button(root, text='Start Game',
                     command=open_quiz, font=("Comic Sans MS", 14))
quiz_button.place(x=450, y=300)

settings_button = Button(root, text='Settings',
                         command=open_settings, font=("Comic Sans MS", 14))
settings_button.place(x=450, y=340)

quit_button = Button(root, text='Quit', command=root.destroy,
                     font=("Comic Sans MS", 14))
quit_button.place(x=450, y=380)

root.mainloop()
