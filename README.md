# Face Recognition with Image Processing Base [OpenCV - Face Recognition]

## Yüz Algılama 
Bir görüntüdeki yüzleri (konum ve boyut) bulma ve muhtemelen yüz tanıma algoritması tarafından kullanılmak üzere çıkarma amacına sahiptir.

## Yüz Tanıma
Yüz görüntüleri zaten ayıklanmış, kırpılmış, yeniden boyutlandırılmış ve genellikle gri tonlamaya dönüştürüldüğünde, yüz tanıma algoritması görüntüyü en iyi tanımlayan özellikleri bulmaktan sorumludur.

##Projemizdeki dosya ve klasörlerle ilgili özet bilgiler

### Projemizde öncelikle yuz_verisi.py , yuz_tanima.py ve deneme.py dosyalarını ve deneme ve veri adında iki adet klasör oluşturduk.

-	yuz_verisi.py: veri setimizi, veri klasörü içine oluşturduğumuz modül.
Veri setimizde yer alacak her kişiyi yuz_ismi değişkenini değiştirerek  kameraya tanıttık.
-	deneme.py: Veri setimizi eğittiğimiz modül
-	yuz_tanima.py: kameraya gösterilen yüzleri, veri setimizdeki yüzlerle karşılaştırarak tanıyacak olan modül
-	veri.yml: veri setimizin tutulduğu klasör
-	deneme.yml: Veri setimizdeki verilerin eğitildikten sonra tutulduğu klasör
