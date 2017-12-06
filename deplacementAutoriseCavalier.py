from data import *
def deplacementAutoriseCavalier (positionDepartX,positionDepartY,positionArriveeX,positionArriveeY, couleurEnnemi):

    if positionArriveeX == positionDepartX + 2 and positionArriveeY == positionDepartY + 1 :
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore'] or echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi:
            return True



    elif positionArriveeX == positionDepartX + 1 and positionArriveeY == positionDepartY + 2:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore'] or echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi:
            return True



    elif positionArriveeX == positionDepartX - 1 and positionArriveeY == positionDepartY + 2:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore'] or echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi:
            return True



    elif positionArriveeX == positionDepartX - 2 and positionArriveeY == positionDepartY + 1:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore'] or echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi:
            return True



    elif positionArriveeX == positionDepartX - 2 and positionArriveeY == positionDepartY - 1:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore'] or echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi:
            return True


    elif positionArriveeX == positionDepartX - 1 and positionArriveeY == positionDepartY - 2:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore'] or echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi:
            return True




    elif positionArriveeX == positionDepartX + 1 and positionArriveeY == positionDepartY - 2:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore'] or echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi:
            return True



    elif positionArriveeX == positionDepartX + 2 and positionArriveeY == positionDepartY - 1:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore'] or echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi:
            return True


    else:
        return False