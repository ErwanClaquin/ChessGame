from RoiEnEchec import *
from data import *

def casesPossibles (piece, positionDepartX, positionDepartY, couleurEnnemi) :
    if piece == ['pion', 'blanc']and not roiBlancEnEchec():
        if dansLEchiquier(positionDepartX,positionDepartY + 1):
            if echiquier[positionDepartX, positionDepartY + 1 ] == ['vide', 'incolore']:
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY+1) * TailleCases))

        if dansLEchiquier(positionDepartX, positionDepartY+1) and dansLEchiquier(positionDepartX, positionDepartY+2):
            if echiquier[positionDepartX, positionDepartY + 2 ] == ['vide', 'incolore'] and echiquier[positionDepartX, positionDepartY + 1 ]==['vide', 'incolore'] and positionDepartY == 1:
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY + 2) * TailleCases))

        if dansLEchiquier(positionDepartX + 1,positionDepartY + 1):
            if echiquier[positionDepartX + 1, positionDepartY + 1 ] != ['vide', 'incolore'] and echiquier[positionDepartX + 1, positionDepartY + 1 ][1] != 'blanc':
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX +1) * TailleCases, (positionDepartY+1) * TailleCases))

        if dansLEchiquier(positionDepartX -1, positionDepartY + 1):
            if echiquier[positionDepartX -1, positionDepartY + 1 ] != ['vide', 'incolore'] and echiquier[positionDepartX - 1, positionDepartY + 1 ][1] != 'blanc':
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX -1) * TailleCases, (positionDepartY+1) * TailleCases))


    if piece == ['pion', 'blanc']and roiBlancEnEchec():
        if dansLEchiquier(positionDepartX, positionDepartY + 1) and echiquier[positionDepartX, positionDepartY + 1] == ['vide', 'incolore']:
            savePieceCaseArrive = echiquier[positionDepartX, positionDepartY + 1]
            echiquier[positionDepartX, positionDepartY + 1] = ['pion', 'blanc']
            echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
            if not roiBlancEnEchec():
                echiquier[positionDepartX, positionDepartY+1] = savePieceCaseArrive
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY + 1) * TailleCases))

            elif roiBlancEnEchec():
                echiquier[positionDepartX, positionDepartY + 1] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX, positionDepartY + 2) and echiquier[positionDepartX, positionDepartY + 2] == ['vide', 'incolore']:
            savePieceCaseArrive = echiquier[positionDepartX, positionDepartY + 2]
            echiquier[positionDepartX, positionDepartY + 2] = ['pion', 'blanc']
            echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
            if not roiBlancEnEchec():
                echiquier[positionDepartX, positionDepartY+2] = savePieceCaseArrive
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY + 2) * TailleCases))

            elif roiBlancEnEchec():
                echiquier[positionDepartX, positionDepartY + 2] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX+1, positionDepartY + 1) and echiquier[positionDepartX + 1, positionDepartY + 1][1] == 'noir':
            savePieceCaseArrive = echiquier[positionDepartX+1, positionDepartY + 1]
            echiquier[positionDepartX+1, positionDepartY + 1] = ['pion', 'blanc']
            echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
            if not roiBlancEnEchec():
                echiquier[positionDepartX+1, positionDepartY+1] = savePieceCaseArrive
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX+1) * TailleCases, (positionDepartY + 1) * TailleCases))

            elif roiBlancEnEchec():
                echiquier[positionDepartX+1, positionDepartY + 1] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX-1, positionDepartY + 1) and echiquier[positionDepartX - 1, positionDepartY + 1][1] == 'noir':
            savePieceCaseArrive = echiquier[positionDepartX-1, positionDepartY + 1]
            echiquier[positionDepartX-1, positionDepartY + 1] = ['pion', 'blanc']
            echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
            if not roiBlancEnEchec():
                echiquier[positionDepartX-1, positionDepartY+1] = savePieceCaseArrive
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX-1) * TailleCases, (positionDepartY + 1) * TailleCases))

            elif roiBlancEnEchec():
                echiquier[positionDepartX-1, positionDepartY + 1] = savePieceCaseArrive



    if piece == ['pion', 'noir'] and not roiNoirEnEchec():
        if dansLEchiquier(positionDepartX, positionDepartY - 1):
            if echiquier[positionDepartX, positionDepartY - 1] == ['vide', 'incolore']:
                selection.fill(
                    (0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY - 1) * TailleCases))


        if dansLEchiquier(positionDepartX, positionDepartY - 2):
            if echiquier[positionDepartX, positionDepartY - 2] == ['vide', 'incolore'] and echiquier[positionDepartX, positionDepartY - 1] == ['vide', 'incolore'] and positionDepartY == 6:
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY - 2) * TailleCases))


        if dansLEchiquier(positionDepartX + 1, positionDepartY - 1):
            if echiquier[positionDepartX + 1, positionDepartY - 1] != ['vide', 'incolore'] and echiquier[positionDepartX + 1, positionDepartY - 1][1] != 'noir':
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX + 1) * TailleCases, (positionDepartY - 1) * TailleCases))


        if dansLEchiquier(positionDepartX - 1, positionDepartY - 1):
            if echiquier[positionDepartX - 1, positionDepartY - 1] != ['vide', 'incolore'] and echiquier[positionDepartX - 1, positionDepartY - 1][1] != 'noir':
                selection.fill((0, 0, 255, 64))
                ecran.blit(selection, ((positionDepartX - 1) * TailleCases, (positionDepartY - 1) * TailleCases))


    if piece == ['pion', 'noir'] and roiNoirEnEchec():
        if dansLEchiquier(positionDepartX, positionDepartY - 1) and echiquier[positionDepartX, positionDepartY - 1] == ['vide', 'incolore']:
            savePieceCaseArrive = echiquier[positionDepartX, positionDepartY - 1]
            echiquier[positionDepartX, positionDepartY - 1] = ['pion', 'noir']
            echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
            if not roiNoirEnEchec():
                echiquier[positionDepartX, positionDepartY - 1] = savePieceCaseArrive
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY - 1) * TailleCases))

            elif roiNoirEnEchec():
                echiquier[positionDepartX, positionDepartY - 1] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX, positionDepartY - 2) and echiquier[positionDepartX, positionDepartY - 2] == ['vide', 'incolore']:
            savePieceCaseArrive = echiquier[positionDepartX, positionDepartY - 2]
            echiquier[positionDepartX, positionDepartY - 2] = ['pion', 'noir']
            echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
            if not roiNoirEnEchec():
                echiquier[positionDepartX, positionDepartY - 2] = savePieceCaseArrive
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY - 2) * TailleCases))

            elif roiNoirEnEchec():
                echiquier[positionDepartX, positionDepartY - 2] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX+1, positionDepartY - 1) and echiquier[positionDepartX + 1, positionDepartY - 1][1] == 'blanc':
            savePieceCaseArrive = echiquier[positionDepartX+1, positionDepartY - 1]
            echiquier[positionDepartX+1, positionDepartY - 1] = ['pion', 'noir']
            echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
            if not roiNoirEnEchec():
                echiquier[positionDepartX+1, positionDepartY - 1] = savePieceCaseArrive
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX+1) * TailleCases, (positionDepartY - 1) * TailleCases))

            elif roiNoirEnEchec():
                echiquier[positionDepartX+1, positionDepartY - 1] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX-1, positionDepartY - 1) and echiquier[positionDepartX - 1, positionDepartY - 1][1] == 'blanc':
            savePieceCaseArrive = echiquier[positionDepartX-1, positionDepartY - 1]
            echiquier[positionDepartX-1, positionDepartY - 1] = ['pion', 'noir']
            echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
            if not roiNoirEnEchec():
                echiquier[positionDepartX-1, positionDepartY - 1] = savePieceCaseArrive
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX-1) * TailleCases, (positionDepartY - 1) * TailleCases))

            elif roiNoirEnEchec():
                echiquier[positionDepartX-1, positionDepartY - 1] = savePieceCaseArrive


