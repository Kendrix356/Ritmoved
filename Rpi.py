import rospy
import socket
from clover import srv
from std_srvs.srv import Trigger
import pretty_midi
import matplotlib.pyplot as plt
import time

rospy.init_node('flight_music')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('0.0.0.0', 9999)
s.bind(server_address)

midi_file_path = 'We Will Rock You.mid'
midi_data = pretty_midi.PrettyMIDI(midi_file_path)

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

def dvig(kk = False):
    if kk == False:
        set_velocity(vx=1, vy=0.0, vz=0, frame_id='body')
        rospy.sleep(0.2)
        set_velocity(vx=0.0, vy=0.0, vz=0, frame_id='body')
    elif kk == True:
        set_velocity(vx=-1, vy=0.0, vz=0, frame_id='body')
        rospy.sleep(0.2)
        set_velocity(vx=0.0, vy=0.0, vz=0, frame_id='body')

navigate(x=0, y=0, z=1, frame_id='body', speed=0.5, auto_arm=True)  # взлет на 1 метра
rospy.sleep(7)
navigate(x=1, y=1, z=1, speed=1, frame_id='aruco_map')  # полет в координату 1:1, высота 1 метра
rospy.sleep(5)

while True:
    data, address = s.recvfrom(4096)
    if data.decode('utf-8') == "Start": 
        break

# rospy.sleep(5)

a = midi_data.get_tempo_changes()[1][0]
times = 1/(a/60)

b = True

while True:
    b = not b
    dvig(b)
    rospy.sleep(times-0.2)