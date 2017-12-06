from RoiEnEchec import *
from data import*

def matchNul(couleurDuJoueur):
    couleurDuJoueur = str(couleurDuJoueur)
    for x in range (0,8) :
        for y in range(0,8):
            if echiquier[x,y][1]==couleurDuJoueur and echiquier [x,y][0] == 'roi':
                return False
            if echiquier[x,y][1] == couleurDuJoueur and echiquier[x,y][0] == 'roi' :
                coordRoiX = x
                cordRoiY = y

    if dansLEchiquier(coordRoiX+1, cordRoiY):
        if echiquier[coordRoiX+1, cordRoiY][1] == ['vide', 'incolore'] or echiquier[coordRoiX+1, cordRoiY+1][1] == changeCouleurDuJoueur(couleurDuJoueur):
            savePieceCaseRoi1 = echiquier[coordRoiX + 1, cordRoiY]
            echiquier[coordRoiX + 1, cordRoiY] = ['roi', couleurDuJoueur]
            echiquier[coordRoiX, cordRoiY] = ['vide', 'incolore']
            if (couleurDuJoueur == 'blanc' and roiBlancEnEchec()) or (couleurDuJoueur == 'noir' and roiNoirEnEchec()) :
                echiquier[coordRoiX + 1, cordRoiY] = savePieceCaseRoi1
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
            else:
                echiquier[coordRoiX + 1, cordRoiY] = savePieceCaseRoi1
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
                return False

    if dansLEchiquier(coordRoiX+1, cordRoiY+1) :
        if echiquier[coordRoiX+1, cordRoiY+1] == ['vide', 'incolore'] or echiquier[coordRoiX+1, cordRoiY+1][1] == changeCouleurDuJoueur(couleurDuJoueur) :
            savePieceCaseRoi2 = echiquier[coordRoiX + 1, cordRoiY + 1]
            echiquier[coordRoiX + 1, cordRoiY + 1] = ['roi', couleurDuJoueur]
            echiquier [coordRoiX, cordRoiY] = ['vide', 'incolore']
            if (couleurDuJoueur == 'blanc' and roiBlancEnEchec()) or (couleurDuJoueur == 'noir' and roiNoirEnEchec()) :
                echiquier[coordRoiX + 1, cordRoiY + 1] = savePieceCaseRoi2
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
            else :
                echiquier[coordRoiX + 1, cordRoiY + 1] = savePieceCaseRoi2
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
                return False


    if  dansLEchiquier(coordRoiX, cordRoiY+1) :
        if echiquier[coordRoiX, cordRoiY+1] == ['vide', 'incolore'] or echiquier[coordRoiX, cordRoiY+1][1] == changeCouleurDuJoueur(couleurDuJoueur):
            savePieceCaseRoi3 = echiquier[coordRoiX, cordRoiY + 1]
            echiquier[coordRoiX, cordRoiY + 1] = ['roi', couleurDuJoueur]
            echiquier[coordRoiX, cordRoiY] = ['vide', 'incolore']
            if (couleurDuJoueur == 'blanc' and roiBlancEnEchec()) or (couleurDuJoueur == 'noir' and roiNoirEnEchec()) :
                echiquier[coordRoiX, cordRoiY + 1] = savePieceCaseRoi3
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
            else :
                echiquier[coordRoiX, cordRoiY + 1] = savePieceCaseRoi3
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
                return False

    if dansLEchiquier(coordRoiX-1, cordRoiY+1):
        if echiquier[coordRoiX-1, cordRoiY+1] == ['vide', 'incolore'] or echiquier[coordRoiX-1, cordRoiY+1][1] == changeCouleurDuJoueur(couleurDuJoueur):
            savePieceCaseRoi4 = echiquier[coordRoiX - 1, cordRoiY + 1]
            echiquier[coordRoiX - 1, cordRoiY + 1] = ['roi', couleurDuJoueur]
            echiquier[coordRoiX, cordRoiY] = ['vide', 'incolore']
            if (couleurDuJoueur == 'blanc' and roiBlancEnEchec()) or (couleurDuJoueur == 'noir' and roiNoirEnEchec()) :
                echiquier[coordRoiX - 1, cordRoiY + 1] = savePieceCaseRoi4
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
            else :
                echiquier[coordRoiX - 1, cordRoiY + 1] = savePieceCaseRoi4
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
                return False

    if dansLEchiquier(coordRoiX-1, cordRoiY):
        if echiquier[coordRoiX-1, cordRoiY] == ['vide', 'incolore'] or echiquier[coordRoiX-1, cordRoiY][1] == changeCouleurDuJoueur(couleurDuJoueur):
            savePieceCaseRoi5 = echiquier[coordRoiX - 1, cordRoiY]
            echiquier[coordRoiX - 1, cordRoiY] = ['roi', couleurDuJoueur]
            echiquier[coordRoiX, cordRoiY] = ['vide', 'incolore']
            if (couleurDuJoueur == 'blanc' and roiBlancEnEchec()) or (couleurDuJoueur == 'noir' and roiNoirEnEchec()) :
                echiquier[coordRoiX - 1, cordRoiY] = savePieceCaseRoi5
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
            else :
                echiquier[coordRoiX - 1, cordRoiY] = savePieceCaseRoi5
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
                return False

    if dansLEchiquier(coordRoiX-1, cordRoiY-1) :
        if echiquier[coordRoiX-1, cordRoiY-1] == ['vide', 'incolore'] or echiquier[coordRoiX-1, cordRoiY-1][1] == changeCouleurDuJoueur(couleurDuJoueur):
            savePieceCaseRoi6 = echiquier[coordRoiX - 1, cordRoiY - 1]
            echiquier[coordRoiX - 1, cordRoiY - 1] = ['roi', couleurDuJoueur]
            echiquier[coordRoiX, cordRoiY]=['vide', 'incolore']
            if (couleurDuJoueur == 'blanc' and roiBlancEnEchec()) or (couleurDuJoueur == 'noir' and roiNoirEnEchec()) :
                echiquier[coordRoiX - 1, cordRoiY - 1] = savePieceCaseRoi6
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
            else :
                echiquier[coordRoiX - 1, cordRoiY - 1] = savePieceCaseRoi6
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
                return False

    if dansLEchiquier(coordRoiX, cordRoiY-1):
        if echiquier[coordRoiX, cordRoiY-1] == ['vide', 'incolore'] or echiquier[coordRoiX, cordRoiY-1][1] == changeCouleurDuJoueur(couleurDuJoueur):
            savePieceCaseRoi7 = echiquier[coordRoiX, cordRoiY - 1]
            echiquier[coordRoiX, cordRoiY - 1] = ['roi', couleurDuJoueur]
            echiquier[coordRoiX, cordRoiY] = ['vide', 'incolore']
            if (couleurDuJoueur == 'blanc' and roiBlancEnEchec()) or (couleurDuJoueur == 'noir' and roiNoirEnEchec()) :
                echiquier[coordRoiX, cordRoiY - 1] = savePieceCaseRoi7
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
            else :
                echiquier[coordRoiX, cordRoiY - 1] = savePieceCaseRoi7
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
                return False

    if dansLEchiquier(coordRoiX+1, cordRoiY-1) :
        if echiquier[coordRoiX+1, cordRoiY-1] == ['vide', 'incolore'] or echiquier[coordRoiX+1, cordRoiY-1][1] == changeCouleurDuJoueur(couleurDuJoueur):
            savePieceCaseRoi8 = echiquier[coordRoiX + 1 , cordRoiY - 1]
            echiquier[coordRoiX + 1 , cordRoiY - 1] = ['roi', couleurDuJoueur]
            echiquier[coordRoiX, cordRoiY] = ['vide', 'incolore']
            if (couleurDuJoueur == 'blanc' and roiBlancEnEchec()) or (couleurDuJoueur == 'noir' and roiNoirEnEchec()) :
                echiquier[coordRoiX + 1, cordRoiY - 1] = savePieceCaseRoi8
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
            else :
                echiquier[coordRoiX + 1, cordRoiY - 1] = savePieceCaseRoi8
                echiquier[coordRoiX, cordRoiY] = ['roi', couleurDuJoueur]
                return False

    return True