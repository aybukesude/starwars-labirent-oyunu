import pygame
from karakter import *
from grafik import haritayiCiz
from utils import haritaOku, karakterleriOku


# Karakter seçimi (Pygame başlamadan önce yapılmalı!)
secim = None
while secim not in ["1", "2"]:
    print("Karakter Seçin:\n1 - Luke Skywalker\n2 - Master Yoda")
    secim = input("Seçiminiz: ")

if secim == "1":
    oyuncu = LukeSkywalker(Lokasyon(6, 5))
else:
    oyuncu = MasterYoda(Lokasyon(6, 5))

# Pygame başlat
pygame.init()

ekran = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Star Wars Labirent Oyunu")
clock = pygame.time.Clock()

# Ses başlat
pygame.mixer.init()
alert = pygame.mixer.Sound("assets/alert.wav")

# Görselleri yükle
resimler = {
    "Luke Skywalker": pygame.image.load("assets/luke.png"),
    "Master Yoda": pygame.image.load("assets/yoda.png"),
    "Stormtrooper": pygame.image.load("assets/stormtrooper.png"),
    "Darth Vader": pygame.image.load("assets/vader.png"),
    "Kylo Ren": pygame.image.load("assets/kylo.png"),
    "Cup": pygame.image.load("assets/cup.png"),
    "Heart": pygame.image.load("assets/heart.png")

}

# Haritayı oku
harita = haritaOku("harita.txt")


dusmanlar = karakterleriOku("harita.txt")


calisiyor = True
while calisiyor:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False



    # Oyuncu hareketi
    keys = pygame.key.get_pressed()
    x, y = oyuncu.konum.getX(), oyuncu.konum.getY()

    if keys[pygame.K_UP] and y > 0 and harita[y - 1][x] != '0':
        oyuncu.konum.setY(y - 1)
    elif keys[pygame.K_DOWN] and y < len(harita) - 1 and harita[y + 1][x] != '0':
        oyuncu.konum.setY(y + 1)
    elif keys[pygame.K_LEFT] and x > 0 and harita[y][x - 1] != '0':
        oyuncu.konum.setX(x - 1)
    elif keys[pygame.K_RIGHT] and x < len(harita[0]) - 1 and harita[y][x + 1] != '0':
        oyuncu.konum.setX(x + 1)

    print("Oyuncunun konumu:", oyuncu.konum.getX(), oyuncu.konum.getY())

    # Düşmanlar oyuncuyu takip etsin
    hedef = (oyuncu.konum.getX(), oyuncu.konum.getY())
    for dusman in dusmanlar:
        yol = dusman.EnKisaYol(harita, hedef)
        if yol:
            print(f"{dusman.getAd()} oyuncuya {len(yol)} adım uzaklıkta.")
            sonraki = yol[0]
            dusman.konum.setX(sonraki[0])
            dusman.konum.setY(sonraki[1])

        # Yakalandı mı?
        if dusman.konum.getX() == oyuncu.konum.getX() and dusman.konum.getY() == oyuncu.konum.getY():
            if isinstance(oyuncu, LukeSkywalker):
                oyuncu.setCan(oyuncu.getCan() - 1)
            elif isinstance(oyuncu, MasterYoda):
                oyuncu.setCan(oyuncu.getCan() - 0.5)
            alert.play()
            print(f"CAN: {oyuncu.getCan()}")
            if oyuncu.getCan() <= 0:
                print("Game Over!")
                calisiyor = False

    # Kupa bulundu mu?
    if harita[oyuncu.konum.getY()][oyuncu.konum.getX()] == 'G':
        print("🎉 Tebrikler! Kupayı buldunuz!")
        calisiyor = False

    # Ekranı çiz
    ekran.fill((200, 230, 255))
    haritayiCiz(ekran, harita)

    # Kupa ikonunu çiz (G harfini atladık, yerine görsel koyuyoruz)
    for y, satir in enumerate(harita):
        for x, hucre in enumerate(satir):
            if hucre == 'G':
                ekran.blit(resimler["Cup"], (x * 50, y * 50))

    # Oyuncuyu çiz
    # Oyuncunun kutusunu sarı kenarlıkla vurgula
    pygame.draw.rect(ekran, (255, 255, 0), (oyuncu.konum.getX() * 50, oyuncu.konum.getY() * 50, 50, 50), 3)

    ekran.blit(resimler[oyuncu.getAd()], (oyuncu.konum.getX()*50, oyuncu.konum.getY()*50))

    # Düşmanları çiz
    for dusman in dusmanlar:
        ekran.blit(resimler[dusman.getAd()], (dusman.konum.getX()*50, dusman.konum.getY()*50))
    # Canları çiz
    for i in range(int(oyuncu.getCan())):
        ekran.blit(resimler["Heart"], (10 + i * 40, 10))

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
input("Oyun bitti. Çıkmak için Enter'a bas.")
