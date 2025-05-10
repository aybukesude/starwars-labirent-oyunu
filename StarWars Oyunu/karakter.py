class Lokasyon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self): return self.x
    def getY(self): return self.y
    def setX(self, x): self.x = x
    def setY(self, y): self.y = y


class Karakter:
    def __init__(self, ad, tur, konum):
        self.ad = ad
        self.tur = tur
        self.konum = konum

    def getAd(self): return self.ad
    def getTur(self): return self.tur
    def getKonum(self): return self.konum
    def setKonum(self, konum): self.konum = konum
    def EnKisaYol(self, harita, hedef): pass


class LukeSkywalker(Karakter):
    def __init__(self, konum):
        super().__init__("Luke Skywalker", "iyi", konum)
        self.can = 3

    def getCan(self): return self.can
    def setCan(self, can): self.can = can


class MasterYoda(Karakter):
    def __init__(self, konum):
        super().__init__("Master Yoda", "iyi", konum)
        self.can = 6

    def getCan(self): return self.can
    def setCan(self, can): self.can = can


class Stormtrooper(Karakter):
    def __init__(self, konum):
        super().__init__("Stormtrooper", "kotu", konum)

    def EnKisaYol(self, harita, hedef):
        from collections import deque
        start = (self.konum.getX(), self.konum.getY())
        visited = set()
        queue = deque([(start, [])])
        while queue:
            (x, y), yol = queue.popleft()
            if (x, y) == hedef:
                return yol
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= ny < len(harita) and 0 <= nx < len(harita[0]) and harita[ny][nx] != '1' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), yol + [(nx, ny)]))
        return []


class DarthVader(Karakter):
    def __init__(self, konum):
        super().__init__("Darth Vader", "Kötü", konum)

    def EnKisaYol(self, harita, hedef):
        from collections import deque
        baslangic = (self.konum.getX(), self.konum.getY())
        kuyruk = deque()
        kuyruk.append((baslangic, []))
        ziyaret_edilen = set()
        ziyaret_edilen.add(baslangic)

        # Duvarları yıkabilir → '#' bile olsa geçebilir
        yonler = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        while kuyruk:
            (x, y), yol = kuyruk.popleft()
            if (x, y) == hedef:
                return yol

            for dx, dy in yonler:
                nx, ny = x + dx, y + dy
                if 0 <= ny < len(harita) and 0 <= nx < len(harita[0]):
                    if (nx, ny) not in ziyaret_edilen:
                        kuyruk.append(((nx, ny), yol + [(nx, ny)]))
                        ziyaret_edilen.add((nx, ny))
        return []



class KyloRen(Karakter):
    def __init__(self, konum):
        super().__init__("Kylo Ren", "Kötü", konum)

    def EnKisaYol(self, harita, hedef):
        from collections import deque
        baslangic = (self.konum.getX(), self.konum.getY())
        kuyruk = deque()
        kuyruk.append((baslangic, []))
        ziyaret_edilen = set()
        ziyaret_edilen.add(baslangic)

        yonler = [(0, -2), (0, 2), (-2, 0), (2, 0)]

        while kuyruk:
            (x, y), yol = kuyruk.popleft()
            if (x, y) == hedef:
                return yol

            for dx, dy in yonler:
                nx, ny = x + dx, y + dy
                ax, ay = x + dx // 2, y + dy // 2  # Ara hücre

                # Hem hedef hem ara hücre harita sınırları içinde mi?
                if (0 <= ny < len(harita) and 0 <= nx < len(harita[0]) and
                    0 <= ay < len(harita) and 0 <= ax < len(harita[0])):

                    if (nx, ny) not in ziyaret_edilen:
                        if harita[ay][ax] != '1' and harita[ny][nx] != '1':
                            kuyruk.append(((nx, ny), yol + [(nx, ny)]))
                            ziyaret_edilen.add((nx, ny))
        return []


