"""veri setimizi, veri klasörü içine olusturduğumuz modül"""

import cv2      #opencv kütüphanesi eklendi

vid_cam = cv2.VideoCapture(0)   #video kamera tanımlandı

#yüz sınıflandırıcı tanımlandı
yuz_dedektor = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

yuz_ismi = 6    #her görüntü için farklı bir kimlik tanımlanacak
sayi = 0        #çekilecek fotoğraf sayısı

while(True):
    resim_cerceve = vid_cam.read()   #kamera görüntüsü alındı

    gri = cv2.cvtColor(resim_cerceve, cv2.COLOR_BGR2GRAY) #görüntüyü griye ceviriyoruz

    yuzler = yuz_dedektor.detectMultiScale(gri, 1.3, 5) #görüntü içindeki yüz alanlarını saptıyoruz

    for(x, y, w, h) in yuzler: #yuzu algılayacak çerçeve ebatları 

        #cerceve kalınlıgı ve rengı
        cv2.rectangle(resim_cerceve, (x, y), (x + w, y + h), (0, 0, 255), 2)
        sayi += 1

        #yakalanan görüntü veri klasörüne aşağıdaki şekilde yazdırılır
        cv2.imwrite("veri/User." + str(yuz_ismi) + '.' + str(sayi) + ".jpg", gri[y: y+h, x: x+w])
       
        #kamera görüntüsünü (tamamını) ekrana yansıtıyoruz
        cv2.imshow('cerceve' , resim_cerceve)   

        #kameradan çıkış tuşu ve gecikme süresi belirlendi
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    elif sayi > 100: #her bir kişi için veri setimizde 100 göruntü olacak
        break

vid_cam.release()   #kamera durduruldu
cv2.destroyAllWindows() #tum pencereler kapatıldı(bellek temizlendi)



