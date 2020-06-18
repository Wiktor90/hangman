import random
import os

# sciezka do pliku z haslami
f = open("C:\\Users\\PL9891\\Desktop\\P\\Projekty\\hangman\\hangman_base.txt","r") 
value = []
 
for line in f:
    # Podział na znakach białych
    words = line.split()
    # Podział na znakach '=' każdego wyrażenia
    for word in words:
        word_and_value = word.split('=')
        # Jeśli chcesz, odkomentuj linię poniżej
        # aby zobaczyć co jest w word_and_value
        #print(word_and_value)
        # Tylko pierwsze słowo jest interesujące
        value.append(word_and_value[0])
f.close()

def cls():
    os.system("cls")
num = random.randint(0,len(value)-1)
spell = value[num]

def hangman(word):
    wrong = 0
    stage = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    board = ["__"] * len(word)
    letter = list(word)
    win = False
    table =[]
    print(".::. HANGMAN GAME .::.")

    while wrong < len(stage) - 1:
        print("\n")
        msg = "Enter the letter: "
        char = input(msg)
        table.append(char)
        if char in letter:
            place = letter.index(char)
            board[place] = char
            letter[place] = "#"
        else:
            wrong += 1
        r = wrong + 1
        cls()
        print (" ".join(board))
        print ("\n".join(stage[0:r]))
        print("Inputed letter: ",table)
        if "__" not in board:
            print("\nYOU WIN !!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\nGAME OVER")
        print("You should spell: '{}'".format(word))

hangman(spell)