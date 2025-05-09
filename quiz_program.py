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

def load_new_question():
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

questions = load_questions("quiz_data.txt")

if not questions:
    print("No questions loaded.")
    exit()