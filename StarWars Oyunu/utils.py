from karakter import Stormtrooper, DarthVader, KyloRen, Lokasyon

def haritaOku(dosyaAdi):
    with open(dosyaAdi, 'r') as f:
        return [satir.strip().split() for satir in f if not satir.startswith("Karakter:")]

def karakterleriOku(dosyaAdi):
    karakterler = []
    konumlar = {
        'A': (0, 5),
        'B': (3, 0),
        'C': (13, 0),
        'D': (13, 5),
        'E': (3, 10)
    }

    with open(dosyaAdi, 'r') as f:
        for satir in f:
            if satir.startswith("Karakter:"):
                try:
                    parcalar = satir.strip().split(",")
                    isim = parcalar[0].split(":")[1]
                    kapi = parcalar[1].split(":")[1]
                    x, y = konumlar.get(kapi, (0, 0))

                    if isim == "Stormtrooper":
                        karakter = Stormtrooper(Lokasyon(x, y))
                    elif isim == "DarthVader":
                        karakter = DarthVader(Lokasyon(x, y))
                        karakter.ad = "Darth Vader"
                    elif isim == "KyloRen":
                        karakter = KyloRen(Lokasyon(x, y))
                        karakter.ad = "Kylo Ren"
                    else:
                        continue  # Tanımlı olmayan karakter varsa geç

                    karakterler.append(karakter)
                except Exception as e:
                    print(f"Karakter yüklenirken hata: {e}")
    return karakterler
