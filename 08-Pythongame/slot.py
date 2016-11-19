#KOMMENT2
import shutil
import tty
import sys
import termios
import os
import random
import curses
import time

started = False
#GLOBAL
lockShow = False
locksIndex = 0
message = "NONE"
firstSpin = False
minBet = 2
maxBet = 100
playerBalance = 50
playerBet = 2

class bcolors:
    HEADER = '\033[95m'
    RED = '\033[93m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

slots = ["$", "💙", "♣", "⌛", "⧫", "❼", "●", "?"]
columns = shutil.get_terminal_size().columns
wins = [0, 0, 0]
icon1 = 7
icon2 = 7
icon3 = 7

def startScreen():
    os.system('clear')
    print("     _____ _     _____ _____  ___  ___  ___  _____  _   _ _____ _   _  _____      ") 
    print("    /  ___| |   |  _  |_   _| |  \/  | / _ \/  __ \| | | |_   _| \ | ||  ___|      ")
    print("    \ `--.| |   | | | | | |   | .  . |/ /_\ \ /  \/| |_| | | | |  \| || |__        ")
    print("     `--. \ |   | | | | | |   | |\/| ||  _  | |    |  _  | | | | . ` ||  __|       ")
    print("    /\__/ / |___\ \_/ / | |   | |  | || | | | \__/\| | | |_| |_| |\  || |___       ")
    print("    \____/\_____/\___/  \_/   \_|  |_/\_| |_/\____/\_| |_/\___/\_| \_/\____/       ")
    print("                                                                                   ")
    print("                                                                                   ")
    print("  _                 _            _   _     _____           _                __ __  ")
    print(" | |               | |          | | | |   /  __ \         | |              / / \ \ ")
    print(" | |__  _   _    __| | __ _ _ __| |_| |__ | /  \/ ___   __| | ___ _ __ ___| |   | |")
    print(" | '_ \| | | |  / _` |/ _` | '__| __| '_ \| |    / _ \ / _` |/ _ \ '__/ __| |   | |")
    print(" | |_) | |_| | | (_| | (_| | |  | |_| | | | \__/\ (_) | (_| |  __/ |  \__ \ |   | |")
    print(" |_.__/ \__, |  \__,_|\__,_|_|   \__|_| |_|\____/\___/ \__,_|\___|_|  |___/ |   | |")
    print("         __/ |                                                             \_\ /_/ ")
    print("        |___/                                                                      ")
    print("")
    print("Press (K) to start.")
startScreen()

def lockPressL():
    global lockShow
    global locksIndex
    if lockShow == False:
        draw(slots[icon1], slots[icon2], slots[icon3], 4, True)
        lockShow = True
    else:
        draw(slots[icon1], slots[icon2], slots[icon3])
        lockShow = False
    if locksIndex > 0:
        lockShow = False
        locksIndex = 0
        draw(slots[icon1], slots[icon2], slots[icon3])

def lock(index):
    global lockShow
    global locksIndex
    if lockShow == True:
        if index == 1:
            locksIndex = 1
            draw(slots[icon1], slots[icon2], slots[icon3], 4)
        elif index == 2:
            locksIndex = 2
            draw(slots[icon1], slots[icon2], slots[icon3], 4)
        elif index == 3:
            locksIndex = 3
            draw(slots[icon1], slots[icon2], slots[icon3], 4)

def printRules():    
    print("\n"*4)
    print("R U L E S".center(columns))
    print("╔═════╦═════════════╦═════════════╦═════════════╗".center(columns))
    print("║     ║  1x symbol  ║  2x symbol  ║  3x symbol  ║".center(columns))
    print("╠═════╬═════════════╬═════════════╬═════════════╣".center(columns))
    print(bcolors.BOLD + "║  $  ║      -      ║     3.0     ║     5.0     ║".center(columns))
    print(bcolors.BOLD + "║  ⌛  ║      -      ║     3.1     ║     5.1     ║".center(columns))
    print(bcolors.BOLD + "║  ♣  ║      -      ║     3.2     ║     5.2     ║".center(columns))
    print(bcolors.BOLD + "║  ⧫  ║      -      ║     3.3     ║     5.3     ║".center(columns))
    print(bcolors.BOLD + "║  ●  ║      -      ║     3.4     ║     5.4     ║".center(columns))
    print(bcolors.BOLD + "║  💙  ║      -      ║     3.5     ║     5.5     ║".center(columns))
    print(bcolors.BOLD + "║  ❼  ║      -      ║     4.0     ║     7.0     ║".center(columns))
    print("╚═════╩═════════════╩═════════════╩═════════════╝".center(columns))
    print("\n"*3)

def lose():
    os.system('clear')
    columns = shutil.get_terminal_size().columns
    print(bcolors.BOLD + "TÁJÉKOZTATÁS".center(columns))
    print(bcolors.ENDC + "Tájékoztatjuk a felhasználót, hogy a jelen honlapon közzétett tartalom, mint elektronikus hírközlő hálózat útján közzétett adat ideiglenes hozzáférhetetlenné tételét a Nemzeti Adó- és Vámhivatal 3056819105 számú határozatával, 365 napos időtartamra elrendelte. Az ideiglenes hozzáférhetetlenné tétel elrendelésére tiltott szerencsejáték szervezés megvalósítása miatt került sor. Az ideiglenes hozzáférhetetlenné tétel elrendelésének jogalapja a szerencsejáték szervezéséről szóló 1991. évi XXXIV. törvény 2. § (2) bekezdése, 37. § 14. pontja, illetve 36/G. § (1) bekezdése.")
    print("\n"*25)
    exit()

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

