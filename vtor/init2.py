import pretty_midi
import matplotlib.pyplot as plt
import time

midi_data = pretty_midi.PrettyMIDI('We Will Rock You.mid')
a = midi_data.estimate_tempi()[0]
takt = 0
while(True):
    for i in a:
        print("takt",takt)
        takt += 1
        time.sleep(1/(i/60))