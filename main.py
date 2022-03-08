newRoomAvailable = True
flache = 0
raeume = []


class Raum:
    def __init__(self, name, groesse=0):
        self.name = name
        self.groesse = groesse


def raumflacheBerechnen(raumArt, raum):
    ersteWandlange = int(input("Geben Sie die Wandlänge der ersten Wand in M an: "))
    zweiteWandlange = int(input("Geben Sie die Wandlänge der zweiten Wand in M an: "))
    raumTypMultiplikator = 1.0
    if raumArt == "t":
        raumTypMultiplikator = 0.5
    if raumArt == "d":
        ganzFlaeche = (ersteWandlange - 2) * (zweiteWandlange - 2)
        teilFlaeche = (ersteWandlange - 1) * (zweiteWandlange - 1)
        raumfleache = ganzFlaeche + ((teilFlaeche - ganzFlaeche) * 0.5)
        raum.groesse = raumfleache
        raeume.append(raum)
        return raumfleache
    raumflache = ersteWandlange * zweiteWandlange * raumTypMultiplikator
    raum.groesse = raumflache
    raeume.append(raum)
    return raumflache


def raumFormDefinition(raumArt, raum):
    istRechtEckig = input("Ist der Raum Rechteckig? (j/n):  ")

    if istRechtEckig == "j":
        global flache
        raumflache = raumflacheBerechnen(raumArt, raum)
        flache += raumflache
    else:
        istRechtEckigTeilbar = input("Ist der Raum in Rechtecke teilbar? (j/n): ")
        if istRechtEckigTeilbar == "n":
            print("Programm nicht anwendbar fur nicht Rechteckig teilbare Räume")
        elif istRechtEckigTeilbar == "j":
            rechtEckVerfugbar = True
            teilRaumFlache = 0
            while rechtEckVerfugbar:
                teilRaumFlache += raumflacheBerechnen(raumArt, raum)
                teilRaum = input("Ist ein teil des Raumes noch ungemessen? (j/n): ")
                if teilRaum == "n":
                    flache += teilRaumFlache
                    rechtEckVerfugbar = False


while newRoomAvailable:
    ungemmessenesZimmer = input("Gibt es noch ein ungemessenes Zimmer? (j/n): ")
    if ungemmessenesZimmer == "n":
        if len(raeume) == 0:
            print("Sie haben keine Eingabe getätigt.")
        else:
            for room in raeume:
                print(str(room.name) + " ist " + str(room.groesse) + " m^2 gross")
            print("Die Wohnung ist: " + str(flache) + " m^2 gross")
        newRoomAvailable = False
    else:
        raumName = input("Was für eine Art von Raum ist es? (Name):")
        raum = Raum(raumName)
        raumArt = input("Ist es ein Normales Zimmer, eine Terasse oder eine Dachschräge? (n/t/d)")
        if raumArt == "n":
            raumFormDefinition("n", raum)
        if raumArt == "t":
            raumFormDefinition("t", raum)
        if raumArt == "d":
            raumFormDefinition("d", raum)

for room in raeume:
    print(str(room.name) + " ist " + str(room.groesse) + " m^2 gross")


