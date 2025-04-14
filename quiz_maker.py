import tkinter as tk
from tkinter import messagebox

questions = []

def save_question():
    question = entry_question.get()
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    d = entry_d.get()
    answer = answer_var.get()

    if not question or not all([a, b, c, d]) or answer not in ['a', 'b', 'c', 'd']:
        messagebox.showerror("Error", "Please fill all fields correctly.")
        return
    
    questions.append({
        "question": question,
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "answer": answer
    })

    # Clear inputs
    entry_question.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_d.delete(0, tk.END)
    answer_var.set("")

    messagebox.showinfo("Saved", "Question saved!")

def save_to_file_and_exit():
    with open("quiz_data.txt", "w", encoding="utf-8") as f:
        for q in questions:
            f.write(f"Question: {q['question']}\n")
            f.write(f"a) {q['a']}\n")
            f.write(f"b) {q['b']}\n")
            f.write(f"c) {q['c']}\n")
            f.write(f"d) {q['d']}\n")
            f.write(f"Answer: {q['answer']}\n")
            f.write("---\n")
    root.destroy()