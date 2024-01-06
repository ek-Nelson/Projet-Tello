import cv2

#print("Before URL")
# url='rtsp://' 

cap = cv2.VideoCapture(0)
qrd = cv2.QRCodeDetector()
s = 'a'
p = 0

while True:
    # Lit chaque trame de le vidéo
    ret, frame = cap.read() # ret est la capture de la trame vidéo
    frame = cv2.flip(frame,1)

    if ret: # Si la capture de trame a été bien faite, on extrait ses élèments
        ret_qr, decoded_info, points, _ = qrd.detectAndDecodeMulti(frame)
        if ret_qr: # si un QR Code a été détectés dans la trame
            for s, p in zip(decoded_info, points):
                color = (0,255,0)
                if s:
                    print('QR Code détecté:')
                    print(s)
                    color = (0, 255, 0)
                else:
                    color = (0,0,255)
            frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
            #Lecture des instructions masquées dans le QR Code
            if s.startswith('http' or 'https'):
                    import webbrowser
                    webbrowser.open(s)       
        
        #Affiche la video en direct
        cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

#Libère la capture vidéo et ferme la fenêtre
cap.release()
cv2.destroyAllWindows()