#Tour
    if piece[0] == 'tour' :
        nombreDeDeplacementSurLaDroite=0
        nombreDeDeplacementSurLaGauche = 0
        nombreDeDeplacementVersLeBas = 0
        nombreDeDeplacementVersLeHaut = 0
        if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
            while dansLEchiquier(positionDepartX+ nombreDeDeplacementSurLaDroite+1, positionDepartY) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroite+1, positionDepartY][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY][1]!= couleurEnnemi:
                nombreDeDeplacementSurLaDroite+=1
            for n in range(1, nombreDeDeplacementSurLaDroite + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX + n) * TailleCases, positionDepartY * TailleCases))


            while dansLEchiquier(positionDepartX -(nombreDeDeplacementSurLaGauche + 1), positionDepartY) and echiquier[positionDepartX - (nombreDeDeplacementSurLaGauche + 1), positionDepartY][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY][1]!= couleurEnnemi:
                nombreDeDeplacementSurLaGauche += 1
            for n in range(1, nombreDeDeplacementSurLaGauche + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX - n) * TailleCases, positionDepartY * TailleCases))


            while dansLEchiquier(positionDepartX, positionDepartY+ nombreDeDeplacementVersLeBas+1) and echiquier[positionDepartX, positionDepartY+nombreDeDeplacementVersLeBas+1][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX , positionDepartY+ nombreDeDeplacementVersLeBas][1]!= couleurEnnemi:
                nombreDeDeplacementVersLeBas+=1
            for n in range(1, nombreDeDeplacementVersLeBas + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY+n) * TailleCases))


            while dansLEchiquier(positionDepartX, positionDepartY- (nombreDeDeplacementVersLeHaut+1)) and echiquier[positionDepartX, positionDepartY-(nombreDeDeplacementVersLeHaut+1)][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX , positionDepartY- nombreDeDeplacementVersLeHaut][1]!= couleurEnnemi:
                nombreDeDeplacementVersLeHaut+=1
            for n in range(1, nombreDeDeplacementVersLeHaut + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY-n) * TailleCases))



        elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
            while dansLEchiquier(positionDepartX+ nombreDeDeplacementSurLaDroite+1, positionDepartY) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroite+1, positionDepartY][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY][1]!= couleurEnnemi:
                nombreDeDeplacementSurLaDroite+=1
                savePieceCaseArrive = echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY]
                echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY] = ['tour', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX + nombreDeDeplacementSurLaDroite) * TailleCases, positionDepartY * TailleCases))

                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY] = savePieceCaseArrive
                    return False
                elif (piece[1] == 'blanc' and  roiBlancEnEchec()) or (piece[1] == 'noir' and  roiNoirEnEchec()):
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX -(nombreDeDeplacementSurLaGauche + 1), positionDepartY) and echiquier[positionDepartX - (nombreDeDeplacementSurLaGauche + 1), positionDepartY][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY][1]!= couleurEnnemi:
                nombreDeDeplacementSurLaGauche += 1
                savePieceCaseArrive = echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY]
                echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY] = ['tour', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX - nombreDeDeplacementSurLaGauche) * TailleCases, positionDepartY * TailleCases))

                    echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY] = savePieceCaseArrive
                    return False
                elif (piece[1] == 'blanc' and  roiBlancEnEchec()) or (piece[1] == 'noir' and  roiNoirEnEchec()):
                    echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX, positionDepartY+ nombreDeDeplacementVersLeBas+1) and echiquier[positionDepartX, positionDepartY+nombreDeDeplacementVersLeBas+1][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX , positionDepartY+ nombreDeDeplacementVersLeBas][1]!= couleurEnnemi:
                nombreDeDeplacementVersLeBas+=1
                savePieceCaseArrive = echiquier[positionDepartX, positionDepartY + nombreDeDeplacementVersLeBas]
                echiquier[positionDepartX, positionDepartY + nombreDeDeplacementVersLeBas] = ['tour', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY + nombreDeDeplacementVersLeBas) * TailleCases))

                    echiquier[positionDepartX, positionDepartY + nombreDeDeplacementVersLeBas] = savePieceCaseArrive
                    return False
                elif (piece[1] == 'blanc' and  roiBlancEnEchec()) or (piece[1] == 'noir' and  roiNoirEnEchec()):
                    echiquier[positionDepartX, positionDepartY + nombreDeDeplacementVersLeBas] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX, positionDepartY- (nombreDeDeplacementVersLeHaut+1)) and echiquier[positionDepartX, positionDepartY-(nombreDeDeplacementVersLeHaut+1)][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX , positionDepartY- nombreDeDeplacementVersLeHaut][1]!= couleurEnnemi:
                nombreDeDeplacementVersLeHaut+=1
                savePieceCaseArrive = echiquier[positionDepartX, positionDepartY - nombreDeDeplacementVersLeHaut]
                echiquier[positionDepartX, positionDepartY - nombreDeDeplacementVersLeHaut] = ['tour', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY - nombreDeDeplacementVersLeHaut) * TailleCases))

                    echiquier[positionDepartX, positionDepartY - nombreDeDeplacementVersLeHaut] = savePieceCaseArrive
                    return False
                elif (piece[1] == 'blanc' and  roiBlancEnEchec()) or (piece[1] == 'noir' and  roiNoirEnEchec()):
                    echiquier[positionDepartX, positionDepartY - nombreDeDeplacementVersLeHaut] = savePieceCaseArrive



