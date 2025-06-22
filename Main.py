import StateFinder
import keyboard

StateFinder.InitializeBoard()
StateFinder.GetBoard()
while True:
    if keyboard.is_pressed("space"):
        StateFinder.UpdateBoard()
