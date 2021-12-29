import platform
import os


def cls():
    """
    The function clears console/terminal based on the user's operating system
    :param: None
    :return: clear  
    """
    clear = ''
    if platform.system() == 'Windows':
        clear = os.system('cls')
    elif platform.system() == 'Darwin':
        clear = os.system('clear')
    elif platform.system() == 'Linux':
        clear = os.system('clear')
    else:
        print("The program can only clear on Window, MacOS and Linux") 
    return clear
