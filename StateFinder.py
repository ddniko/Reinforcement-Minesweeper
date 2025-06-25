#asdasdasda
#test program

import pyautogui as gui
import PIL
from PIL import Image
import cv2 as cv
import numpy as np
import time

#Noter til fremtidig udvikling:
#Vi kan måske bruge gui.center() metoden til at finde middlepxiel, i stedet for det jeg har lavet
#Med center() metoden kan man bruge center[0] eller center.x
#Man kan i stedet for arrCoordinates[0][0] og skrive arrCoordinates[0].left: kan gøre koden nemmere at læse

#Noter for at få ting til at fungere:
#Websiden skal være i fuldskærm og 100% zoom
#Tingene på websiden må ikke flyttes rundt, Min bærbar er ikke stor nok til dette

#https://minesweeper.one/

rows, cols = (16, 16)
arrCoordinates = [0 for i in range(256)]
arrBoard = [[0 for i in range(cols)] for j in range(rows)]
arrColors = [(189,189,189),(0,0,255),(12,127,12),(255,0,0),(0,0,123),(123,0,0),(0,123,123)]




def InitializeBoard():
    Minesweeper = gui.locateOnScreen("minesweeper.png", confidence=0.9)
    i = 0
    for pos in gui.locateAllOnScreen("field.png", grayscale=True, region=(Minesweeper), confidence=0.9):
        columb = i / cols
        arrCoordinates[i] = pos
        arrBoard[int(columb)][i % rows] = "O"
        i = i + 1
    global ColorBlank
    ColorBlank = GetColor(arrCoordinates[0])

    #Debugging
    #print(ColorBlank == arrColors[0])
    #print(ColorBlank)
    #print(arrColors[0])
    #print(GetMiddlePixel(arrCoordinatesOne[0]))


def UpdateBoard():
    print("New Board loading")
    i = 0
    for x in arrCoordinates:
        columb = i / cols
        #if GetColor(arrCoordinates[i]) != ColorBlank: #Gammel kode
            #arrBoard[int(columb)][i % rows] = 0

        if GetColor(arrCoordinates[i]) != ColorBlank: #Tjekker for om det er en unknown field
            try: #Hvis den finder en farve som ikke er i arrColors, crasher programmet ikke
                arrBoard[int(columb)][i % rows] = arrColors.index(GetColor(GetMiddlePixel(arrCoordinates[i]))) #Tager farven af midterste pixel og finde hvilket index det har i array'et af farver
            except: #Hvis der er en farve som ikke er i arrColors kører den det her
                print("Error another color was found")

        #Mulig løsning som også inkludere en tolerance, så websiden ikke er ligeså unreliable, men koden er også langsommere
        #for x in arrColors:
            #if gui.pixelMatchesColor(GetMiddlePixel(arrCoordinates[i])[0],GetMiddlePixel(arrCoordinates[i])[1], x, tolerance=10):
                #arrBoard[int(columb)][i % rows] = arrColors.index(x)

        i = i + 1
    GetBoard()



    #Debugging
    #print(GetColor(GetMiddlePixel(arrCoordinatesOne[1])))
    #FindAllColors()


def GetColor(pos):
    return gui.pixel(int(pos[0]), int(pos[1]))


def GetMiddlePixel(pos):
    return [pos[0]+(pos[2]/2), pos[1]+(pos[3]/2)]

def GetBoard():
    for row in arrBoard:
        print(row)

def FindAllColors(): #Debugging - finding colors of all numbers
    for x in arrCoordinates:
        color = GetColor(GetMiddlePixel(x))
        if color != (189,189,189):
            print(color)