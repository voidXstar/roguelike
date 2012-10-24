#!/usr/bin/python

'''
Just starting out, let's get the basics down...
Currently this just prints an @ sign and does not respond to normal attempts to close the program.
I have to hit Ctrl+C in the console I started it from.
'''


import libtcodpy as libtcod


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50


def get_key(key):
  if key.vk == libtcod.KEY_CHAR:
    return chr(key.c)
  else:
    return key.vk

libtcod.console_set_custom_font('terminal8x8_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'window title here', False)

while not libtcod.console_is_window_closed():
  libtcod.console_set_default_foreground(0, libtcod.white)
  libtcod.console_set_alignment(0, libtcod.LEFT)
  libtcod.console_print(0, 1, 1, '@')
  libtcod.console_flush()



