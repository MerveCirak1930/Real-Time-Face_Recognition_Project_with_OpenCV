
""" kameraya gösterilen yüzleri, veri setimizdeki yüzlerle karşılaştırarak tanıyacak olan modül"""

import cv2      #opencv kütüphanesi eklendi
import numpy as np
from PIL import Image

taniyici = cv2.face.LBPHFaceRecognizer_create()     #yüz tanıyıcı olusturuldu (tanıyıcı değişkeni, yüz tanıma nesnesi)
taniyici.read("deneme/deneme.yml")                  #tanıyıcı deneme.yml dosyasını okuyacak

#canlı kamera görüntülerindeki yüzleri de yine haarcascade_frontalface_default.xml filtresi ile yakalayacağız
yolsiniflandirici = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
yuzsiniflandirici = cv2.CascadeClassifier(yolsiniflandirici)   

font = cv2.FONT_HERSHEY_SIMPLEX #yazi tipi belirlendi
vid_cam = cv2.VideoCapture(0)   # Bilgisayara bağlı kameradan alınan görüntü vid_cam değişkenine atandı.

while(True):
    ret, kamera = vid_cam.read()    #vid_cam den okunan görüntü kameraya atandı
    gri = cv2.cvtColor(kamera, cv2.COLOR_BGR2GRAY)  #Kameradan alınan görüntü daha iyi bir tespit için BGR den gri ye çevirildi.
    yuzler = yuzsiniflandirici.detectMultiScale(gri, 1.2, 5)    #görüntü karesindeki tüm yüzleri yakalıyoruz 

    for(x, y, w, h) in yuzler:
        cv2.rectangle(kamera, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)   #Yüzün çevresini çevreleyen dikdörtgen.
        Id, confidence = taniyici.predict(gri[y: y+h, x: x+w])    
        print(Id)
        print(100 - confidence) #Doğruluk oranı
        print("\n")

        #Id leri tanıtılan kişilerin tanındıktan sonra ceza eklendiği kısım.
        if(Id == 1):
            name = "Ali"
        elif(Id == 2):
            name = "Ayşe"
        elif(Id == 3):
            name = "Ebru"
        elif(Id == 4):
            name = "Fatih"
        elif(Id == 5):
            name = "Melis"
            

        #yuz tanıma için cerceve ebatları belirlendi
        cv2.rectangle(kamera, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
        
        #yazılacak ismin boyutları,rengi ve kalınlığı belirlendi
        cv2.putText(kamera, str(name), (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)

    cv2.imshow('Goruntu', kamera)    #Kameradan alınan görüntü ekranda gösterilir

    #Yuz tanıma programının sonlandırılması.
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

vid_cam.release()
cv2.destroyAllWindows()