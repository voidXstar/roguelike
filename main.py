#!/usr/bin/python

'''
Just starting out, let's get the basics down...
'''


import libtcodpy as libtcod


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

playerx = SCREEN_WIDTH / 2
playery = SCREEN_HEIGHT / 2


def get_key(key):
  if key.vk == libtcod.KEY_CHAR:
    return chr(key.c)
  else:
    return key.vk

def handle_keys():

  global playerx, playery

  #this is blocking, console_check_for_keypress() is nonblocking
  key = libtcod.console_wait_for_keypress(True)

  #exit
  if key.vk == libtcod.KEY_ESCAPE:
    return True

  #Alt+Enter: toggle fullscreen
  elif key.vk == libtcod.KEY_ENTER and key.lalt:
    libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

  #movement keys
  # checked this way so you can just hold it down
  elif libtcod.console_is_key_pressed(libtcod.KEY_UP):
    playery -= 1
  elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
    playery += 1
  elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
    playerx -= 1
  elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
    playerx += 1


libtcod.console_set_custom_font('terminal8x8_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'window title here', False)

while not libtcod.console_is_window_closed():
  libtcod.console_set_default_foreground(0, libtcod.white)
  libtcod.console_set_alignment(0, libtcod.LEFT)
  libtcod.console_print(0, 1, 1, '@')
  libtcod.console_flush()
  libtcod.console_print(0, playerx, playery, ' ')

  exit = handle_keys()
  if exit:
    break


