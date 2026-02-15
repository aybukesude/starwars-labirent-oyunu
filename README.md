# Star Wars Labirent Oyunu

Bu proje, Star Wars evreninden ilham alınarak geliştirilmiş, algoritma tabanlı bir labirent keşif oyunudur. Projenin odak noktası, harita verilerini dış bir dosyadan okuyarak dinamik bir oyun alanı oluşturmak ve karakter hareketlerini bu yapı üzerinde simüle etmektir.

## Proje Vizyonu

Yazılım, dosya okuma işlemleriyle oyun haritası oluşturma (parsing) ve grafiksel arayüz (GUI) katmanlarını bir araya getirir. Temel amacı, mantıksal bir labirent yapısı içerisinde karakterin engellere takılmadan ilerlemesini ve belirli hedeflere ulaşmasını sağlayan mekaniği kurgulamaktır.

## Teknik Mimari ve Dosya Yapısı

Proje, işlevselliği artırmak adına aşağıdaki modüllere ayrılmıştır:

| Dosya Adı | Teknik Rol | Fonksiyonel Açıklama |
| --- | --- | --- |
| **ana.py** | Controller | Oyunun ana döngüsünü yönetir ve diğer tüm modülleri koordine eder. |
| **grafik.py** | View | Oyunun görsel sunumunu, çizim işlemlerini ve kullanıcı arayüzünü kontrol eder. |
| **karakter.py** | Model | Karakterin yeteneklerini, hareket mantığını ve koordinat sistemini tanımlar. |
| **harita.txt** | Data | Labirentin yapısını (duvarlar, yollar, çıkışlar) temsil eden veri dosyasıdır. |
| **utils.py** | Helper | Çarpışma algoritmaları ve koordinat dönüşümleri gibi yardımcı araçları içerir. |

## Kurulum ve Çalıştırma

Sistemi yerel ortamınızda yapılandırmak için şu adımları izleyebilirsiniz:

1. **Depoyu Klonlayın:**
```bash
git clone https://github.com/aybukesude/starwars-labirent-oyunu.git

```


2. **Dizine Geçiş Yapın:**
```bash
cd starwars-labirent-oyunu/Star Wars Oyunu

```


3. **Uygulamayı Başlatın:**
```bash
python ana.py

```



## Uygulanan Metodolojiler

* **Dinamik Harita Yönetimi:** Oyun alanı `harita.txt` dosyasından okunarak oluşturulur; bu sayede kod değişmeden farklı labirent tasarımları yüklenebilir.
* **Modüler Tasarım:** Grafik işlemleri ve oyun mantığı birbirinden ayrılarak temiz bir kod yapısı hedeflenmiştir.
* **Hata Yönetimi:** Dosya okuma ve karakter sınır kontrolleri gibi süreçlerde veri bütünlüğü korunur.

---

**Not:** Bu proje, Python programlama dili ve grafik kütüphaneleri kullanılarak geliştirilmiş bir eğitim uygulamasıdır.

---

Bu metin, projenin sadece bir "oyun" değil, aynı zamanda veri yönetimi ve modüler kodlama üzerine bir çalışma olduğunu gösterir. **Labirentin çözümü için kullandığın özel bir algoritma (örneğin A* veya DFS) varsa onu da teknik bölüme ekleyebiliriz?**
