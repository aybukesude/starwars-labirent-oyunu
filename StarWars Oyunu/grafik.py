import pygame

def haritayiCiz(ekran, harita):
    for y, satir in enumerate(harita):
        for x, hucre in enumerate(satir):
            if hucre == '0':  # Duvar - açık mavi kutu
                pygame.draw.rect(ekran, (180, 220, 255), (x * 50, y * 50, 50, 50))  # Mavi
            elif hucre == '1':  # Yol - beyaz
                pygame.draw.rect(ekran, (255, 255, 255), (x * 50, y * 50, 50, 50))  # Beyaz


            elif hucre == 'G':
                pygame.draw.rect(ekran, (20, 20, 20), (x*50, y*50, 50, 50))  # Kupa alt zemin
            elif hucre in ['A', 'B', 'C', 'D', 'E']:
                pygame.draw.rect(ekran, (20, 20, 20), (x * 50, y * 50, 50, 50))  # Zemin koyu
                pygame.draw.rect(ekran, (0, 0, 255), (x * 50 + 5, y * 50 + 5, 40, 40))  # Mavi kare
                font = pygame.font.SysFont(None, 30)
                text = font.render(hucre, True, (255, 255, 255))
                ekran.blit(text, (x * 50 + 15, y * 50 + 10))

                # Ok çiz (süsleme için istersen)
                if hucre == 'A':
                    pygame.draw.polygon(ekran, (0, 0, 255),
                                        [(x * 50, y * 50 + 25), (x * 50 + 15, y * 50 + 10), (x * 50 + 15, y * 50 + 40)])
                elif hucre == 'B':
                    pygame.draw.polygon(ekran, (0, 0, 255),
                                        [(x * 50 + 25, y * 50), (x * 50 + 10, y * 50 + 15), (x * 50 + 40, y * 50 + 15)])
                # Diğerleri benzer şekilde eklenebilir

