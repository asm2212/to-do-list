import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=60)  
        self.task_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 

    
        self.important_var = tk.BooleanVar()
        self.important_checkbox = tk.Checkbutton(master, text="Important", variable=self.important_var)
        self.important_checkbox.grid(row=1, column=0, padx=5, pady=10)

        self.add_button = tk.Button(master, text="+", width=2, command=self.add_task)
        self.add_button.grid(row=1, column=1, padx=5, pady=10)

        self.task_text = tk.Text(master, width=80, height=15) 
        self.task_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, padx=5, pady=10)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=3, column=1, padx=5, pady=10)

        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=3, column=2, padx=5, pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            if self.important_var.get():
                task = "⭐ " + task
            self.tasks.append(task)
            self.task_text.insert(tk.END, task + "\n", ("task",))
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        try:
            index = self.task_text.index(tk.ACTIVE)
            self.task_text.delete(index)
            self.save_tasks()
        except tk.TclError:
            messagebox.showwarning("Warning", "No task selected!")

    def update_task(self):
        try:
            index = self.task_text.index(tk.ACTIVE)
            task = self.task_entry.get()
            if task:
                if self.important_var.get():
                    task = "⭐ " + task
                self.task_text.delete(index)
                self.task_text.insert(index, task + "\n", ("task",))
                self.task_entry.delete(0, tk.END)
                self.save_tasks()
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        except tk.TclError:
            messagebox.showwarning("Warning", "No task selected!")
    def complete_task(self):
        try:
            index = self.task_text.index(tk.ACTIVE)
            self.task_text.tag_configure("completed", background="black", foreground="yellow")
            self.task_text.tag_add("completed", index + "linestart", index + "lineend")
        except tk.TclError:
            messagebox.showwarning("Warning", "No task selected!")

    def save_tasks(self):
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as f:
                for task in f.readlines():
                    self.tasks.append(task.strip())
                    self.task_text.insert(tk.END, task.strip() + "\n", ("task",))
        except FileNotFoundError:
            pass
def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()