#Cavalier
    if piece[0] == 'cavalier':
        if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):

            if dansLEchiquier(positionDepartX+2, positionDepartY+1):
                if echiquier[positionDepartX+2, positionDepartY+1] == ['vide', 'incolore'] or echiquier[positionDepartX+2, positionDepartY+1][1] == couleurEnnemi :
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX+2) * TailleCases, (positionDepartY +1) * TailleCases))


            if dansLEchiquier(positionDepartX+1, positionDepartY+2):
                if echiquier[positionDepartX+1, positionDepartY+2] == ['vide', 'incolore'] or echiquier[positionDepartX+1, positionDepartY+2][1] == couleurEnnemi :
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX+1) * TailleCases, (positionDepartY +2) * TailleCases))


            if dansLEchiquier(positionDepartX-1, positionDepartY+2):
                if echiquier[positionDepartX-1, positionDepartY+2] == ['vide', 'incolore'] or echiquier[positionDepartX-1, positionDepartY+2][1] == couleurEnnemi :
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX-1) * TailleCases, (positionDepartY +2) * TailleCases))


            if dansLEchiquier(positionDepartX-2, positionDepartY+1):
                if echiquier[positionDepartX-2, positionDepartY+1] == ['vide', 'incolore'] or echiquier[positionDepartX-2, positionDepartY+1][1] == couleurEnnemi :
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX-2) * TailleCases, (positionDepartY +1) * TailleCases))


            if dansLEchiquier(positionDepartX-2, positionDepartY-1):
                if echiquier[positionDepartX-2, positionDepartY-1] == ['vide', 'incolore'] or echiquier[positionDepartX-2, positionDepartY-1][1] == couleurEnnemi :
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX-2) * TailleCases, (positionDepartY - 1) * TailleCases))


            if dansLEchiquier(positionDepartX-1, positionDepartY-2):
                if echiquier[positionDepartX-1, positionDepartY-2] == ['vide', 'incolore'] or echiquier[positionDepartX-1, positionDepartY-2][1] == couleurEnnemi :
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX-1) * TailleCases, (positionDepartY - 2) * TailleCases))


            if dansLEchiquier(positionDepartX+1, positionDepartY-2):
                if echiquier[positionDepartX+1, positionDepartY-2] == ['vide', 'incolore'] or echiquier[positionDepartX+1, positionDepartY-2][1] == couleurEnnemi :
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX+1) * TailleCases, (positionDepartY - 2) * TailleCases))


            if dansLEchiquier(positionDepartX+2, positionDepartY-1):
                if echiquier[positionDepartX+2, positionDepartY-1] == ['vide', 'incolore'] or echiquier[positionDepartX+2, positionDepartY-1][1] == couleurEnnemi :
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX+2) * TailleCases, (positionDepartY - 1) * TailleCases))



        if (piece[1] == 'blanc' and  roiBlancEnEchec()) or (piece[1] == 'noir' and  roiNoirEnEchec()):
            if dansLEchiquier(positionDepartX + 2, positionDepartY + 1):
                if echiquier[positionDepartX + 2, positionDepartY + 1] == ['vide', 'incolore'] or echiquier[positionDepartX + 2, positionDepartY + 1][1] == couleurEnnemi:
                    savePieceCaseArrive = echiquier[positionDepartX + 2, positionDepartY + 1]
                    echiquier[positionDepartX + 2, positionDepartY + 1] = ['cavalier', changeCouleurDuJoueur(couleurEnnemi)]
                    echiquier[positionDepartX,positionDepartY]=['vide', 'incolore']
                    if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection,((positionDepartX + 2) * TailleCases, (positionDepartY + 1) * TailleCases))
                        echiquier[positionDepartX + 2, positionDepartY + 1] = savePieceCaseArrive

                        #return False
                    elif (piece[1] == 'blanc' and  roiBlancEnEchec()) or (piece[1] == 'noir' and  roiNoirEnEchec()):
                        echiquier[positionDepartX + 2, positionDepartY + 1] = savePieceCaseArrive

            if dansLEchiquier(positionDepartX + 1, positionDepartY + 2):
                if echiquier[positionDepartX + 1, positionDepartY + 2] == ['vide', 'incolore'] or echiquier[positionDepartX + 1, positionDepartY + 2][1] == couleurEnnemi:
                    savePieceCaseArrive = echiquier[positionDepartX + 1, positionDepartY + 2]
                    echiquier[positionDepartX + 1, positionDepartY + 2] = ['cavalier', changeCouleurDuJoueur(couleurEnnemi)]
                    echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                    if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection,((positionDepartX + 1) * TailleCases, (positionDepartY + 2) * TailleCases))
                        echiquier[positionDepartX + 1, positionDepartY + 2] = savePieceCaseArrive

                        #return False
                    elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                        echiquier[positionDepartX + 1, positionDepartY + 2] = savePieceCaseArrive

            if dansLEchiquier(positionDepartX - 1, positionDepartY + 2):
                if echiquier[positionDepartX - 1, positionDepartY + 2] == ['vide', 'incolore'] or echiquier[positionDepartX - 1, positionDepartY + 2][1] == couleurEnnemi:
                    savePieceCaseArrive = echiquier[positionDepartX - 1, positionDepartY + 2]
                    echiquier[positionDepartX - 1, positionDepartY + 2] = ['cavalier', changeCouleurDuJoueur(couleurEnnemi)]
                    echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                    if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection,((positionDepartX - 1) * TailleCases, (positionDepartY + 2) * TailleCases))
                        echiquier[positionDepartX - 1, positionDepartY + 2] = savePieceCaseArrive

                        #return False
                    elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                        echiquier[positionDepartX - 1, positionDepartY + 2] = savePieceCaseArrive

            if dansLEchiquier(positionDepartX - 2, positionDepartY + 1):
                if echiquier[positionDepartX - 2, positionDepartY + 1] == ['vide', 'incolore'] or echiquier[positionDepartX - 2, positionDepartY + 1][1] == couleurEnnemi:
                    savePieceCaseArrive = echiquier[positionDepartX - 2, positionDepartY + 1]
                    echiquier[positionDepartX - 2, positionDepartY + 1] = ['cavalier', changeCouleurDuJoueur(couleurEnnemi)]
                    echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                    if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection,((positionDepartX - 2) * TailleCases, (positionDepartY + 1) * TailleCases))
                        echiquier[positionDepartX - 2, positionDepartY + 1] = savePieceCaseArrive

                        #return False
                    elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                        echiquier[positionDepartX - 2, positionDepartY + 1] = savePieceCaseArrive

            if dansLEchiquier(positionDepartX - 2, positionDepartY - 1):
                if echiquier[positionDepartX - 2, positionDepartY - 1] == ['vide', 'incolore'] or echiquier[positionDepartX - 2, positionDepartY - 1][1] == couleurEnnemi:
                    savePieceCaseArrive = echiquier[positionDepartX - 2, positionDepartY - 1]
                    echiquier[positionDepartX - 2, positionDepartY - 1] = ['cavalier', changeCouleurDuJoueur(couleurEnnemi)]
                    echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                    if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection, ((positionDepartX - 2) * TailleCases, (positionDepartY - 1) * TailleCases))
                        echiquier[positionDepartX - 2, positionDepartY - 1] = savePieceCaseArrive

                        #return False
                    elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                        echiquier[positionDepartX - 2, positionDepartY - 1] = savePieceCaseArrive

            if dansLEchiquier(positionDepartX - 1, positionDepartY - 2):
                if echiquier[positionDepartX - 1, positionDepartY - 2] == ['vide', 'incolore'] or echiquier[positionDepartX - 1, positionDepartY - 2][1] == couleurEnnemi:
                    savePieceCaseArrive = echiquier[positionDepartX - 1, positionDepartY - 2]
                    echiquier[positionDepartX - 1, positionDepartY - 2] = ['cavalier', changeCouleurDuJoueur(couleurEnnemi)]
                    echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                    if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection,((positionDepartX - 1) * TailleCases, (positionDepartY - 2) * TailleCases))
                        echiquier[positionDepartX - 1, positionDepartY - 2] = savePieceCaseArrive

                        #return False
                    elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                        echiquier[positionDepartX - 1, positionDepartY - 2] = savePieceCaseArrive

            if dansLEchiquier(positionDepartX + 1, positionDepartY - 2):
                if echiquier[positionDepartX + 1, positionDepartY - 2] == ['vide', 'incolore'] or echiquier[positionDepartX + 1, positionDepartY - 2][1] == couleurEnnemi:
                    savePieceCaseArrive = echiquier[positionDepartX + 1, positionDepartY - 2]
                    echiquier[positionDepartX + 1, positionDepartY - 2] = ['cavalier', changeCouleurDuJoueur(couleurEnnemi)]
                    echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                    if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection,((positionDepartX + 1) * TailleCases, (positionDepartY - 2) * TailleCases))
                        echiquier[positionDepartX + 1, positionDepartY - 2] = savePieceCaseArrive

                        #return False
                    elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                        echiquier[positionDepartX + 1, positionDepartY - 2] = savePieceCaseArrive

            if dansLEchiquier(positionDepartX + 2, positionDepartY - 1):
                if echiquier[positionDepartX + 2, positionDepartY - 1] == ['vide', 'incolore'] or echiquier[positionDepartX + 2, positionDepartY - 1][1] == couleurEnnemi:
                    savePieceCaseArrive = echiquier[positionDepartX + 2, positionDepartY - 1]
                    echiquier[positionDepartX + 2, positionDepartY - 1] = ['cavalier', changeCouleurDuJoueur(couleurEnnemi)]
                    if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                        selection.fill((0, 0, 255, 80))
                        ecran.blit(selection,((positionDepartX + 2) * TailleCases, (positionDepartY - 1) * TailleCases))
                        echiquier[positionDepartX + 2, positionDepartY - 1] = savePieceCaseArrive

                        #return False
                    elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                        echiquier[positionDepartX + 2, positionDepartY - 1] = savePieceCaseArrive


