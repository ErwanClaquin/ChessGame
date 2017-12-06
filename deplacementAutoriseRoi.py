from data import *
def deplacementAutoriseRoi (positionDepartX,positionDepartY,positionArriveeX,positionArriveeY, couleurEnnemi) :

    if  echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:

        if positionArriveeX == positionDepartX + 1 and positionArriveeY == positionDepartY :
            return True

        elif positionArriveeX == positionDepartX + 1 and positionArriveeY == positionDepartY + 1 :
            return True

        elif positionArriveeX == positionDepartX  and positionArriveeY == positionDepartY +1 :
            return True

        elif positionArriveeX == positionDepartX - 1 and positionArriveeY == positionDepartY +1 :
            return True

        elif positionArriveeX == positionDepartX - 1 and positionArriveeY == positionDepartY :
            return True

        elif positionArriveeX == positionDepartX - 1 and positionArriveeY == positionDepartY - 1 :
            return True

        elif positionArriveeX == positionDepartX  and positionArriveeY == positionDepartY - 1 :
            return True

        elif positionArriveeX == positionDepartX + 1 and positionArriveeY == positionDepartY - 1:
            return True

    return False