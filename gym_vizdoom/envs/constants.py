from os import path as osp
import numpy as np

# vizdoom
MAP_NAME_TEMPLATE = 'map%02d'
MOVE_FORWARD = [0, 0, 0, 1, 0, 0, 0]
MOVE_BACKWARD = [0, 0, 0, 0, 1, 0, 0]
MOVE_LEFT = [1, 0, 0, 0, 0, 0, 0]
MOVE_RIGHT = [0, 1, 0, 0, 0, 0, 0]
STAY_IDLE = [0, 0, 0, 0, 0, 0, 0]
TURN_LEFT = [0, 0, 0, 0, 0, 1, 0]
TURN_RIGHT = [0, 0, 0, 0, 0, 0, 1]
# ACTIONS_LIST = [MOVE_FORWARD, MOVE_BACKWARD, MOVE_LEFT, MOVE_RIGHT, STAY_IDLE, TURN_LEFT, TURN_RIGHT]
# ACTION_NAMES = ['MOVE_FORWARD', 'MOVE_BACKWARD', 'MOVE_LEFT', 'MOVE_RIGHT', 'STAY_IDLE', 'TURN_LEFT', 'TURN_RIGHT']
ACTIONS_LIST = [MOVE_FORWARD, TURN_LEFT, TURN_RIGHT]
ACTION_NAMES = ['MOVE_FORWARD', 'TURN_LEFT', 'TURN_RIGHT']

WAIT_BEFORE_START_TICS = 140
VIZDOOM_TO_TF = [1, 2, 0]
ACTION_CLASSES = len(ACTIONS_LIST)
MIN_RANDOM_TEXTURE_MAP_INDEX = 2
MAX_RANDOM_TEXTURE_MAP_INDEX = 401
REPEAT = 4
NET_WIDTH = 160
NET_HEIGHT = 120
NET_CHANNELS = 3

# general
DIR = osp.dirname(__file__)
DEFAULT_CONFIG = osp.join(DIR, 'data', 'default.cfg')
TRAIN_WAD = osp.join(DIR, 'Train', 'D3_exploration_train.wad_manymaps.wad_exploration.wad')

# test envs
STATE_AFTER_GAME_END = np.zeros((NET_HEIGHT, NET_WIDTH, NET_CHANNELS), dtype=np.uint8)
EXPLORATION_GOAL = np.zeros((NET_HEIGHT, NET_WIDTH, NET_CHANNELS), dtype=np.uint8) - 1
MAX_STEP_NAVIGATION = 5000 // REPEAT
MAX_STEP_EXPLORATION = 10000 // REPEAT
GOAL_DISTANCE_ALLOWANCE = 63
EXPLORATION_STATUS = 0
NAVIGATION_STATUS = 1

DATA_PATH = 'data'
DEFAULT_TEST_MAPS = ['map02', 'map03', 'map04', 'map05']
DEFAULT_TEST_EXPLORATION_MAP = 'map06'
DEFAULT_TEST_GOAL_NAMES = ['tall_red_pillar',
                           'candelabra',
                           'tall_blue_torch',
                           'short_green_pillar']
GOAL_EXTENDED_OBSERVATION_SHAPE = [NET_HEIGHT, NET_WIDTH, 2 * NET_CHANNELS]