#Fou
    if piece[0] == 'fou':
        nombreDeDeplacementSurLaDroiteEtLeBas = 0
        nombreDeDeplacementSurLaGaucheEtLeBas = 0
        nombreDeDeplacementSurLaDroiteEtLeHaut = 0
        nombreDeDeplacementSurLaGaucheEtLeHaut = 0
        if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
            while dansLEchiquier(positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas + 1, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas +1) and (echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas+1, positionDepartY+nombreDeDeplacementSurLaDroiteEtLeBas+1][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY+ nombreDeDeplacementSurLaDroiteEtLeBas][1]!= couleurEnnemi):
                nombreDeDeplacementSurLaDroiteEtLeBas += 1
            for n in range(1, nombreDeDeplacementSurLaDroiteEtLeBas + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX + n) * TailleCases, (positionDepartY + n) * TailleCases))


            while dansLEchiquier(positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas + 1), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas + 1 ) and (echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas + 1), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas + 1][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGaucheEtLeBas, positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas][1] != couleurEnnemi):
                nombreDeDeplacementSurLaGaucheEtLeBas += 1
            for n in range(1, nombreDeDeplacementSurLaGaucheEtLeBas + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX - n) * TailleCases, (positionDepartY + n) * TailleCases))


            while dansLEchiquier(positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut + 1,positionDepartY -( nombreDeDeplacementSurLaDroiteEtLeHaut + 1)) and( (echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut + 1, positionDepartY -( nombreDeDeplacementSurLaDroiteEtLeHaut + 1)][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut, positionDepartY - nombreDeDeplacementSurLaDroiteEtLeHaut][1] != couleurEnnemi)):
                nombreDeDeplacementSurLaDroiteEtLeHaut += 1
            for n in range(1, nombreDeDeplacementSurLaDroiteEtLeHaut + 1):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX + n) * TailleCases, (positionDepartY - n) * TailleCases))


            while dansLEchiquier(positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut +1), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1)) and (echiquier[positionDepartX -(nombreDeDeplacementSurLaGaucheEtLeHaut + 1), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1)][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGaucheEtLeHaut, positionDepartY - nombreDeDeplacementSurLaGaucheEtLeHaut][1] != couleurEnnemi):
                nombreDeDeplacementSurLaGaucheEtLeHaut += 1
            for n in range(1, nombreDeDeplacementSurLaGaucheEtLeHaut + 1):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX - n) * TailleCases, (positionDepartY - n) * TailleCases))



        elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
            while dansLEchiquier(positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas + 1, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas + 1) and (echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas+1, positionDepartY+nombreDeDeplacementSurLaDroiteEtLeBas+1][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY+ nombreDeDeplacementSurLaDroiteEtLeBas][1]!= couleurEnnemi):
                nombreDeDeplacementSurLaDroiteEtLeBas += 1
                savePieceCaseArrive = echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas]
                echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas] = ['fou', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection,((positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas) * TailleCases, (positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas) * TailleCases))
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas] = savePieceCaseArrive

                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas + 1, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas + 1] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas + 1), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas + 1) and (echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas + 1), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas + 1][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGaucheEtLeBas, positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas][1] != couleurEnnemi):
                nombreDeDeplacementSurLaGaucheEtLeBas += 1
                savePieceCaseArrive = echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas ), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas ]
                echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas] = ['fou', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection,((positionDepartX - nombreDeDeplacementSurLaGaucheEtLeBas) * TailleCases, (positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas) * TailleCases))
                    echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas ] = savePieceCaseArrive

                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas ), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas ] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut + 1,positionDepartY -( nombreDeDeplacementSurLaDroiteEtLeHaut + 1)) and( (echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut + 1, positionDepartY -( nombreDeDeplacementSurLaDroiteEtLeHaut + 1)][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut, positionDepartY - nombreDeDeplacementSurLaDroiteEtLeHaut][1] != couleurEnnemi)):
                nombreDeDeplacementSurLaDroiteEtLeHaut += 1
                savePieceCaseArrive = echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut , positionDepartY - (nombreDeDeplacementSurLaDroiteEtLeHaut)]
                echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut, positionDepartY - (nombreDeDeplacementSurLaDroiteEtLeHaut)] = ['fou', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection,((positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut) * TailleCases, (positionDepartY - nombreDeDeplacementSurLaDroiteEtLeHaut) * TailleCases))
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut , positionDepartY - (nombreDeDeplacementSurLaDroiteEtLeHaut )] = savePieceCaseArrive

                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut , positionDepartY - (nombreDeDeplacementSurLaDroiteEtLeHaut )] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1)) and (echiquier[positionDepartX -(nombreDeDeplacementSurLaGaucheEtLeHaut + 1), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1)][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGaucheEtLeHaut, positionDepartY - nombreDeDeplacementSurLaGaucheEtLeHaut][1] != couleurEnnemi):
                nombreDeDeplacementSurLaGaucheEtLeHaut += 1
                savePieceCaseArrive = echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut ), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut )]
                echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut ), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut )] = ['fou', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX - nombreDeDeplacementSurLaGaucheEtLeHaut) * TailleCases, (positionDepartY - nombreDeDeplacementSurLaGaucheEtLeHaut) * TailleCases))
                    echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut ), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut)] = savePieceCaseArrive

                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut ), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut )] = savePieceCaseArrive



