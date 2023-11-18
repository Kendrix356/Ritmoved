import pretty_midi
import matplotlib.pyplot as plt
import time
import pygame

midi_file_path = 'We Will Rock You.mid'
midi_data = pretty_midi.PrettyMIDI(midi_file_path)

print(midi_data.get_tempo_changes())
a = midi_data.get_tempo_changes()[1][0]
#a = int(str(a)[1:-2])
takt = 0
times = 1/(a/60)

pygame.init()
# pygame.mixer.init()
pygame.mixer.music.load(midi_file_path)
pygame.mixer.music.play()

while(True):
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(60)
    takt += 1
    print("takt", takt, " time= ", times-0.2)
    time.sleep(times)
