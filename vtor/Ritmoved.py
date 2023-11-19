import socket
import time
import pretty_midi
import matplotlib.pyplot as plt
import pygame

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

midi_file_path = 'We Will Rock You.mid'
midi_data = pretty_midi.PrettyMIDI(midi_file_path)

print(midi_data.get_tempo_changes())
a = midi_data.get_tempo_changes()[1][0]
takt = 0
times = 1/(a/60)

pygame.init()
pygame.mixer.music.load(midi_file_path)
pygame.mixer.music.play()

s.sendto('Start'.encode('utf-8'), ('192.168.11.1', 9999))

while(True):
    takt += 1
    print("takt",takt)
    time.sleep(times)
