from RoiEnEchec import *
"""Dans ces quatres fonctions, on vérifie à chaque fois que le roi et la tour n'ont jamais été déplacés, ainsi que le chemin entre les deux qui doit être vide"""

def petitRocBlanc(positionDepartX,positionDepartY,positionArriveeX,positionArriveeY, compteur, piece):
    if positionArriveeX == 6 and positionArriveeY == 0 and compteur == 0 and piece[0] == 'roi':
        for i in range(1, abs(positionArriveeX - positionDepartX) + 1):
            if echiquier[positionDepartX + i, positionDepartY] != ['vide', 'incolore']:
                return False
        if echiquier[7, 0] == ['tour', 'blanc']:
            echiquier[6,0] == ['roi','blanc']
            echiquier[4,0] == ['vide', 'incolore']
            if roiBlancEnEchec():
                return False
            else:
                return True

        return False



def grandRocBlanc (positionDepartX,positionDepartY,positionArriveeX,positionArriveeY, compteur, piece):
    if positionArriveeX == 2 and positionArriveeY == 0 and compteur == 0 and piece[0] == 'roi':
        for i in range(1, abs(positionArriveeX - positionDepartX) + 1 ):
            if echiquier[positionDepartX - i , positionDepartY] != ['vide', 'incolore']:
                return False
        if echiquier[0, 0] == ['tour', 'blanc']:
            echiquier[2,0] == ['roi','blanc']
            echiquier[4,0] == ['vide', 'incolore']
            if roiBlancEnEchec():
                return False
            else:
                return True


    return False



def petitRocNoir(positionDepartX,positionDepartY,positionArriveeX,positionArriveeY, compteur, piece):
    if positionArriveeX == 6 and positionArriveeY == 7 and compteur == 0 and piece[0] == 'roi':
        for i in range(1, abs(positionArriveeX - positionDepartX) + 1 ):
            if echiquier[positionDepartX + i , positionDepartY] != ['vide', 'incolore']:
                return False
        if echiquier[7, 7] == ['tour', 'noir']:
            echiquier[6,7] == ['roi','noir']
            echiquier[4,7] == ['vide', 'incolore']
            if roiNoirEnEchec():
                return False
            else:
                return True

    return False



def grandRocNoir(positionDepartX,positionDepartY,positionArriveeX,positionArriveeY, compteur, piece):
    if positionArriveeX == 2 and positionArriveeY == 7 and compteur == 0 and piece[0] == 'roi':
        for i in range(1, abs(positionArriveeX - positionDepartX) + 1 ):
            if echiquier[positionDepartX - i , positionDepartY] != ['vide', 'incolore']:
                return False
        if echiquier[0, 7] == ['tour', 'noir']:
            echiquier[2,7] == ['roi','noir']
            echiquier[4,7] == ['vide', 'incolore']
            if roiNoirEnEchec():
                return False
            else:
                return True

    return False