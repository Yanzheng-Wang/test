import tools  # 使用绝对导入


class Menu(tools._State):
    def __init__(self):
        """Initializes the state"""
        tools._State.__init__(self)
        persist = {c.COIN_TOTAL: 0,
                   c.SCORE: 0,
                   c.LIVES: 23,  # 修改这里
                   c.TOP_SCORE: 0,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_STATE: None,
                   c.CAMERA_START_X: 0,
                   c.MARIO_DEAD: False}
        self.startup(0.0, persist)


#!/usr/bin/env python
__author__ = 'justinarmstrong'

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.
"""

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    main()
    pg.quit()
    sys.exit()
