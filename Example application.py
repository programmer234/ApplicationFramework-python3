import pygame
from layersystem import application

function_list = []
ui_list = []
threads = []


def exit_function():
    global threads
    #Add exit_code_here

def button_1_click():
    pass

def draw_ui():
    global ui_list
    
    # you can add ui here
    #TextPosition = [0, 0]
    #Text example: ui_list.append(application.text("TYPE YOUR TEXT HERE", 100, TextPosition))

def initializer():
    global function_list, ui_list
    draw_ui()
    
    # add initialization code here



application.initialize_application(initializer)
application.initialize_screen()
application.runtime(exit_function, function_list, ui_list)