#Reine
    if piece[0] == 'reine' :
        nombreDeDeplacementSurLaDroite = 0
        nombreDeDeplacementSurLaGauche = 0
        nombreDeDeplacementVersLeBas = 0
        nombreDeDeplacementVersLeHaut = 0
        nombreDeDeplacementSurLaDroiteEtLeBas = 0
        nombreDeDeplacementSurLaGaucheEtLeBas = 0
        nombreDeDeplacementSurLaDroiteEtLeHaut = 0
        nombreDeDeplacementSurLaGaucheEtLeHaut = 0
        if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
            while dansLEchiquier(positionDepartX+ nombreDeDeplacementSurLaDroite+1, positionDepartY) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroite+1, positionDepartY][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY][1]!= couleurEnnemi:
                nombreDeDeplacementSurLaDroite+=1
            for n in range(1, nombreDeDeplacementSurLaDroite + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX + n) * TailleCases, positionDepartY * TailleCases))


            while dansLEchiquier(positionDepartX -(nombreDeDeplacementSurLaGauche + 1), positionDepartY) and echiquier[positionDepartX - (nombreDeDeplacementSurLaGauche + 1), positionDepartY][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY][1]!= couleurEnnemi:
                nombreDeDeplacementSurLaGauche += 1
            for n in range(1, nombreDeDeplacementSurLaGauche + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX - n) * TailleCases, positionDepartY * TailleCases))


            while dansLEchiquier(positionDepartX, positionDepartY+ nombreDeDeplacementVersLeBas+1) and echiquier[positionDepartX, positionDepartY+nombreDeDeplacementVersLeBas+1][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX , positionDepartY+ nombreDeDeplacementVersLeBas][1]!= couleurEnnemi:
                nombreDeDeplacementVersLeBas+=1
            for n in range(1, nombreDeDeplacementVersLeBas + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY+n) * TailleCases))


            while dansLEchiquier(positionDepartX, positionDepartY- (nombreDeDeplacementVersLeHaut+1)) and echiquier[positionDepartX, positionDepartY-(nombreDeDeplacementVersLeHaut+1)][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX , positionDepartY- nombreDeDeplacementVersLeHaut][1]!= couleurEnnemi:
                nombreDeDeplacementVersLeHaut+=1
            for n in range(1, nombreDeDeplacementVersLeHaut + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY-n) * TailleCases))


            while dansLEchiquier(positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas + 1, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas +1) and (echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas+1, positionDepartY+nombreDeDeplacementSurLaDroiteEtLeBas+1][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY+ nombreDeDeplacementSurLaDroiteEtLeBas][1]!= couleurEnnemi):
                nombreDeDeplacementSurLaDroiteEtLeBas += 1
            for n in range(1, nombreDeDeplacementSurLaDroiteEtLeBas + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX + n) * TailleCases, (positionDepartY + n) * TailleCases))


            while dansLEchiquier(positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas + 1), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas + 1 ) and (echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas + 1), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas + 1][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGaucheEtLeBas, positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas][1] != couleurEnnemi):
                nombreDeDeplacementSurLaGaucheEtLeBas += 1
            for n in range(1, nombreDeDeplacementSurLaGaucheEtLeBas + 1):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX - n) * TailleCases, (positionDepartY + n) * TailleCases))


            while dansLEchiquier(positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut + 1,positionDepartY -( nombreDeDeplacementSurLaDroiteEtLeHaut + 1)) and( (echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut + 1, positionDepartY -( nombreDeDeplacementSurLaDroiteEtLeHaut + 1)][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut, positionDepartY - nombreDeDeplacementSurLaDroiteEtLeHaut][1] != couleurEnnemi)):
                nombreDeDeplacementSurLaDroiteEtLeHaut += 1
            for n in range(1, nombreDeDeplacementSurLaDroiteEtLeHaut + 1):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX + n) * TailleCases, (positionDepartY - n) * TailleCases))


            while dansLEchiquier(positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut +1), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1)) and (echiquier[positionDepartX -(nombreDeDeplacementSurLaGaucheEtLeHaut + 1), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1)][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGaucheEtLeHaut, positionDepartY - nombreDeDeplacementSurLaGaucheEtLeHaut][1] != couleurEnnemi):
                nombreDeDeplacementSurLaGaucheEtLeHaut += 1
            for n in range(1, nombreDeDeplacementSurLaGaucheEtLeHaut + 1):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX - n) * TailleCases, (positionDepartY - n) * TailleCases))



        elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
            while dansLEchiquier(positionDepartX+ nombreDeDeplacementSurLaDroite+1, positionDepartY) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroite+1, positionDepartY][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY][1]!= couleurEnnemi:
                nombreDeDeplacementSurLaDroite+=1
                savePieceCaseArrive = echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY]
                echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY] = ['reine', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX + nombreDeDeplacementSurLaDroite) * TailleCases, positionDepartY * TailleCases))

                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY] = savePieceCaseArrive
                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroite, positionDepartY] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX -(nombreDeDeplacementSurLaGauche + 1), positionDepartY) and echiquier[positionDepartX - (nombreDeDeplacementSurLaGauche + 1), positionDepartY][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY][1]!= couleurEnnemi:
                nombreDeDeplacementSurLaGauche += 1
                savePieceCaseArrive = echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY]
                echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY] = ['reine', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX - nombreDeDeplacementSurLaGauche) * TailleCases, positionDepartY * TailleCases))

                    echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY] = savePieceCaseArrive
                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX - nombreDeDeplacementSurLaGauche, positionDepartY] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX, positionDepartY+ nombreDeDeplacementVersLeBas+1) and echiquier[positionDepartX, positionDepartY+nombreDeDeplacementVersLeBas+1][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX , positionDepartY+ nombreDeDeplacementVersLeBas][1]!= couleurEnnemi:
                nombreDeDeplacementVersLeBas+=1
                savePieceCaseArrive = echiquier[positionDepartX, positionDepartY + nombreDeDeplacementVersLeBas]
                echiquier[positionDepartX, positionDepartY + nombreDeDeplacementVersLeBas] = ['reine', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY + nombreDeDeplacementVersLeBas) * TailleCases))

                    echiquier[positionDepartX, positionDepartY + nombreDeDeplacementVersLeBas] = savePieceCaseArrive
                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX, positionDepartY + nombreDeDeplacementVersLeBas] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX, positionDepartY- (nombreDeDeplacementVersLeHaut+1)) and echiquier[positionDepartX, positionDepartY-(nombreDeDeplacementVersLeHaut+1)][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX , positionDepartY- nombreDeDeplacementVersLeHaut][1]!= couleurEnnemi:
                nombreDeDeplacementVersLeHaut+=1
                savePieceCaseArrive = echiquier[positionDepartX, positionDepartY - nombreDeDeplacementVersLeHaut]
                echiquier[positionDepartX, positionDepartY - nombreDeDeplacementVersLeHaut] = ['reine', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, (positionDepartX * TailleCases, (positionDepartY - nombreDeDeplacementVersLeHaut) * TailleCases))

                    echiquier[positionDepartX, positionDepartY - nombreDeDeplacementVersLeHaut] = savePieceCaseArrive
                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX, positionDepartY - nombreDeDeplacementVersLeHaut] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas + 1, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas + 1) and (echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas+1, positionDepartY+nombreDeDeplacementSurLaDroiteEtLeBas+1][1]!= changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY+ nombreDeDeplacementSurLaDroiteEtLeBas][1]!= couleurEnnemi):
                nombreDeDeplacementSurLaDroiteEtLeBas += 1
                savePieceCaseArrive = echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas]
                echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas] = ['reine', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection,((positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas) * TailleCases, (positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas) * TailleCases))
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas + 1, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas + 1] = savePieceCaseArrive

                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeBas + 1, positionDepartY + nombreDeDeplacementSurLaDroiteEtLeBas + 1] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas + 1), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas + 1 ) and (echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas + 1), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas + 1][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGaucheEtLeBas, positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas][1] != couleurEnnemi):
                nombreDeDeplacementSurLaGaucheEtLeBas += 1
                savePieceCaseArrive = echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas ), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas ]
                echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas ), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas] = ['reine', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection,((positionDepartX - nombreDeDeplacementSurLaGaucheEtLeBas) * TailleCases, (positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas) * TailleCases))
                    echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas ), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas ] = savePieceCaseArrive

                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeBas ), positionDepartY + nombreDeDeplacementSurLaGaucheEtLeBas ] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut + 1,positionDepartY -( nombreDeDeplacementSurLaDroiteEtLeHaut + 1)) and( (echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut + 1, positionDepartY -( nombreDeDeplacementSurLaDroiteEtLeHaut + 1)][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut, positionDepartY - nombreDeDeplacementSurLaDroiteEtLeHaut][1] != couleurEnnemi)):
                nombreDeDeplacementSurLaDroiteEtLeHaut += 1
                savePieceCaseArrive = echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut , positionDepartY - (nombreDeDeplacementSurLaDroiteEtLeHaut)]
                echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut, positionDepartY - (nombreDeDeplacementSurLaDroiteEtLeHaut)] = ['reine', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection,((positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut) * TailleCases, (positionDepartY - nombreDeDeplacementSurLaDroiteEtLeHaut) * TailleCases))
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut , positionDepartY - (nombreDeDeplacementSurLaDroiteEtLeHaut )] = savePieceCaseArrive

                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX + nombreDeDeplacementSurLaDroiteEtLeHaut , positionDepartY - (nombreDeDeplacementSurLaDroiteEtLeHaut )] = savePieceCaseArrive

            while dansLEchiquier(positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1)) and (echiquier[positionDepartX -(nombreDeDeplacementSurLaGaucheEtLeHaut + 1), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut + 1)][1] != changeCouleurDuJoueur(couleurEnnemi) and echiquier[positionDepartX - nombreDeDeplacementSurLaGaucheEtLeHaut, positionDepartY - nombreDeDeplacementSurLaGaucheEtLeHaut][1] != couleurEnnemi):
                nombreDeDeplacementSurLaGaucheEtLeHaut += 1
                savePieceCaseArrive = echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut ), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut )]
                echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut ), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut )] = ['reine', changeCouleurDuJoueur(couleurEnnemi)]
                echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']
                if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                    selection.fill((0, 0, 255, 80))
                    ecran.blit(selection, ((positionDepartX - nombreDeDeplacementSurLaGaucheEtLeHaut) * TailleCases, (positionDepartY - nombreDeDeplacementSurLaGaucheEtLeHaut) * TailleCases))
                    echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut ), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut)] = savePieceCaseArrive

                    return False
                elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                    echiquier[positionDepartX - (nombreDeDeplacementSurLaGaucheEtLeHaut ), positionDepartY - (nombreDeDeplacementSurLaGaucheEtLeHaut )] = savePieceCaseArrive