def draw(i1, i2, i3, delspc = 5, locks = False):
    os.system('clear')
    print("*"*columns)
    print(bcolors.BOLD + "| Balance: $" + str(format(playerBalance, ".2f")) +
            " | Bet: $" + str(format(playerBet, ".2f")) +
            " | Press (Q) to quit |")
    print("*"*columns)
    print("\n"*delspc)
    if locks == True:
        print("(1)     (2)     (3)".center(columns))
    
    if locksIndex == 1:
        print("🔒                ".center(columns))
    if locksIndex == 2:
        print("🔒".center(columns))
    if locksIndex == 3:
        print("                🔒".center(columns))
    global message
    if message != "NONE":
        print(message.center(columns))
        
    slotsLine = bcolors.HEADER + "##   " + str(i1)  + "   #   " + str(i2) + "   #   " + str(i3) + "   ##"
    slotsKeys = bcolors.ENDC + bcolors.BOLD + "       Keys: " + bcolors.ENDC + "(Space)Spin (L)Lock (G/B)Change bet"
    line = "="*(columns)
    credits = bcolors.BOLD + "Made by: " + bcolors.ENDC + "Marcell Miso & Gabor Varga | © 2016"
    print(bcolors.HEADER + "###########################".center(columns))
    print(bcolors.HEADER + "##       #       #       ##".center(columns))
    print("  " + slotsLine.center(columns))
    print(bcolors.HEADER + "##       #       #       ##".center(columns))
    print(bcolors.HEADER + "###########################".center(columns))
    print(slotsKeys.center(columns))
    
    printRules()
    print(line.center(columns))
    print(credits.center(columns))

def win(id):
    global message
    tmpBalance = 0
    if id == 0:
        tmpBalance = playerBet * 3
    elif id == 1:
        tmpBalance = playerBet * 3.5
    elif id == 2:
        tmpBalance = playerBet * 3.2
    elif id == 3:
        tmpBalance = playerBet * 3.1
    elif id == 4:
        tmpBalance = playerBet * 3.3
    elif id == 5:
        tmpBalance = playerBet * 4
    elif id == 6:
        tmpBalance = playerBet * 3.4
    
    msgBalance = str(format(tmpBalance, ".2f"))
    message = "   " + bcolors.RED + "      Win: $" + msgBalance + bcolors.ENDC
    return tmpBalance

def bigWin(id):
    global message
    tmpBalance = 0
    if id == 0:
        tmpBalance = playerBet * 5
    elif id == 1:
        tmpBalance = playerBet * 5.5
    elif id == 2:
        tmpBalance = playerBet * 5.2
    elif id == 3:
        tmpBalance = playerBet * 5.1
    elif id == 4:
        tmpBalance = playerBet * 5.3
    elif id == 5:
        tmpBalance = playerBet * 7
    elif id == 6:
        tmpBalance = playerBet * 5.4
    
    msgBalance = str(format(tmpBalance, ".2f"))
    message = "   " + bcolors.RED + "      !!! BIG WIN: $" + msgBalance + "!!!" + bcolors.ENDC
    return tmpBalance

def checkForWins():
    tmpBalance = 0
    if wins[0] == wins[1] and wins[1] == wins[2]:
        tmpBalance = bigWin(wins[1])
    elif wins[0] == wins[1] or wins[1] == wins[2]:
        tmpBalance = win(wins[1])
    else:
        return 0
    return tmpBalance

while True:
    if playerBalance <= minBet:
        lose()
    ch = getchar()
    if ch == "q":
        exit()
    elif ch == "k":
        if started == False:
            started = True
            draw("?", "?", "?")
    elif ch == "g":
        if playerBet < maxBet and playerBet + 2 <= playerBalance:
            playerBet = playerBet + 2
            draw(slots[icon1], slots[icon2], slots[icon3])
    elif ch == "b":
        if playerBet > minBet:
            playerBet = playerBet - 2
            draw(slots[icon1], slots[icon2], slots[icon3])
    elif ch == "l":
        if started == True:
            if firstSpin == True:
                lockPressL()
    elif ch == "1":
        if started == True:
            lock(1)
    elif ch == "2":
        if started == True:
            lock(2)
    elif ch == "3":
        if started == True:    
            lock(3)
    elif ch == " ":
        if firstSpin == False:
            firstSpin = True
        message = ""
        if started == True:
            playerBalance = playerBalance - playerBet
            if playerBet > playerBalance:
                playerBet = playerBalance
            for i in range(20):
                time.sleep(0.1)
                os.system('clear')
                if locksIndex != 1:
                    icon1 = random.randint(0, 6)
                if locksIndex != 2:
                    icon2 = random.randint(0, 6)
                if locksIndex != 3:
                    icon3 = random.randint(0, 6)
                if locksIndex > 0:
                    draw(slots[icon1], slots[icon2], slots[icon3], 4)
                else:
                    draw(slots[icon1], slots[icon2], slots[icon3])
            wins[0] = icon1
            wins[1] = icon2
            wins[2] = icon3
            lockShow = False
            locksIndex = 0
            draw(slots[icon1], slots[icon2], slots[icon3])
            if checkForWins() > 0:
                playerBalance = playerBalance + checkForWins()
                draw(slots[icon1], slots[icon2], slots[icon3])
#KOMMENT-Gabi