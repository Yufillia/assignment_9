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