from tkinter import *
from random import *

class Test:
    def __init__(self, parent):
        self.parent = parent

        self.question = Label(self.parent, text="", anchor=CENTER)
        self.question.grid(row=0, column=0, padx=40, pady=10)

        self.entry = Entry(self.parent, width=6)
        self.entry.grid(row=0, column=1, padx=4, pady=10)

        self.check_answer_button = Button(self.parent, text="Check Answer", command=self.check_answer)
        self.check_answer_button.grid(row=1, column=0, padx=4, pady=10)

        self.next_button = Button(self.parent, text="Next", command=self.generate_question)
        self.next_button.grid(row=1, column=1, padx=4, pady=10)

        self.result = Label(self.parent, text="")
        self.result.grid(row=0, column=2, padx=4, pady=10)

        self.generate_question()
    
    def generate_question(self):
        self.entry.delete(0, END)
        n1 = randint(0, 12)
        n2 = randint(0, 12)
        self.ans = n1 * n2
        self.question.configure(text=f"{n1} * {n2} = ")
        self.result.configure(text="")
    
    def check_answer(self):
        if self.entry.get().strip() == str(self.ans):
            self.result.configure(text="Correct!")
        else:
            self.result.configure(text="Incorrect!")

root = Tk()
root.geometry("250x90")
test = Test(root)
root.mainloop()