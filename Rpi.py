import rospy
import socket
from clover import srv
from std_srvs.srv import Trigger
import time
from clover.srv import SetLEDEffect

rospy.init_node('flight_music')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('0.0.0.0', 9999)
s.bind(server_address)

led_color = [
    {"r": 255, "g": 0, "b": 0},
    {"r": 0, "g": 255, "b": 0},
    {"r": 0, "g": 0, "b": 255},
    {"r": 255, "g": 255, "b": 255},
]

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
        set_position(x=1.5, y=1, z=1, frame_id='aruco_map')
    elif phase == [True, False]:
        set_position(x=0, y=1, z=1, frame_id='aruco_map')
    elif phase == [False, True]:
        set_position(x=1, y=0.5, z=1, frame_id='aruco_map')
    elif phase == [False, False]:
        set_position(x=1, y=2, z=1, frame_id='aruco_map')

def backstart():
    navigate(x=1, y=1, z=1, speed=1, frame_id='aruco_map')  # полет в координату 1:1, высота 1 метра
    rospy.sleep(1)
    set_effect(r=255, g=0, b=0)
    rospy.sleep(1)
    set_effect(r=0, g=0, b=0)
    rospy.sleep(1)
    set_effect(r=255, g=0, b=0)
    rospy.sleep(1)
    set_effect(r=0, g=0, b=0)
    rospy.sleep(1)

def svmusic(temp):
    global rate
    global st
    global st2
    rate = rospy.Rate(float(temp)/60)
    st = False
    st2 = False

navigate(x=0, y=0, z=1, frame_id='body', speed=0.5, auto_arm=True)  # взлет на 1 метра
rospy.sleep(5)
navigate(x=1, y=1, z=1, speed=1, frame_id='aruco_map')  # полет в координату 1:1, высота 1 метра
rospy.sleep(5)

while True:
    data, address = s.recvfrom(4096)
    data = data.decode('utf-8')
    data = data.split(" ")
    if "Start" in data:
        temp = float(data[1])
        break

svmusic(temp)

s.setblocking(False)

while True:
    if st == False and st2 == False:
        for i in range(4):
            dvig(phases[i])
            set_effect(**led_color[i])
            rate.sleep()
    try:
        data, address = s.recvfrom(4096)
        data = data.decode('utf-8')
    except: continue 

    if data.split(" ")[0] == "Start": svmusic(data.split(" ")[1])
    elif data == "Music": 
        backstart()
        st2 = True
    elif data == "Stop": 
        if st == True: break
        backstart()
        st = True
land()
