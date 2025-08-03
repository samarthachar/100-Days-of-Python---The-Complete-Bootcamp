from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        self.text = self.canvas.create_text(150,125,text="Text", font=("Arial", 20, "italic"), fill="black", width=280)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_button_img, highlightthickness=0, highlightcolor=THEME_COLOR, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)


        self.wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_button_img, highlightthickness=0, highlightcolor=THEME_COLOR, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true_pressed(self):
        self.update_score(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.update_score(self.quiz.check_answer("False"))

    def update_score(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


