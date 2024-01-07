from djitellopy import Tello
import cv2
import time

qrd = cv2.QRCodeDetector()


###############################################
startCounter = 1
height = 720
width = 1080
################################################

# Connection to Tello 
me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())

def wake_up():
    me.takeoff()
    time.sleep(2)
    me.rotate_clockwise(-90)
    time.sleep(3)
    time.sleep(3)
    print ("Tello waked-up")

def step1():
    time.sleep(2)
    me.rotate_clockwise(90)
    time.sleep(3)
    me.move_forward(20)
    time.sleep(4)
    print("Tello reached step1")

def step2():
    time.sleep(2)
    me.rotate_clockwise(-90)
    time.sleep(3)
    print("Tello reached step2")



me.streamoff()
me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.flip(img,1)
    if img is not None and len(img) > 0:
        ret_qr, decoded_info, points, _ = qrd.detectAndDecodeMulti(img)
        if ret_qr:
            for s,p in zip(decoded_info, points):
                color = (0, 255, 0)
                if s:
                    print('QR Code détecté:')
                    print(s)
                    color = (0, 255, 0)
                else:
                    color = (0,0,255)
            img = cv2.polylines(img, [p.astype(int)], True, color, 8)
        
            if s.startswith('wake'):
                wake_up()
                me.streamon()
            elif s.startswith('mvl'):
                step1() #move_left
                me.streamon()
            elif s.startswith('mvr'):
                step2()
                me.streamon()


    # Display the image
    img = cv2.resize(img, (width, height))
    cv2.imshow("MyResult", img)

    # Wait for the 'Q' button to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break
