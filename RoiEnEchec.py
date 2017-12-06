from ihm import*


def roiBlancEnEchec():
    for y in range(0,8):
        for x in range(0,8):

            if echiquier[x, y] == ['pion', 'noir']:

                if dansLEchiquier(x+1, y-1) and echiquier[x+1, y-1] == ['roi', 'blanc']:
                    return True

                if dansLEchiquier(x-1, y-1) and echiquier[x-1, y-1] ==['roi', 'blanc']:
                    return True

            if echiquier[x,y] == ['tour', 'noir'] :
                nombreDeDeplacementVersLeHautTourNoir = 0
                nombreDeDeplacementSurLaGaucheTourNoir = 0
                nombreDeDeplacementSurLaDroiteTourNoir = 0
                nombreDeDeplacementVersLeBasTourNoir = 0

                while dansLEchiquier(x + nombreDeDeplacementSurLaDroiteTourNoir + 1, y) and (echiquier[x + nombreDeDeplacementSurLaDroiteTourNoir + 1, y][1] != 'noir' and echiquier[x + nombreDeDeplacementSurLaDroiteTourNoir, y][1] != 'blanc'):
                    nombreDeDeplacementSurLaDroiteTourNoir+=1
                for n in range (1, nombreDeDeplacementSurLaDroiteTourNoir +1) :
                    if echiquier[x + n, y] == ['roi', 'blanc'] :
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaGaucheTourNoir - 1, y) and (echiquier[x - nombreDeDeplacementSurLaGaucheTourNoir - 1, y][1] != 'noir' and echiquier[x - nombreDeDeplacementSurLaGaucheTourNoir, y][1] != 'blanc'):
                    nombreDeDeplacementSurLaGaucheTourNoir += 1
                for n in range(1, nombreDeDeplacementSurLaGaucheTourNoir +1):
                    if echiquier[x - n, y] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x , y - nombreDeDeplacementVersLeHautTourNoir - 1) and (echiquier[x, y - nombreDeDeplacementVersLeHautTourNoir - 1][1] != 'noir' and echiquier[x, y - nombreDeDeplacementVersLeHautTourNoir ][1] != 'blanc'):
                    nombreDeDeplacementVersLeHautTourNoir += 1
                for n in range(1, nombreDeDeplacementVersLeHautTourNoir+1):
                    if echiquier[x , y-n] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x , y + nombreDeDeplacementVersLeBasTourNoir + 1) and (echiquier[x, y + nombreDeDeplacementVersLeBasTourNoir + 1][1] != 'noir' and echiquier[x, y + nombreDeDeplacementVersLeBasTourNoir ][1] != 'blanc'):
                    nombreDeDeplacementVersLeBasTourNoir += 1
                for n in range(1, nombreDeDeplacementVersLeBasTourNoir +1):
                    if echiquier[x , y+n] == ['roi', 'blanc']:
                        return True

            if echiquier[x,y] == ['cavalier', 'noir'] :

                if x + 2 < 8 and y + 1 < 8 and echiquier[x + 2, y + 1] == ['roi', 'blanc'] :
                    return True

                if x + 1 < 8 and y + 2 < 8 and echiquier[x + 1, y + 2] == ['roi', 'blanc'] :
                    return True

                if x - 1 > -1 and y + 2 < 8 and echiquier[x - 1, y + 2] == ['roi', 'blanc'] :
                    return True

                if x - 2 > -1 and y + 1 < 8 and echiquier[x - 2, y + 1] == ['roi', 'blanc'] :
                    return True

                if x - 2 > - 1 and y - 1 > - 1 and echiquier[x - 2, y - 1] == ['roi', 'blanc'] :
                    return True

                if x - 1 > -1 and y - 2 > - 1 and echiquier[x - 1, y - 2] == ['roi', 'blanc'] :
                    return True

                if x + 1 < 8 and y - 2 > - 1 and echiquier[x + 1, y - 2] == ['roi', 'blanc'] :
                    return True

                if x + 2 < 8 and y - 1 > -1 and echiquier[x + 2, y - 1] == ['roi', 'blanc'] :
                    return True

            if echiquier[x, y] == ['fou', 'noir']:

                nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir = 0
                nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir = 0
                nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir = 0
                nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir = 0

                while dansLEchiquier(x + nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir + 1,y - nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir - 1) and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir + 1, y - nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir - 1][1] != 'noir' and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir, y - nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir][1] != 'blanc':
                    nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir += 1
                for n in range (1, nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouNoir+1):
                    if echiquier[x + n,y - n]==['roi', 'blanc']:
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir - 1,y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir - 1) and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir - 1, y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir - 1][1] != 'noir' and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir, y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir][1] != 'blanc':
                    nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouNoir + 1):
                    if echiquier[x - n, y - n] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir + 1,y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir + 1) and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir + 1, y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir + 1][1] != 'noir' and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir, y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir][1] != 'blanc':
                    nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouNoir + 1):
                    if echiquier[x + n, y + n] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir - 1,y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir + 1) and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir - 1, y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir + 1][1] != 'noir' and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir, y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir][1] != 'blanc':
                    nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouNoir + 1):
                    if echiquier[x - n, y + n] == ['roi', 'blanc']:
                        return True



            if echiquier[x,y] == ['reine', 'noir'] :

                nombreDeDeplacementVersLeHautReineNoir = 0
                nombreDeDeplacementSurLaGaucheReineNoir = 0
                nombreDeDeplacementSurLaDroiteReineNoir = 0
                nombreDeDeplacementVersLeBasReineNoir = 0
                nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir = 0
                nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir = 0
                nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir = 0
                nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir = 0

                while dansLEchiquier(x + nombreDeDeplacementSurLaDroiteReineNoir + 1, y) and echiquier[x + nombreDeDeplacementSurLaDroiteReineNoir + 1, y][1] != 'noir' and echiquier[x + nombreDeDeplacementSurLaDroiteReineNoir, y][1] != 'blanc':
                    nombreDeDeplacementSurLaDroiteReineNoir+=1
                for n in range (1, nombreDeDeplacementSurLaDroiteReineNoir +1) :
                    if echiquier[x + n, y] == ['roi', 'blanc'] :
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaGaucheReineNoir - 1, y) and echiquier[x - nombreDeDeplacementSurLaGaucheReineNoir - 1, y][1] != 'noir' and echiquier[x - nombreDeDeplacementSurLaGaucheReineNoir, y][1] != 'blanc':
                    nombreDeDeplacementSurLaGaucheReineNoir += 1
                for n in range(1, nombreDeDeplacementSurLaGaucheReineNoir + 1):
                    if echiquier[x - n, y] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x , y - nombreDeDeplacementVersLeHautReineNoir - 1) and echiquier[x, y - nombreDeDeplacementVersLeHautReineNoir - 1][1] != 'noir' and echiquier[x, y - nombreDeDeplacementVersLeHautReineNoir ][1] != 'blanc':
                    nombreDeDeplacementVersLeHautReineNoir += 1
                for n in range(1, nombreDeDeplacementVersLeHautReineNoir + 1):
                    if echiquier[x , y-n] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x , y + nombreDeDeplacementVersLeBasReineNoir + 1) and echiquier[x, y + nombreDeDeplacementVersLeBasReineNoir + 1][1] != 'noir' and echiquier[x, y + nombreDeDeplacementVersLeBasReineNoir ][1] != 'blanc':
                    nombreDeDeplacementVersLeBasReineNoir += 1
                for n in range(1, nombreDeDeplacementVersLeBasReineNoir + 1):
                    if echiquier[x , y+n] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x + nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir + 1,y - nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir - 1) and echiquier[x + nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir + 1, y - nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir - 1][1] != 'noir' and echiquier[x + nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir, y - nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir][1] != 'blanc':
                    nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaEnHautADroiteReineNoir + 1):
                    if echiquier[x + n, y - n] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir - 1,y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir - 1) and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir - 1, y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir - 1][1] != 'noir' and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir, y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir][1] != 'blanc':
                    nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineNoir + 1):
                    if echiquier[x - n, y - n] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir + 1,y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir + 1) and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir + 1, y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir + 1][1] != 'noir' and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir, y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir][1] != 'blanc':
                    nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineNoir + 1):
                    if echiquier[x + n, y + n] == ['roi', 'blanc']:
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir - 1,y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir + 1) and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir - 1, y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir + 1][1] != 'noir' and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir, y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir][1] != 'blanc':
                    nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineNoir + 1):
                    if echiquier[x - n, y + n] == ['roi', 'blanc']:
                        return True

            if echiquier[x, y] == ['roi', 'noir']:
                if dansLEchiquier(x+1,y+1) and echiquier[x+1,y+1] == ['roi', 'blanc'] :
                    return True

                if dansLEchiquier(x+1,y-1) and echiquier[x+1,y-1] == ['roi', 'blanc'] :
                    return True

                if dansLEchiquier(x - 1, y + 1) and echiquier[x - 1, y + 1] == ['roi', 'blanc']:
                    return True

                if dansLEchiquier(x-1,y-1) and echiquier[x-1,y-1] == ['roi', 'blanc'] :
                    return True

                if dansLEchiquier(x+1,y) and echiquier[x+1,y] == ['roi', 'blanc'] :
                    return True

                if dansLEchiquier(x,y+1) and echiquier[x,y+1] == ['roi', 'blanc'] :
                    return True

                if dansLEchiquier(x-1,y) and echiquier[x-1,y] == ['roi', 'blanc'] :
                    return True

                if dansLEchiquier(x,y-1) and echiquier[x,y-1] == ['roi', 'blanc'] :
                    return True


    return False


