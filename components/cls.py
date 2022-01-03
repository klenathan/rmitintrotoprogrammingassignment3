# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author: 
#         Thai Tran (s3891890)
#         Thu Pham (s3878246)
#         Thinh Nguyen (s3914412)
#         Soohyuk Jang (s3928379)
# Created date: 20/12/2021
# Last modified date: 03/01/2022
# Python version: 3.10.0


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
