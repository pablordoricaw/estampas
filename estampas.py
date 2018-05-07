import re, os
import argparse # argument parser for the arguments

def setupArgParse():
    parser = argparse.ArgumentParser()
    parser.add_argument("faltantes", help="txt file with missing \"estampas\"")
    parser.add_argument("repetidas", help="txt file with repeated \"estampas\"")
    return parser

def readEstampas(estampas_file):
    estampas = []
    try:
        with open(estampas_file, 'r') as f:
            for line in f:
                for estampa in re.findall(r"\d+", line):
                    estampas.append(int(estampa))
    except OSError:
        print("Cannot open", estampas_file)
    return estampas

def trade(faltantes, repetidas):
    cambiables = []
    for estampa in repetidas:
        if estampa in faltantes:
            cambiables.append(estampa)
    printEstampas(cambiables)

def printEstampas(estampas):
    _, columns = os.popen('stty size', 'r').read().split()
    l = 0
    for i in range(0, len(estampas), int(int(columns)/8)):

        for _ in range(0, int(int(columns)/8)):
            if not (i + int(int(columns)/8) > len(estampas)):
                print("|¯¯¯¯¯|", end=" ")

        if (i + int(int(columns)/8) > len(estampas)):
            for j in range(i, len(estampas)):
                if(estampas[j]):
                    l+=1
                    print("|¯¯¯¯¯|", end=" ")
        print()

        for _ in range(0, int(int(columns)/8)):
            if(i < len(estampas)):
                if(3 == len(str(estampas[i]))):
                    print("| " + str(estampas[i]) + " |" , end=" ")
                if(2 == len(str(estampas[i]))):
                    print("|  " + str(estampas[i]) + " |", end=" ")
                if(1 == len(str(estampas[i]))):
                    print("|  " + str(estampas[i]) + "  |" , end=" ")
                i+=1
        print()

        for _ in range(0, int(int(columns)/8)):
            if(i < len(estampas)):
                print("|_____|", end=" ")

        if (i + int(int(columns)/8) > len(estampas)):
            for j in range(0, l):
                if(estampas[j]):
                    print("|_____|", end=" ")
        print("\n")

def main():
    parser = setupArgParse()
    args = parser.parse_args()
    trade(readEstampas(args.faltantes), readEstampas(args.repetidas))
    
if __name__ == '__main__':
    main()