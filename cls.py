import platform
import os

def cls():
    '''
    The function clear console/terminal based on the user's operating system
    '''
    if platform.system() == 'Windows':
        return os.system('cls')
    elif platform.system() == 'Darwin':
        return os.system('clear')
    elif platform.system() == 'Linux':
        return os.system('clear')
    else:
        return print("The program can only clear on Window, MacOS and Linux")