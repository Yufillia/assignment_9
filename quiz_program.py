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