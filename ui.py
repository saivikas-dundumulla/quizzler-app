from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizzInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label
        self.score_label = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR, fg="white",
                                 font=("Courier", 15, "bold"))
        self.score_label.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.text = self.canvas.create_text(150, 125, width=280, text="", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=true_img, highlightthickness=False, command=self.is_true)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=false_img, highlightthickness=False, command=self.is_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            self.canvas.itemconfigure(tagOrId=self.text, text=question)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfigure(self.text, text="Yeah, You Finished the Quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def is_true(self):
        result = self.quiz.check_answer("True")
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)

    def is_false(self):
        result = self.quiz.check_answer("False")
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)
