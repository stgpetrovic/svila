class Vrijeme():
    def __init__(self, H, M, S):
        if not (isinstance(H, int) and isinstance(M, int)
                and isinstance(S, int)):
            raise TypeError("sat, minuta i sekunda moraju biti cijeli brojevi")
        if H > 23 or M > 59 or S > 59:
            raise ValueError("sat, minuta i sekunda manji od 24 tj. 60")
        self.H = H
        self.M = M
        self.S = S

    def __repr__(self):
        return "{0:02}:{1:02}:{2:02}".format(self.H, self.M, self.S)

    def __gt__(self, drugi):
        if not isinstance(drugi, Vrijeme):
            raise TypeError("argument za usporedbu mora biti istog tipa")
        if self.H == drugi.H:
            if self.M == drugi.M:
                return self.S > drugi.S
            else:
                return self.M > drugi.M
        else:
            return self.H > drugi.H

    def __eq__(self, drugi):
        return self.H == drugi.H and self.M == drugi.M and self.S == drugi.S

    def __lt__(self, drugi):
        if not isinstance(drugi, Vrijeme):
            raise TypeError("argument za usporedbu mora biti istog tipa")
        if not self == drugi:
            return not (self > drugi)
        return False

    def __sub__(self, drugi):
        if not isinstance(drugi, Vrijeme):
            raise TypeError("argument za usporedbu mora biti istog tipa")
        if self < drugi:
            raise ValueError(
                "drugo vrijeme mora biti manje da bi se moglo oduzeti")
        delta = Vrijeme(self.H, self.M, self.S)
        delta.H -= drugi.H
        delta.M -= drugi.M
        if delta.M < 0:
            delta.M += 60
            delta.H -= 1
        delta.S -= drugi.S
        if delta.S < 0:
            delta.S += 60
            delta.M -= 1
        return delta


class Emisija(object):
    def __init__(self, ime, pocetak, kraj):
        if not (isinstance(pocetak, Vrijeme) and isinstance(kraj, Vrijeme)):
            raise TypeError(
                "poceak i kraj moraju biti instance razreda Vrijeme")
        self.ime = ime
        self.pocetak = pocetak
        self.kraj = kraj

    def __repr__(self):
        return "[%s][%s][%s]" % (self.ime, repr(self.pocetak), repr(self.kraj))

    def __lt__(self, drugi):
        if not isinstance(drugi, Emisija):
            raise TypeError("argument za usporedbu mora biti istog tipa")
        return self.kraj - self.pocetak < drugi.kraj - drugi.pocetak

    def __gt__(self, drugi):
        if not isinstance(drugi, Emisija):
            raise TypeError("argument za usporedbu mora biti istog tipa")
        d1 = self.kraj - self.pocetak
        d2 = drugi.kraj - drugi.pocetak
        return not (d1 == d2) and not (d1 < d2)
