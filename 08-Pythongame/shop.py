import os
import operator
import shutil
import locale
import slot


class bcolors:
    HEADER = '\033[95m'
    RED = '\033[93m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

shop = False
player_balance = 0
item_list = [""]
columns = shutil.get_terminal_size().columns
line = "=" * (columns)
credits = bcolors.BOLD + "Created by " + \
    bcolors.ENDC + "Marcell Miso & Gabor Varga | © 2016"


shop_items = {
    "Chocolate": 1,
    "Coffee": 2,
    "Sandwitch": 3,
    "Beer": 5,
    "Wine": 10,
    "Cuban cigar": 30,
    "Souvenir": 50,
    "Shoes": 100,
    "Whisky": 200,
    "Sunglasses": 400,
    "Smart phone": 600,
    "9mm pistol": 800,
    "Tattoo": 1000,
    "Plastic woman": 2000,
    "Gamer notebook": 5000,
    "Rolex watch": 10000,
    "Cosmetic surgery": 50000,
    "Porsche": 100000,
    "Yacht": 500000,
    "Mansion": 1000000
}


def give_data(balance, items):
    global player_balance
    global item_list
    player_balance = balance
    item_list = items

    start()


def check_for_bought(item):
    for i in item_list:
        if i == item:
            return True
    return False


def form_int(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))


def getchar():
    # Returns a single character from standard input
    import tty
    import termios
    import sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

selected = 0


def draw_shop(action="none", message=""):
    global selected
    global player_balance
    global shop

    os.system('clear')
    print("*" * columns)
    print(bcolors.BOLD + "| Balance: $" + form_int(player_balance) +
          " | Press (B) to back" +
          " | Press (Q) to quit game |")
    print("*" * columns)

    print("\n" + "(W/D) Navigate, (ENTER) Buy")

    sorted_shop_items = sorted(shop_items.items(), key=operator.itemgetter(1))

    if action == "up":
        if selected > 0:
            selected = selected - 1
    elif action == "down":
        if selected < len(sorted_shop_items) - 1:
            selected = selected + 1
    elif action == "mark":
        if check_for_bought(sorted_shop_items[selected][0]) == False:
            if player_balance >= sorted_shop_items[selected][1]:
                item_list.append(sorted_shop_items[selected][0])
                player_balance = player_balance - \
                    sorted_shop_items[selected][1]
                draw_shop("", "Succesfully bought " +
                          sorted_shop_items[selected][0] + "!")
                return
            else:
                draw_shop("", "You dont have enough money!")
                return
        else:
            draw_shop("", "You already have this item!")
            return

    for i in range(0, len(sorted_shop_items)):
        mark = " "
        for x in item_list:
            if sorted_shop_items[i][0] == x:
                mark = "X"

        loc_selected = "    "
        if selected == i:
            loc_selected = "->  "
        spc = 30 - (len(
            form_int(sorted_shop_items[i][1])) + len(sorted_shop_items[i][0]))
        print(loc_selected + "[" + mark + "] " + sorted_shop_items[i][0] + "." * spc + "$" + form_int(sorted_shop_items[
            i][1]))
    print("\n")
    print(message)

    print(line.center(columns))
    print(credits.center(columns))
    print("\n")

    if len(item_list) == len(sorted_shop_items):
        os.system('clear')
        print("Congratulations! You bought everything on the Black Market!")
        print("\n" * 3)
        print(
            "$$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\  $$$$$$\  $$\   $$\       $$\ ")
        print(
            "\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |$$  __$$\ $$$\  $$ |      $$ |")
        print(
            " \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |$$ /  $$ |$$$$\ $$ |      $$ |")
        print(
            "  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |$$ |  $$ |$$ $$\$$ |      $$ |")
        print(
            "   \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |$$ |  $$ |$$ \$$$$ |      \__|")
        print(
            "    $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$ |  $$ |$$ |\$$$ |          ")
        print(
            "    $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ | $$$$$$  |$$ | \$$ |      $$\ ")
        print(
            "    \__|     \______/  \______/       \__/     \__| \______/ \__|  \__|      \__|")
        exit()

    return selected


def start():
    shop = True
    draw_shop()
    while shop == True:
        ch = getchar()
        if ch == "w":
            draw_shop("up")
        if ch == "s":
            draw_shop("down")
        if ch == "\r":
            draw_shop("mark")
        if ch == "b":
            shop = False
            slot.get_data(player_balance, item_list)
        if ch == "q":
            exit()
