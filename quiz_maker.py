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

# GUI Setup
root = tk.Tk()
root.title("Quiz Creator GUI")

tk.Label(root, text="Question:").grid(row=0, column=0, sticky="w")
entry_question = tk.Entry(root, width=50)
entry_question.grid(row=0, column=1)

tk.Label(root, text="Choice a:").grid(row=1, column=0, sticky="w")
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1)

tk.Label(root, text="Choice b:").grid(row=2, column=0, sticky="w")
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)

tk.Label(root, text="Choice c:").grid(row=3, column=0, sticky="w")
entry_c = tk.Entry(root)
entry_c.grid(row=3, column=1)

tk.Label(root, text="Choice d:").grid(row=4, column=0, sticky="w")
entry_d = tk.Entry(root)
entry_d.grid(row=4, column=1)

tk.Label(root, text="Correct Answer (a/b/c/d):").grid(row=5, column=0, sticky="w")
answer_var = tk.StringVar()
entry_answer = tk.Entry(root, textvariable=answer_var)
entry_answer.grid(row=5, column=1)

tk.Button(root, text="Save Question", command=save_question).grid(row=6, column=0, pady=10)
tk.Button(root, text="❌ Exit & Save to File", command=save_to_file_and_exit).grid(row=6, column=1)

root.mainloop()