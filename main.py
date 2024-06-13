import tkinter as tk 
from tkinter import Message, mainloop, messagebox
import os 

#criar janela principal 
root = tk.Tk() 
root.title("Lista de Tarefas")
root.geometry("300x400")

#entrada de texto para nova tarefa
task_entry = tk.Entry(root, width=20) 
task_entry.pack (pady=10) 


#carregar tarefas de um arquivo
def load_tasks():
  if os.path.exists("takss.txt"):
    with open("tasks.txt", "r") as file:
      tasks = file.readlines
#listbox para mostrar tarefas 
tasks_listbox = tk.Listbox(root, width=30, height=10)
tasks_listbox.pack(pady=10)

#salvar tarefas em um arquivo 
def save_tasks():
  with open("tasks.txt", "w") as file:
    task = tasks_listbox.get(0, tk.END)
    for task in tasks: 
      file.write(task + "\n")


#função para adicionar tarefa 
def add_task(): 
  task = task_entry.get()
  if task :
    tasks_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    save_tasks()
  else: 
    messagebox.showwarning("Aviso", "Digite uma tarefa.")

#botao de adicionar tarefa
add_boton = tk.Button(root, text = "Adicionar Tarefa", command = add_task)
add_boton.pack(pady=5)
                      
#função remover tarefa
def remove_task():
  try:
    selected_task_index = tasks_listbox.curselection()[0]
    tasks_listbox.delete(selected_task_index)
    save_tasks()
  except IndexError:
    messagebox.showwarning("Aviso", "selecione uma tarefa para remover")

#botao remover tarefa
remove_button = tk.Button(root, text="Remover Tarefa", command = remove_task)
remove_button.pack(pady=5)

#carregar tarefas ao iniciar programa
load_tasks()

root.mainloop()

  
    
                      

















