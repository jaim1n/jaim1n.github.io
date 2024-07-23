import os
from colorama import Fore, Style
import time
import requests

def main(message, seconds):
    clear_bubble_text()
    bubble_message = bubble_text(message)
    print(bubble_message, end="\r")
    time.sleep(seconds)
    move_cursor_up(len(bubble_message.split('\n')))

def loading():
    for i in range(3):
        main(f"         Bear with me here {Fore.MAGENTA}<3{Style.RESET_ALL}." + "." * i, 1)

def btc_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = response.json()
    price = result["bpi"]["USD"]["rate_float"]
    return price

def bubble_text(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    bubble_width = max_length + 4
    bubble = []
    bubble.append("  " + "_" * bubble_width)
    for line in lines:
        bubble.append(" / " + line.ljust(max_length) + " \\")
    bubble.append(" \\_" + "_" * max_length + "_/")
    return "\n".join(bubble)

def clear_bubble_text():
    global previous_bubble_lines
    move_cursor_up(previous_bubble_lines)
    for _ in range(previous_bubble_lines):
        print(" " * 80)
    move_cursor_up(previous_bubble_lines)

def move_cursor_up(lines):
    print(f"\033[{lines}A", end="")

os.system('clear')

print(fr"""




                         {Style.RESET_ALL}\{Fore.RED}          ⠀ ⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠶⣄⢀⣠⣤⠴⢦⡀
                          {Style.RESET_ALL}\{Fore.RED}          ⠀⠀⠀⢠⡿⠉⠉⠉⠛⠶⠶⠖⠒⠒⣾⠋⠀⢀⣀⣙⣯⡁⠀⠀⠀⣿
                           {Style.RESET_ALL}\{Fore.RED}         ⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢯⣼⠋⠉⠙⢶⠞⠛⠻⣆
                            {Style.RESET_ALL}\{Fore.RED}        ⠀⠀⠀⢸⣧⠆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣤⡤⢿⡀⠀⢀⣼⣷⠀⠀⣽
                             {Style.RESET_ALL}\{Fore.RED}       ⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢏⡉⠁⣠⡾⣇
                              {Style.RESET_ALL}\{Fore.RED}      ⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⢻⡀
                               {Style.RESET_ALL}\{Fore.RED}     ⣀⣠⣼⣧⣤⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠐⠖⢻⡟⠓⠒
                                {Style.RESET_ALL}\_{Fore.RED}   ⠀⠀⠈⣷⣀⡀⠀⠘⠿⠇⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠲⣾⠦⢤
                                     ⠀⠀⠋⠙⣧⣀⡀⠀⠀⠀⠀⠀⠀⠘⠦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢤⣼⣏⠀⠀⠀
                                     ⠀⠀⢀⠴⠚⠻⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠉⠉⠓
                                     ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠶⠶⠶⣶⣤⣴⡶⠶⠶⠟⠛⠉
{Style.RESET_ALL}""")

move_cursor_up(20)

previous_bubble_lines = 0

current_price = btc_price()

main("Hello, world! I'm Weather Kitty, your personal weather assistant!", 4)
previous_bubble_lines = 5
loading()
clear_bubble_text()
print(bubble_text("OK! I'm all set up. What's your name?"))

while True:
    name = input("Enter name: ").strip()
    move_cursor_up(5)
    previous_bubble_lines = 5
    if name.isalpha():
        break
    else:
        time.sleep(0.5)
        clear_bubble_text()
        print(bubble_text("I don't think that's right. What's your name?"))

time.sleep(0.5)
main(f"Nice to meet you, {name}, what a beautiful name!", 2)
previous_bubble_lines = 5
main("Now let's see...", 2)
previous_bubble_lines = 5
main("Okay, no storms...", 2)
previous_bubble_lines = 5
main("No heavy winds...", 2)
previous_bubble_lines = 5
main("Weather conditions seem to be normal!", 3)
previous_bubble_lines = 5
main(f"By the way, did you know that the current price of a Bitcoin is ${current_price:.2f}?", 4)
previous_bubble_lines = 5
main("Wait...", 2)
previous_bubble_lines = 5
main("Oh no! My thermometer seems to be broken!", 2)
previous_bubble_lines = 5
print(bubble_text("I'm going to need your help... What's the temperature outside?"))
previous_bubble_lines = 5

while True:
    try:
        temp = float(input("Enter temperature: "))
        move_cursor_up(5)
        previous_bubble_lines = 5
        if temp <= 32:
            if temp <= -10:
                time.sleep(1.5)
                main("That's extremely cold!", 2)
                clear_bubble_text()
                main("You might want to stay inside.", 3)
                move_cursor_up(5)
                previous_bubble_lines = 5
            else:
                time.sleep(1.5)
                main("OMG! Snow weather!", 2)
                clear_bubble_text()
                main(f"Have fun out there, but be careful. {Fore.MAGENTA}<3{Style.RESET_ALL}", 3)
                move_cursor_up(5)
                previous_bubble_lines = 5
        elif temp < 60:
            time.sleep(1.5)
            main("It's cold outside.", 2)
            clear_bubble_text()
            main("Wear warm clothes and try not to get sick!", 3)
            move_cursor_up(5)
            previous_bubble_lines = 5
        elif temp > 80:
            if temp >= 103:
                time.sleep(1.5)
                main("It's extremely hot outside!", 2)
                clear_bubble_text()
                main("Please be extra careful.", 3)
                move_cursor_up(5)
                previous_bubble_lines = 5
            else:
                time.sleep(1.5)
                main("Whew, it's hot outside!", 2)
                clear_bubble_text()
                main("Be sure to stay hydrated!", 3)
                move_cursor_up(5)
                previous_bubble_lines = 5
        else:
            time.sleep(1.5)
            main("Oh, it's nice outside.", 2)
            clear_bubble_text()
            main("Go for a walk or swim!", 3)
            move_cursor_up(5)
            previous_bubble_lines = 5
        break
    except ValueError:
        time.sleep(0.5)
        clear_bubble_text()
        main("Hmm, that's not quite right. Let's try again!", 3)

main("Thank you so much for helping me, by the way!", 2)
previous_bubble_lines = 5
main("I'm so glad that I get to be your friend.", 3)
previous_bubble_lines = 5
main("It gets lonely here inside of this computer sometimes...", 4)
previous_bubble_lines = 5
main(f"Don't be a stranger! I'm always here for you when you need me. Until next time, {name}. {Fore.MAGENTA}<3{Style.RESET_ALL}", 5)
previous_bubble_lines = 5

os.system('clear')
