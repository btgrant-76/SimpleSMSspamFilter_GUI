# DearPyGUI Imports
from dearpygui.core import *
from dearpygui.simple import *

pred = []


def check_spam(sender, data):
    if pred == []:
        input_value = get_value('Input')
        pred.append(input_value)
        print(f'scenario #1: {input_value}')
    else:
        input_value = get_value('Input')
        pred.append(input_value)
        print(f'scenario #2: {input_value}')


# Window object settings
set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme('Gold')
set_style_window_padding(30, 30)

with window('Simple SMS Spam Filter', width=520, height=677):  # this is a 2nd window
    print('GUI is running...')
    set_window_pos('Simple SMS Spam Filter', 0, 0)

    # logo
    add_drawing('logo', width=520, height=290)
    add_separator()
    add_spacing(count=12)

    # instructions
    add_text("Please enter an SMS message of your choice to check if it's spam or not",
             color=[232, 163, 33], wrap=520)
    add_spacing(count=12)

    # collect input
    add_input_text('Input', width=415, default_value='type message here')
    add_spacing(count=12)
    add_button('Check', callback=check_spam)

draw_image('logo', 'logo_spamFilter.png', [0, 0], [458, 192])

start_dearpygui()
