import cv2
from ultralytics import YOLO
import winsound
import threading
import time

# Kendi eğittiğimiz zeki beyni projeye dahil ediyoruz
model = YOLO('best.pt')
sinif_isimleri = model.names

kamera = cv2.VideoCapture(0)

# Seslerin üst üste binmesini engellemek için bir zamanlayıcı tutuyoruz
son_alarm_zamani = 0

def alarm_cal():
    # 2500 Hz frekansında (ince bir ses), 300 milisaniye boyunca çal
    winsound.Beep(2500, 300)

while True:
    basarili_mi, kare = kamera.read()
    if not basarili_mi:
        break

    sonuclar = model(kare)
    cizimli_kare = sonuclar[0].plot()

    tespit_edilenler = []
    for kutu in sonuclar[0].boxes:
        sinif_id = int(kutu.cls[0])
        sinif_adi = sinif_isimleri[sinif_id]
        tespit_edilenler.append(sinif_adi)

    print("Ekranda Bulunanlar:", tespit_edilenler)

    # KURAL KONTROLÜ
    if "person" in tespit_edilenler:
        if "hardhat" not in tespit_edilenler or "vest" not in tespit_edilenler:
            
            yukseklik, genislik, _ = cizimli_kare.shape
            
            # Kırmızı çerçeve ve yazı
            cv2.rectangle(cizimli_kare, (0, 0), (genislik, yukseklik), (0, 0, 255), 20)
            cv2.putText(cizimli_kare, "DIKKAT: KISISEL DONANIM EKSIK!", (30, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            
            # SESLİ ALARM KONTROLÜ (Saniyede sadece 1 kez çalmasına izin veriyoruz)
            su_an = time.time()
            if su_an - son_alarm_zamani > 1.0:
                # Kamerayı dondurmamak için sesi arka planda (Thread ile) başlatıyoruz
                threading.Thread(target=alarm_cal).start()
                son_alarm_zamani = su_an

    cv2.imshow("Guvenli Santiye AI - Canli Denetim", cizimli_kare)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


kamera.release()
cv2.destroyAllWindows()