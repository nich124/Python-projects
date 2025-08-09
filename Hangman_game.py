from faker import Faker
from time import sleep
import random
from demo import words
from demo import popular_fruits

hangman_art = {
    0: """
        _______
        |     |
        |
        |
        |
        |
    ___________""",
    1: """
        _______
        |     |
        |     O
        |
        |
        |
    ___________""",
    2: """
        _______
        |     |
        |     O
        |     |
        |
        |
    ___________""",
    3: """
        _______
        |     |
        |     O
        |    /|
        |
        |
    ___________""",
    4: """
        _______
        |     |
        |     O
        |    /|\\
        |
        |
    ___________""",
    5: """
        _______
        |     |
        |     O
        |    /|\\
        |    /
        |
    ___________""",
    6: """
        _______
        |     |
        |     O
        |    /|\\
        |    / \\
        |
    ___________"""
}


def hang(hangs):
    print(hangman_art[hangs])

def guess(what):
    return input(what)

def rand(level):
    easy = random.choice(popular_fruits)
    medium = random.choice(words)
    fake = Faker()
    hard = fake.word()
    if level == 1:
        return easy
    elif level == 2:
        return medium
    elif level == 3:
        return hard

    
def showHint(hint):
    print(" ".join(hint))
   


def showAnswer(answer):
    print(" ".join(answer))

def showHelp(help):
    if help == 1:
        print('You chose easy so Hints: Fruits')
    elif help == 2:
        print('You chose medium so Hints: Animals')
    elif help == 3:
        print('Wow you get mind oo You are in hard no hints for you')


def game():
    try:
        live = 6
        difficulty = int(input('select level: Enter 1 for easy, 2 for medium , 3 for hard: '))
        cpu = rand(difficulty)
        # cpu = 'american'
        showHelp(difficulty)
        hinted = ['_'] * len(cpu)
        guessed_letters = []
        hearts = '❤️ '
        wrongGuess = 0
        print('💻 Computer has choosen a word')
        while live > 0:
            print(f'{hearts * live} You have {live} chances left')
            showHint(hinted)
            hang(wrongGuess)
            # showAnswer(cpu)
            user = guess('Guess a letter of the word 🤔 : ').lower()
            sleep(1)
            if not user.isalpha() or len(user) != 1:
                print('❌ Pls enter a single letter !!!')
                continue

            if user in guessed_letters:
                live-=1
                wrongGuess += 1
                print("⚠️ You already guessed that letter!")
                continue

            guessed_letters.append(user)

            if user in cpu: 
                sleep(1)
                print(f'✅ You guessed right {user} is part of the word')
                for i in range(0,len(cpu)):
                    if cpu[i] == user:
                        hinted[i] = user
                        
            else:
                sleep(1)
                print(f'❌ You guessed wrong {user} is not part of the word')
                live-=1
                wrongGuess += 1
                

            if "_" not in hinted:
                sleep(1)
                showAnswer(cpu)
                print(f'{cpu.upper()}')
                print('🎉🎉🎉 YOU WIN! 🎉🎉🎉')
                again()
                break
            
        if live == 0:
            sleep(1)
            print(f'the word was {cpu.upper()}')
            showAnswer(cpu)
            hang(6)
            print('\n😢💀 GAME OVER!')
            again()
    except:
        print('Invalid Entry')
        game()
        

def again():
    print('\nEnter 1. to play again 🔁  or 2. to quit 🚪')
    user = int(guess(''))
    if user == 1:
        sleep(1)
        game()
    elif user == 2:
        sleep(1)
        print('Good bye 👋')
    else:
        sleep(1)
        print('\nInvalid Entry... tryy again')
        again()

    
        





        

def welcome():
    print('🎭 WELCOME TO HANGMAN! 🎭\nGuess the word before you run out of lives!\nYou start with 6 hearts ❤️ ❤️ ❤️ ❤️ ❤️ ❤️')   
    game()
if __name__ == "__main__":
    welcome()