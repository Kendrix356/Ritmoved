import pretty_midi
import time
midi_data = pretty_midi.PrettyMIDI("barbiegirl_mono.mid")

pretty_midi.note_number_to_name

led_color = {
    'A': {"r": 255, "g": 0, "b": 0},
    'F': {"r": 0, "g": 255, "b": 0},
    'G': {"r": 0, "g": 0, "b": 255},
    'B': {"r": 148, "g": 0, "b": 211},
    'C': {"r": 255, "g": 255, "b": 0},
    'E': {"r": 66, "g": 170, "b": 255},
    'D': {"r": 255, "g": 255, "b": 255},
} 

instrument = midi_data.instruments[0]

# for note in instrument.notes:
print(instrument.notes)