def roiNoirEnEchec() :
    for y in range(0,8):
        for x in range(0,8):

            if echiquier[x,y] == ['pion', 'blanc'] :
                if dansLEchiquier(x+1,y+1) and echiquier[x+1,y+1] == ['roi', 'noir'] :
                    return True
                if dansLEchiquier(x-1,y+1) and echiquier[x-1, y+1] ==['roi', 'noir'] :
                    return True

            if echiquier[x,y] == ['tour', 'blanc'] :
                nombreDeDeplacementVersLeHautTourBlanc = 0
                nombreDeDeplacementSurLaGaucheTourBlanc = 0
                nombreDeDeplacementSurLaDroiteTourBlanc = 0
                nombreDeDeplacementVersLeBasTourBlanc = 0

                while dansLEchiquier(x + nombreDeDeplacementSurLaDroiteTourBlanc + 1, y) and echiquier[x + nombreDeDeplacementSurLaDroiteTourBlanc + 1, y][1] != 'blanc' and echiquier[x + nombreDeDeplacementSurLaDroiteTourBlanc, y][1] != 'noir':
                    nombreDeDeplacementSurLaDroiteTourBlanc+=1
                for n in range (1, nombreDeDeplacementSurLaDroiteTourBlanc +1) :
                    if echiquier[x + n, y] == ['roi', 'noir'] :
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaGaucheTourBlanc - 1, y) and echiquier[x - nombreDeDeplacementSurLaGaucheTourBlanc - 1, y][1] != 'blanc' and echiquier[x - nombreDeDeplacementSurLaGaucheTourBlanc, y][1] != 'noir':
                    nombreDeDeplacementSurLaGaucheTourBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaGaucheTourBlanc + 1):
                    if echiquier[x - n, y] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x , y - nombreDeDeplacementVersLeHautTourBlanc - 1) and echiquier[x, y - nombreDeDeplacementVersLeHautTourBlanc - 1][1] != 'blanc' and echiquier[x, y - nombreDeDeplacementVersLeHautTourBlanc ][1] != 'noir':
                    nombreDeDeplacementVersLeHautTourBlanc += 1
                for n in range(1, nombreDeDeplacementVersLeHautTourBlanc + 1):
                    if echiquier[x , y-n] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x , y + nombreDeDeplacementVersLeBasTourBlanc + 1) and echiquier[x, y + nombreDeDeplacementVersLeBasTourBlanc + 1][1] != 'blanc' and echiquier[x, y + nombreDeDeplacementVersLeBasTourBlanc ][1] != 'noir':
                    nombreDeDeplacementVersLeBasTourBlanc += 1
                for n in range(1, nombreDeDeplacementVersLeBasTourBlanc + 1):
                    if echiquier[x , y+n] == ['roi', 'noir']:
                        return True

            if echiquier[x,y] == ['cavalier', 'blanc'] :

                if x + 2 < 8 and y + 1 < 8 and echiquier[x + 2, y + 1] == ['roi', 'noir'] :
                    return True

                if x + 1 < 8 and y + 2 < 8 and echiquier[x + 1, y + 2] == ['roi', 'noir'] :
                    return True

                if x - 1 > -1 and y + 2 < 8 and echiquier[x - 1, y + 2] == ['roi', 'noir'] :
                    return True

                if x - 2 > -1 and y + 1 < 8 and echiquier[x - 2, y + 1] == ['roi', 'noir'] :
                    return True

                if x - 2 > - 1 and y - 1 > - 1 and echiquier[x - 2, y - 1] == ['roi', 'noir'] :
                    return True

                if x - 1 > -1 and y - 2 > - 1 and echiquier[x - 1, y - 2] == ['roi', 'noir'] :
                    return True

                if x + 1 < 8 and y - 2 > - 1 and echiquier[x + 1, y - 2] == ['roi', 'noir'] :
                    return True

                if x + 2 < 8 and y - 1 > -1 and echiquier[x + 2, y - 1] == ['roi', 'noir'] :
                    return True

            if echiquier[x, y] == ['fou', 'blanc']:

                nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc = 0
                nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc = 0
                nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc = 0
                nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc = 0

                while dansLEchiquier(x + nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc + 1,y - nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc - 1) and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc + 1, y - nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc - 1][1] != 'blanc' and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc, y - nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc][1] != 'noir':
                    nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc += 1
                for n in range (1, nombreDeDeplacementSurLaDiagonaleEnHautADroiteFouBlanc+1):
                    if echiquier[x + n,y - n]==['roi', 'noir']:
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc - 1,y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc - 1) and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc - 1, y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc - 1][1] != 'blanc' and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc, y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc][1] != 'noir':
                    nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnHautAGaucheFouBlanc + 1):
                    if echiquier[x - n, y - n] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc + 1,y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc + 1) and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc + 1, y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc + 1][1] != 'blanc' and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc, y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc][1] != 'noir':
                    nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnBasADroiteFouBlanc + 1):
                    if echiquier[x + n, y + n] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc - 1,y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc + 1) and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc - 1, y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc + 1][1] != 'blanc' and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc, y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc][1] != 'noir':
                    nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnBasAGaucheFouBlanc + 1):
                    if echiquier[x - n, y + n] == ['roi', 'noir']:
                        return True

            if echiquier[x,y] == ['reine', 'blanc'] :
                nombreDeDeplacementVersLeHautReineBlanc = 0
                nombreDeDeplacementSurLaGaucheReineBlanc = 0
                nombreDeDeplacementSurLaDroiteReineBlanc = 0
                nombreDeDeplacementVersLeBasReineBlanc = 0
                nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc = 0
                nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc = 0
                nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc = 0
                nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc = 0

                while dansLEchiquier(x + nombreDeDeplacementSurLaDroiteReineBlanc + 1, y) and echiquier[x + nombreDeDeplacementSurLaDroiteReineBlanc + 1, y][1] != 'blanc' and echiquier[x + nombreDeDeplacementSurLaDroiteReineBlanc, y][1] != 'noir':
                    nombreDeDeplacementSurLaDroiteReineBlanc+=1
                for n in range (1, nombreDeDeplacementSurLaDroiteReineBlanc +1) :
                    if echiquier[x + n, y] == ['roi', 'noir'] :
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaGaucheReineBlanc - 1, y) and echiquier[x - nombreDeDeplacementSurLaGaucheReineBlanc - 1, y][1] != 'blanc' and echiquier[x - nombreDeDeplacementSurLaGaucheReineBlanc, y][1] != 'noir':
                    nombreDeDeplacementSurLaGaucheReineBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaGaucheReineBlanc + 1):
                    if echiquier[x - n, y] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x , y - nombreDeDeplacementVersLeHautReineBlanc - 1) and echiquier[x, y - nombreDeDeplacementVersLeHautReineBlanc - 1][1] != 'blanc' and echiquier[x, y - nombreDeDeplacementVersLeHautReineBlanc ][1] != 'noir':
                    nombreDeDeplacementVersLeHautReineBlanc += 1
                for n in range(1, nombreDeDeplacementVersLeHautReineBlanc + 1):
                    if echiquier[x , y-n] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x , y + nombreDeDeplacementVersLeBasReineBlanc + 1) and echiquier[x, y + nombreDeDeplacementVersLeBasReineBlanc + 1][1] != 'blanc' and echiquier[x, y + nombreDeDeplacementVersLeBasReineBlanc ][1] != 'noir':
                    nombreDeDeplacementVersLeBasReineBlanc += 1
                for n in range(1, nombreDeDeplacementVersLeBasReineBlanc + 1):
                    if echiquier[x , y+n] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x + nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc + 1,y - nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc - 1) and echiquier[x + nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc + 1, y - nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc - 1][1] != 'blanc' and echiquier[x + nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc, y - nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc][1] != 'noir':
                    nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaEnHautADroiteReineBlanc + 1):
                    if echiquier[x + n, y - n] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc - 1,y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc - 1) and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc - 1, y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc - 1][1] != 'blanc' and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc, y - nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc][1] != 'noir':
                    nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnHautAGaucheReineBlanc + 1):
                    if echiquier[x - n, y - n] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc + 1,y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc + 1) and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc + 1, y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc + 1][1] != 'blanc' and echiquier[x + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc, y + nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc][1] != 'noir':
                    nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnBasADroiteReineBlanc + 1):
                    if echiquier[x + n, y + n] == ['roi', 'noir']:
                        return True

                while dansLEchiquier(x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc - 1,y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc + 1) and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc - 1, y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc + 1][1] != 'blanc' and echiquier[x - nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc, y + nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc][1] != 'noir':
                    nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc += 1
                for n in range(1, nombreDeDeplacementSurLaDiagonaleEnBasAGaucheReineBlanc + 1):
                    if echiquier[x - n, y + n] == ['roi', 'noir']:
                        return True

            if echiquier[x, y] == ['roi', 'blanc']:
                if dansLEchiquier(x + 1, y + 1) and echiquier[x + 1, y + 1] == ['roi', 'noir']:
                    return True

                if dansLEchiquier(x + 1, y - 1) and echiquier[x + 1, y - 1] == ['roi', 'noir']:
                    return True

                if dansLEchiquier(x - 1, y + 1) and echiquier[x - 1, y + 1] == ['roi', 'noir']:
                    return True

                if dansLEchiquier(x - 1, y - 1) and echiquier[x - 1, y - 1] == ['roi', 'noir']:
                    return True

                if dansLEchiquier(x + 1, y) and echiquier[x + 1, y ] == ['roi', 'noir']:
                    return True

                if dansLEchiquier(x, y + 1) and echiquier[x , y + 1] == ['roi', 'noir']:
                    return True

                if dansLEchiquier(x - 1, y) and echiquier[x - 1, y ] == ['roi', 'noir']:
                    return True

                if dansLEchiquier(x, y - 1) and echiquier[x , y - 1] == ['roi', 'noir']:
                    return True

    return False