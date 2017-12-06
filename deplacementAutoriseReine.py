from data import *
def deplacementAutoriseReine(positionDepartX,positionDepartY,positionArriveeX,positionArriveeY, couleurEnnemi):


    if positionArriveeX > positionDepartX and positionArriveeY == positionDepartY :
        for i in range (1, abs(positionArriveeX - positionDepartX)) :
            if echiquier[positionDepartX + i, positionDepartY] != ['vide', 'incolore'] :
                return False

        if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
            return True



    elif positionArriveeX < positionDepartX and positionArriveeY == positionDepartY:
        for i in range(1, abs(positionArriveeX - positionDepartX)):
            if echiquier[positionDepartX - i, positionDepartY] != ['vide', 'incolore']:
                return False

        if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
            return True



    elif positionArriveeX == positionDepartX and positionArriveeY > positionDepartY:
        for i in range(1, abs(positionArriveeY - positionDepartY)):
            if echiquier[positionDepartX, positionDepartY + i ] != ['vide', 'incolore']:
                return False

        if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
            return True

    elif positionArriveeX == positionDepartX and positionArriveeY < positionDepartY:
        for i in range(1, abs(positionArriveeY - positionDepartY)):
            if echiquier[positionDepartX, positionDepartY - i ] != ['vide', 'incolore']:
                return False

        if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
            return True

    elif abs(positionArriveeX - positionDepartX) == abs(positionArriveeY - positionDepartY) :

        if positionArriveeX > positionDepartX and positionArriveeY > positionDepartY :
            for i in range (1, abs(positionArriveeX - positionDepartX)) :
                if echiquier[positionDepartX + i, positionDepartY + i] != ['vide', 'incolore'] :
                    return False
            if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
                return True


        elif positionArriveeX < positionDepartX and positionArriveeY > positionDepartY :
            for i in range (1, abs(positionArriveeX - positionDepartX)) :
                if echiquier[positionDepartX - i, positionDepartY + i] != ['vide', 'incolore'] :
                    return False
            if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
                return True


        elif positionArriveeX < positionDepartX and positionArriveeY < positionDepartY :
            for i in range (1, abs(positionArriveeX - positionDepartX)) :
                if echiquier[positionDepartX - i, positionDepartY - i] != ['vide', 'incolore'] :
                    return False
            if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
               return True



        elif positionArriveeX > positionDepartX and positionArriveeY < positionDepartY :
            for i in range (1, abs(positionArriveeX - positionDepartX)) :
                if echiquier[positionDepartX + i, positionDepartY - i] != ['vide', 'incolore'] :
                    return False
            if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
                return True




    return False