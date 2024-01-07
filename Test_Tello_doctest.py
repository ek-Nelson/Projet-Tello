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
        time.sleep(5)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.move_left(35)
        time.sleep(3)
        me.land()



#cap = cv2.VideoCapture(me)

me.streamoff()
me.streamon()
#fourcc = cv2.VideoWriter_fourcc(* 'XVID')


while True:
    frame_read = me.get_frame_read()
    myframe = frame_read.frame
    #img = cv2.resize(myframe, (width, height))
    myframe = cv2.flip(myframe,1)
    #img = cv2.resize(myframe, (width, height))

    if myframe is not None and len(myframe) > 0:
        ret_qr, decoded_info, points, _ = qrd.detectAndDecodeMulti(myframe)
        if ret_qr:
            for s,p in zip(decoded_info, points):
                color = (0, 255, 0)
                if s:
                    print('QR Code détecté:')
                    print(s)
                    color = (0, 255, 0)
                else:
                    color = (0,0,255)
            myframe = cv2.polylines(myframe, [p.astype(int)], True, color, 8)
            if s.startswith('wake'):
                wake_up()


    # TO GO UP IN THE BEGINNING
    if startCounter == 0:
       # me.takeoff()
        #time.sleep(8)
        #me.rotate_clockwise(90)
        #time.sleep(3)
        #me.move_left(35)
        #time.sleep(3)
        #me.land()
        startCounter = 1

    # Display the image
    img = cv2.resize(myframe, (width, height))
    cv2.imshow("MyResult", img)

    # Wait for the 'Q' button to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break

if __name__ == "__main__":
    import doctest
    doctest.testmood()