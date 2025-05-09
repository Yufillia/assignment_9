import tkinter as tk
from tkinter import messagebox
import random

def loaded_questions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip().split("---\n")
    
    questions = []
    for block in content:
        lines = block.strip().split("\n")
        if len(lines) < 6:
            continue
        
        q = {
            "question": lines[0].replace("Question: ", ""),
            "a": lines[1].replace("a) ", ""),
            "b": lines[2].replace("b) ", ""),
            "c": lines[3].replace("c) ", ""),
            "d": lines[4].replace("d) ", ""),
            "answer": lines[5].replace("Answer: ", "").strip().lower()
            
        }
        questions.append(q)
    return questions

def load_new_questions():
    global current_question
    current_question = random.choice(questions)
    questions_label.config(text=current_question["question"])
    var.set(None)
    rb_a.config(text="a) " + current_question["a"])
    rb_b.config(text="b) " + current_question["b"])
    rb_c.config(text="c) " + current_question["c"])
    rb_d.config(text="d) " + current_question["d"])

def check_answer():
    selected = var.get()
    if selected == "":
        messagebox.showwarning("No Answer", "Please selec an answer.")
        return
    
    if selected == current_question["answer"]:
        messagebox.showinfo("Result", "Correct!")
    else:
        correct = current_question["answer"]
        messagebox.showinfo("Result", f"Wrong! Correct answer is: {correct}.")

def next_question():
    load_new_question()

questions = loaded_questions("quiz_data.txt")

if not questions:
    print("No questions loaded.")
    exit()

current_question = None

root = tk.Tk()
root.title("Quiz Program")

question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14), justify="left")
question_label.pack(pady=20)

var = tk.StringVar(value="")

rb_a = tk.Radiobutton(root, text="", variable=var,value="a" font=("Arial", 12))
rb_a.pack(anchor="w", padx=20)

rb_b = tk.Radiobutton(root, text="", variable=var,value="b" font=("Arial", 12))
rb_b.pack(anchor="w", padx=20)

rb_c = tk.Radiobutton(root, text="", variable=var,value="c" font=("Arial", 12))
rb_c.pack(anchor="w", padx=20)

rb_d = tk.Radiobutton(root, text="", variable=var,value="d" font=("Arial", 12))
rb_d.pack(anchor="w", padx=20)

tk.Button(root, text="Submit Answer", command=check_answer).pack(pady=10)
tk.Button(root, text="Next Question", command=next_question).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

load_new_questions()
root.mainloop()
