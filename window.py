import tkinter as tk
import socket
import time
import pretty_midi
import matplotlib.pyplot as plt
import pygame

root = tk.Tk()
root.title("CheckRpi")
root.geometry("500x300")
root.resizable(False, False)
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

pygame.init()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
a = 0

listm = ("mus1.mid","mus2.mid","mus3.mid","mus4.mid")

def display_mode():
    print(mode.get())

def music_mode():
    pygame.mixer.music.stop()
    s.sendto('Music'.encode('utf-8'), ('192.168.11.1', 9999))

def start_action():
    global a
    n = int(mode_m.get())
    midi_data = pretty_midi.PrettyMIDI(listm[n])
    pygame.mixer.music.load(listm[n])
    pygame.mixer.music.play()
    a = midi_data.get_tempo_changes()[1][0]
    s.sendto(f'Start {a}'.encode('utf-8'), ('192.168.11.1', 9999))

def stop_action():
    pygame.mixer.music.stop()
    s.sendto(f'Stop'.encode('utf-8'), ('192.168.11.1', 9999))

canvas.create_line(250, 0, 250, 300, width=5)
canvas.create_line(0, 150, 500, 150, width=5)

text = """Список команд:"""
canvas.create_text(10, 10, anchor="nw", text=text, font=("Arial", 15))
text = "1) Влево\n2) Вправо\n3) Флип"
canvas.create_text(30, 30, anchor="nw", text=text, font=("Arial", 12))

mode = tk.StringVar(value=1)
mode1 = tk.Radiobutton(root, text="Импровизация", variable=mode, value=1, command=display_mode)
mode2 = tk.Radiobutton(root, text="Повторение", variable=mode, value=2, command=display_mode)
mode1.place(x=30, y=180)
mode2.place(x=30, y=200)
mode_text = canvas.create_text(10, 160, anchor="nw", text="Режим:", font=("Arial", 15))

mode_m = tk.StringVar(value=0)
mode1 = tk.Radiobutton(root, text="Музыка1", variable=mode_m, value=0, command=music_mode)
mode2 = tk.Radiobutton(root, text="Музыка2", variable=mode_m, value=1, command=music_mode)
mode3 = tk.Radiobutton(root, text="Музыка3", variable=mode_m, value=2, command=music_mode)
mode4 = tk.Radiobutton(root, text="Музыка4", variable=mode_m, value=3, command=music_mode)
mode1.place(x=280, y=30)
mode2.place(x=280, y=50)
mode3.place(x=280, y=70)
mode4.place(x=280, y=90)
mode_text = canvas.create_text(260, 10, anchor="nw", text="Музыка:", font=("Arial", 15))

start_button = tk.Button(root, text="Старт", width= 30, command=start_action)
start_button.place(x=10, y=230)
start_button = tk.Button(root, text="Стоп", width= 30, command=stop_action)
start_button.place(x=10, y=260)

root.mainloop()

# while(True):
#     takt += 1
#     print("takt",takt)
#     time.sleep(times)


