__author__ = 'Emanuel'

import mraa
import time

# Set port numbers
bt_Up = mraa.Gpio(45)
bt_Down = mraa.Gpio(47)
# bt_Left = mraa.Gpio(13)
# bt_Right = mraa.Gpio(13)
# bt_Enter = mraa.Gpio(13)

# Set port direction
bt_Up.dir(mraa.DIR_IN)
bt_Down.dir(mraa.DIR_IN)
# bt_Left.dir(mraa.DIR_IN)
# bt_Right.dir(mraa.DIR_IN)
# bt_Enter.dir(mraa.DIR_IN)

# menu_opt = [""]


def show_menu1():
    print("*** Sensor Menu ***  \n "
          "> Add Item \n "
          "  View Item")


def show_menu2():
    print("*** Sensor Menu ***  \n "
          "  Add Item \n "
          "> View Item")


def main():
    screen = 0;
    old = 1
    while True:
        if bt_Up.read():
            screen -= 1
            if screen < 0:
                screen = 0
        if bt_Down.read():
            screen += 1
            if screen > 1:
                screen = 1
        if screen != old:
            if screen == 0:
                show_menu1()
            elif screen == 1:
                show_menu2()
            old = screen


if __name__ == '__main__':
    main()
