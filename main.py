from pygame import mixer
import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter import *


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
            self.root, text=self.questions[0], fg="white", font=("Comic Sans MS", 16), bg="#18141D")
        self.question_label.pack(pady=20)

        self.answer_var = IntVar()
        self.option_buttons = []
        for i, option in enumerate(self.options[0]):
            option_button = Radiobutton(
                self.root, text=option, font=("Comic Sans MS", 14), bg="black", variable=self.answer_var, value=i)
            option_button.pack(anchor=W, padx=20)
            self.option_buttons.append(option_button)

        self.next_button = Button(
            self.root, text="Next", fg="black", font=("Comic Sans MS", 14), bg="#18141D", command=self.next_question)
        self.next_button.pack(pady=20)

        self.next_question()

    # Load and play music
    pygame.mixer.init()
    pygame.mixer.music.load('/Users/reenokouch/Downloads/background_music.mp3')
    pygame.mixer.music.play(-1)

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
        quiz_back = Button(root, text='Go Back', font=(
            "Comic Sans MS", 14), command=open_start_page)
        scale = Scale(root, from_=0, to=100,
                      orient=HORIZONTAL, command=change_volume)
        scale.set(50)
        title_label = Label(root, text='Settings', bg="#18141D", font=(
            "Comic Sans MS", 26), fg="black")
        title_label.place(x=425, y=100)

        scale.place(x=450, y=300)
        quiz_back.place(x=0, y=0)


def change_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)


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

    quiz_button = Button(root, text='Start Game', bg="#18141D", fg="black",
                         command=open_quiz, font=("Comic Sans MS", 14))
    quiz_button.place(x=450, y=250)

    settings_button = Button(root, text='Settings', bg="#18141D", fg="black",
                             command=open_settings, font=("Comic Sans MS", 14))
    settings_button.place(x=465, y=300)

    quit_button = Button(root, text='Quit', command=root.destroy, bg="#18141D", fg="black",
                         font=("Comic Sans MS", 14))
    quit_button.place(x=480, y=350)


def open_quiz():
    clear_window()
    quiz_app = QuizApp(root)


def open_settings():
    clear_window()
    quiz_app = QuizSettings(root)


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# start page window
root = tk.Tk()
root.geometry('1000x600')
root.title('My Quiz Academy')

open_start_page()

root.mainloop()
