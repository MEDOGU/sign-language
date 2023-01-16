import cv2
import time
import HandTrackingModule as htm

import  time


#görüntüyü cap değikenine atıyoruz
cap=cv2.VideoCapture(0)

#görüntü boyutlarını ayarlıyoruz
wCam,hCAm=640,480
cap.set(3,wCam)
cap.set(4,hCAm)



detector=htm.handDetector(detectionCon=0.8)

tips_id=[4,8,12,16,20]



while True:

   #aldığımız görüntüyü  okuyoruz
   success, img = cap.read()
   #aldığımız görüntüde bulunan elleri buluyoruz.( kütüphane ile)
   img = detector.findHands(img)
   lmllist = detector.findPosition(img, draw=False)







   if len(lmllist) != 0:
       mesaj=[]

       if lmllist[tips_id[4]][2]<lmllist[tips_id[0]][2] and lmllist[20][2]<lmllist[18][2] and lmllist[8][2]>lmllist[6][2] and lmllist[12][2]>lmllist[10][2] and lmllist[16][2]>lmllist[14][2]:
           cv2.rectangle(img, (20, 225), (170, 425), (0, 0, 255), cv2.FILLED)
           cv2.putText(img, str("Y"), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
           mesaj.append("y")
       if lmllist[tips_id[4]][2]<lmllist[tips_id[0]][2] and lmllist[20][2]<lmllist[18][2] and lmllist[8][2]<lmllist[6][2] and lmllist[12][2]>lmllist[10][2] and lmllist[16][2]>lmllist[14][2]:
           cv2.putText(img, str("Seni seviyorum"), (50, 400), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 2)

           #speak("seni seviyorum")


       fingers = []
        #bu sadece baş parmak için
       if lmllist[tips_id[0]][1] > lmllist[tips_id[0] - 1][1]:
           # print("finger open")
           fingers.append("1")

       else:
           fingers.append("0")
        #burası diğer parmaklar için geçerli
       for id in range(1, 5):
           if lmllist[tips_id[id]][2] < lmllist[tips_id[id] - 2][2]:
               # print("finger open")
               fingers.append("1")
           else:
               fingers.append("0")





       totalFingers = fingers.count("1")
       print(totalFingers)
       print(mesaj)


       cv2.circle(img,(lmllist[18][1],lmllist[18][2]),4,(0,255,0),cv2.FILLED)
       cv2.circle(img, (lmllist[20][1], lmllist[20][2]), 4, (255, 255, 0), cv2.FILLED)

       #cv2.rectangle(img, (20, 225), (170, 425), (0, 0, 255), cv2.FILLED)
       #cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

   cv2.imshow("cap", img)

   k = cv2.waitKey(1)

   if k == ord("q"):
       cap.release()
