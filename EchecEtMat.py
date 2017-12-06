from RoiEnEchec import *
from data import *

def roiBlancEchecEtMat() :
    if roiBlancEnEchec() :
        for x in range(0, 8):
            for y in range(0, 8):

                if echiquier[x, y] == ['pion', 'blanc']:

                    if dansLEchiquier(x, y+1) and echiquier[x, y + 1] == ['vide', 'incolore']:
                        savePieceCasePionBlanc1 = echiquier[x, y + 1]
                        echiquier[x, y + 1] = ['pion', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec():
                            echiquier[x, y] = ['pion', 'blanc']
                            echiquier[x, y + 1] = savePieceCasePionBlanc1
                            return False
                        echiquier[x, y] = ['pion', 'blanc']
                        echiquier[x, y + 1] = savePieceCasePionBlanc1

                    if y == 1 and echiquier[x, y + 2] == ['vide', 'incolore'] :
                        savePieceCasePionBlanc2 = echiquier[x, y + 2]
                        echiquier[x, y + 2] = ['pion', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec():
                            echiquier[x, y] = ['pion', 'blanc']
                            echiquier[x, y + 2] = savePieceCasePionBlanc2
                            return False
                        echiquier[x, y] = ['pion', 'blanc']
                        echiquier[x, y + 2] = savePieceCasePionBlanc2


                    if dansLEchiquier(x+1, y+1) and echiquier[x + 1, y + 1][1] == 'noir':
                        savePieceCasePionBlanc3 = echiquier[x + 1, y + 1]
                        echiquier[x + 1, y + 1] = ['pion', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec():
                            echiquier[x, y] = ['pion', 'blanc']
                            echiquier[x + 1, y + 1] = savePieceCasePionBlanc3
                            return False
                        echiquier[x, y] = ['pion', 'blanc']
                        echiquier[x + 1, y + 1] = savePieceCasePionBlanc3

                    if dansLEchiquier(x-1, y+1) and echiquier[x - 1, y + 1][1] == 'noir':
                        savePieceCasePionBlanc4 = echiquier[x - 1, y + 1]
                        echiquier[x - 1, y + 1] = ['pion', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec():
                            echiquier[x, y] = ['pion', 'blanc']
                            echiquier[x - 1, y + 1] = savePieceCasePionBlanc4
                            return False
                        echiquier[x, y] = ['pion', 'blanc']
                        echiquier[x - 1, y + 1] = savePieceCasePionBlanc4

                if echiquier[x, y] == ['tour', 'blanc']:

                    nombreDeDeplacementSurLaDroiteTourBlanc = 0
                    nombreDeDeplacementSurLaGaucheTourBlanc = 0
                    nombreDeDeplacementVersLeBasTourBlanc = 0
                    nombreDeDeplacementVersLeHautTourBlanc = 0

                    while dansLEchiquier(x + nombreDeDeplacementSurLaDroiteTourBlanc+1, y) and echiquier[x + nombreDeDeplacementSurLaDroiteTourBlanc +1 , y][1] != 'blanc' and echiquier[x+nombreDeDeplacementSurLaDroiteTourBlanc, y] != 'noir' :
                        nombreDeDeplacementSurLaDroiteTourBlanc +=1
                    for n in range (1, nombreDeDeplacementSurLaDroiteTourBlanc+1) :
                        savePieceCaseTourBlanc1 = echiquier[x + n, y]
                        echiquier[x + n, y] = ['tour', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x + n, y] = savePieceCaseTourBlanc1
                            echiquier[x, y] = ['tour', 'blanc']
                            return False
                        echiquier[x + n, y] = savePieceCaseTourBlanc1
                        echiquier[x, y] = ['tour', 'blanc']

                    while dansLEchiquier(x - nombreDeDeplacementSurLaGaucheTourBlanc-1, y) and echiquier[x - nombreDeDeplacementSurLaGaucheTourBlanc -1 , y][1] != 'blanc' and echiquier[x-nombreDeDeplacementSurLaGaucheTourBlanc, y] != 'noir' :
                        nombreDeDeplacementSurLaGaucheTourBlanc +=1
                    for n in range (1, nombreDeDeplacementSurLaGaucheTourBlanc+1) :
                        savePieceCaseTourBlanc2 = echiquier[x - n, y]
                        echiquier[x - n, y] = ['tour', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x - n, y] = savePieceCaseTourBlanc2
                            echiquier[x, y] = ['tour', 'blanc']
                            return False
                        echiquier[x - n, y] = savePieceCaseTourBlanc2
                        echiquier[x, y] = ['tour', 'blanc']

                    while dansLEchiquier(x, y+nombreDeDeplacementVersLeBasTourBlanc+1) and echiquier[x, y+nombreDeDeplacementVersLeBasTourBlanc+1][1] != 'blanc' and echiquier[x, y+nombreDeDeplacementVersLeBasTourBlanc] != 'noir' :
                        nombreDeDeplacementVersLeBasTourBlanc +=1
                    for n in range (1, nombreDeDeplacementVersLeBasTourBlanc+1) :
                        savePieceCaseTourBlanc3 = echiquier[x, y + n]
                        echiquier[x, y + n] = ['tour', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x, y + n] = savePieceCaseTourBlanc3
                            echiquier[x, y] = ['tour', 'blanc']
                            return False
                        echiquier[x, y + n] = savePieceCaseTourBlanc3
                        echiquier[x, y] = ['tour', 'blanc']

                    while dansLEchiquier(x, y-nombreDeDeplacementVersLeHautTourBlanc-1) and echiquier[x, y-nombreDeDeplacementVersLeHautTourBlanc-1][1] != 'blanc' and echiquier[x, y-nombreDeDeplacementVersLeHautTourBlanc] != 'noir' :
                        nombreDeDeplacementVersLeHautTourBlanc +=1
                    for n in range (1, nombreDeDeplacementVersLeHautTourBlanc+1) :
                        savePieceCaseTourBlanc4 = echiquier[x, y - n]
                        echiquier[x, y - n] = ['tour', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x, y - n] = savePieceCaseTourBlanc4
                            echiquier[x, y] = ['tour', 'blanc']
                            return False
                        echiquier[x, y - n] = savePieceCaseTourBlanc4
                        echiquier[x, y] = ['tour', 'blanc']


                if echiquier[x, y] == ['fou', 'blanc']:

                    nombreDeDeplacementEnBasADroiteFouBlanc = 0
                    nombreDeDeplacementEnBasAGaucheFouBlanc = 0
                    nombreDeDeplacementEnHautADroiteFouBlanc = 0
                    nombreDeDeplacementEnHautAGaucheFouBlanc = 0

                    while dansLEchiquier(x + nombreDeDeplacementEnBasADroiteFouBlanc+1, y + nombreDeDeplacementEnBasADroiteFouBlanc+1) and echiquier[x + nombreDeDeplacementEnBasADroiteFouBlanc +1 , y+ nombreDeDeplacementEnBasADroiteFouBlanc +1][1] != 'blanc' and echiquier[x+nombreDeDeplacementEnBasADroiteFouBlanc, y + nombreDeDeplacementEnBasADroiteFouBlanc] != 'noir' :
                        nombreDeDeplacementEnBasADroiteFouBlanc +=1
                    for n in range (1, nombreDeDeplacementEnBasADroiteFouBlanc+1) :
                        savePieceCaseFouBlanc1 = echiquier[x + n, y + n]
                        echiquier[x + n, y + n] = ['fou', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x + n, y + n] = savePieceCaseFouBlanc1
                            echiquier[x, y] = ['fou', 'blanc']
                            return False
                        echiquier[x + n, y + n] = savePieceCaseFouBlanc1
                        echiquier[x, y] = ['fou', 'blanc']

                    while dansLEchiquier(x - nombreDeDeplacementEnBasAGaucheFouBlanc-1, y +nombreDeDeplacementEnBasAGaucheFouBlanc+1) and echiquier[x - nombreDeDeplacementEnBasAGaucheFouBlanc -1 , y + nombreDeDeplacementEnBasAGaucheFouBlanc +1][1] != 'blanc' and echiquier[x-nombreDeDeplacementEnBasAGaucheFouBlanc, y +nombreDeDeplacementEnBasAGaucheFouBlanc] != 'noir' :
                        nombreDeDeplacementEnBasAGaucheFouBlanc +=1
                    for n in range (1, nombreDeDeplacementEnBasAGaucheFouBlanc+1) :
                        savePieceCaseFouBlanc2 = echiquier[x - n, y + n]
                        echiquier[x - n, y + n] = ['fou', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x - n, y + n] = savePieceCaseFouBlanc2
                            echiquier[x, y] = ['fou', 'blanc']
                            return False
                        echiquier[x - n, y + n] = savePieceCaseFouBlanc2
                        echiquier[x, y] = ['fou', 'blanc']

                    while dansLEchiquier(x+ nombreDeDeplacementEnHautADroiteFouBlanc + 1, y - nombreDeDeplacementEnHautADroiteFouBlanc -1) and echiquier[x + nombreDeDeplacementEnHautADroiteFouBlanc +1, y - nombreDeDeplacementEnHautADroiteFouBlanc - 1][1] != 'blanc' and echiquier[x + nombreDeDeplacementEnHautADroiteFouBlanc, y - nombreDeDeplacementEnHautADroiteFouBlanc] != 'noir' :
                        nombreDeDeplacementEnHautADroiteFouBlanc +=1
                    for n in range (1, nombreDeDeplacementEnHautADroiteFouBlanc+1) :
                        savePieceCaseFouBlanc3 = echiquier[x + n, y - n]
                        echiquier[x + n, y - n] = ['fou', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x + n, y - n] = savePieceCaseFouBlanc3
                            echiquier[x, y] = ['fou', 'blanc']
                            return False
                        echiquier[x + n, y - n] = savePieceCaseFouBlanc3
                        echiquier[x, y] = ['fou', 'blanc']

                    while dansLEchiquier(x - nombreDeDeplacementEnHautAGaucheFouBlanc -1, y-nombreDeDeplacementEnHautAGaucheFouBlanc-1) and echiquier[x- nombreDeDeplacementEnHautAGaucheFouBlanc -1, y-nombreDeDeplacementEnHautAGaucheFouBlanc-1][1] != 'blanc' and echiquier[x - nombreDeDeplacementEnHautAGaucheFouBlanc, y-nombreDeDeplacementEnHautAGaucheFouBlanc] != 'noir' :
                        nombreDeDeplacementEnHautAGaucheFouBlanc +=1
                    for n in range (1, nombreDeDeplacementEnHautAGaucheFouBlanc+1) :
                        savePieceCaseFouBlanc4 = echiquier[x - n, y - n]
                        echiquier[x - n, y - n] = ['fou', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x - n, y - n] = savePieceCaseFouBlanc4
                            echiquier[x, y] = ['fou', 'blanc']
                            return False
                        echiquier[x - n, y - n] = savePieceCaseFouBlanc4
                        echiquier[x, y] = ['fou', 'blanc']

                if echiquier[x, y] == ['cavalier', 'blanc'] :

                    if dansLEchiquier(x + 2, y + 1) and echiquier[x+2, y+1][1] != 'blanc':
                        savePieceCaseCavalierBlanc1 = echiquier[x + 2, y + 1]
                        echiquier[x + 2, y + 1] = ['cavalier', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier [x + 2, y + 1]= savePieceCaseCavalierBlanc1
                            echiquier[x, y] = ['cavalier', 'blanc']
                            return False
                        echiquier[x + 2, y + 1] = savePieceCaseCavalierBlanc1
                        echiquier[x, y] = ['cavalier', 'blanc']

                    if dansLEchiquier(x + 1, y + 2) and echiquier[x+1, y+2][1] != 'blanc':
                        savePieceCaseCavalierBlanc2 = echiquier[x + 1, y + 2]
                        echiquier[x + 1, y + 2] = ['cavalier', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier [x + 1, y + 2]= savePieceCaseCavalierBlanc2
                            echiquier[x, y] = ['cavalier', 'blanc']
                            return False
                        echiquier[x + 1, y + 2] = savePieceCaseCavalierBlanc2
                        echiquier[x, y] = ['cavalier', 'blanc']

                    if dansLEchiquier(x - 1, y + 2) and echiquier[x-1, y+2][1] != 'blanc':
                        savePieceCaseCavalierBlanc3 = echiquier[x - 1, y + 2]
                        echiquier[x - 1, y + 2] = ['cavalier', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier [x - 1, y + 2]= savePieceCaseCavalierBlanc3
                            echiquier[x, y] = ['cavalier', 'blanc']
                            return False
                        echiquier[x - 1, y + 2] = savePieceCaseCavalierBlanc3
                        echiquier[x, y] = ['cavalier', 'blanc']

                    if dansLEchiquier(x - 2, y + 1) and echiquier[x-2, y+1][1] != 'blanc':
                        savePieceCaseCavalierBlanc4 = echiquier[x - 2, y + 1]
                        echiquier[x - 2, y + 1] = ['cavalier', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier [x - 2, y + 1]= savePieceCaseCavalierBlanc4
                            echiquier[x, y] = ['cavalier', 'blanc']
                            return False
                        echiquier[x - 2, y + 1] = savePieceCaseCavalierBlanc4
                        echiquier[x, y] = ['cavalier', 'blanc']

                    if dansLEchiquier(x - 2, y - 1) and echiquier[x-2, y-1][1] != 'blanc':
                        savePieceCaseCavalierBlanc5 = echiquier[x - 2, y - 1]
                        echiquier[x - 2, y - 1] = ['cavalier', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier [x - 2, y - 1]= savePieceCaseCavalierBlanc5
                            echiquier[x, y] = ['cavalier', 'blanc']
                            return False
                        echiquier[x - 2, y - 1] = savePieceCaseCavalierBlanc5
                        echiquier[x, y] = ['cavalier', 'blanc']

                    if dansLEchiquier(x - 1, y - 2) and echiquier[x-1, y-2][1] != 'blanc':
                        savePieceCaseCavalierBlanc6 = echiquier[x - 1, y - 2]
                        echiquier[x - 1, y - 2] = ['cavalier', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier [x - 1, y - 2]= savePieceCaseCavalierBlanc6
                            echiquier[x, y] = ['cavalier', 'blanc']
                            return False
                        echiquier[x - 1, y - 2] = savePieceCaseCavalierBlanc6
                        echiquier[x, y] = ['cavalier', 'blanc']

                    if dansLEchiquier(x + 1, y - 2) and echiquier[x+1, y-2][1] != 'blanc':
                        savePieceCaseCavalierBlanc7 = echiquier[x + 1, y - 2]
                        echiquier[x + 1, y - 2] = ['cavalier', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier [x + 1, y - 2]= savePieceCaseCavalierBlanc7
                            echiquier[x, y] = ['cavalier', 'blanc']
                            return False
                        echiquier[x + 1, y - 2] = savePieceCaseCavalierBlanc7
                        echiquier[x, y] = ['cavalier', 'blanc']

                    if dansLEchiquier(x + 2, y - 1) and echiquier[x+2, y-1][1] != 'blanc':
                        savePieceCaseCavalierBlanc8 = echiquier[x + 2, y - 1]
                        echiquier[x + 2, y - 1] = ['cavalier', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier [x + 2, y - 1]= savePieceCaseCavalierBlanc8
                            echiquier[x, y] = ['cavalier', 'blanc']
                            return False
                        echiquier[x + 2, y - 1] = savePieceCaseCavalierBlanc8
                        echiquier[x, y] = ['cavalier', 'blanc']



                if echiquier[x, y] == ['reine', 'blanc']:

                    nombreDeDeplacementSurLaDroiteReineBlanc = 0
                    nombreDeDeplacementSurLaGaucheReineBlanc = 0
                    nombreDeDeplacementVersLeBasReineBlanc = 0
                    nombreDeDeplacementVersLeHautReineBlanc = 0
                    nombreDeDeplacementEnBasADroiteReineBlanc = 0
                    nombreDeDeplacementEnBasAGaucheReineBlanc = 0
                    nombreDeDeplacementEnHautADroiteReineBlanc = 0
                    nombreDeDeplacementEnHautAGaucheReineBlanc = 0

                    while dansLEchiquier(x + nombreDeDeplacementSurLaDroiteReineBlanc+1, y) and echiquier[x + nombreDeDeplacementSurLaDroiteReineBlanc +1 , y][1] != 'blanc' and echiquier[x+nombreDeDeplacementSurLaDroiteReineBlanc, y] != 'noir' :
                        nombreDeDeplacementSurLaDroiteReineBlanc +=1
                    for n in range (1, nombreDeDeplacementSurLaDroiteReineBlanc+1) :
                        savePieceCaseReineBlanc1 = echiquier[x + n, y]
                        echiquier[x + n, y] = ['reine', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x + n, y] = savePieceCaseReineBlanc1
                            echiquier[x, y] = ['reine', 'blanc']
                            return False
                        echiquier[x + n, y] = savePieceCaseReineBlanc1
                        echiquier[x, y] = ['reine', 'blanc']

                    while dansLEchiquier(x - nombreDeDeplacementSurLaGaucheReineBlanc-1, y) and echiquier[x - nombreDeDeplacementSurLaGaucheReineBlanc -1 , y][1] != 'blanc' and echiquier[x-nombreDeDeplacementSurLaGaucheReineBlanc, y] != 'noir' :
                        nombreDeDeplacementSurLaGaucheReineBlanc +=1
                    for n in range (1, nombreDeDeplacementSurLaGaucheReineBlanc+1) :
                        savePieceCaseReineBlanc2 = echiquier[x - n, y]
                        echiquier[x - n, y] = ['reine', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x - n, y] = savePieceCaseReineBlanc2
                            echiquier[x, y] = ['reine', 'blanc']
                            return False
                        echiquier[x - n, y] = savePieceCaseReineBlanc2
                        echiquier[x, y] = ['reine', 'blanc']

                    while dansLEchiquier(x, y+nombreDeDeplacementVersLeBasReineBlanc+1) and echiquier[x, y+nombreDeDeplacementVersLeBasReineBlanc+1][1] != 'blanc' and echiquier[x, y+nombreDeDeplacementVersLeBasReineBlanc] != 'noir' :
                        nombreDeDeplacementVersLeBasReineBlanc +=1
                    for n in range (1, nombreDeDeplacementVersLeBasReineBlanc+1) :
                        savePieceCaseReineBlanc3 = echiquier[x, y + n]
                        echiquier[x, y + n] = ['reine', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x, y + n] = savePieceCaseReineBlanc3
                            echiquier[x, y] = ['reine', 'blanc']
                            return False
                        echiquier[x, y + n] = savePieceCaseReineBlanc3
                        echiquier[x, y] = ['reine', 'blanc']

                    while dansLEchiquier(x, y-nombreDeDeplacementVersLeHautReineBlanc-1) and echiquier[x, y-nombreDeDeplacementVersLeHautReineBlanc-1][1] != 'blanc' and echiquier[x, y-nombreDeDeplacementVersLeHautReineBlanc] != 'noir' :
                        nombreDeDeplacementVersLeHautReineBlanc +=1
                    for n in range (1, nombreDeDeplacementVersLeHautReineBlanc+1) :
                        savePieceCaseReineBlanc4 = echiquier[x, y - n]
                        echiquier[x, y - n] = ['reine', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x, y - n] = savePieceCaseReineBlanc4
                            echiquier[x, y] = ['reine', 'blanc']
                            return False
                        echiquier[x, y - n] = savePieceCaseReineBlanc4
                        echiquier[x, y] = ['reine', 'blanc']

                    while dansLEchiquier(x + nombreDeDeplacementEnBasADroiteReineBlanc+1, y + nombreDeDeplacementEnBasADroiteReineBlanc+1) and echiquier[x + nombreDeDeplacementEnBasADroiteReineBlanc +1 , y+ nombreDeDeplacementEnBasADroiteReineBlanc +1][1] != 'blanc' and echiquier[x+nombreDeDeplacementEnBasADroiteReineBlanc, y + nombreDeDeplacementEnBasADroiteReineBlanc] != 'noir' :
                        nombreDeDeplacementEnBasADroiteReineBlanc +=1
                    for n in range (1, nombreDeDeplacementEnBasADroiteReineBlanc+1) :
                        savePieceCaseReineBlanc5 = echiquier[x + n, y + n]
                        echiquier[x + n, y + n] = ['reine', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x + n, y + n] = savePieceCaseReineBlanc5
                            echiquier[x, y] = ['reine', 'blanc']
                            return False
                        echiquier[x + n, y + n] = savePieceCaseReineBlanc5
                        echiquier[x, y] = ['reine', 'blanc']

                    while dansLEchiquier(x - nombreDeDeplacementEnBasAGaucheReineBlanc-1, y +nombreDeDeplacementEnBasAGaucheReineBlanc+1) and echiquier[x - nombreDeDeplacementEnBasAGaucheReineBlanc -1 , y + nombreDeDeplacementEnBasAGaucheReineBlanc +1][1] != 'blanc' and echiquier[x-nombreDeDeplacementEnBasAGaucheReineBlanc, y +nombreDeDeplacementEnBasAGaucheReineBlanc] != 'noir' :
                        nombreDeDeplacementEnBasAGaucheReineBlanc +=1
                    for n in range (1, nombreDeDeplacementEnBasAGaucheReineBlanc+1) :
                        savePieceCaseReineBlanc6 = echiquier[x - n, y + n]
                        echiquier[x - n, y + n] = ['reine', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x - n, y + n] = savePieceCaseReineBlanc6
                            echiquier[x, y] = ['reine', 'blanc']
                            return False
                        echiquier[x - n, y + n] = savePieceCaseReineBlanc6
                        echiquier[x, y] = ['reine', 'blanc']

                    while dansLEchiquier(x+ nombreDeDeplacementEnHautADroiteReineBlanc + 1, y - nombreDeDeplacementEnHautADroiteReineBlanc -1) and echiquier[x + nombreDeDeplacementEnHautADroiteReineBlanc +1, y - nombreDeDeplacementEnHautADroiteReineBlanc - 1][1] != 'blanc' and echiquier[x + nombreDeDeplacementEnHautADroiteReineBlanc, y - nombreDeDeplacementEnHautADroiteReineBlanc] != 'noir' :
                        nombreDeDeplacementEnHautADroiteReineBlanc +=1
                    for n in range (1, nombreDeDeplacementEnHautADroiteReineBlanc+1) :
                        savePieceCaseReineBlanc7 = echiquier[x + n, y - n]
                        echiquier[x + n, y - n] = ['reine', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x + n, y - n] = savePieceCaseReineBlanc7
                            echiquier[x, y] = ['reine', 'blanc']
                            return False
                        echiquier[x + n, y - n] = savePieceCaseReineBlanc7
                        echiquier[x, y] = ['reine', 'blanc']

                    while dansLEchiquier(x - nombreDeDeplacementEnHautAGaucheReineBlanc -1, y-nombreDeDeplacementEnHautAGaucheReineBlanc-1) and echiquier[x- nombreDeDeplacementEnHautAGaucheReineBlanc -1, y-nombreDeDeplacementEnHautAGaucheReineBlanc-1][1] != 'blanc' and echiquier[x - nombreDeDeplacementEnHautAGaucheReineBlanc, y-nombreDeDeplacementEnHautAGaucheReineBlanc] != 'noir' :
                        nombreDeDeplacementEnHautAGaucheReineBlanc +=1
                    for n in range (1, nombreDeDeplacementEnHautAGaucheReineBlanc+1) :
                        savePieceCaseReineBlanc8 = echiquier[x - n, y - n]
                        echiquier[x - n, y - n] = ['reine', 'blanc']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiBlancEnEchec() :
                            echiquier[x - n, y - n] = savePieceCaseReineBlanc8
                            echiquier[x, y] = ['reine', 'blanc']
                            return False
                        echiquier[x - n, y - n] = savePieceCaseReineBlanc8
                        echiquier[x, y] = ['reine', 'blanc']



                if echiquier[x, y] == ['roi', 'blanc']:
                    if dansLEchiquier(x+1, y) :
                        if echiquier[x+1, y][1] == ['vide', 'incolore'] or echiquier[x+1, y+1][1] == 'noir':
                            savePieceCaseRoiBlanc1 = echiquier[x + 1, y]
                            echiquier[x + 1, y] = ['roi', 'blanc']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiBlancEnEchec() :
                                echiquier[x + 1, y] = savePieceCaseRoiBlanc1
                                echiquier[x, y] = ['roi', 'blanc']
                            else:
                                echiquier[x + 1, y] = savePieceCaseRoiBlanc1
                                echiquier[x, y] = ['roi', 'blanc']
                                return False

                    if dansLEchiquier(x+1, y+1) :
                        if echiquier[x+1, y+1] == ['vide', 'incolore'] or echiquier[x+1, y+1][1] == 'noir':
                            savePieceCaseRoiBlanc2 = echiquier[x + 1, y + 1]
                            echiquier[x + 1, y + 1] = ['roi', 'blanc']
                            echiquier [x, y] = ['vide', 'incolore']
                            if roiBlancEnEchec():
                                echiquier[x + 1, y + 1] = savePieceCaseRoiBlanc2
                                echiquier[x, y] = ['roi', 'blanc']
                            else :
                                echiquier[x + 1, y + 1] = savePieceCaseRoiBlanc2
                                echiquier[x, y] = ['roi', 'blanc']
                                return False


                    if  dansLEchiquier(x, y+1) :
                        if echiquier[x, y+1] == ['vide', 'incolore'] or echiquier[x, y+1][1] == 'noir':
                            savePieceCaseRoiBlanc3 = echiquier[x, y + 1]
                            echiquier[x, y + 1] = ['roi', 'blanc']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiBlancEnEchec():
                                echiquier[x, y + 1] = savePieceCaseRoiBlanc3
                                echiquier[x, y] = ['roi', 'blanc']
                            else :
                                echiquier[x, y + 1] = savePieceCaseRoiBlanc3
                                echiquier[x, y] = ['roi', 'blanc']
                                return False

                    if dansLEchiquier(x-1, y+1):
                        if echiquier[x-1, y+1] == ['vide', 'incolore'] or echiquier[x-1, y+1][1] == 'noir':
                            savePieceCaseRoiBlanc4 = echiquier[x - 1, y + 1]
                            echiquier[x - 1, y + 1] = ['roi', 'blanc']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiBlancEnEchec():
                                echiquier[x - 1, y + 1] = savePieceCaseRoiBlanc4
                                echiquier[x, y] = ['roi', 'blanc']
                            else :
                                echiquier[x - 1, y + 1] = savePieceCaseRoiBlanc4
                                echiquier[x, y] = ['roi', 'blanc']
                                return False

                    if dansLEchiquier(x-1, y):
                        if echiquier[x-1, y] == ['vide', 'incolore'] or echiquier[x-1, y][1] == 'noir':
                            savePieceCaseRoiBlanc5 = echiquier[x - 1, y]
                            echiquier[x - 1, y] = ['roi', 'blanc']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiBlancEnEchec():
                                echiquier[x - 1, y] = savePieceCaseRoiBlanc5
                                echiquier[x, y] = ['roi', 'blanc']
                            else :
                                echiquier[x - 1, y] = savePieceCaseRoiBlanc5
                                echiquier[x, y] = ['roi', 'blanc']
                                return False

                    if dansLEchiquier(x-1, y-1) :
                        if echiquier[x-1, y-1] == ['vide', 'incolore'] or echiquier[x-1, y-1][1] == 'noir':
                            savePieceCaseRoiBlanc6 = echiquier[x - 1, y - 1]
                            echiquier[x - 1, y - 1] = ['roi', 'blanc']
                            echiquier[x, y]=['vide', 'incolore']
                            if roiBlancEnEchec():
                                echiquier[x - 1, y - 1] = savePieceCaseRoiBlanc6
                                echiquier[x, y] = ['roi', 'blanc']
                            else :
                                echiquier[x - 1, y - 1] = savePieceCaseRoiBlanc6
                                echiquier[x, y] = ['roi', 'blanc']
                                return False

                    if dansLEchiquier(x, y-1):
                        if echiquier[x, y-1] == ['vide', 'incolore'] or echiquier[x, y-1][1] == 'noir':
                            savePieceCaseRoiBlanc7 = echiquier[x, y - 1]
                            echiquier[x, y - 1] = ['roi', 'blanc']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiBlancEnEchec():
                                echiquier[x, y - 1] = savePieceCaseRoiBlanc7
                                echiquier[x, y] = ['roi', 'blanc']
                            else :
                                echiquier[x, y - 1] = savePieceCaseRoiBlanc7
                                echiquier[x, y] = ['roi', 'blanc']
                                return False

                    if dansLEchiquier(x+1, y-1) :
                        if echiquier[x+1, y-1] == ['vide', 'incolore'] or echiquier[x+1, y-1][1] == 'noir':
                            savePieceCaseRoiBlanc8 = echiquier[x + 1 , y - 1]
                            echiquier[x + 1 , y - 1] = ['roi', 'blanc']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiBlancEnEchec():
                                echiquier[x + 1, y - 1] = savePieceCaseRoiBlanc8
                                echiquier[x, y] = ['roi', 'blanc']
                            else :
                                echiquier[x + 1, y - 1] = savePieceCaseRoiBlanc8
                                echiquier[x, y] = ['roi', 'blanc']
                                return False
        return True
    return False




def roiNoirEchecEtMat() :
    if roiNoirEnEchec() :
        for x in range(0, 8):
            for y in range(0, 8):

                if echiquier[x, y] == ['pion', 'noir']:

                    if dansLEchiquier(x, y-1) and echiquier[x, y - 1] == ['vide', 'incolore']:
                        savePieceCasePionNoir1 = echiquier[x, y - 1]
                        echiquier[x, y - 1] = ['pion', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec():
                            echiquier[x, y] = ['pion', 'noir']
                            echiquier[x, y - 1] = savePieceCasePionNoir1
                            return False
                        echiquier[x, y] = ['pion', 'noir']
                        echiquier[x, y - 1] = savePieceCasePionNoir1

                    if y == 6 and echiquier[x, y - 2] == ['vide', 'incolore'] :
                        savePieceCasePionNoir2 = echiquier[x, y - 2]
                        echiquier[x, y - 2] = ['pion', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec():
                            echiquier[x, y] = ['pion', 'noir']
                            echiquier[x, y - 2] = savePieceCasePionNoir2
                            return False
                        echiquier[x, y] = ['pion', 'noir']
                        echiquier[x, y - 2] = savePieceCasePionNoir2


                    if dansLEchiquier(x+1, y-1) and echiquier[x + 1, y - 1][1] == 'blanc':
                        savePieceCasePionNoir3 = echiquier[x + 1, y - 1]
                        echiquier[x + 1, y - 1] = ['pion', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec():
                            echiquier[x, y] = ['pion', 'noir']
                            echiquier[x + 1, y - 1] = savePieceCasePionNoir3
                            return False
                        echiquier[x, y] = ['pion', 'noir']
                        echiquier[x + 1, y - 1] = savePieceCasePionNoir3

                    if dansLEchiquier(x-1, y-1) and echiquier[x - 1, y - 1][1] == 'blanc':
                        savePieceCasePionNoir4 = echiquier[x - 1, y - 1]
                        echiquier[x - 1, y - 1] = ['pion', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec():
                            echiquier[x, y] = ['pion', 'noir']
                            echiquier[x - 1, y - 1] = savePieceCasePionNoir4
                            return False
                        echiquier[x, y] = ['pion', 'noir']
                        echiquier[x - 1, y - 1] = savePieceCasePionNoir4

                if echiquier[x, y] == ['tour', 'noir']:

                    nombreDeDeplacementSurLaDroiteTourNoir = 0
                    nombreDeDeplacementSurLaGaucheTourNoir = 0
                    nombreDeDeplacementVersLeBasTourNoir = 0
                    nombreDeDeplacementVersLeHautTourNoir = 0

                    while dansLEchiquier(x + nombreDeDeplacementSurLaDroiteTourNoir+1, y) and echiquier[x + nombreDeDeplacementSurLaDroiteTourNoir +1 , y][1] != 'blanc' and echiquier[x+nombreDeDeplacementSurLaDroiteTourNoir, y] != 'blanc' :
                        nombreDeDeplacementSurLaDroiteTourNoir +=1
                    for n in range (1, nombreDeDeplacementSurLaDroiteTourNoir+1) :
                        savePieceCaseTourNoir1 = echiquier[x + n, y]
                        echiquier[x + n, y] = ['tour', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x + n, y] = savePieceCaseTourNoir1
                            echiquier[x, y] = ['tour', 'noir']
                            return False
                        echiquier[x + n, y] = savePieceCaseTourNoir1
                        echiquier[x, y] = ['tour', 'noir']

                    while dansLEchiquier(x - nombreDeDeplacementSurLaGaucheTourNoir-1, y) and echiquier[x - nombreDeDeplacementSurLaGaucheTourNoir -1 , y][1] != 'blanc' and echiquier[x-nombreDeDeplacementSurLaGaucheTourNoir, y] != 'blanc' :
                        nombreDeDeplacementSurLaGaucheTourNoir +=1
                    for n in range (1, nombreDeDeplacementSurLaGaucheTourNoir+1) :
                        savePieceCaseTourNoir2 = echiquier[x - n, y]
                        echiquier[x - n, y] = ['tour', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x - n, y] = savePieceCaseTourNoir2
                            echiquier[x, y] = ['tour', 'noir']
                            return False
                        echiquier[x - n, y] = savePieceCaseTourNoir2
                        echiquier[x, y] = ['tour', 'noir']

                    while dansLEchiquier(x, y+nombreDeDeplacementVersLeBasTourNoir+1) and echiquier[x, y+nombreDeDeplacementVersLeBasTourNoir+1][1] != 'blanc' and echiquier[x, y+nombreDeDeplacementVersLeBasTourNoir] != 'blanc' :
                        nombreDeDeplacementVersLeBasTourNoir +=1
                    for n in range (1, nombreDeDeplacementVersLeBasTourNoir+1) :
                        savePieceCaseTourNoir3 = echiquier[x, y + n]
                        echiquier[x, y + n] = ['tour', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x, y + n] = savePieceCaseTourNoir3
                            echiquier[x, y] = ['tour', 'noir']
                            return False
                        echiquier[x, y + n] = savePieceCaseTourNoir3
                        echiquier[x, y] = ['tour', 'noir']

                    while dansLEchiquier(x, y-nombreDeDeplacementVersLeHautTourNoir-1) and echiquier[x, y-nombreDeDeplacementVersLeHautTourNoir-1][1] != 'blanc' and echiquier[x, y-nombreDeDeplacementVersLeHautTourNoir] != 'blanc' :
                        nombreDeDeplacementVersLeHautTourNoir +=1
                    for n in range (1, nombreDeDeplacementVersLeHautTourNoir+1) :
                        savePieceCaseTourNoir4 = echiquier[x, y - n]
                        echiquier[x, y - n] = ['tour', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x, y - n] = savePieceCaseTourNoir4
                            echiquier[x, y] = ['tour', 'noir']
                            return False
                        echiquier[x, y - n] = savePieceCaseTourNoir4
                        echiquier[x, y] = ['tour', 'noir']


                if echiquier[x, y] == ['fou', 'noir']:

                    nombreDeDeplacementEnBasADroiteFouNoir = 0
                    nombreDeDeplacementEnBasAGaucheFouNoir = 0
                    nombreDeDeplacementEnHautADroiteFouNoir = 0
                    nombreDeDeplacementEnHautAGaucheFouNoir = 0

                    while dansLEchiquier(x + nombreDeDeplacementEnBasADroiteFouNoir+1, y + nombreDeDeplacementEnBasADroiteFouNoir+1) and echiquier[x + nombreDeDeplacementEnBasADroiteFouNoir +1 , y+ nombreDeDeplacementEnBasADroiteFouNoir +1][1] != 'blanc' and echiquier[x+nombreDeDeplacementEnBasADroiteFouNoir, y + nombreDeDeplacementEnBasADroiteFouNoir] != 'blanc' :
                        nombreDeDeplacementEnBasADroiteFouNoir +=1
                    for n in range (1, nombreDeDeplacementEnBasADroiteFouNoir+1) :
                        savePieceCaseFouNoir1 = echiquier[x + n, y + n]
                        echiquier[x + n, y + n] = ['fou', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x + n, y + n] = savePieceCaseFouNoir1
                            echiquier[x, y] = ['fou', 'noir']
                            return False
                        echiquier[x + n, y + n] = savePieceCaseFouNoir1
                        echiquier[x, y] = ['fou', 'noir']

                    while dansLEchiquier(x - nombreDeDeplacementEnBasAGaucheFouNoir-1, y +nombreDeDeplacementEnBasAGaucheFouNoir+1) and echiquier[x - nombreDeDeplacementEnBasAGaucheFouNoir -1 , y + nombreDeDeplacementEnBasAGaucheFouNoir +1][1] != 'blanc' and echiquier[x-nombreDeDeplacementEnBasAGaucheFouNoir, y +nombreDeDeplacementEnBasAGaucheFouNoir] != 'blanc' :
                        nombreDeDeplacementEnBasAGaucheFouNoir +=1
                    for n in range (1, nombreDeDeplacementEnBasAGaucheFouNoir+1) :
                        savePieceCaseFouNoir2 = echiquier[x - n, y + n]
                        echiquier[x - n, y + n] = ['fou', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x - n, y + n] = savePieceCaseFouNoir2
                            echiquier[x, y] = ['fou', 'noir']
                            return False
                        echiquier[x - n, y + n] = savePieceCaseFouNoir2
                        echiquier[x, y] = ['fou', 'noir']

                    while dansLEchiquier(x+ nombreDeDeplacementEnHautADroiteFouNoir + 1, y - nombreDeDeplacementEnHautADroiteFouNoir -1) and echiquier[x + nombreDeDeplacementEnHautADroiteFouNoir +1, y - nombreDeDeplacementEnHautADroiteFouNoir - 1][1] != 'blanc' and echiquier[x + nombreDeDeplacementEnHautADroiteFouNoir, y - nombreDeDeplacementEnHautADroiteFouNoir] != 'blanc' :
                        nombreDeDeplacementEnHautADroiteFouNoir +=1
                    for n in range (1, nombreDeDeplacementEnHautADroiteFouNoir+1) :
                        savePieceCaseFouNoir3 = echiquier[x + n, y - n]
                        echiquier[x + n, y - n] = ['fou', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x + n, y - n] = savePieceCaseFouNoir3
                            echiquier[x, y] = ['fou', 'noir']
                            return False
                        echiquier[x + n, y - n] = savePieceCaseFouNoir3
                        echiquier[x, y] = ['fou', 'noir']

                    while dansLEchiquier(x - nombreDeDeplacementEnHautAGaucheFouNoir -1, y-nombreDeDeplacementEnHautAGaucheFouNoir-1) and echiquier[x- nombreDeDeplacementEnHautAGaucheFouNoir -1, y-nombreDeDeplacementEnHautAGaucheFouNoir-1][1] != 'blanc' and echiquier[x - nombreDeDeplacementEnHautAGaucheFouNoir, y-nombreDeDeplacementEnHautAGaucheFouNoir] != 'blanc' :
                        nombreDeDeplacementEnHautAGaucheFouNoir +=1
                    for n in range (1, nombreDeDeplacementEnHautAGaucheFouNoir+1) :
                        savePieceCaseFouNoir4 = echiquier[x - n, y - n]
                        echiquier[x - n, y - n] = ['fou', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x - n, y - n] = savePieceCaseFouNoir4
                            echiquier[x, y] = ['fou', 'noit']
                            return False
                        echiquier[x - n, y - n] = savePieceCaseFouNoir4
                        echiquier[x, y] = ['fou', 'noir']

                if echiquier[x, y] == ['cavalier', 'noir'] :

                    if dansLEchiquier(x + 2, y + 1) and echiquier[x+2, y+1][1] != 'noir':
                        savePieceCaseCavalierNoir1 = echiquier[x + 2, y + 1]
                        echiquier[x + 2, y + 1] = ['cavalier', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier [x + 2, y + 1]= savePieceCaseCavalierNoir1
                            echiquier[x, y] = ['cavalier', 'noir']
                            return False
                        echiquier[x + 2, y + 1] = savePieceCaseCavalierNoir1
                        echiquier[x, y] = ['cavalier', 'noir']

                    if dansLEchiquier(x + 1, y + 2) and echiquier[x+1, y+2][1] != 'noir':
                        savePieceCaseCavalierNoir2 = echiquier[x + 1, y + 2]
                        echiquier[x + 1, y + 2] = ['cavalier', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier [x + 1, y + 2]= savePieceCaseCavalierNoir2
                            echiquier[x, y] = ['cavalier', 'noir']
                            return False
                        echiquier[x + 1, y + 2] = savePieceCaseCavalierNoir2
                        echiquier[x, y] = ['cavalier', 'noir']

                    if dansLEchiquier(x - 1, y + 2) and echiquier[x-1, y+2][1] != 'noir':
                        savePieceCaseCavalierNoir3 = echiquier[x - 1, y + 2]
                        echiquier[x - 1, y + 2] = ['cavalier', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier [x - 1, y + 2]= savePieceCaseCavalierNoir3
                            echiquier[x, y] = ['cavalier', 'noir']
                            return False
                        echiquier[x - 1, y + 2] = savePieceCaseCavalierNoir3
                        echiquier[x, y] = ['cavalier', 'noir']

                    if dansLEchiquier(x - 2, y + 1) and echiquier[x-2, y+1][1] != 'noir':
                        savePieceCaseCavalierNoir4 = echiquier[x - 2, y + 1]
                        echiquier[x - 2, y + 1] = ['cavalier', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier [x - 2, y + 1]= savePieceCaseCavalierNoir4
                            echiquier[x, y] = ['cavalier', 'noir']
                            return False
                        echiquier[x - 2, y + 1] = savePieceCaseCavalierNoir4
                        echiquier[x, y] = ['cavalier', 'noir']

                    if dansLEchiquier(x - 2, y - 1) and echiquier[x-2, y-1][1] != 'noir':
                        savePieceCaseCavalierNoir5 = echiquier[x - 2, y - 1]
                        echiquier[x - 2, y - 1] = ['cavalier', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier [x - 2, y - 1]= savePieceCaseCavalierNoir5
                            echiquier[x, y] = ['cavalier', 'noir']
                            return False
                        echiquier[x - 2, y - 1] = savePieceCaseCavalierNoir5
                        echiquier[x, y] = ['cavalier', 'noir']

                    if dansLEchiquier(x - 1, y - 2) and echiquier[x-1, y-2][1] != 'noir':
                        savePieceCaseCavalierNoir6 = echiquier[x - 1, y - 2]
                        echiquier[x - 1, y - 2] = ['cavalier', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier [x - 1, y - 2]= savePieceCaseCavalierNoir6
                            echiquier[x, y] = ['cavalier', 'noir']
                            return False
                        echiquier[x - 1, y - 2] = savePieceCaseCavalierNoir6
                        echiquier[x, y] = ['cavalier', 'noir']

                    if dansLEchiquier(x + 1, y - 2) and echiquier[x+1, y-2][1] != 'noir':
                        savePieceCaseCavalierNoir7 = echiquier[x + 1, y - 2]
                        echiquier[x + 1, y - 2] = ['cavalier', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier [x + 1, y - 2]= savePieceCaseCavalierNoir7
                            echiquier[x, y] = ['cavalier', 'noir']
                            return False
                        echiquier[x + 1, y - 2] = savePieceCaseCavalierNoir7
                        echiquier[x, y] = ['cavalier', 'noir']

                    if dansLEchiquier(x + 2, y - 1) and echiquier[x+2, y-1][1] != 'noir':
                        savePieceCaseCavalierNoir8 = echiquier[x + 2, y - 1]
                        echiquier[x + 2, y - 1] = ['cavalier', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier [x + 2, y - 1]= savePieceCaseCavalierNoir8
                            echiquier[x, y] = ['cavalier', 'noir']
                            return False
                        echiquier[x + 2, y - 1] = savePieceCaseCavalierNoir8
                        echiquier[x, y] = ['cavalier', 'noir']



                if echiquier[x, y] == ['reine', 'noir']:

                    nombreDeDeplacementSurLaDroiteReineNoir = 0
                    nombreDeDeplacementSurLaGaucheReineNoir = 0
                    nombreDeDeplacementVersLeBasReineNoir = 0
                    nombreDeDeplacementVersLeHautReineNoir = 0
                    nombreDeDeplacementEnBasADroiteReineNoir = 0
                    nombreDeDeplacementEnBasAGaucheReineNoir = 0
                    nombreDeDeplacementEnHautADroiteReineNoir = 0
                    nombreDeDeplacementEnHautAGaucheReineNoir = 0

                    while dansLEchiquier(x + nombreDeDeplacementSurLaDroiteReineNoir+1, y) and echiquier[x + nombreDeDeplacementSurLaDroiteReineNoir +1 , y][1] != 'blanc' and echiquier[x+nombreDeDeplacementSurLaDroiteReineNoir, y] != 'blanc' :
                        nombreDeDeplacementSurLaDroiteReineNoir +=1
                    for n in range (1, nombreDeDeplacementSurLaDroiteReineNoir+1) :
                        savePieceCaseReineNoir1 = echiquier[x + n, y]
                        echiquier[x + n, y] = ['reine', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x + n, y] = savePieceCaseReineNoir1
                            echiquier[x, y] = ['reine', 'noir']
                            return False
                        echiquier[x + n, y] = savePieceCaseReineNoir1
                        echiquier[x, y] = ['reine', 'noir']

                    while dansLEchiquier(x - nombreDeDeplacementSurLaGaucheReineNoir-1, y) and echiquier[x - nombreDeDeplacementSurLaGaucheReineNoir -1 , y][1] != 'blanc' and echiquier[x-nombreDeDeplacementSurLaGaucheReineNoir, y] != 'blanc' :
                        nombreDeDeplacementSurLaGaucheReineNoir +=1
                    for n in range (1, nombreDeDeplacementSurLaGaucheReineNoir+1) :
                        savePieceCaseReineNoir2 = echiquier[x - n, y]
                        echiquier[x - n, y] = ['reine', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x - n, y] = savePieceCaseReineNoir2
                            echiquier[x, y] = ['reine', 'noir']
                            return False
                        echiquier[x - n, y] = savePieceCaseReineNoir2
                        echiquier[x, y] = ['reine', 'noir']

                    while dansLEchiquier(x, y+nombreDeDeplacementVersLeBasReineNoir+1) and echiquier[x, y+nombreDeDeplacementVersLeBasReineNoir+1][1] != 'blanc' and echiquier[x, y+nombreDeDeplacementVersLeBasReineNoir] != 'blanc' :
                        nombreDeDeplacementVersLeBasReineNoir +=1
                    for n in range (1, nombreDeDeplacementVersLeBasReineNoir+1) :
                        savePieceCaseReineNoir3 = echiquier[x, y + n]
                        echiquier[x, y + n] = ['reine', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x, y + n] = savePieceCaseReineNoir3
                            echiquier[x, y] = ['reine', 'noir']
                            return False
                        echiquier[x, y + n] = savePieceCaseReineNoir3
                        echiquier[x, y] = ['reine', 'noir']

                    while dansLEchiquier(x, y-nombreDeDeplacementVersLeHautReineNoir-1) and echiquier[x, y-nombreDeDeplacementVersLeHautReineNoir-1][1] != 'blanc' and echiquier[x, y-nombreDeDeplacementVersLeHautReineNoir] != 'blanc' :
                        nombreDeDeplacementVersLeHautReineNoir +=1
                    for n in range (1, nombreDeDeplacementVersLeHautReineNoir+1) :
                        savePieceCaseReineNoir4 = echiquier[x, y - n]
                        echiquier[x, y - n] = ['reine', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x, y - n] = savePieceCaseReineNoir4
                            echiquier[x, y] = ['reine', 'noir']
                            return False
                        echiquier[x, y - n] = savePieceCaseReineNoir4
                        echiquier[x, y] = ['reine', 'noir']

                    while dansLEchiquier(x + nombreDeDeplacementEnBasADroiteReineNoir+1, y + nombreDeDeplacementEnBasADroiteReineNoir+1) and echiquier[x + nombreDeDeplacementEnBasADroiteReineNoir +1 , y+ nombreDeDeplacementEnBasADroiteReineNoir +1][1] != 'blanc' and echiquier[x+nombreDeDeplacementEnBasADroiteReineNoir, y + nombreDeDeplacementEnBasADroiteReineNoir] != 'blanc' :
                        nombreDeDeplacementEnBasADroiteReineNoir +=1
                    for n in range (1, nombreDeDeplacementEnBasADroiteReineNoir+1) :
                        savePieceCaseReineNoir5 = echiquier[x + n, y + n]
                        echiquier[x + n, y + n] = ['reine', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x + n, y + n] = savePieceCaseReineNoir5
                            echiquier[x, y] = ['reine', 'noir']
                            return False
                        echiquier[x + n, y + n] = savePieceCaseReineNoir5
                        echiquier[x, y] = ['reine', 'noir']

                    while dansLEchiquier(x - nombreDeDeplacementEnBasAGaucheReineNoir-1, y +nombreDeDeplacementEnBasAGaucheReineNoir+1) and echiquier[x - nombreDeDeplacementEnBasAGaucheReineNoir -1 , y + nombreDeDeplacementEnBasAGaucheReineNoir +1][1] != 'blanc' and echiquier[x-nombreDeDeplacementEnBasAGaucheReineNoir, y +nombreDeDeplacementEnBasAGaucheReineNoir] != 'blanc' :
                        nombreDeDeplacementEnBasAGaucheReineNoir +=1
                    for n in range (1, nombreDeDeplacementEnBasAGaucheReineNoir+1) :
                        savePieceCaseReineNoir6 = echiquier[x - n, y + n]
                        echiquier[x - n, y + n] = ['reine', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x - n, y + n] = savePieceCaseReineNoir6
                            echiquier[x, y] = ['reine', 'noir']
                            return False
                        echiquier[x - n, y + n] = savePieceCaseReineNoir6
                        echiquier[x, y] = ['reine', 'noir']

                    while dansLEchiquier(x+ nombreDeDeplacementEnHautADroiteReineNoir + 1, y - nombreDeDeplacementEnHautADroiteReineNoir -1) and echiquier[x + nombreDeDeplacementEnHautADroiteReineNoir +1, y - nombreDeDeplacementEnHautADroiteReineNoir - 1][1] != 'blanc' and echiquier[x + nombreDeDeplacementEnHautADroiteReineNoir, y - nombreDeDeplacementEnHautADroiteReineNoir] != 'blanc' :
                        nombreDeDeplacementEnHautADroiteReineNoir +=1
                    for n in range (1, nombreDeDeplacementEnHautADroiteReineNoir+1) :
                        savePieceCaseReineNoir7 = echiquier[x + n, y - n]
                        echiquier[x + n, y - n] = ['reine', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x + n, y - n] = savePieceCaseReineNoir7
                            echiquier[x, y] = ['reine', 'noir']
                            return False
                        echiquier[x + n, y - n] = savePieceCaseReineNoir7
                        echiquier[x, y] = ['reine', 'noir']

                    while dansLEchiquier(x - nombreDeDeplacementEnHautAGaucheReineNoir -1, y-nombreDeDeplacementEnHautAGaucheReineNoir-1) and echiquier[x- nombreDeDeplacementEnHautAGaucheReineNoir -1, y-nombreDeDeplacementEnHautAGaucheReineNoir-1][1] != 'blanc' and echiquier[x - nombreDeDeplacementEnHautAGaucheReineNoir, y-nombreDeDeplacementEnHautAGaucheReineNoir] != 'blanc' :
                        nombreDeDeplacementEnHautAGaucheReineNoir +=1
                    for n in range (1, nombreDeDeplacementEnHautAGaucheReineNoir+1) :
                        savePieceCaseReineNoir8 = echiquier[x - n, y - n]
                        echiquier[x - n, y - n] = ['reine', 'noir']
                        echiquier[x, y] = ['vide', 'incolore']
                        if not roiNoirEnEchec() :
                            echiquier[x - n, y - n] = savePieceCaseReineNoir8
                            echiquier[x, y] = ['reine', 'noir']
                            return False
                        echiquier[x - n, y - n] = savePieceCaseReineNoir8
                        echiquier[x, y] = ['reine', 'noir']

                if echiquier[x, y] == ['roi', 'noir']:
                    if dansLEchiquier(x+1, y):
                        if echiquier[x+1, y][1] == ['vide', 'incolore'] or echiquier[x+1, y+1][1] == 'blanc':
                            savePieceCaseRoiNoir1 = echiquier[x + 1, y]
                            echiquier[x + 1, y] = ['roi', 'noir']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiNoirEnEchec() :
                                echiquier[x + 1, y] = savePieceCaseRoiNoir1
                                echiquier[x, y] = ['roi', 'noir']
                            else:
                                echiquier[x + 1, y] = savePieceCaseRoiNoir1
                                echiquier[x, y] = ['roi', 'noir']
                                return False

                    if dansLEchiquier(x+1, y+1) :
                        if echiquier[x+1, y+1] == ['vide', 'incolore'] or echiquier[x+1, y+1][1] == 'blanc':
                            savePieceCaseRoiNoir2 = echiquier[x + 1, y + 1]
                            echiquier[x + 1, y + 1] = ['roi', 'noir']
                            echiquier [x, y] = ['vide', 'incolore']
                            if roiNoirEnEchec():
                                echiquier[x + 1, y + 1] = savePieceCaseRoiNoir2
                                echiquier[x, y] = ['roi', 'noir']
                            else :
                                echiquier[x + 1, y + 1] = savePieceCaseRoiNoir2
                                echiquier[x, y] = ['roi', 'noir']
                                return False


                    if  dansLEchiquier(x, y+1) :
                        if echiquier[x, y+1] == ['vide', 'incolore'] or echiquier[x, y+1][1] == 'blanc':
                            savePieceCaseRoiNoir3 = echiquier[x, y + 1]
                            echiquier[x, y + 1] = ['roi', 'noir']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiNoirEnEchec():
                                echiquier[x, y + 1] = savePieceCaseRoiNoir3
                                echiquier[x, y] = ['roi', 'noir']
                            else :
                                echiquier[x, y + 1] = savePieceCaseRoiNoir3
                                echiquier[x, y] = ['roi', 'noir']
                                return False

                    if dansLEchiquier(x-1, y+1):
                        if echiquier[x-1, y+1] == ['vide', 'incolore'] or echiquier[x-1, y+1][1] == 'blanc':
                            savePieceCaseRoiNoir4 = echiquier[x - 1, y + 1]
                            echiquier[x - 1, y + 1] = ['roi', 'noir']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiNoirEnEchec():
                                echiquier[x - 1, y + 1] = savePieceCaseRoiNoir4
                                echiquier[x, y] = ['roi', 'noir']
                            else :
                                echiquier[x - 1, y + 1] = savePieceCaseRoiNoir4
                                echiquier[x, y] = ['roi', 'noir']
                                return False

                    if dansLEchiquier(x-1, y):
                        if echiquier[x-1, y] == ['vide', 'incolore'] or echiquier[x-1, y][1] == 'blanc':
                            savePieceCaseRoiNoir5 = echiquier[x - 1, y]
                            echiquier[x - 1, y] = ['roi', 'noir']
                            echiquier[x, y]= ['vide', 'incolore']
                            if roiNoirEnEchec():
                                echiquier[x - 1, y] = savePieceCaseRoiNoir5
                                echiquier[x, y] = ['roi', 'noir']
                            else :
                                echiquier[x - 1, y] = savePieceCaseRoiNoir5
                                echiquier[x, y] = ['roi', 'noir']
                                return False

                    if dansLEchiquier(x-1, y-1) :
                        if echiquier[x-1, y-1] == ['vide', 'incolore'] or echiquier[x-1, y-1][1] == 'blanc':
                            savePieceCaseRoiNoir6 = echiquier[x - 1, y - 1]
                            echiquier[x - 1, y - 1] = ['roi', 'noir']
                            echiquier[x, y]=['vide', 'incolore']
                            if roiNoirEnEchec():
                                echiquier[x - 1, y - 1] = savePieceCaseRoiNoir6
                                echiquier[x, y] = ['roi', 'noir']
                            else :
                                echiquier[x - 1, y - 1] = savePieceCaseRoiNoir6
                                echiquier[x, y] = ['roi', 'noir']
                                return False

                    if dansLEchiquier(x, y-1):
                        if echiquier[x, y-1] == ['vide', 'incolore'] or echiquier[x, y-1][1] == 'blanc':
                            savePieceCaseRoiNoir7 = echiquier[x, y - 1]
                            echiquier[x, y - 1] = ['roi', 'noir']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiNoirEnEchec():
                                echiquier[x, y - 1] = savePieceCaseRoiNoir7
                                echiquier[x, y] = ['roi', 'noir']
                            else :
                                echiquier[x, y - 1] = savePieceCaseRoiNoir7
                                echiquier[x, y] = ['roi', 'noir']
                                return False

                    if dansLEchiquier(x+1, y-1) :
                        if echiquier[x+1, y-1] == ['vide', 'incolore'] or echiquier[x+1, y-1][1] == 'blanc':
                            savePieceCaseRoiNoir8 = echiquier[x + 1 , y - 1]
                            echiquier[x + 1 , y - 1] = ['roi', 'noir']
                            echiquier[x, y] = ['vide', 'incolore']
                            if roiNoirEnEchec():
                                echiquier[x + 1, y - 1] = savePieceCaseRoiNoir8
                                echiquier[x, y] = ['roi', 'noir']
                            else :
                                echiquier[x + 1, y - 1] = savePieceCaseRoiNoir8
                                echiquier[x, y] = ['roi', 'noir']
                                return False

        return True
    return False