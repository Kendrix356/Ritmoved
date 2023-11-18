import pretty_midi
import time
import rospy
from clover.srv import SetLEDEffect
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)
midi_data = pretty_midi.PrettyMIDI("barbiegirl_with_chords.mid")

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

for note in instrument.notes:
    note_name = pretty_midi.note_number_to_name(note.pitch)
    note_letter = note_name[0]
    print(note_name, led_color[note_letter])
    if note_letter == 'A':
        set_effect(r=255, g=0, b=0)
    if note_letter == 'F':
        set_effect(r=0, g=255, b=0)  
    if note_letter == 'G':
        set_effect(r=0, g=0, b=255)
    if note_letter == 'B':
        set_effect(r=148, g=0, b=211)
    if note_letter == 'C':
        set_effect(r=255, g=255, b=0)
    if note_letter == 'E':
        set_effect(r=66, g=170, b=255)
    if note_letter == 'D':
        set_effect(r=255, g=255, b=255) 
    time.sleep(0.5)
