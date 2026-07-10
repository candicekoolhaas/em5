#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.3),
    on September 16, 2024, at 12:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.3'
expName = 'wm'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'order': ['B','D', 'A', 'C'],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Canna_d\\EM5_stuff\\EM5_experiments\\EM5_experiment\\wm_tap5.3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "loading" ---
# Run 'Begin Experiment' code from loadList
#productList is the products on the shelf
#have to load the lish here separately othewise 
#the repeat time of the loop = the number of row
# stop using load becasue I need it to be loaded at the begining of the exepriment4/9/2022
productList1 = data.importConditions("productList1.csv")
productList2 = data.importConditions("productList2.csv")
productList3 = data.importConditions("productList3.csv")
allList = [productList1,productList2,productList3]
shuffle(allList)
#productList = data.importConditions('animalList.csv')
totalStars = 0
correctSound = sound.Sound('sound\correctPick.wav')
wrongSound = sound.Sound('sound\wrongPick.wav')
adultAndKid = visual.ImageStim(
    win=win,
    name='adultAndKid', 
    image='image/adultAndKid.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.13, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
endFirstLine = keyboard.Keyboard()

# --- Initialize components for Routine "blockBegin" ---
blockBeginMsg = visual.TextStim(win=win, name='blockBeginMsg',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
endBlockMsg = keyboard.Keyboard()

# --- Initialize components for Routine "trialBegin" ---
trialMessage = visual.TextStim(win=win, name='trialMessage',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
storeImages = visual.ImageStim(
    win=win,
    name='storeImages', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
storeImageEnd = keyboard.Keyboard()

# --- Initialize components for Routine "initializeNewTrial" ---
# Run 'Begin Experiment' code from makeShopStim
# shopPos mean the postion of the list
shopPosX = [-0.27,-0.39,-0.51,-0.27,-0.39,-0.51,
-0.27,-0.39,-0.51,-0.51]
shopPosY = [0.34,0.34,0.34,0.21,0.21,0.21,
0.08,0.08,0.08,-0.05]
# Run 'Begin Experiment' code from makeShelfStim



# --- Initialize components for Routine "justStore" ---
shoppingbasket_3 = visual.ImageStim(
    win=win,
    name='shoppingbasket_3', 
    image='image/basket.png', mask=None, anchor='center',
    ori=0.0, pos=(0.28, -0.42), size=(0.5, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
SmallShelf5_2 = visual.ImageStim(
    win=win,
    name='SmallShelf5_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, 0.32), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
SmallShelf5_1 = visual.ImageStim(
    win=win,
    name='SmallShelf5_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, 0.32), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
SmallShelf1_1 = visual.ImageStim(
    win=win,
    name='SmallShelf1_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, 0.19), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
SmallShelf1_2 = visual.ImageStim(
    win=win,
    name='SmallShelf1_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, 0.19), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
SmallShelf2_1 = visual.ImageStim(
    win=win,
    name='SmallShelf2_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, 0.06), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
SmallShelf2_2 = visual.ImageStim(
    win=win,
    name='SmallShelf2_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, 0.06), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
SmallShelf3_1 = visual.ImageStim(
    win=win,
    name='SmallShelf3_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, -.07), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
SmallShelf3_2 = visual.ImageStim(
    win=win,
    name='SmallShelf3_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, -.07), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
SmallShelf4_1 = visual.ImageStim(
    win=win,
    name='SmallShelf4_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, -.2), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
SmallShelf4_2 = visual.ImageStim(
    win=win,
    name='SmallShelf4_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, -.2), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
shopper_2 = visual.ImageStim(
    win=win,
    name='shopper_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
kid_2 = visual.ImageStim(
    win=win,
    name='kid_2', 
    image='image/kidSmall.png', mask=None, anchor='center',
    ori=0.0, pos=(0.01, -0.42), size=(0.05, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
imageMouse_2 = event.Mouse(win=win)
x, y = [None, None]
imageMouse_2.mouseClock = core.Clock()
# Run 'Begin Experiment' code from clickResponse_2
def copyImage(image, pos, name, size):
    return visual.ImageStim(win, 
        name=name, image=image.image, mask=image.mask,
        anchor=image.anchor, ori = image.ori, size=size, 
        pos=pos,color=image.color, colorSpace=image.colorSpace, 
        opacity=image.opacity,flipHoriz=image.flipHoriz, 
        flipVert=image.flipVert,texRes=image.texRes, 
        interpolate=image.interpolate, depth=image.depth)


    
def drawClicked(clicked):
    for each in clicked:
        each.draw()
        
starsPosX = [0.12,0.18,0.24,0.30,0.36,0.42,0.48,0.54,0.60,0.66,
0.12,0.18,0.24,0.30,0.36,0.42,0.48,0.54,0.60,0.66]
starsPosY = [0.46,0.46,0.46,0.46,0.46,0.46,0.46,0.46,0.46,0.46,
0.41,0.41,0.41,0.41,0.41,0.41,0.41,0.41,0.41,0.41]


def makeStars(starCounts,starsPosX,starsPosY):
    stars=[]
    for i in range(starCounts):
        star = visual.ShapeStim(
        win=win, name='polygon', vertices='star7',
        size=(0.05, 0.05),ori=0.0, 
        pos=(starsPosX[i], starsPosY[i]), 
        anchor='center',lineWidth=1.0, 
        colorSpace='rgb',  lineColor='gold', 
        fillColor='yellow',opacity=None, depth=-4.0, 
        interpolate=True)
        stars.append(star)
    return stars


    
def drawStars(stars):
    for each in stars:
        each.draw()




# --- Initialize components for Routine "mask" ---
maskText = visual.TextStim(win=win, name='maskText',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
walkingShopper = visual.ImageStim(
    win=win,
    name='walkingShopper', 
    image='image/walkShopper.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.19, 0.17),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
kid2 = visual.ImageStim(
    win=win,
    name='kid2', 
    image='image/kidSmall.png', mask=None, anchor='center',
    ori=0.0, pos=(0.01, -0.42), size=(0.05, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "template" ---
# Run 'Begin Experiment' code from drawShopStim
listimage2 = visual.ImageStim(
    win=win,
    name="list", 
    image="image\shopList.png", 
    mask=None, anchor='center',ori=0.0, 
    pos=(-0.4, 0.15),
    size=((0.7, 0.7)),
    color="burlywood", colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
goRight = visual.ImageStim(
    win=win,
    name='goRight', 
    image='image/right.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
goRightMouse = event.Mouse(win=win)
x, y = [None, None]
goRightMouse.mouseClock = core.Clock()
clock = visual.ImageStim(
    win=win,
    name='clock', 
    image='image/clock.png', mask=None, anchor='center',
    ori=0.0, pos=(0.6, 0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "working" ---
shoppingbasket = visual.ImageStim(
    win=win,
    name='shoppingbasket', 
    image='image/basket.png', mask=None, anchor='center',
    ori=0.0, pos=(0.28, -0.42), size=(0.5, 0.14),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
SmallShelf5_1_2 = visual.ImageStim(
    win=win,
    name='SmallShelf5_1_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, 0.32), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
SmallShelf5_1_1 = visual.ImageStim(
    win=win,
    name='SmallShelf5_1_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, 0.32), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
SmallShelf1_1_1 = visual.ImageStim(
    win=win,
    name='SmallShelf1_1_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, 0.19), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
SmallShelf1_1_2 = visual.ImageStim(
    win=win,
    name='SmallShelf1_1_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, 0.19), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
SmallShelf2_1_1 = visual.ImageStim(
    win=win,
    name='SmallShelf2_1_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, 0.06), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
SmallShelf2_1_2 = visual.ImageStim(
    win=win,
    name='SmallShelf2_1_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, 0.06), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
SmallShelf3_1_1 = visual.ImageStim(
    win=win,
    name='SmallShelf3_1_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, -.07), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
SmallShelf3_1_2 = visual.ImageStim(
    win=win,
    name='SmallShelf3_1_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, -.07), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
SmallShelf4_1_1 = visual.ImageStim(
    win=win,
    name='SmallShelf4_1_1', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.16, -.2), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
SmallShelf4_1_2 = visual.ImageStim(
    win=win,
    name='SmallShelf4_1_2', 
    image='image/shelf1.png', mask=None, anchor='center',
    ori=0.0, pos=(0.475, -.2), size=(0.3, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
shopper = visual.ImageStim(
    win=win,
    name='shopper', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
kid = visual.ImageStim(
    win=win,
    name='kid', 
    image='image/kidSmall.png', mask=None, anchor='center',
    ori=0.0, pos=(0.01, -0.42), size=(0.05, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
imageMouse = event.Mouse(win=win)
x, y = [None, None]
imageMouse.mouseClock = core.Clock()
# Run 'Begin Experiment' code from clickResponse
def copyImage(image, pos, name, size):
    return visual.ImageStim(win, 
        name=name, image=image.image, mask=image.mask,
        anchor=image.anchor, ori = image.ori, size=size, 
        pos=pos,color=image.color, colorSpace=image.colorSpace, 
        opacity=image.opacity,flipHoriz=image.flipHoriz, 
        flipVert=image.flipVert,texRes=image.texRes, 
        interpolate=image.interpolate, depth=image.depth) 


    
def drawClicked(clicked):
    for each in clicked:
        each.draw()
        
starsPosX = [0.12,0.18,0.24,0.30,0.36,0.42,0.48,0.54,0.60,0.66,
0.12,0.18,0.24,0.30,0.36,0.42,0.48,0.54,0.60,0.66]
starsPosY = [0.46,0.46,0.46,0.46,0.46,0.46,0.46,0.46,0.46,0.46,
0.41,0.41,0.41,0.41,0.41,0.41,0.41,0.41,0.41,0.41]


def makeStars(starCounts,starsPosX,starsPosY):
    stars=[]
    for i in range(starCounts):
        star = visual.ShapeStim(
        win=win, name='polygon', vertices='star7',
        size=(0.05, 0.05),ori=0.0, 
        pos=(starsPosX[i], starsPosY[i]), 
        anchor='center',lineWidth=1.0, 
        colorSpace='rgb',  lineColor='gold', 
        fillColor='yellow',opacity=None, depth=-4.0, 
        interpolate=True)
        stars.append(star)
    return stars


    
def drawStars(stars):
    for each in stars:
        each.draw()


#NEW
def makeGrey(item):
    for image in item:
        image.opacity = 0.5
        
def makeWhite(item):
    for image in item:
        image.opacity = 1.0
        
def makeInvisible(item):
    for image in item:
        image.opacity = 0.0

# --- Initialize components for Routine "mask" ---
maskText = visual.TextStim(win=win, name='maskText',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
walkingShopper = visual.ImageStim(
    win=win,
    name='walkingShopper', 
    image='image/walkShopper.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.19, 0.17),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
kid2 = visual.ImageStim(
    win=win,
    name='kid2', 
    image='image/kidSmall.png', mask=None, anchor='center',
    ori=0.0, pos=(0.01, -0.42), size=(0.05, 0.11),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "trialFeedback" ---
# Run 'Begin Experiment' code from makeFeedback
trialFeedback=""
trialFeedBackPress = keyboard.Keyboard()
goodJobV = visual.MovieStim3(
    win=win, name='goodJobV', units='',
    noAudio = False,
    filename='image/goodJob.mp4',
    ori=0.0, pos=(0, 0.2), opacity=None,
    loop=True, anchor='center',
    size=[0.4,0.3],
    depth=-2.0,
    )
goodJobI = visual.ImageStim(
    win=win,
    name='goodJobI', 
    image='image/goodJob.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.2), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
trialFeedBackText = visual.TextStim(win=win, name='trialFeedBackText',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "finalQ" ---
sMarket = visual.ImageStim(
    win=win,
    name='sMarket', 
    image='image/longDelay.jpg', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.75, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
cStore = visual.ImageStim(
    win=win,
    name='cStore', 
    image='image/nodelay.jpg', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.26, 0.26),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
endQ = keyboard.Keyboard()

# --- Initialize components for Routine "expEnd" ---
# Run 'Begin Experiment' code from expFeedback
expFeedback=""
endExp = keyboard.Keyboard()
expFeedbackText = visual.TextStim(win=win, name='expFeedbackText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "loading" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
endFirstLine.keys = []
endFirstLine.rt = []
_endFirstLine_allKeys = []
# keep track of which components have finished
loadingComponents = [adultAndKid, endFirstLine]
for thisComponent in loadingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "loading" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *adultAndKid* updates
    if adultAndKid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        adultAndKid.frameNStart = frameN  # exact frame index
        adultAndKid.tStart = t  # local t and not account for scr refresh
        adultAndKid.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(adultAndKid, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'adultAndKid.started')
        adultAndKid.setAutoDraw(True)
    
    # *endFirstLine* updates
    waitOnFlip = False
    if endFirstLine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endFirstLine.frameNStart = frameN  # exact frame index
        endFirstLine.tStart = t  # local t and not account for scr refresh
        endFirstLine.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endFirstLine, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endFirstLine.started')
        endFirstLine.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endFirstLine.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endFirstLine.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endFirstLine.status == STARTED and not waitOnFlip:
        theseKeys = endFirstLine.getKeys(keyList=['q'], waitRelease=False)
        _endFirstLine_allKeys.extend(theseKeys)
        if len(_endFirstLine_allKeys):
            endFirstLine.keys = _endFirstLine_allKeys[-1].name  # just the last key pressed
            endFirstLine.rt = _endFirstLine_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "loading" ---
for thisComponent in loadingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if endFirstLine.keys in ['', [], None]:  # No response was made
    endFirstLine.keys = None
thisExp.addData('endFirstLine.keys',endFirstLine.keys)
if endFirstLine.keys != None:  # we had a response
    thisExp.addData('endFirstLine.rt', endFirstLine.rt)
thisExp.nextEntry()
# the Routine "loading" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("blockOrder"+expInfo['order']+"5.2.csv"),
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "blockBegin" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    blockBeginMsg.setText(blockMsg)
    endBlockMsg.keys = []
    endBlockMsg.rt = []
    _endBlockMsg_allKeys = []
    # keep track of which components have finished
    blockBeginComponents = [blockBeginMsg, endBlockMsg]
    for thisComponent in blockBeginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blockBegin" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blockBeginMsg* updates
        if blockBeginMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blockBeginMsg.frameNStart = frameN  # exact frame index
            blockBeginMsg.tStart = t  # local t and not account for scr refresh
            blockBeginMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blockBeginMsg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blockBeginMsg.started')
            blockBeginMsg.setAutoDraw(True)
        
        # *endBlockMsg* updates
        waitOnFlip = False
        if endBlockMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endBlockMsg.frameNStart = frameN  # exact frame index
            endBlockMsg.tStart = t  # local t and not account for scr refresh
            endBlockMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endBlockMsg, 'tStartRefresh')  # time at next scr refresh
            endBlockMsg.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endBlockMsg.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endBlockMsg.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endBlockMsg.status == STARTED and not waitOnFlip:
            theseKeys = endBlockMsg.getKeys(keyList=['q'], waitRelease=False)
            _endBlockMsg_allKeys.extend(theseKeys)
            if len(_endBlockMsg_allKeys):
                endBlockMsg.keys = _endBlockMsg_allKeys[-1].name  # just the last key pressed
                endBlockMsg.rt = _endBlockMsg_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockBeginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockBegin" ---
    for thisComponent in blockBeginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if endBlockMsg.keys in ['', [], None]:  # No response was made
        endBlockMsg.keys = None
    block.addData('endBlockMsg.keys',endBlockMsg.keys)
    if endBlockMsg.keys != None:  # we had a response
        block.addData('endBlockMsg.rt', endBlockMsg.rt)
    # the Routine "blockBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    multipleTrials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condsFile),
        seed=None, name='multipleTrials')
    thisExp.addLoop(multipleTrials)  # add the loop to the experiment
    thisMultipleTrial = multipleTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMultipleTrial.rgb)
    if thisMultipleTrial != None:
        for paramName in thisMultipleTrial:
            exec('{} = thisMultipleTrial[paramName]'.format(paramName))
    
    for thisMultipleTrial in multipleTrials:
        currentLoop = multipleTrials
        # abbreviate parameter names if possible (e.g. rgb = thisMultipleTrial.rgb)
        if thisMultipleTrial != None:
            for paramName in thisMultipleTrial:
                exec('{} = thisMultipleTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trialBegin" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        trialMessage.setText(delayMessage)
        storeImages.setSize((storeSizeW, storeSizeH))
        storeImages.setImage(storeImage)
        storeImageEnd.keys = []
        storeImageEnd.rt = []
        _storeImageEnd_allKeys = []
        # keep track of which components have finished
        trialBeginComponents = [trialMessage, storeImages, storeImageEnd]
        for thisComponent in trialBeginComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialBegin" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trialMessage* updates
            if trialMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialMessage.frameNStart = frameN  # exact frame index
                trialMessage.tStart = t  # local t and not account for scr refresh
                trialMessage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialMessage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialMessage.started')
                trialMessage.setAutoDraw(True)
            
            # *storeImages* updates
            if storeImages.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                storeImages.frameNStart = frameN  # exact frame index
                storeImages.tStart = t  # local t and not account for scr refresh
                storeImages.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(storeImages, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'storeImages.started')
                storeImages.setAutoDraw(True)
            
            # *storeImageEnd* updates
            waitOnFlip = False
            if storeImageEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                storeImageEnd.frameNStart = frameN  # exact frame index
                storeImageEnd.tStart = t  # local t and not account for scr refresh
                storeImageEnd.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(storeImageEnd, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'storeImageEnd.started')
                storeImageEnd.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(storeImageEnd.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(storeImageEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if storeImageEnd.status == STARTED and not waitOnFlip:
                theseKeys = storeImageEnd.getKeys(keyList=['q'], waitRelease=False)
                _storeImageEnd_allKeys.extend(theseKeys)
                if len(_storeImageEnd_allKeys):
                    storeImageEnd.keys = _storeImageEnd_allKeys[-1].name  # just the last key pressed
                    storeImageEnd.rt = _storeImageEnd_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialBeginComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialBegin" ---
        for thisComponent in trialBeginComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if storeImageEnd.keys in ['', [], None]:  # No response was made
            storeImageEnd.keys = None
        multipleTrials.addData('storeImageEnd.keys',storeImageEnd.keys)
        if storeImageEnd.keys != None:  # we had a response
            multipleTrials.addData('storeImageEnd.rt', storeImageEnd.rt)
        # the Routine "trialBegin" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "initializeNewTrial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from initializeTrialList
        randProdList = allList[listNum].copy()
        shuffle(randProdList)#Why is this being shuffled? The rows in the csv file are in an arbitrary order aren't they?
        import random
        #NEW
        #pair_values = list(set(object['pair'] for object in randProdList if 'pair' in object))
        
        selected_items = {}
        for pair_label in ['A', 'B', 'C', 'D', 'E', 'F','G','H','I', 'J']:
            
            items_in_pair = [object for object in randProdList if object['pair'] == pair_label]
            
            if items_in_pair:
                selected_item = random.choice(items_in_pair)
                selected_items[pair_label] = selected_item
               
        shopList = list(selected_items.values())
        
        #shopList = randProdList[0:10]
        correctImages=[object['imageName'] for object in shopList]
        #create a list of running correct images so clicking the same image twice won't cout as two correct
        curCorrectImages = correctImages.copy()
        correctCount =0
        incorrectCount =0
        starCounts = 1
        # Run 'Begin Routine' code from makeShopStim
        shopImages = []
        for i in range(10):
            myImage = visual.ImageStim(
                win=win,
                name=shopList[i]['imageName'], 
                image=shopList[i]['animalImage'], 
                mask=None, anchor='center',ori=0.0, 
                pos=(shopPosX[i], shopPosY[i]),
                size=(0.1, 0.1),
                color=[1,1,1], colorSpace='rgb', opacity=None,
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)
            shopImages.append(myImage)
        # Run 'Begin Routine' code from makeShelfStim
        # I move this to begin Experiment since the shelves fixed
        # If we want to chagne it each trial, more to Begin Routine
        productImages = []
        
        for count, curImage in enumerate(allList[listNum]):
            image = visual.ImageStim(
            #globals()['image'+str(count+1)] = visual.ImageStim(
                win=win,
                name=curImage['imageName'], 
                image=curImage['animalImage'], 
                mask=None, anchor='center',ori=0.0, 
                pos=(curImage['PositionX'], curImage['PositionY']),
                size=(0.1, 0.1),
                color=[1,1,1], colorSpace='rgb', opacity=None,
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=0.0)
            image.pair = curImage['pair']
            variable_name = 'image' + str(count + 1)
            globals()[variable_name] = image
            #productImages.append(eval('image'+str(count+1))
            productImages.append(image)
            
        clickables = productImages.copy() #Added here
        # keep track of which components have finished
        initializeNewTrialComponents = []
        for thisComponent in initializeNewTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "initializeNewTrial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in initializeNewTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "initializeNewTrial" ---
        for thisComponent in initializeNewTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "initializeNewTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "justStore" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        shopper_2.setPos((storeShopperPosX, storeShopperPosY))
        shopper_2.setSize((storeShopperSizeW, storeShopperSizeH))
        shopper_2.setImage(storeShopperImage)
        # Run 'Begin Routine' code from drawShelfStim_2
        for image in productImages:
            image.setAutoDraw(True)
        # setup some python lists for storing info about the imageMouse_2
        imageMouse_2.x = []
        imageMouse_2.y = []
        imageMouse_2.leftButton = []
        imageMouse_2.midButton = []
        imageMouse_2.rightButton = []
        imageMouse_2.time = []
        imageMouse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from clickResponse_2
        imageMouse.setPos(newPos = (-0.5,0.4))
        # may a list to store the images they click
        #clickables = productImages
        # clikedImages is the imageStim object, clickedImageName is the corresponding 
        # name. This is the final list. allClickedImageName are all the product they 
        # ever clicked, including those put into the cart but remove later, the clicked 
        # back is remomved for now,so remove the variable for now 04/2022 
        clickedImages = []
        clickedImagesName=[]
        clickedImagesTime=[]
        correctClickedsName=[]
        correctClickedsTime=[]
        # allClickedImagesName=[]
        clickedImage = None
        curIncorrectCount=0
        curCorrectCount=0
        curStarCount=starCounts
        
        #for item in clickedImages:
        #        pair_label = item.pair
        #        clickables = [item for item in clickables if item.pair != pair_label]
        
        cartPosX = [0.10,0.19,0.28,0.37,0.46,
        0.10,0.19,0.28,0.37,0.46,
        0.10,0.19,0.28,0.37,0.46,
        0.10,0.19,0.28,0.37,0.46,]
        cartPosY = [-0.34,-0.34,-0.34,-0.34,-0.34,
        -0.42,-0.42,-0.42,-0.42,-0.42,
        -0.34,-0.34,-0.34,-0.34,-0.34,
        -0.42,-0.42,-0.42,-0.42,-0.42]
        # keep track of which components have finished
        justStoreComponents = [shoppingbasket_3, SmallShelf5_2, SmallShelf5_1, SmallShelf1_1, SmallShelf1_2, SmallShelf2_1, SmallShelf2_2, SmallShelf3_1, SmallShelf3_2, SmallShelf4_1, SmallShelf4_2, shopper_2, kid_2, imageMouse_2]
        for thisComponent in justStoreComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "justStore" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *shoppingbasket_3* updates
            if shoppingbasket_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                shoppingbasket_3.frameNStart = frameN  # exact frame index
                shoppingbasket_3.tStart = t  # local t and not account for scr refresh
                shoppingbasket_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(shoppingbasket_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'shoppingbasket_3.started')
                shoppingbasket_3.setAutoDraw(True)
            
            # *SmallShelf5_2* updates
            if SmallShelf5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf5_2.frameNStart = frameN  # exact frame index
                SmallShelf5_2.tStart = t  # local t and not account for scr refresh
                SmallShelf5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf5_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf5_2.started')
                SmallShelf5_2.setAutoDraw(True)
            
            # *SmallShelf5_1* updates
            if SmallShelf5_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf5_1.frameNStart = frameN  # exact frame index
                SmallShelf5_1.tStart = t  # local t and not account for scr refresh
                SmallShelf5_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf5_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf5_1.started')
                SmallShelf5_1.setAutoDraw(True)
            
            # *SmallShelf1_1* updates
            if SmallShelf1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf1_1.frameNStart = frameN  # exact frame index
                SmallShelf1_1.tStart = t  # local t and not account for scr refresh
                SmallShelf1_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf1_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf1_1.started')
                SmallShelf1_1.setAutoDraw(True)
            
            # *SmallShelf1_2* updates
            if SmallShelf1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf1_2.frameNStart = frameN  # exact frame index
                SmallShelf1_2.tStart = t  # local t and not account for scr refresh
                SmallShelf1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf1_2.started')
                SmallShelf1_2.setAutoDraw(True)
            
            # *SmallShelf2_1* updates
            if SmallShelf2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf2_1.frameNStart = frameN  # exact frame index
                SmallShelf2_1.tStart = t  # local t and not account for scr refresh
                SmallShelf2_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf2_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf2_1.started')
                SmallShelf2_1.setAutoDraw(True)
            
            # *SmallShelf2_2* updates
            if SmallShelf2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf2_2.frameNStart = frameN  # exact frame index
                SmallShelf2_2.tStart = t  # local t and not account for scr refresh
                SmallShelf2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf2_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf2_2.started')
                SmallShelf2_2.setAutoDraw(True)
            
            # *SmallShelf3_1* updates
            if SmallShelf3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf3_1.frameNStart = frameN  # exact frame index
                SmallShelf3_1.tStart = t  # local t and not account for scr refresh
                SmallShelf3_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf3_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf3_1.started')
                SmallShelf3_1.setAutoDraw(True)
            
            # *SmallShelf3_2* updates
            if SmallShelf3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf3_2.frameNStart = frameN  # exact frame index
                SmallShelf3_2.tStart = t  # local t and not account for scr refresh
                SmallShelf3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf3_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf3_2.started')
                SmallShelf3_2.setAutoDraw(True)
            
            # *SmallShelf4_1* updates
            if SmallShelf4_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf4_1.frameNStart = frameN  # exact frame index
                SmallShelf4_1.tStart = t  # local t and not account for scr refresh
                SmallShelf4_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf4_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf4_1.started')
                SmallShelf4_1.setAutoDraw(True)
            
            # *SmallShelf4_2* updates
            if SmallShelf4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SmallShelf4_2.frameNStart = frameN  # exact frame index
                SmallShelf4_2.tStart = t  # local t and not account for scr refresh
                SmallShelf4_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SmallShelf4_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SmallShelf4_2.started')
                SmallShelf4_2.setAutoDraw(True)
            
            # *shopper_2* updates
            if shopper_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                shopper_2.frameNStart = frameN  # exact frame index
                shopper_2.tStart = t  # local t and not account for scr refresh
                shopper_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(shopper_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'shopper_2.started')
                shopper_2.setAutoDraw(True)
            
            # *kid_2* updates
            if kid_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                kid_2.frameNStart = frameN  # exact frame index
                kid_2.tStart = t  # local t and not account for scr refresh
                kid_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(kid_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'kid_2.started')
                kid_2.setAutoDraw(True)
            # *imageMouse_2* updates
            if imageMouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imageMouse_2.frameNStart = frameN  # exact frame index
                imageMouse_2.tStart = t  # local t and not account for scr refresh
                imageMouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imageMouse_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('imageMouse_2.started', t)
                imageMouse_2.status = STARTED
                imageMouse_2.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if imageMouse_2.status == STARTED:  # only update if started and not finished!
                buttons = imageMouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(shopper_2)
                            clickableList = shopper_2
                        except:
                            clickableList = [shopper_2]
                        for obj in clickableList:
                            if obj.contains(imageMouse_2):
                                gotValidClick = True
                                imageMouse_2.clicked_name.append(obj.name)
                        x, y = imageMouse_2.getPos()
                        imageMouse_2.x.append(x)
                        imageMouse_2.y.append(y)
                        buttons = imageMouse_2.getPressed()
                        imageMouse_2.leftButton.append(buttons[0])
                        imageMouse_2.midButton.append(buttons[1])
                        imageMouse_2.rightButton.append(buttons[2])
                        imageMouse_2.time.append(imageMouse_2.mouseClock.getTime())
            # Run 'Each Frame' code from clickResponse_2
            #collect the cliked image and make the copy and calculat the correct and incorrect clicked
            #here the logic is that if the mouse is press (new or lingeringone) in any clickable, 
            #it break the for loop. And if all the clickable is not click, then clear out the clickedImage.
            #So it prevent it from collect the same click across frames.
            #NEW
            
            for clickable in clickables:
                if clickable.contains(imageMouse):
                    #clickables.remove(clickable)
                    #pair_label = clickable.pair
                    #clickables = [item for item in clickables if item.pair != pair_label]
                    #if clickable in shopImages: #Tried doing this to get rid of sticky image. No luck
                        #shopImages.remove(clickable)
            
            #     if imageMouse.isPressedIn(clickable): 
                    if clickedImage == None:
                        clickedImage = copyImage(clickable,
                                    (cartPosX[0],cartPosY[0]),
                                    clickable.name,0.07)
                        clickedImages.append(clickedImage)
                        # clickedImagesName are the images that art in the basket, if inclued 
                        # once the click on the selved and remove those click back, the click back
                        # function is disable currently 04/2022
                        clickedImagesName.append(clickedImage.name)
                        clickedImagesTime.append(t)
                        # allClickedImagesName.append(clickedImage.name)
                        cartPosX.pop(0)
                        cartPosY.pop(0)
                        #this is to collect the correct and incorrect response and mark the correct on the template
                        if clickable.name in curCorrectImages:
                            correctSound.stop()
                            wrongSound.stop()
                            correctSound.play()                  
                            #correctClickedsName.append(clickable.name)
                            #correctClickedsTime.append(t)
                            #correctCount +=1
                            # print(correctCount)
                            curCorrectCount +=1
                            # remove the already clicked correct image so it can't be count as two correct
                            #curCorrectImages.remove(clickable.name)
                            #shopImages[correctImages.index(clickable.name)].mask='image\cross.jpg'
                        else:
                            correctSound.stop()
                            wrongSound.stop()
                            wrongSound.play()                  
                            #incorrectCount +=1
                            curIncorrectCount +=1
                        #this is to count the stars
                        if starCounts+curCorrectCount-curIncorrectCount<0:
                            curStarCount = 0
                            starCounts = 0
                            curIncorrectCount = 0
                            curCorrectCount =0
                        else:
                            curStarCount = starCounts+curCorrectCount-curIncorrectCount
                        #this line reset the mouse pos so it is not stay in the same place
                        imageMouse.setPos(newPos=(-0.5,0.4))
                        break
                    else:
                        #this line reset the mouse pos so it is not stay in the same place
                        imageMouse.setPos(newPos=(-0.5,0.4))
                        break
            else:
                if clickedImage is not None:
                    clickedImage = None
                
                        
                        
            
                   
            ## prevent the mouse collecting the same click accross frames
            #if clickedImage is not None and imageMouse.getPressed()[0] == 0:
            #    clickedImage = None
                
            ##remove image from the cart if it is clicked and also free up the space
            #for cartIndex, cartImage in enumerate(clickedImages):
            ##    if  clickImage.contains(imageMouse):
            #     if imageMouse.isPressedIn(cartImage):
            #        cartPosX.insert(0,cartImage.pos[0])
            #        cartPosY.insert(0,cartImage.pos[1])
            #        clickedImages.pop(cartIndex)
            #        clickedImagesName.remove(cartImage.name)
            
            drawClicked(clickedImages)     
            stars=makeStars(curStarCount,starsPosX,starsPosY)
            drawStars(stars)
            
            if correctCount >=6:
                continueRoutine = False 
                delayDuration =0
                oneTrial.finished=True
                
            
            if  shopper_2.contains(imageMouse_2):
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in justStoreComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "justStore" ---
        for thisComponent in justStoreComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from drawShelfStim_2
        for image in productImages:
            
            image.setAutoDraw(False)
            
        #for image in clickedImages:
        #    image.setAutoDraw(False)
        #for image in shopImages:
        #    image.setAutoDraw(False)
            
        #for clicked in everyClicked:
        #    clicked.setAutoDraw(False)
        
        
        # store data for multipleTrials (TrialHandler)
        multipleTrials.addData('imageMouse_2.x', imageMouse_2.x)
        multipleTrials.addData('imageMouse_2.y', imageMouse_2.y)
        multipleTrials.addData('imageMouse_2.leftButton', imageMouse_2.leftButton)
        multipleTrials.addData('imageMouse_2.midButton', imageMouse_2.midButton)
        multipleTrials.addData('imageMouse_2.rightButton', imageMouse_2.rightButton)
        multipleTrials.addData('imageMouse_2.time', imageMouse_2.time)
        multipleTrials.addData('imageMouse_2.clicked_name', imageMouse_2.clicked_name)
        # the Routine "justStore" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "mask" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        maskComponents = [maskText, walkingShopper, kid2]
        for thisComponent in maskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mask" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *maskText* updates
            if maskText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maskText.frameNStart = frameN  # exact frame index
                maskText.tStart = t  # local t and not account for scr refresh
                maskText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(maskText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'maskText.started')
                maskText.setAutoDraw(True)
            if maskText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maskText.tStartRefresh + delayDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    maskText.tStop = t  # not accounting for scr refresh
                    maskText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maskText.stopped')
                    maskText.setAutoDraw(False)
            
            # *walkingShopper* updates
            if walkingShopper.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                walkingShopper.frameNStart = frameN  # exact frame index
                walkingShopper.tStart = t  # local t and not account for scr refresh
                walkingShopper.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(walkingShopper, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'walkingShopper.started')
                walkingShopper.setAutoDraw(True)
            if walkingShopper.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > walkingShopper.tStartRefresh + delayDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    walkingShopper.tStop = t  # not accounting for scr refresh
                    walkingShopper.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'walkingShopper.stopped')
                    walkingShopper.setAutoDraw(False)
            if walkingShopper.status == STARTED:  # only update if drawing
                walkingShopper.setPos((-0.65+0.5*t/delayDuration, -0.4), log=False)
            
            # *kid2* updates
            if kid2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                kid2.frameNStart = frameN  # exact frame index
                kid2.tStart = t  # local t and not account for scr refresh
                kid2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(kid2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'kid2.started')
                kid2.setAutoDraw(True)
            if kid2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > kid2.tStartRefresh + delayDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    kid2.tStop = t  # not accounting for scr refresh
                    kid2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'kid2.stopped')
                    kid2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mask" ---
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "mask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        oneTrial = data.TrialHandler(nReps=repeatTimes, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='oneTrial')
        thisExp.addLoop(oneTrial)  # add the loop to the experiment
        thisOneTrial = oneTrial.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisOneTrial.rgb)
        if thisOneTrial != None:
            for paramName in thisOneTrial:
                exec('{} = thisOneTrial[paramName]'.format(paramName))
        
        for thisOneTrial in oneTrial:
            currentLoop = oneTrial
            # abbreviate parameter names if possible (e.g. rgb = thisOneTrial.rgb)
            if thisOneTrial != None:
                for paramName in thisOneTrial:
                    exec('{} = thisOneTrial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "template" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from drawShopStim
            if oneTrial.finished:
                continueRoutine = False 
                
            listimage2.setAutoDraw(True)
            
            for image in shopImages:
               image.setAutoDraw(True)
            
            win.getMovieFrame()
            # setup some python lists for storing info about the goRightMouse
            goRightMouse.clicked_name = []
            gotValidClick = False  # until a click is received
            goRightMouse.mouseClock.reset()
            # keep track of which components have finished
            templateComponents = [goRight, goRightMouse, clock]
            for thisComponent in templateComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "template" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *goRight* updates
                if goRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    goRight.frameNStart = frameN  # exact frame index
                    goRight.tStart = t  # local t and not account for scr refresh
                    goRight.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(goRight, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'goRight.started')
                    goRight.setAutoDraw(True)
                # *goRightMouse* updates
                if goRightMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    goRightMouse.frameNStart = frameN  # exact frame index
                    goRightMouse.tStart = t  # local t and not account for scr refresh
                    goRightMouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(goRightMouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'goRightMouse.started')
                    goRightMouse.status = STARTED
                    prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
                if goRightMouse.status == STARTED:  # only update if started and not finished!
                    buttons = goRightMouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(goRight)
                                clickableList = goRight
                            except:
                                clickableList = [goRight]
                            for obj in clickableList:
                                if obj.contains(goRightMouse):
                                    gotValidClick = True
                                    goRightMouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                # Run 'Each Frame' code from endList
                if  goRight.contains(goRightMouse):
                    continueRoutine = False     
                
                # *clock* updates
                if clock.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
                    # keep track of start time/frame for later
                    clock.frameNStart = frameN  # exact frame index
                    clock.tStart = t  # local t and not account for scr refresh
                    clock.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(clock, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'clock.started')
                    clock.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in templateComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "template" ---
            for thisComponent in templateComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from drawShopStim
            for image in shopImages:
                image.setAutoDraw(False)
            
            listimage2.setAutoDraw(False)
            
            oneTrial.addData("templateTime", t);
            oneTrial.addData("templateFrame", frameN);
            
            win.saveMovieFrames("list.png")
            
            # store data for oneTrial (TrialHandler)
            x, y = goRightMouse.getPos()
            buttons = goRightMouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(goRight)
                    clickableList = goRight
                except:
                    clickableList = [goRight]
                for obj in clickableList:
                    if obj.contains(goRightMouse):
                        gotValidClick = True
                        goRightMouse.clicked_name.append(obj.name)
            oneTrial.addData('goRightMouse.x', x)
            oneTrial.addData('goRightMouse.y', y)
            oneTrial.addData('goRightMouse.leftButton', buttons[0])
            oneTrial.addData('goRightMouse.midButton', buttons[1])
            oneTrial.addData('goRightMouse.rightButton', buttons[2])
            if len(goRightMouse.clicked_name):
                oneTrial.addData('goRightMouse.clicked_name', goRightMouse.clicked_name[0])
            # the Routine "template" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "working" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            shopper.setPos((shopperPosX, shopperPosY))
            shopper.setSize((shopperSizeW, shopperSizeH))
            shopper.setImage(shopperImage)
            # Run 'Begin Routine' code from drawShelfStim
            for image in productImages:
                image.setAutoDraw(True)
                
            win.getMovieFrame()
            # setup some python lists for storing info about the imageMouse
            imageMouse.x = []
            imageMouse.y = []
            imageMouse.leftButton = []
            imageMouse.midButton = []
            imageMouse.rightButton = []
            imageMouse.time = []
            imageMouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # Run 'Begin Routine' code from clickResponse
            #Trying to make items clickable again after list trip
            clickables = productImages.copy()
            for clickable in clickables:
                makeWhite([clickable])
            
            imageMouse.setPos(newPos = (-0.5,0.4))
            # may a list to store the images they click
            
            
            # clikedImages is the imageStim object, clickedImageName is the corresponding 
            # name. This is the final list. allClickedImageName are all the product they 
            # ever clicked, including those put into the cart but remove later, the clicked 
            # back is remomved for now,so remove the variable for now 04/2022 
            clickedImages = []
            clickedImagesPair = []
            clickedImagesName=[]
            clickedImagesTime=[]
            correctClickedsName=[]
            correctClickedsTime=[]
            # allClickedImagesName=[]
            clickedImage = None
            curIncorrectCount=0
            curCorrectCount=0
            curStarCount=starCounts
            
            #for item in clickedImages:
            #        pair_label = item.pair
            #        clickables = [item for item in clickables if item.pair != pair_label]
            
            
            
            
            cartPosX = [0.10,0.19,0.28,0.37,0.46,
            0.10,0.19,0.28,0.37,0.46,
            0.10,0.19,0.28,0.37,0.46,
            0.10,0.19,0.28,0.37,0.46,]
            cartPosY = [-0.34,-0.34,-0.34,-0.34,-0.34,
            -0.42,-0.42,-0.42,-0.42,-0.42,
            -0.34,-0.34,-0.34,-0.34,-0.34,
            -0.42,-0.42,-0.42,-0.42,-0.42]
            
            
            # keep track of which components have finished
            workingComponents = [shoppingbasket, SmallShelf5_1_2, SmallShelf5_1_1, SmallShelf1_1_1, SmallShelf1_1_2, SmallShelf2_1_1, SmallShelf2_1_2, SmallShelf3_1_1, SmallShelf3_1_2, SmallShelf4_1_1, SmallShelf4_1_2, shopper, kid, imageMouse]
            for thisComponent in workingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "working" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *shoppingbasket* updates
                if shoppingbasket.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    shoppingbasket.frameNStart = frameN  # exact frame index
                    shoppingbasket.tStart = t  # local t and not account for scr refresh
                    shoppingbasket.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(shoppingbasket, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'shoppingbasket.started')
                    shoppingbasket.setAutoDraw(True)
                
                # *SmallShelf5_1_2* updates
                if SmallShelf5_1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf5_1_2.frameNStart = frameN  # exact frame index
                    SmallShelf5_1_2.tStart = t  # local t and not account for scr refresh
                    SmallShelf5_1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf5_1_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf5_1_2.started')
                    SmallShelf5_1_2.setAutoDraw(True)
                
                # *SmallShelf5_1_1* updates
                if SmallShelf5_1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf5_1_1.frameNStart = frameN  # exact frame index
                    SmallShelf5_1_1.tStart = t  # local t and not account for scr refresh
                    SmallShelf5_1_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf5_1_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf5_1_1.started')
                    SmallShelf5_1_1.setAutoDraw(True)
                
                # *SmallShelf1_1_1* updates
                if SmallShelf1_1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf1_1_1.frameNStart = frameN  # exact frame index
                    SmallShelf1_1_1.tStart = t  # local t and not account for scr refresh
                    SmallShelf1_1_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf1_1_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf1_1_1.started')
                    SmallShelf1_1_1.setAutoDraw(True)
                
                # *SmallShelf1_1_2* updates
                if SmallShelf1_1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf1_1_2.frameNStart = frameN  # exact frame index
                    SmallShelf1_1_2.tStart = t  # local t and not account for scr refresh
                    SmallShelf1_1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf1_1_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf1_1_2.started')
                    SmallShelf1_1_2.setAutoDraw(True)
                
                # *SmallShelf2_1_1* updates
                if SmallShelf2_1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf2_1_1.frameNStart = frameN  # exact frame index
                    SmallShelf2_1_1.tStart = t  # local t and not account for scr refresh
                    SmallShelf2_1_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf2_1_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf2_1_1.started')
                    SmallShelf2_1_1.setAutoDraw(True)
                
                # *SmallShelf2_1_2* updates
                if SmallShelf2_1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf2_1_2.frameNStart = frameN  # exact frame index
                    SmallShelf2_1_2.tStart = t  # local t and not account for scr refresh
                    SmallShelf2_1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf2_1_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf2_1_2.started')
                    SmallShelf2_1_2.setAutoDraw(True)
                
                # *SmallShelf3_1_1* updates
                if SmallShelf3_1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf3_1_1.frameNStart = frameN  # exact frame index
                    SmallShelf3_1_1.tStart = t  # local t and not account for scr refresh
                    SmallShelf3_1_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf3_1_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf3_1_1.started')
                    SmallShelf3_1_1.setAutoDraw(True)
                
                # *SmallShelf3_1_2* updates
                if SmallShelf3_1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf3_1_2.frameNStart = frameN  # exact frame index
                    SmallShelf3_1_2.tStart = t  # local t and not account for scr refresh
                    SmallShelf3_1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf3_1_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf3_1_2.started')
                    SmallShelf3_1_2.setAutoDraw(True)
                
                # *SmallShelf4_1_1* updates
                if SmallShelf4_1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf4_1_1.frameNStart = frameN  # exact frame index
                    SmallShelf4_1_1.tStart = t  # local t and not account for scr refresh
                    SmallShelf4_1_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf4_1_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf4_1_1.started')
                    SmallShelf4_1_1.setAutoDraw(True)
                
                # *SmallShelf4_1_2* updates
                if SmallShelf4_1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SmallShelf4_1_2.frameNStart = frameN  # exact frame index
                    SmallShelf4_1_2.tStart = t  # local t and not account for scr refresh
                    SmallShelf4_1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SmallShelf4_1_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SmallShelf4_1_2.started')
                    SmallShelf4_1_2.setAutoDraw(True)
                
                # *shopper* updates
                if shopper.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    shopper.frameNStart = frameN  # exact frame index
                    shopper.tStart = t  # local t and not account for scr refresh
                    shopper.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(shopper, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'shopper.started')
                    shopper.setAutoDraw(True)
                
                # *kid* updates
                if kid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    kid.frameNStart = frameN  # exact frame index
                    kid.tStart = t  # local t and not account for scr refresh
                    kid.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(kid, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'kid.started')
                    kid.setAutoDraw(True)
                # *imageMouse* updates
                if imageMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    imageMouse.frameNStart = frameN  # exact frame index
                    imageMouse.tStart = t  # local t and not account for scr refresh
                    imageMouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(imageMouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('imageMouse.started', t)
                    imageMouse.status = STARTED
                    imageMouse.mouseClock.reset()
                    prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
                if imageMouse.status == STARTED:  # only update if started and not finished!
                    buttons = imageMouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(shopper)
                                clickableList = shopper
                            except:
                                clickableList = [shopper]
                            for obj in clickableList:
                                if obj.contains(imageMouse):
                                    gotValidClick = True
                                    imageMouse.clicked_name.append(obj.name)
                            x, y = imageMouse.getPos()
                            imageMouse.x.append(x)
                            imageMouse.y.append(y)
                            buttons = imageMouse.getPressed()
                            imageMouse.leftButton.append(buttons[0])
                            imageMouse.midButton.append(buttons[1])
                            imageMouse.rightButton.append(buttons[2])
                            imageMouse.time.append(imageMouse.mouseClock.getTime())
                # Run 'Each Frame' code from clickResponse
                #collect the cliked image and make the copy and calculat the correct and incorrect clicked
                #here the logic is that if the mouse is press (new or lingeringone) in any clickable, 
                #it break the for loop. And if all the clickable is not click, then clear out the clickedImage.
                #So it prevent it from collect the same click across frames.
                
                
                for clickable in clickables:
                    if clickable.contains(imageMouse):
                        clickables.remove(clickable) 
                        makeGrey([clickable])
                        clickedImagesPair.append(clickable.pair) 
                        pair_label = clickable.pair
                        same_pair_items = [item for item in clickables if item.pair == pair_label]
                        makeGrey(same_pair_items)
                        clickables = [item for item in clickables if item.pair != pair_label]
                        
                
                
                #     if imageMouse.isPressedIn(clickable): 
                        if clickedImage == None:
                            clickedImage = copyImage(clickable,
                                        (cartPosX[0],cartPosY[0]),
                                        clickable.name,0.07)
                            clickedImages.append(clickedImage)
                
                            # clickedImagesName are the images that art in the basket, if inclued 
                            # ones the clied on the selved and remove those click back, the click back
                            # function is disable currently 04/2022
                            clickedImagesName.append(clickedImage.name)
                            clickedImagesTime.append(t)
                            # allClickedImagesName.append(clickedImage.name)
                            cartPosX.pop(0)
                            cartPosY.pop(0)
                            #this is to collect the correct and incorrect response and mark the correct on the template
                            if clickable.name in curCorrectImages:
                                correctSound.stop()
                                wrongSound.stop()
                                correctSound.play()                  
                                correctClickedsName.append(clickable.name)
                                correctClickedsTime.append(t)
                                correctCount +=1
                                # print(correctCount)
                                curCorrectCount +=1
                                # remove the already clicked correct image so it can't be count as two correct
                                curCorrectImages.remove(clickable.name)
                                shopImages[correctImages.index(clickable.name)].mask='image\cross.jpg'
                            else:
                                correctSound.stop()
                                wrongSound.stop()
                                wrongSound.play()                  
                                incorrectCount +=1
                                curIncorrectCount +=1
                            #this is to count the stars
                            if starCounts+curCorrectCount-curIncorrectCount<0:
                                curStarCount = 0
                                starCounts = 0
                                curIncorrectCount = 0
                                curCorrectCount =0
                            else:
                                curStarCount = starCounts+curCorrectCount-curIncorrectCount
                            #this line reset the mouse pos so it is not stay in the same place
                            imageMouse.setPos(newPos=(-0.5,0.4))
                            break
                        else:
                            #this line reset the mouse pos so it is not stay in the same place
                            imageMouse.setPos(newPos=(-0.5,0.4))
                            break
                else:
                    if clickedImage is not None:
                        clickedImage = None
                
                
                        clickedImage = None
                
                
                    
                
                
                       
                ## prevent the mouse collecting the same click accross frames
                #if clickedImage is not None and imageMouse.getPressed()[0] == 0:
                #    clickedImage = None
                    
                ##remove image from the cart if it is clicked and also free up the space
                #for cartIndex, cartImage in enumerate(clickedImages):
                ##    if  clickImage.contains(imageMouse):
                #     if imageMouse.isPressedIn(cartImage):
                #        cartPosX.insert(0,cartImage.pos[0])
                #        cartPosY.insert(0,cartImage.pos[1])
                #        clickedImages.pop(cartIndex)
                #        clickedImagesName.remove(cartImage.name)
                
                drawClicked(clickedImages)     
                stars=makeStars(curStarCount,starsPosX,starsPosY)
                drawStars(stars)
                
                #NEW code below and commented out old code
                if correctCount >= 6 and shopper.contains(imageMouse) and closing == 0:
                    continueRoutine = False
                    delayDuration = 0
                    oneTrial.finished = True
                #if correctCount >=6:
                #    continueRoutine = False 
                #    delayDuration =0
                #    oneTrial.finished=True
                #NEW code below
                #if not clickables:
                #    oneTrial.finished=True
                
                if  shopper.contains(imageMouse) and closing == 0:
                    continueRoutine = False
                    
                if closing == 1 and not clickables:
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in workingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "working" ---
            for thisComponent in workingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from drawShelfStim
            for image in productImages:
                image.setAutoDraw(False)
            
            win.saveMovieFrames("shelf.png")
            # store data for oneTrial (TrialHandler)
            oneTrial.addData('imageMouse.x', imageMouse.x)
            oneTrial.addData('imageMouse.y', imageMouse.y)
            oneTrial.addData('imageMouse.leftButton', imageMouse.leftButton)
            oneTrial.addData('imageMouse.midButton', imageMouse.midButton)
            oneTrial.addData('imageMouse.rightButton', imageMouse.rightButton)
            oneTrial.addData('imageMouse.time', imageMouse.time)
            oneTrial.addData('imageMouse.clicked_name', imageMouse.clicked_name)
            # Run 'End Routine' code from clickResponse
            oneTrial.addData("nCorrect", correctCount);
            oneTrial.addData("nIncorrect", incorrectCount);
            oneTrial.addData("clickedImages", clickedImagesName);
            oneTrial.addData("whichPair", clickedImagesPair);
            oneTrial.addData("clickedImagesTime", clickedImagesTime);
            # no click back function, no need for allClickedImages
            # oneTrial.addData("alLClickedImages", allClickedImagesName);
            oneTrial.addData("correctClickedsName",correctClickedsName)
            oneTrial.addData("correctClickedsTime",correctClickedsTime)
            oneTrial.addData("correctImages",correctImages);
            oneTrial.addData("curCorrectImages",curCorrectImages)
            oneTrial.addData("workingTime", t);
            oneTrial.addData("workingFrame", frameN);
            starCounts=curStarCount
            
            
            
            
            # the Routine "working" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "mask" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            maskComponents = [maskText, walkingShopper, kid2]
            for thisComponent in maskComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mask" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *maskText* updates
                if maskText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    maskText.frameNStart = frameN  # exact frame index
                    maskText.tStart = t  # local t and not account for scr refresh
                    maskText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(maskText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maskText.started')
                    maskText.setAutoDraw(True)
                if maskText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > maskText.tStartRefresh + delayDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        maskText.tStop = t  # not accounting for scr refresh
                        maskText.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'maskText.stopped')
                        maskText.setAutoDraw(False)
                
                # *walkingShopper* updates
                if walkingShopper.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    walkingShopper.frameNStart = frameN  # exact frame index
                    walkingShopper.tStart = t  # local t and not account for scr refresh
                    walkingShopper.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(walkingShopper, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'walkingShopper.started')
                    walkingShopper.setAutoDraw(True)
                if walkingShopper.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > walkingShopper.tStartRefresh + delayDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        walkingShopper.tStop = t  # not accounting for scr refresh
                        walkingShopper.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'walkingShopper.stopped')
                        walkingShopper.setAutoDraw(False)
                if walkingShopper.status == STARTED:  # only update if drawing
                    walkingShopper.setPos((-0.65+0.5*t/delayDuration, -0.4), log=False)
                
                # *kid2* updates
                if kid2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    kid2.frameNStart = frameN  # exact frame index
                    kid2.tStart = t  # local t and not account for scr refresh
                    kid2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(kid2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'kid2.started')
                    kid2.setAutoDraw(True)
                if kid2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > kid2.tStartRefresh + delayDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        kid2.tStop = t  # not accounting for scr refresh
                        kid2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'kid2.stopped')
                        kid2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in maskComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mask" ---
            for thisComponent in maskComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "mask" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed repeatTimes repeats of 'oneTrial'
        
        
        # --- Prepare to start Routine "trialFeedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from makeFeedback
        if realOrNot ==1:
            totalStars = totalStars + starCounts
        
        if starCounts >0:
            trialFeedback="Great! You win %i sticker.\n Lets try another trial "%(starCounts)
        else:
            trialFeedback="Sorry, you didn't win any sticker.\n Lets try another trial "
            
        
        trialFeedBackPress.keys = []
        trialFeedBackPress.rt = []
        _trialFeedBackPress_allKeys = []
        trialFeedBackText.setText(trialFeedback)
        # keep track of which components have finished
        trialFeedbackComponents = [trialFeedBackPress, goodJobV, goodJobI, trialFeedBackText]
        for thisComponent in trialFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFeedback" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trialFeedBackPress* updates
            waitOnFlip = False
            if trialFeedBackPress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialFeedBackPress.frameNStart = frameN  # exact frame index
                trialFeedBackPress.tStart = t  # local t and not account for scr refresh
                trialFeedBackPress.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialFeedBackPress, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialFeedBackPress.started')
                trialFeedBackPress.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trialFeedBackPress.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trialFeedBackPress.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trialFeedBackPress.status == STARTED and not waitOnFlip:
                theseKeys = trialFeedBackPress.getKeys(keyList=['q'], waitRelease=False)
                _trialFeedBackPress_allKeys.extend(theseKeys)
                if len(_trialFeedBackPress_allKeys):
                    trialFeedBackPress.keys = _trialFeedBackPress_allKeys[-1].name  # just the last key pressed
                    trialFeedBackPress.rt = _trialFeedBackPress_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *goodJobV* updates
            if goodJobV.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                goodJobV.frameNStart = frameN  # exact frame index
                goodJobV.tStart = t  # local t and not account for scr refresh
                goodJobV.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(goodJobV, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'goodJobV.started')
                goodJobV.setAutoDraw(True)
            if goodJobV.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > goodJobV.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    goodJobV.tStop = t  # not accounting for scr refresh
                    goodJobV.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'goodJobV.stopped')
                    goodJobV.setAutoDraw(False)
            
            # *goodJobI* updates
            if goodJobI.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
                # keep track of start time/frame for later
                goodJobI.frameNStart = frameN  # exact frame index
                goodJobI.tStart = t  # local t and not account for scr refresh
                goodJobI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(goodJobI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'goodJobI.started')
                goodJobI.setAutoDraw(True)
            
            # *trialFeedBackText* updates
            if trialFeedBackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialFeedBackText.frameNStart = frameN  # exact frame index
                trialFeedBackText.tStart = t  # local t and not account for scr refresh
                trialFeedBackText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialFeedBackText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialFeedBackText.started')
                trialFeedBackText.setAutoDraw(True)
            # Run 'Each Frame' code from endBlock
            if event.getKeys(['p']):
              continueRoutine = False
              multipleTrials.finished = 1
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFeedback" ---
        for thisComponent in trialFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if trialFeedBackPress.keys in ['', [], None]:  # No response was made
            trialFeedBackPress.keys = None
        multipleTrials.addData('trialFeedBackPress.keys',trialFeedBackPress.keys)
        if trialFeedBackPress.keys != None:  # we had a response
            multipleTrials.addData('trialFeedBackPress.rt', trialFeedBackPress.rt)
        goodJobV.stop()
        # the Routine "trialFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'multipleTrials'
    
    
    # --- Prepare to start Routine "finalQ" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sMarket.setPos((0, finalQSMY))
    cStore.setPos((0, finalQCSY))
    endQ.keys = []
    endQ.rt = []
    _endQ_allKeys = []
    # keep track of which components have finished
    finalQComponents = [sMarket, cStore, endQ]
    for thisComponent in finalQComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "finalQ" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sMarket* updates
        if sMarket.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sMarket.frameNStart = frameN  # exact frame index
            sMarket.tStart = t  # local t and not account for scr refresh
            sMarket.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sMarket, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sMarket.started')
            sMarket.setAutoDraw(True)
        if sMarket.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sMarket.tStartRefresh + finalQduration-frameTolerance:
                # keep track of stop time/frame for later
                sMarket.tStop = t  # not accounting for scr refresh
                sMarket.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sMarket.stopped')
                sMarket.setAutoDraw(False)
        
        # *cStore* updates
        if cStore.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cStore.frameNStart = frameN  # exact frame index
            cStore.tStart = t  # local t and not account for scr refresh
            cStore.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cStore, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cStore.started')
            cStore.setAutoDraw(True)
        if cStore.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cStore.tStartRefresh + finalQduration-frameTolerance:
                # keep track of stop time/frame for later
                cStore.tStop = t  # not accounting for scr refresh
                cStore.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cStore.stopped')
                cStore.setAutoDraw(False)
        
        # *endQ* updates
        waitOnFlip = False
        if endQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endQ.frameNStart = frameN  # exact frame index
            endQ.tStart = t  # local t and not account for scr refresh
            endQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endQ, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endQ.started')
            endQ.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endQ.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endQ.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endQ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endQ.tStartRefresh + finalQduration-frameTolerance:
                # keep track of stop time/frame for later
                endQ.tStop = t  # not accounting for scr refresh
                endQ.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'endQ.stopped')
                endQ.status = FINISHED
        if endQ.status == STARTED and not waitOnFlip:
            theseKeys = endQ.getKeys(keyList=['q'], waitRelease=False)
            _endQ_allKeys.extend(theseKeys)
            if len(_endQ_allKeys):
                endQ.keys = _endQ_allKeys[-1].name  # just the last key pressed
                endQ.rt = _endQ_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finalQComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "finalQ" ---
    for thisComponent in finalQComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if endQ.keys in ['', [], None]:  # No response was made
        endQ.keys = None
    block.addData('endQ.keys',endQ.keys)
    if endQ.keys != None:  # we had a response
        block.addData('endQ.rt', endQ.rt)
    # the Routine "finalQ" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'block'


# --- Prepare to start Routine "expEnd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from expFeedback
expFeedback ="You have done all the shopping.\n You win %i sticker in total. "%(totalStars)

endExp.keys = []
endExp.rt = []
_endExp_allKeys = []
expFeedbackText.setText(expFeedback)
# keep track of which components have finished
expEndComponents = [endExp, expFeedbackText]
for thisComponent in expEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "expEnd" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endExp* updates
    waitOnFlip = False
    if endExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endExp.frameNStart = frameN  # exact frame index
        endExp.tStart = t  # local t and not account for scr refresh
        endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endExp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endExp.started')
        endExp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endExp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endExp.status == STARTED and not waitOnFlip:
        theseKeys = endExp.getKeys(keyList=['q'], waitRelease=False)
        _endExp_allKeys.extend(theseKeys)
        if len(_endExp_allKeys):
            endExp.keys = _endExp_allKeys[-1].name  # just the last key pressed
            endExp.rt = _endExp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *expFeedbackText* updates
    if expFeedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        expFeedbackText.frameNStart = frameN  # exact frame index
        expFeedbackText.tStart = t  # local t and not account for scr refresh
        expFeedbackText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(expFeedbackText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'expFeedbackText.started')
        expFeedbackText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in expEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "expEnd" ---
for thisComponent in expEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if endExp.keys in ['', [], None]:  # No response was made
    endExp.keys = None
thisExp.addData('endExp.keys',endExp.keys)
if endExp.keys != None:  # we had a response
    thisExp.addData('endExp.rt', endExp.rt)
thisExp.nextEntry()
# the Routine "expEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
