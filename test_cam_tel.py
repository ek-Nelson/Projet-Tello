from djitellopy import Tello
import cv2
import time

###############################################
startCounter = 1
height = 240
width = 320
################################################
def wake_up():
    # Connection to Tello    
    if startCounter == 0:
        me.takeoff()
        time.sleep(5)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.move_left(35)
        time.sleep(3)
        me.land()
        startCounter = 1


# Connection to Tello 
me = Tello()
me.connect()
if (me.connect()):
    print ("connection succeed")

qrd = cv2.QRCodeDetector()
print(me.get_battery())
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

me.streamon()

while True:
    frame_read = me.get_frame_read()
    myframe = frame_read.frame
    img = myframe

    ret_qr, decoded_info, points, _ = qrd.detectAndDecodeMulti(img)
    if ret_qr: # si un QR Code a été détectés dans la trame
        for s, p in zip(decoded_info, points):
            color = (0,255,0)
            if s:
                print('QR Code détecté:')
                print(s)
                color = (0, 255, 0)
            else:
                color = (0,0,255)
        frame = cv2.polylines(img, [p.astype(int)], True, color, 8)       

    # Display the image
    if not img is None and not img.size == 0:
        cv2.imshow("MyResult", img)
    else:
        print("Frame is empty or None")
        break

    # Wait for the 'Q' button to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break