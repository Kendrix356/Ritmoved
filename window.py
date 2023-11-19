import tkinter as tk

root = tk.Tk()
root.title("CheckRpi")
root.geometry("500x300")
root.resizable(False, False)
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

def display_mode():
    print(mode.get())

def start_action():
    print("Start button clicked!")

canvas.create_line(250, 0, 250, 300, width=5)
canvas.create_line(0, 150, 500, 150, width=5)

text = """Список команд:"""
canvas.create_text(10, 10, anchor="nw", text=text, font=("Arial", 15))
text = "1) Влево\n2) Вправо\n3) Флип"
canvas.create_text(30, 30, anchor="nw", text=text, font=("Arial", 12))

mode = tk.StringVar()
mode1 = tk.Radiobutton(root, text="Импровизация", variable=mode, value=1, command=display_mode)
mode2 = tk.Radiobutton(root, text="Повторение", variable=mode, value=2, command=display_mode)
mode1.place(x=30, y=180)
mode2.place(x=30, y=200)
mode_text = canvas.create_text(10, 160, anchor="nw", text="Режим:", font=("Arial", 15))

start_button = tk.Button(root, text="Старт", width= 30, command=start_action)
start_button.place(x=10, y=250)

root.mainloop()