#Roi
    if piece[0] == 'roi':
        if dansLEchiquier(positionDepartX+1,positionDepartY) and echiquier[positionDepartX+1, positionDepartY][1] != changeCouleurDuJoueur(couleurEnnemi):
            savePieceCaseArrive = echiquier[positionDepartX+1, positionDepartY]
            echiquier[positionDepartX+1, positionDepartY] = ['roi', changeCouleurDuJoueur(couleurEnnemi)]
            echiquier[positionDepartX,positionDepartY] = ['vide', 'incolore']
            if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection,((positionDepartX +1) * TailleCases, (positionDepartY ) * TailleCases))
                echiquier[positionDepartX + 1, positionDepartY] = savePieceCaseArrive

            elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                echiquier[positionDepartX + 1, positionDepartY] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX+1,positionDepartY+1) and echiquier[positionDepartX+1, positionDepartY+1][1] != changeCouleurDuJoueur(couleurEnnemi):
            savePieceCaseArrive = echiquier[positionDepartX+1, positionDepartY+1]
            echiquier[positionDepartX+1, positionDepartY+1] = ['roi', changeCouleurDuJoueur(couleurEnnemi)]
            echiquier[positionDepartX,positionDepartY] = ['vide', 'incolore']
            if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection, ((positionDepartX + 1) * TailleCases, (positionDepartY+1) * TailleCases))
                echiquier[positionDepartX + 1, positionDepartY+1] = savePieceCaseArrive

            elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                echiquier[positionDepartX + 1, positionDepartY +1 ] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX,positionDepartY+1) and echiquier[positionDepartX, positionDepartY+1][1] != changeCouleurDuJoueur(couleurEnnemi):
            savePieceCaseArrive = echiquier[positionDepartX, positionDepartY+1]
            echiquier[positionDepartX, positionDepartY+1] = ['roi', changeCouleurDuJoueur(couleurEnnemi)]
            echiquier[positionDepartX,positionDepartY] = ['vide', 'incolore']
            if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection,(positionDepartX * TailleCases, (positionDepartY + 1) * TailleCases))
                echiquier[positionDepartX , positionDepartY+1] = savePieceCaseArrive

            elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                echiquier[positionDepartX, positionDepartY + 1] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX-1,positionDepartY+1) and echiquier[positionDepartX-1, positionDepartY+1][1] != changeCouleurDuJoueur(couleurEnnemi):
            savePieceCaseArrive = echiquier[positionDepartX-1, positionDepartY+1]
            echiquier[positionDepartX-1, positionDepartY+1] = ['roi', changeCouleurDuJoueur(couleurEnnemi)]
            echiquier[positionDepartX,positionDepartY] = ['vide', 'incolore']
            if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection,((positionDepartX-1) * TailleCases, (positionDepartY + 1) * TailleCases))
                echiquier[positionDepartX -1, positionDepartY+1] = savePieceCaseArrive

            elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                echiquier[positionDepartX-1, positionDepartY + 1] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX-1,positionDepartY) and echiquier[positionDepartX-1, positionDepartY][1] != changeCouleurDuJoueur(couleurEnnemi):
            savePieceCaseArrive = echiquier[positionDepartX-1, positionDepartY]
            echiquier[positionDepartX-1, positionDepartY] = ['roi', changeCouleurDuJoueur(couleurEnnemi)]
            echiquier[positionDepartX,positionDepartY] = ['vide', 'incolore']
            if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection,((positionDepartX -1) * TailleCases, (positionDepartY ) * TailleCases))
                echiquier[positionDepartX - 1, positionDepartY] = savePieceCaseArrive

            elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                echiquier[positionDepartX - 1, positionDepartY] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX-1,positionDepartY-1) and echiquier[positionDepartX-1, positionDepartY-1][1] != changeCouleurDuJoueur(couleurEnnemi):
            savePieceCaseArrive = echiquier[positionDepartX-1, positionDepartY-1]
            echiquier[positionDepartX-1, positionDepartY-1] = ['roi', changeCouleurDuJoueur(couleurEnnemi)]
            echiquier[positionDepartX,positionDepartY] = ['vide', 'incolore']
            if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection,((positionDepartX-1) * TailleCases, (positionDepartY - 1) * TailleCases))
                echiquier[positionDepartX -1, positionDepartY-1] = savePieceCaseArrive

            elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                echiquier[positionDepartX-1, positionDepartY - 1] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX,positionDepartY-1) and echiquier[positionDepartX, positionDepartY-1][1] != changeCouleurDuJoueur(couleurEnnemi):
            savePieceCaseArrive = echiquier[positionDepartX, positionDepartY-1]
            echiquier[positionDepartX, positionDepartY-1] = ['roi', changeCouleurDuJoueur(couleurEnnemi)]
            echiquier[positionDepartX,positionDepartY] = ['vide', 'incolore']
            if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection,(positionDepartX * TailleCases, (positionDepartY - 1) * TailleCases))
                echiquier[positionDepartX , positionDepartY-1] = savePieceCaseArrive

            elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                echiquier[positionDepartX, positionDepartY - 1] = savePieceCaseArrive

        if dansLEchiquier(positionDepartX+1,positionDepartY-1) and echiquier[positionDepartX+1, positionDepartY-1][1] != changeCouleurDuJoueur(couleurEnnemi):
            savePieceCaseArrive = echiquier[positionDepartX+1, positionDepartY-1]
            echiquier[positionDepartX+1, positionDepartY-1] = ['roi', changeCouleurDuJoueur(couleurEnnemi)]
            echiquier[positionDepartX,positionDepartY] = ['vide', 'incolore']
            if (piece[1] == 'blanc' and not roiBlancEnEchec()) or (piece[1] == 'noir' and not roiNoirEnEchec()):
                selection.fill((0, 0, 255, 80))
                ecran.blit(selection,((positionDepartX+1) * TailleCases, (positionDepartY - 1) * TailleCases))
                echiquier[positionDepartX +1, positionDepartY-1] = savePieceCaseArrive

            elif (piece[1] == 'blanc' and roiBlancEnEchec()) or (piece[1] == 'noir' and roiNoirEnEchec()):
                echiquier[positionDepartX+1, positionDepartY - 1] = savePieceCaseArrive
