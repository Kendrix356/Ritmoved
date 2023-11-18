import rospy
import socket
from clover import srv
from std_srvs.srv import Trigger
import pretty_midi
import time
from clover.srv import SetLEDEffect

rospy.init_node('flight_music')

pretty_midi.note_number_to_name


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('0.0.0.0', 9999)
s.bind(server_address)

midi_file_path = 'We Will Rock You.mid'
midi_data = pretty_midi.PrettyMIDI(midi_file_path)

instrument = midi_data.instruments[0]

led_color = {
    'A': {"r": 255, "g": 0, "b": 0},
    'F': {"r": 0, "g": 255, "b": 0},
    'G': {"r": 0, "g": 0, "b": 255},
    'B': {"r": 148, "g": 0, "b": 211},
    'C': {"r": 255, "g": 255, "b": 0},
    'E': {"r": 66, "g": 170, "b": 255},
    'D': {"r": 255, "g": 255, "b": 255},
} 

phases = [
    [True, True],
    [True, False],
    [False, True],
    [False, False]
]

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_altitude = rospy.ServiceProxy('set_altitude', srv.SetAltitude)
set_yaw = rospy.ServiceProxy('set_yaw', srv.SetYaw)
set_yaw_rate = rospy.ServiceProxy('set_yaw_rate', srv.SetYawRate)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)

def dvig(phase):
    if phase == [True, True]:
        set_position(x=2, y=1, z=1, frame_id='aruco_map')
    elif phase == [True, False]:
        set_position(x=0, y=1, z=1, frame_id='aruco_map')
    elif phase == [False, True]:
        set_position(x=1, y=2, z=1, frame_id='aruco_map')
    elif phase == [False, False]:
        set_position(x=1, y=0, z=1, frame_id='aruco_map')


    # for note in instrument.notes:
    #     note_name = pretty_midi.note_number_to_name(note.pitch)
    #     note_letter = note_name[0]
    #     if note_letter == 'A': set_effect(r=255, g=0, b=0)
    #     if note_letter == 'F': set_effect(r=0, g=255, b=0)  
    #     if note_letter == 'G': set_effect(r=0, g=0, b=255)
    #     if note_letter == 'B': set_effect(r=148, g=0, b=211)
    #     if note_letter == 'C': set_effect(r=255, g=255, b=0)
    #     if note_letter == 'E': set_effect(r=66, g=170, b=255)
    #     if note_letter == 'D': set_effect(r=255, g=255, b=255) 


navigate(x=0, y=0, z=1, frame_id='body', speed=0.5, auto_arm=True)  # взлет на 1 метра
rospy.sleep(7)
navigate(x=1, y=1, z=1, speed=1, frame_id='aruco_map')  # полет в координату 1:1, высота 1 метра
rospy.sleep(5)

while True:
    data, address = s.recvfrom(4096)
    if data.decode('utf-8') == "Start": 
        break


a = midi_data.get_tempo_changes()[1][0]
times = 1/(a/60)

rate = rospy.Rate(a/60)
while True:
    for i in phases:
        dvig(i)
        rate.sleep()
