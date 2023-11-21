from tkinter import *
from PIL import Image, ImageTk
from tkextrafont import Font
from tkinter import filedialog, ttk
import tkinter as tk
import socket
import pretty_midi
import pygame


root = tk.Tk()
root.title("CheckRpi")
root.geometry("500x500")
root.resizable(False, False)
root.configure(background='black')
canvas = Canvas(root,background='black', highlightbackground="black",width=500,height=500)
canvas.pack()


pygame.init()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

a = 0
listm = ("mus1.mid","mus2.mid","mus3.mid","mus4.mid")

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
  
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True, outline="grey", width=3)

def display_mode():
    print(mode.get())

def music_mode():
    pygame.mixer.music.stop()
    s.sendto('Music'.encode('utf-8'), ('192.168.11.1', 9999))

def open_file_dialog():
    global file_path
    file_path = filedialog.askopenfilename()
    file_label.config(text=file_path.split("/")[-1])

def start_action():
    global a
    global file_path 
    try:
      print(file_path)
      midi_data = pretty_midi.PrettyMIDI(file_path)
      pygame.mixer.music.load(file_path)
      pygame.mixer.music.play()
      a = midi_data.get_tempo_changes()[1][0]
      s.sendto(f'Start {a}'.encode('utf-8'), ('192.168.11.1', 9999))
      print(f'Start {a}')
    except: pass

def stop_action():
    pygame.mixer.music.stop()
    s.sendto(f'Stop'.encode('utf-8'), ('192.168.11.1', 9999))

my_rectangle = round_rectangle(10, 10, 245, 245, radius=50, fill="#2D9CAF")
my_rectangle = round_rectangle(255, 10, 490, 245, radius=50, fill="#2D9CAF")
my_rectangle = round_rectangle(10, 255, 245, 490, radius=50, fill="#2D9CAF")
my_rectangle = round_rectangle(255, 255, 490, 490, radius=50, fill="#2D9CAF")

image = Image.open("pic1.png")
photo = ImageTk.PhotoImage(image)
image_item = canvas.create_image(130, 130, image=photo)
canvas.image = photo

text = "Ритмовед"
canvas.create_text(31, 23, anchor="nw", text=text, font=('Bicubik', 30), fill="white")

mode = tk.StringVar(value=1)
mode1 = tk.Radiobutton(root, text="Импровизация", variable=mode, value=1, command=display_mode, background="#2D9CAF", font=("Arial", 15))
mode2 = tk.Radiobutton(root, text="Повторение", variable=mode, value=2, command=display_mode, background="#2D9CAF", font=("Arial", 15))
mode1.place(x=40, y=310)
mode2.place(x=40, y=340)
mode_text = canvas.create_text(31, 265, anchor="nw", text="Режим:", font=("Arial", 30), fill="white")


image_pic2 = Image.open("pic2.png").resize((200, 50))
image2 = ImageTk.PhotoImage(image_pic2)

start_button = tk.Button(root, command=start_action, background="#2D9CAF", borderwidth=0, border="0", width=200, height=50)
start_button.config(image=image2, compound=tk.CENTER)


image_pic3 = Image.open("pic3.png").resize((196, 45))
image3 = ImageTk.PhotoImage(image_pic3)

stop_button = tk.Button(root, command=start_action, background="#2D9CAF", borderwidth=0, border="0", width=200, height=50)
stop_button.config(image=image3, compound=tk.CENTER)

start_button.place(x=31, y=370)
stop_button.place(x=28, y=430)

mode_text = canvas.create_text(271, 23, anchor="nw", text="Музыка:", font=("Arial", 30), fill="white")


image_pic4 = Image.open("pic4.png").resize((200, 50))
image4 = ImageTk.PhotoImage(image_pic4)

upload_button = tk.Button(root, background="#2D9CAF", borderwidth=0, border="0", width=200, height=50, command=open_file_dialog)
upload_button.config(image=image4, compound=tk.CENTER)
upload_button.place(x=271, y=73)

file_label = tk.Label(root, text="", wraplength=150, background="#2D9CAF")
file_label.place(x=291, y=143)

root.mainloop()












