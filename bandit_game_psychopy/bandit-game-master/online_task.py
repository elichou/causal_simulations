#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on May 03, 2022, at 21:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\ralit\\Downloads\\labs\\labs\\online_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "info_start1"
info_start1Clock = core.Clock()
stim_sizes = [0.1, 0.1];
instr = '';
mov = '';
green_f = 0;
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Open Sans',
    pos=(0, 0.05), height=0.02, wrapWidth=0.56, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None,
    ori=0, pos=(-0.1, -0.2), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='sin', mask=None,
    ori=0, pos=(-0.034, -0.2), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None,
    ori=0, pos=(0.034, -0.2), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0, pos=(0.1, -0.2), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "info_stim1"
info_stim1Clock = core.Clock()
stim_sizes = [0.1, 0.1];
instr = '';
mov = '';
green_f = 0;
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0.05), height=0.02, wrapWidth=0.56, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(-0.1, -0.1), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.034, -0.1), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(0.034, -0.1), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0, pos=(0.1, -0.1), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
green_frame = visual.ImageStim(
    win=win,
    name='green_frame', 
    image='outline.png', mask=None,
    ori=0, pos=(0, 0), size=(1.7778, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
portt = [];

stim_sizes = [0.15, 0.15];
fix_size = [0.015,0.015]
cross_fixation = visual.ShapeStim(
    win=win, name='cross_fixation', vertices='cross',
    size=fix_size,
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=-1.0, interpolate=True)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "cues"
cuesClock = core.Clock()
show_me_left = 0
show_me_right = 0
keep_me_left = 0
keep_me_right = 0
correct_count = 0

msg = '';
points_won = 0;
grand_total = 0;
portt = 99;
cross_stim2 = visual.ShapeStim(
    win=win, name='cross_stim2', vertices='cross',
    size=fix_size,
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=-1.0, interpolate=True)
symbol_left = visual.ImageStim(
    win=win,
    name='symbol_left', 
    image='sin', mask=None,
    ori=0, pos=(-0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
symbol_right = visual.ImageStim(
    win=win,
    name='symbol_right', 
    image='sin', mask=None,
    ori=0, pos=(0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "selection_animation"
selection_animationClock = core.Clock()
cross_sel = visual.ShapeStim(
    win=win, name='cross_sel', vertices='cross',
    size=fix_size,
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=-1.0, interpolate=True)
s_left_3 = visual.ImageStim(
    win=win,
    name='s_left_3', 
    image='sin', mask=None,
    ori=0, pos=(-0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
s_right_3 = visual.ImageStim(
    win=win,
    name='s_right_3', 
    image='sin', mask=None,
    ori=0, pos=(0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
s_if_left_3 = visual.ImageStim(
    win=win,
    name='s_if_left_3', 
    image='sin', mask=None,
    ori=0, pos=(-0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
s_if_right_3 = visual.ImageStim(
    win=win,
    name='s_if_right_3', 
    image='sin', mask=None,
    ori=0, pos=(0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
cross_feed = visual.ShapeStim(
    win=win, name='cross_feed', vertices='cross',
    size=fix_size,
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=-1.0, interpolate=True)
s_left = visual.ImageStim(
    win=win,
    name='s_left', 
    image='sin', mask=None,
    ori=0, pos=(-0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
s_right = visual.ImageStim(
    win=win,
    name='s_right', 
    image='sin', mask=None,
    ori=0, pos=(0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
s_if_left = visual.ImageStim(
    win=win,
    name='s_if_left', 
    image='sin', mask=None,
    ori=0, pos=(-0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
s_if_right = visual.ImageStim(
    win=win,
    name='s_if_right', 
    image='sin', mask=None,
    ori=0, pos=(0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "too_slow"
too_slowClock = core.Clock()
cross_slow = visual.ShapeStim(
    win=win, name='cross_slow', vertices='cross',
    size=fix_size,
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=-1.0, interpolate=True)
s_left_2 = visual.ImageStim(
    win=win,
    name='s_left_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
s_right_2 = visual.ImageStim(
    win=win,
    name='s_right_2', 
    image='sin', mask=None,
    ori=0, pos=(0.06, 0), size=stim_sizes,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=[0,-0.06], height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "general_feed"
general_feedClock = core.Clock()
fix_size = [0.02,0.02]
opacity_im = 1
msg_end = '';
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Arial',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ending"
endingClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='Please notify the experimenter that you have completed the task. ',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('prep_stim_info.csv'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "info_start1"-------
    continueRoutine = True
    # update component parameters for each repeat
    if trial_n in [1]:
        continueRoutine = True
    else:
        continueRoutine = False
    
    im1 = 'b_4.png'
    im2 = 'g_4.png'
    im3 = 'p_4.png'
    im4 = 'y_4.png'
    instr = "In this practice block, you will choose between pairs of slot machines (shown below) that give you variable points. To win the game you should select the slot machines strategically so that by the end of the block you have as many points as possible. Select the left or right slot machine by using the left or right keys on the keyboard. You have 2 seconds to make your choice. \n Now we will do a short practice. Press the left or right key to start whenever you're ready."
    
    text_10.setText(instr)
    image_9.setImage(im1)
    image_10.setImage(im2)
    image_11.setImage(im3)
    image_12.setImage(im4)
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    info_start1Components = [text_10, image_9, image_10, image_11, image_12, key_resp_9]
    for thisComponent in info_start1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    info_start1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "info_start1"-------
    while continueRoutine:
        # get current time
        t = info_start1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=info_start1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *image_9* updates
        if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            image_9.setAutoDraw(True)
        
        # *image_10* updates
        if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_10.frameNStart = frameN  # exact frame index
            image_10.tStart = t  # local t and not account for scr refresh
            image_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
            image_10.setAutoDraw(True)
        
        # *image_11* updates
        if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_11.frameNStart = frameN  # exact frame index
            image_11.tStart = t  # local t and not account for scr refresh
            image_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
            image_11.setAutoDraw(True)
        
        # *image_12* updates
        if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            image_12.setAutoDraw(True)
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in info_start1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "info_start1"-------
    for thisComponent in info_start1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('text_10.started', text_10.tStartRefresh)
    trials_3.addData('text_10.stopped', text_10.tStopRefresh)
    trials_3.addData('image_9.started', image_9.tStartRefresh)
    trials_3.addData('image_9.stopped', image_9.tStopRefresh)
    trials_3.addData('image_10.started', image_10.tStartRefresh)
    trials_3.addData('image_10.stopped', image_10.tStopRefresh)
    trials_3.addData('image_11.started', image_11.tStartRefresh)
    trials_3.addData('image_11.stopped', image_11.tStopRefresh)
    trials_3.addData('image_12.started', image_12.tStartRefresh)
    trials_3.addData('image_12.stopped', image_12.tStopRefresh)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    trials_3.addData('key_resp_9.started', key_resp_9.tStartRefresh)
    trials_3.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
    # the Routine "info_start1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "info_stim1"-------
    continueRoutine = True
    # update component parameters for each repeat
    if trial_n in [11]:
        continueRoutine = True
    else:
        continueRoutine = False
        
    
    im1 = 'b_4.png'
    im2 = 'g_4.png'
    im3 = 'p_4.png'
    im4 = 'y_4.png'
    instr = 'Well done! You gained ' + str(points_won) + ' points. There is no perfect number of points but try to always maximise them. \n Press a button to start the main game whenever you`re ready.'
    
    text.setText(instr)
    image.setImage(im1)
    image_2.setImage(im2)
    image_3.setImage(im3)
    image_4.setImage(im4)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    green_frame.setOpacity(green_f)
    # keep track of which components have finished
    info_stim1Components = [text, image, image_2, image_3, image_4, key_resp_2, green_frame]
    for thisComponent in info_stim1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    info_stim1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "info_stim1"-------
    while continueRoutine:
        # get current time
        t = info_stim1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=info_stim1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *green_frame* updates
        if green_frame.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            green_frame.frameNStart = frameN  # exact frame index
            green_frame.tStart = t  # local t and not account for scr refresh
            green_frame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(green_frame, 'tStartRefresh')  # time at next scr refresh
            green_frame.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in info_stim1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "info_stim1"-------
    for thisComponent in info_stim1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('text.started', text.tStartRefresh)
    trials_3.addData('text.stopped', text.tStopRefresh)
    trials_3.addData('image.started', image.tStartRefresh)
    trials_3.addData('image.stopped', image.tStopRefresh)
    trials_3.addData('image_2.started', image_2.tStartRefresh)
    trials_3.addData('image_2.stopped', image_2.tStopRefresh)
    trials_3.addData('image_3.started', image_3.tStartRefresh)
    trials_3.addData('image_3.stopped', image_3.tStopRefresh)
    trials_3.addData('image_4.started', image_4.tStartRefresh)
    trials_3.addData('image_4.stopped', image_4.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials_3.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_3.addData('key_resp_2.rt', key_resp_2.rt)
    trials_3.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials_3.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    trials_3.addData('green_frame.started', green_frame.tStartRefresh)
    trials_3.addData('green_frame.stopped', green_frame.tStopRefresh)
    # the Routine "info_stim1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    # update component parameters for each repeat
    buttons = 0;
    dur_fix = 60
    #dur_fix = randint(low = 120/2, high = 180/2) # values will range from 60 to 90
    thisExp.addData('dur_fix', dur_fix)
    
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    fixationComponents = [cross_fixation, key_resp]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_fixation* updates
        if cross_fixation.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            cross_fixation.frameNStart = frameN  # exact frame index
            cross_fixation.tStart = t  # local t and not account for scr refresh
            cross_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_fixation, 'tStartRefresh')  # time at next scr refresh
            cross_fixation.setAutoDraw(True)
        if cross_fixation.status == STARTED:
            if frameN >= dur_fix:
                # keep track of stop time/frame for later
                cross_fixation.tStop = t  # not accounting for scr refresh
                cross_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_fixation, 'tStopRefresh')  # time at next scr refresh
                cross_fixation.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            if frameN >= dur_fix:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('cross_fixation.started', cross_fixation.tStartRefresh)
    trials_3.addData('cross_fixation.stopped', cross_fixation.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_3.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_3.addData('key_resp.rt', key_resp.rt)
    trials_3.addData('key_resp.started', key_resp.tStartRefresh)
    trials_3.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "cues"-------
    continueRoutine = True
    # update component parameters for each repeat
    dur_cues = 120
    
    if trial_n == 11:
        points_won = 0;
    
    symbol_left.setImage(left)
    symbol_right.setImage(right)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    cuesComponents = [cross_stim2, symbol_left, symbol_right, key_resp_3]
    for thisComponent in cuesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cuesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cues"-------
    while continueRoutine:
        # get current time
        t = cuesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cuesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_stim2* updates
        if cross_stim2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            cross_stim2.frameNStart = frameN  # exact frame index
            cross_stim2.tStart = t  # local t and not account for scr refresh
            cross_stim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_stim2, 'tStartRefresh')  # time at next scr refresh
            cross_stim2.setAutoDraw(True)
        if cross_stim2.status == STARTED:
            if frameN >= dur_cues:
                # keep track of stop time/frame for later
                cross_stim2.tStop = t  # not accounting for scr refresh
                cross_stim2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_stim2, 'tStopRefresh')  # time at next scr refresh
                cross_stim2.setAutoDraw(False)
        
        # *symbol_left* updates
        if symbol_left.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            symbol_left.frameNStart = frameN  # exact frame index
            symbol_left.tStart = t  # local t and not account for scr refresh
            symbol_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symbol_left, 'tStartRefresh')  # time at next scr refresh
            symbol_left.setAutoDraw(True)
        if symbol_left.status == STARTED:
            if frameN >= dur_cues:
                # keep track of stop time/frame for later
                symbol_left.tStop = t  # not accounting for scr refresh
                symbol_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(symbol_left, 'tStopRefresh')  # time at next scr refresh
                symbol_left.setAutoDraw(False)
        
        # *symbol_right* updates
        if symbol_right.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            symbol_right.frameNStart = frameN  # exact frame index
            symbol_right.tStart = t  # local t and not account for scr refresh
            symbol_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symbol_right, 'tStartRefresh')  # time at next scr refresh
            symbol_right.setAutoDraw(True)
        if symbol_right.status == STARTED:
            if frameN >= dur_cues:
                # keep track of stop time/frame for later
                symbol_right.tStop = t  # not accounting for scr refresh
                symbol_right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(symbol_right, 'tStopRefresh')  # time at next scr refresh
                symbol_right.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cuesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cues"-------
    for thisComponent in cuesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    msg = 'Too slow'
    if key_resp_3.keys in 'right':
       show_me_left = 0
       show_me_right = 1
       keep_me_left = 1
       keep_me_right = 0
       feed =  right_rew
       feed_pos = [0.06, -0.028]
       msg = ''
       points_won = points_won + right_rew_dbl;
       grand_total = grand_total + right_rew_dbl;
    elif key_resp_3.keys in 'left':
       show_me_left = 1
       show_me_right = 0
       keep_me_left = 0
       keep_me_right = 1
       feed = left_rew
       feed_pos = [-0.06, -0.028]
       msg = ''
       points_won = points_won + left_rew_dbl;
       grand_total = grand_total + left_rew_dbl;
    elif key_resp_3.keys != None: 
       msg = 'Wrong button'
       show_me_left = 0
       show_me_right = 0
       keep_me_left = 1
       keep_me_right = 1
       feed = left_rew
       feed_pos = [1, -0.01]
    
    if feed_pos == [-0.06, -0.028] and correct == 0:
        correct_count = correct_count+1;
    elif feed_pos == [0.06, -0.028] and correct == 1:
        correct_count = correct_count+1;
    
    trials_3.addData('cross_stim2.started', cross_stim2.tStartRefresh)
    trials_3.addData('cross_stim2.stopped', cross_stim2.tStopRefresh)
    trials_3.addData('symbol_left.started', symbol_left.tStartRefresh)
    trials_3.addData('symbol_left.stopped', symbol_left.tStopRefresh)
    trials_3.addData('symbol_right.started', symbol_right.tStartRefresh)
    trials_3.addData('symbol_right.stopped', symbol_right.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_3.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_3.addData('key_resp_3.rt', key_resp_3.rt)
    trials_3.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials_3.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "cues" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "selection_animation"-------
    continueRoutine = True
    # update component parameters for each repeat
    if msg == 'Wrong button' or msg == 'Too slow':
        continueRoutine = False
    else:
        continueRoutine = True
    
    dur_sel = 50 # values will range from 60 to 90
    #dur_sel = randint(low = 120/2, high = 180/2) # values will range from 60 to 90
    
    
    
    
    
    s_left_3.setOpacity(keep_me_left)
    s_left_3.setImage(left)
    s_right_3.setOpacity(keep_me_right)
    s_right_3.setImage(right)
    s_if_left_3.setOpacity(show_me_left)
    s_if_left_3.setImage(left_selected)
    s_if_right_3.setOpacity(show_me_right)
    s_if_right_3.setImage(right_selected)
    # keep track of which components have finished
    selection_animationComponents = [cross_sel, s_left_3, s_right_3, s_if_left_3, s_if_right_3]
    for thisComponent in selection_animationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    selection_animationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "selection_animation"-------
    while continueRoutine:
        # get current time
        t = selection_animationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=selection_animationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_sel* updates
        if cross_sel.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            cross_sel.frameNStart = frameN  # exact frame index
            cross_sel.tStart = t  # local t and not account for scr refresh
            cross_sel.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_sel, 'tStartRefresh')  # time at next scr refresh
            cross_sel.setAutoDraw(True)
        if cross_sel.status == STARTED:
            if frameN >= dur_sel:
                # keep track of stop time/frame for later
                cross_sel.tStop = t  # not accounting for scr refresh
                cross_sel.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_sel, 'tStopRefresh')  # time at next scr refresh
                cross_sel.setAutoDraw(False)
        
        # *s_left_3* updates
        if s_left_3.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            s_left_3.frameNStart = frameN  # exact frame index
            s_left_3.tStart = t  # local t and not account for scr refresh
            s_left_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_left_3, 'tStartRefresh')  # time at next scr refresh
            s_left_3.setAutoDraw(True)
        if s_left_3.status == STARTED:
            if frameN >= dur_sel:
                # keep track of stop time/frame for later
                s_left_3.tStop = t  # not accounting for scr refresh
                s_left_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_left_3, 'tStopRefresh')  # time at next scr refresh
                s_left_3.setAutoDraw(False)
        
        # *s_right_3* updates
        if s_right_3.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            s_right_3.frameNStart = frameN  # exact frame index
            s_right_3.tStart = t  # local t and not account for scr refresh
            s_right_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_right_3, 'tStartRefresh')  # time at next scr refresh
            s_right_3.setAutoDraw(True)
        if s_right_3.status == STARTED:
            if frameN >= dur_sel:
                # keep track of stop time/frame for later
                s_right_3.tStop = t  # not accounting for scr refresh
                s_right_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_right_3, 'tStopRefresh')  # time at next scr refresh
                s_right_3.setAutoDraw(False)
        
        # *s_if_left_3* updates
        if s_if_left_3.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            s_if_left_3.frameNStart = frameN  # exact frame index
            s_if_left_3.tStart = t  # local t and not account for scr refresh
            s_if_left_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_if_left_3, 'tStartRefresh')  # time at next scr refresh
            s_if_left_3.setAutoDraw(True)
        if s_if_left_3.status == STARTED:
            if frameN >= dur_sel:
                # keep track of stop time/frame for later
                s_if_left_3.tStop = t  # not accounting for scr refresh
                s_if_left_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_if_left_3, 'tStopRefresh')  # time at next scr refresh
                s_if_left_3.setAutoDraw(False)
        
        # *s_if_right_3* updates
        if s_if_right_3.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            s_if_right_3.frameNStart = frameN  # exact frame index
            s_if_right_3.tStart = t  # local t and not account for scr refresh
            s_if_right_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_if_right_3, 'tStartRefresh')  # time at next scr refresh
            s_if_right_3.setAutoDraw(True)
        if s_if_right_3.status == STARTED:
            if frameN >= dur_sel:
                # keep track of stop time/frame for later
                s_if_right_3.tStop = t  # not accounting for scr refresh
                s_if_right_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_if_right_3, 'tStopRefresh')  # time at next scr refresh
                s_if_right_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selection_animationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "selection_animation"-------
    for thisComponent in selection_animationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('cross_sel.started', cross_sel.tStartRefresh)
    trials_3.addData('cross_sel.stopped', cross_sel.tStopRefresh)
    trials_3.addData('s_left_3.started', s_left_3.tStartRefresh)
    trials_3.addData('s_left_3.stopped', s_left_3.tStopRefresh)
    trials_3.addData('s_right_3.started', s_right_3.tStartRefresh)
    trials_3.addData('s_right_3.stopped', s_right_3.tStopRefresh)
    trials_3.addData('s_if_left_3.started', s_if_left_3.tStartRefresh)
    trials_3.addData('s_if_left_3.stopped', s_if_left_3.tStopRefresh)
    trials_3.addData('s_if_right_3.started', s_if_right_3.tStartRefresh)
    trials_3.addData('s_if_right_3.stopped', s_if_right_3.tStopRefresh)
    # the Routine "selection_animation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    if msg == 'Wrong button' or msg == 'Too slow':
        continueRoutine = False
    else:
        continueRoutine = True
    
    
    
    
    
    
    s_left.setOpacity(keep_me_left)
    s_left.setImage(left)
    s_right.setOpacity(keep_me_right)
    s_right.setImage(right)
    s_if_left.setOpacity(show_me_left)
    s_if_left.setImage(left_selected)
    s_if_right.setOpacity(show_me_right)
    s_if_right.setImage(right_selected)
    text_2.setPos(feed_pos)
    text_2.setText(feed)
    # keep track of which components have finished
    feedbackComponents = [cross_feed, s_left, s_right, s_if_left, s_if_right, text_2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_feed* updates
        if cross_feed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_feed.frameNStart = frameN  # exact frame index
            cross_feed.tStart = t  # local t and not account for scr refresh
            cross_feed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_feed, 'tStartRefresh')  # time at next scr refresh
            cross_feed.setAutoDraw(True)
        if cross_feed.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_feed.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                cross_feed.tStop = t  # not accounting for scr refresh
                cross_feed.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_feed, 'tStopRefresh')  # time at next scr refresh
                cross_feed.setAutoDraw(False)
        
        # *s_left* updates
        if s_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            s_left.frameNStart = frameN  # exact frame index
            s_left.tStart = t  # local t and not account for scr refresh
            s_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_left, 'tStartRefresh')  # time at next scr refresh
            s_left.setAutoDraw(True)
        if s_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > s_left.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                s_left.tStop = t  # not accounting for scr refresh
                s_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_left, 'tStopRefresh')  # time at next scr refresh
                s_left.setAutoDraw(False)
        
        # *s_right* updates
        if s_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            s_right.frameNStart = frameN  # exact frame index
            s_right.tStart = t  # local t and not account for scr refresh
            s_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_right, 'tStartRefresh')  # time at next scr refresh
            s_right.setAutoDraw(True)
        if s_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > s_right.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                s_right.tStop = t  # not accounting for scr refresh
                s_right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_right, 'tStopRefresh')  # time at next scr refresh
                s_right.setAutoDraw(False)
        
        # *s_if_left* updates
        if s_if_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            s_if_left.frameNStart = frameN  # exact frame index
            s_if_left.tStart = t  # local t and not account for scr refresh
            s_if_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_if_left, 'tStartRefresh')  # time at next scr refresh
            s_if_left.setAutoDraw(True)
        if s_if_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > s_if_left.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                s_if_left.tStop = t  # not accounting for scr refresh
                s_if_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_if_left, 'tStopRefresh')  # time at next scr refresh
                s_if_left.setAutoDraw(False)
        
        # *s_if_right* updates
        if s_if_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            s_if_right.frameNStart = frameN  # exact frame index
            s_if_right.tStart = t  # local t and not account for scr refresh
            s_if_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_if_right, 'tStartRefresh')  # time at next scr refresh
            s_if_right.setAutoDraw(True)
        if s_if_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > s_if_right.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                s_if_right.tStop = t  # not accounting for scr refresh
                s_if_right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_if_right, 'tStopRefresh')  # time at next scr refresh
                s_if_right.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('cross_feed.started', cross_feed.tStartRefresh)
    trials_3.addData('cross_feed.stopped', cross_feed.tStopRefresh)
    trials_3.addData('s_left.started', s_left.tStartRefresh)
    trials_3.addData('s_left.stopped', s_left.tStopRefresh)
    trials_3.addData('s_right.started', s_right.tStartRefresh)
    trials_3.addData('s_right.stopped', s_right.tStopRefresh)
    trials_3.addData('s_if_left.started', s_if_left.tStartRefresh)
    trials_3.addData('s_if_left.stopped', s_if_left.tStopRefresh)
    trials_3.addData('s_if_right.started', s_if_right.tStartRefresh)
    trials_3.addData('s_if_right.stopped', s_if_right.tStopRefresh)
    trials_3.addData('text_2.started', text_2.tStartRefresh)
    trials_3.addData('text_2.stopped', text_2.tStopRefresh)
    
    # ------Prepare to start Routine "too_slow"-------
    continueRoutine = True
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    if msg == 'Wrong button' or msg == 'Too slow':
        continueRoutine = True
    else:
        continueRoutine = False
    
    
    
    
    s_left_2.setOpacity(1)
    s_left_2.setImage(left)
    s_right_2.setOpacity(1)
    s_right_2.setImage(right)
    text_3.setText(msg)
    # keep track of which components have finished
    too_slowComponents = [cross_slow, s_left_2, s_right_2, text_3]
    for thisComponent in too_slowComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    too_slowClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "too_slow"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = too_slowClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=too_slowClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross_slow* updates
        if cross_slow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross_slow.frameNStart = frameN  # exact frame index
            cross_slow.tStart = t  # local t and not account for scr refresh
            cross_slow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross_slow, 'tStartRefresh')  # time at next scr refresh
            cross_slow.setAutoDraw(True)
        if cross_slow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross_slow.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                cross_slow.tStop = t  # not accounting for scr refresh
                cross_slow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross_slow, 'tStopRefresh')  # time at next scr refresh
                cross_slow.setAutoDraw(False)
        
        # *s_left_2* updates
        if s_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            s_left_2.frameNStart = frameN  # exact frame index
            s_left_2.tStart = t  # local t and not account for scr refresh
            s_left_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_left_2, 'tStartRefresh')  # time at next scr refresh
            s_left_2.setAutoDraw(True)
        if s_left_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > s_left_2.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                s_left_2.tStop = t  # not accounting for scr refresh
                s_left_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_left_2, 'tStopRefresh')  # time at next scr refresh
                s_left_2.setAutoDraw(False)
        
        # *s_right_2* updates
        if s_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            s_right_2.frameNStart = frameN  # exact frame index
            s_right_2.tStart = t  # local t and not account for scr refresh
            s_right_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_right_2, 'tStartRefresh')  # time at next scr refresh
            s_right_2.setAutoDraw(True)
        if s_right_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > s_right_2.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                s_right_2.tStop = t  # not accounting for scr refresh
                s_right_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(s_right_2, 'tStopRefresh')  # time at next scr refresh
                s_right_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in too_slowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "too_slow"-------
    for thisComponent in too_slowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    msg = '';
    trials_3.addData('cross_slow.started', cross_slow.tStartRefresh)
    trials_3.addData('cross_slow.stopped', cross_slow.tStopRefresh)
    trials_3.addData('s_left_2.started', s_left_2.tStartRefresh)
    trials_3.addData('s_left_2.stopped', s_left_2.tStopRefresh)
    trials_3.addData('s_right_2.started', s_right_2.tStartRefresh)
    trials_3.addData('s_right_2.stopped', s_right_2.tStopRefresh)
    trials_3.addData('text_3.started', text_3.tStartRefresh)
    trials_3.addData('text_3.stopped', text_3.tStopRefresh)
    
    # ------Prepare to start Routine "general_feed"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    if correct_count > 20:
        continueRoutine = True
    else:
        continueRoutine = False
    
    opacity_n = 1
    msg_end = 'Task finished. Well Done! Total points won: ' + str(grand_total) + '\n Ending experiment'
    
    
    
    text_6.setText(msg_end)
    # keep track of which components have finished
    general_feedComponents = [text_6]
    for thisComponent in general_feedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    general_feedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "general_feed"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = general_feedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=general_feedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in general_feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "general_feed"-------
    for thisComponent in general_feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if correct_count > 20:
        trials_3.finished = True;
    trials_3.addData('text_6.started', text_6.tStartRefresh)
    trials_3.addData('text_6.stopped', text_6.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "ending"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endingComponents = [text_9]
for thisComponent in endingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ending"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    if text_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_9.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_9.tStop = t  # not accounting for scr refresh
            text_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
            text_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ending"-------
for thisComponent in endingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
