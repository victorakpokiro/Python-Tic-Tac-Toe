#+--------------------------+-----------------------------+
# Author:=> Victor Akpokiro
#+--------------------------+-----------------------------+
# Description:=> X and O
#+--------------------------+-----------------------------+


#  Program to simulate X & O

from termcolor import colored
from colorama import init
init()


def main():
    print("""
    Program to simulate X and O For Humans NOT Computers

        9   |  8  |   7
        ___ | ___ | ___
        6   |  5  |  4
        ___ | ___ | ___
        3   |  2  |  1
            |     |

        Player Names: X & O
        # X is true; O is false
        # Use numbers as position
""")

    #import pudb
    #pudb.set_trace()
    
    msg = "Please choose your player name"
    print(msg)
    tmp = input("--> ")

    if tmp.lower() == 'o':
        player_one = True
        player_two = False
    else:
        player_one = False
        player_two = True

    player = {
                False: add_color("O", "green"),
                True: add_color("X", "yellow")
            }

    print("Player One is : ", player[player_one])
    print("Player Two is : ", player[player_two])

    add_new_line()
    print("From numbers 1 - 9, choose a number")

    available_play = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    positions = {False: [], True: []}

    next_signal = player_one

    while len(available_play) > 0:
        print("\nNext Player: ", player[next_signal], "\n")
        new_play = input("--> ")
        # ideally check for strings and

        new_play = new_play.strip()

        if not new_play or int(new_play) > 9:
            print("please pick a position")
            continue

        if new_play.lower() == 'exit':
            available_play = []
            continue  #  to exit

        if not new_play.isdigit():
            print("please pick a number")
            continue

        if (new_play in positions[player_one]) or (new_play in
                                                    positions[player_two]):
            print("position already taken, please choose another one")
            continue

        # add color to the letters

        positions[next_signal].append(new_play)

        draw_the_board(positions)
        available_play.pop()

        # check for a winner
        if check_winner(positions[next_signal]):

            print("Player ", player[next_signal], " Wins...")
            print("Game Over...")
            available_play = []


        next_signal = not next_signal


def draw_the_board(position):

    _positions = {
        "1": "1", "2": "2", "3": "3",
        "4": "4", "5": "5", "6": "6",
        "7": "7", "8": "8", "9": "9"
    }

    # high light the boxes
    for key, item in position.items():
        name = add_color("O", "green")
        if key:
            name = add_color("X", "yellow")

        for x in item:
            _positions[x] = name


    add_new_line()

    counter = 1
    border = get_border()

    content = ""

    for item in range(9, 0, -1):

        size = 20
        content = _positions[str(item)]
        if len(content) == 1:
            size = 11

        content = content.center(size, " ")

        if counter % 3 != 0:
            content += " | "

        print(content, end='')


        if counter % 3 == 0 and counter < 9:
            # print a border line here
            add_new_line()
            print(border)

        counter += 1

    add_new_line()


def add_new_line():
    print("\n")


def check_winner(points):

    _tmp_point = "".join(points)
    winning_points = [
        "963", "852", "741", "987",
        "654", "321", "951", "753"
    ]

    for win in winning_points:
        win_count = 0
        for x in win:

            if x in _tmp_point:
                win_count += 1

        if win_count == 3:
            break

    return win_count == 3


# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

def get_border():

    cnt = 0
    line = ""
    for item in range(3):
        out = ("-" * 11).center(11, " ")

        cnt += 1
        line += out
        if cnt < 3:
            line += " + "

    return line


# +-------------------------+-------------------------+
# +-------------------------+-------------------------+


# def draw_layer(_data):

#     line = ''
#     cnt = 0

#     for item, spacing in _data:
#         item = str(item)
#         output = item.center(20, " ")

#         line += output
#         cnt += 1
#         if cnt < 3:
#             line += " | "

#     print(line)


def draw_layer(_data):

    line = ''
    border = ''

    cnt = 0

    for item, spacing in _data:

        output = item.center(spacing, " ")
        border += ("-" * 11).center(11, ' ')
        line += output
        cnt += 1
        if cnt <= 3:
            line += " | "

        if cnt < 3:
            border += " + "

        print(line, end='')
        line = ''

    print("\n")
    print(border)

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+

def add_color(data, _color='green'):
    return colored(data, _color)

# +-------------------------+-------------------------+
# +-------------------------+-------------------------+


if __name__ == '__main__':

    main()