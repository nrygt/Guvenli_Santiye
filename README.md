# 👷‍♂️ Güvenli Şantiye Yapay Zeka Sistemi

Bu proje, inşaat ve şantiye alanlarında iş güvenliğini artırmak amacıyla **YOLOv8** kullanılarak geliştirilmiş gerçek zamanlı bir bilgisayarlı görü (Computer Vision) sistemidir.

## 🚀 Özellikler
* **Gerçek Zamanlı Tespit:** Kameradan anlık olarak personeli takip eder.
* **Kişisel Koruyucu Donanım (KKD) Kontrolü:** Özel olarak eğitilmiş model ile Baret (hardhat) ve fosforlu yelek (vest) kullanımını denetler.
* **Akıllı Alarm Sistemi:** Ekranda tespit edilen personelin üzerinde baret veya yelek eksikse anında **kırmızı çerçeveli görsel uyarı** ve **sesli alarm** verir.

## 🛠️ Kullanılan Teknolojiler
* Python
* OpenCV (Görüntü İşleme ve Arayüz)
* Ultralytics YOLOv8 (Nesne Tespiti & Model Eğitimi)
* Google Colab (Model Eğitimi için Bulut GPU)

## ⚙️ Kurulum ve Çalıştırma
1. Dosyaları bilgisayarınıza indirin.
2. Gerekli kütüphaneleri kurun:
   `pip install ultralytics opencv-python`
3. `best.pt` model dosyasının `kamera.py` ile aynı klasörde olduğundan emin olun.
4. Sistemi başlatın:
   `python kamera.py`

*Not: Bu proje, iş sağlığı ve güvenliği süreçlerini otonomlaştırmak amacıyla sıfırdan veri seti ile eğitilerek geliştirilmiştir.*
