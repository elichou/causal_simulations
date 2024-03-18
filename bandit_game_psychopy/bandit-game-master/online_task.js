/********************
 * Online_Task Test
 ********************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'online_task';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(endingRoutineBegin());
flowScheduler.add(endingRoutineEachFrame());
flowScheduler.add(endingRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'g_4_d.png', 'path': 'g_4_d.png'},
    {'name': 'b_4.png', 'path': 'b_4.png'},
    {'name': 'y_4_d.png', 'path': 'y_4_d.png'},
    {'name': 'p_4_d.png', 'path': 'p_4_d.png'},
    {'name': 'y_4.png', 'path': 'y_4.png'},
    {'name': 'prep_stim_info.csv', 'path': 'prep_stim_info.csv'},
    {'name': 'b_4_d.png', 'path': 'b_4_d.png'},
    {'name': 'outline.png', 'path': 'outline.png'},
    {'name': 'p_4.png', 'path': 'p_4.png'},
    {'name': 'g_4.png', 'path': 'g_4.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);

  return Scheduler.Event.NEXT;
}


var info_start1Clock;
var stim_sizes;
var instr;
var mov;
var green_f;
var text_10;
var image_9;
var image_10;
var image_11;
var image_12;
var key_resp_9;
var info_stim1Clock;
var text;
var image;
var image_2;
var image_3;
var image_4;
var key_resp_2;
var green_frame;
var fixationClock;
var portt;
var fix_size;
var cross_fixation;
var key_resp;
var cuesClock;
var show_me_left;
var show_me_right;
var keep_me_left;
var keep_me_right;
var correct_count;
var msg;
var points_won;
var grand_total;
var res;
var cross_stim2;
var symbol_left;
var symbol_right;
var key_resp_3;
var selection_animationClock;
var cross_sel;
var s_left_3;
var s_right_3;
var s_if_left_3;
var s_if_right_3;
var feedbackClock;
var cross_feed;
var s_left;
var s_right;
var s_if_left;
var s_if_right;
var text_2;
var text_5;
var too_slowClock;
var cross_slow;
var s_left_2;
var s_right_2;
var text_3;
var general_feedClock;
var opacity_im;
var msg_end;
var text_6;
var endingClock;
var text_9;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "info_start1"
  info_start1Clock = new util.Clock();
  stim_sizes = [0.1, 0.1];
  instr = "";
  mov = "";
  green_f = 0;

  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.05], height: 0.026,  wrapWidth: 0.56, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0
  });

  image_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_9', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.1), (- 0.2)], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0
  });
  image_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_10', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.034), (- 0.2)], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0
  });
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.034, (- 0.2)], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0
  });
  image_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_12', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.1, (- 0.2)], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0
  });
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  // Initialize components for Routine "info_stim1"
  info_stim1Clock = new util.Clock();
  stim_sizes = [0.1, 0.1];
  instr = "";
  mov = "";
  green_f = 0;

  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.05], height: 0.026,  wrapWidth: 0.56, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0
  });

  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.1), (- 0.1)], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0
  });
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.034), (- 0.1)], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0
  });
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.034, (- 0.1)], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0
  });
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.1, (- 0.1)], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  green_frame = new visual.ImageStim({
    win : psychoJS.window,
    name : 'green_frame', units : undefined,
    image : 'outline.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.7778, 1],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0
  });
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  portt = [];
  stim_sizes = [0.15, 0.15];
  fix_size = [0.015, 0.015];

  cross_fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cross_fixation',
    vertices: 'cross', size:fix_size,
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });

  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  // Initialize components for Routine "cues"
  cuesClock = new util.Clock();
  show_me_left = 0;
  show_me_right = 0;
  keep_me_left = 0;
  keep_me_right = 0;
  correct_count = 0;
  msg = "";
  points_won = 0;
  grand_total = 0;
  portt = 99;
  res = "";
  cross_stim2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cross_stim2',
    vertices: 'cross', size:fix_size,
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });

  symbol_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'symbol_left', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.06), 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0
  });
  symbol_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'symbol_right', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.06, 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0
  });
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  // Initialize components for Routine "selection_animation"
  selection_animationClock = new util.Clock();
  cross_sel = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cross_sel',
    vertices: 'cross', size:fix_size,
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });

  s_left_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_left_3', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.06), 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0
  });
  s_right_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_right_3', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.06, 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0
  });
  s_if_left_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_if_left_3', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.06), 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0
  });
  s_if_right_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_if_right_3', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.06, 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0
  });
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  cross_feed = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cross_feed',
    vertices: 'cross', size:fix_size,
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });

  s_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_left', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.06), 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0
  });
  s_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_right', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.06, 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0
  });
  s_if_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_if_left', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.06), 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0
  });
  s_if_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_if_right', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.06, 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined,
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0
  });

  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.8)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0
  });

  // Initialize components for Routine "too_slow"
  too_slowClock = new util.Clock();
  cross_slow = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cross_slow',
    vertices: 'cross', size:fix_size,
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: 1, depth: -1, interpolate: true,
  });

  s_left_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_left_2', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.06), 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0
  });
  s_right_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 's_right_2', units : undefined,
    image : undefined, mask : undefined,
    ori : 0, pos : [0.06, 0], size : stim_sizes,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0
  });
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '',
    font: 'Arial',
    units: undefined,
    pos: [0, (- 0.08)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0
  });

  // Initialize components for Routine "general_feed"
  general_feedClock = new util.Clock();
  fix_size = [0.02, 0.02];
  opacity_im = 1;
  msg_end = "";

  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '',
    font: 'Arial',
    units: undefined,
    pos: [0, 0], height: 0.026,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0
  });

  // Initialize components for Routine "ending"
  endingClock = new util.Clock();
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'Please notify the experimenter that you have completed the task. ',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], height: 0.026,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });

  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine

  return Scheduler.Event.NEXT;
}


var trials_3;
var currentLoop;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop

    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'prep_stim_info.csv',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop

    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      const snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(info_start1RoutineBegin(snapshot));
      trials_3LoopScheduler.add(info_start1RoutineEachFrame());
      trials_3LoopScheduler.add(info_start1RoutineEnd());
      trials_3LoopScheduler.add(info_stim1RoutineBegin(snapshot));
      trials_3LoopScheduler.add(info_stim1RoutineEachFrame());
      trials_3LoopScheduler.add(info_stim1RoutineEnd());
      trials_3LoopScheduler.add(fixationRoutineBegin(snapshot));
      trials_3LoopScheduler.add(fixationRoutineEachFrame());
      trials_3LoopScheduler.add(fixationRoutineEnd());
      trials_3LoopScheduler.add(cuesRoutineBegin(snapshot));
      trials_3LoopScheduler.add(cuesRoutineEachFrame());
      trials_3LoopScheduler.add(cuesRoutineEnd());
      trials_3LoopScheduler.add(selection_animationRoutineBegin(snapshot));
      trials_3LoopScheduler.add(selection_animationRoutineEachFrame());
      trials_3LoopScheduler.add(selection_animationRoutineEnd());
      trials_3LoopScheduler.add(feedbackRoutineBegin(snapshot));
      trials_3LoopScheduler.add(feedbackRoutineEachFrame());
      trials_3LoopScheduler.add(feedbackRoutineEnd());
      trials_3LoopScheduler.add(too_slowRoutineBegin(snapshot));
      trials_3LoopScheduler.add(too_slowRoutineEachFrame());
      trials_3LoopScheduler.add(too_slowRoutineEnd());
      trials_3LoopScheduler.add(general_feedRoutineBegin(snapshot));
      trials_3LoopScheduler.add(general_feedRoutineEachFrame());
      trials_3LoopScheduler.add(general_feedRoutineEnd());
      trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
    }

    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _pj;
var im1;
var im2;
var im3;
var im4;
var _key_resp_9_allKeys;
var info_start1Components;
function info_start1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'info_start1'-------
    t = 0;
    info_start1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6(trial_n, [1])) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    im1 = "b_4.png";
    im2 = "g_4.png";
    im3 = "p_4.png";
    im4 = "y_4.png";
    instr = "In this practice block, you will choose between pairs of slot machines (shown below) that give you variable points. To win the game you should select the slot machines strategically so that by the end of the block you have as many points as possible. Select the left or right slot machine by using the left or right keys on the keyboard. You have 2 seconds to make your choice. \n Now we will do a short practice. Press the left or right key to start whenever you're ready.";

    text_10.setText(instr);
    image_9.setImage(im1);
    image_10.setImage(im2);
    image_11.setImage(im3);
    image_12.setImage(im4);
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    // keep track of which components have finished
    info_start1Components = [];
    info_start1Components.push(text_10);
    info_start1Components.push(image_9);
    info_start1Components.push(image_10);
    info_start1Components.push(image_11);
    info_start1Components.push(image_12);
    info_start1Components.push(key_resp_9);

    for (const thisComponent of info_start1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function info_start1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'info_start1'-------
    // get current time
    t = info_start1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index

      text_10.setAutoDraw(true);
    }


    // *image_9* updates
    if (t >= 0.0 && image_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_9.tStart = t;  // (not accounting for frame time here)
      image_9.frameNStart = frameN;  // exact frame index

      image_9.setAutoDraw(true);
    }


    // *image_10* updates
    if (t >= 0.0 && image_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_10.tStart = t;  // (not accounting for frame time here)
      image_10.frameNStart = frameN;  // exact frame index

      image_10.setAutoDraw(true);
    }


    // *image_11* updates
    if (t >= 0.0 && image_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_11.tStart = t;  // (not accounting for frame time here)
      image_11.frameNStart = frameN;  // exact frame index

      image_11.setAutoDraw(true);
    }


    // *image_12* updates
    if (t >= 0.0 && image_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_12.tStart = t;  // (not accounting for frame time here)
      image_12.frameNStart = frameN;  // exact frame index

      image_12.setAutoDraw(true);
    }


    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of info_start1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function info_start1RoutineEnd() {
  return async function () {
    //------Ending Routine 'info_start1'-------
    for (const thisComponent of info_start1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        routineTimer.reset();
        }

    key_resp_9.stop();
    // the Routine "info_start1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var info_stim1Components;
function info_stim1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'info_stim1'-------
    t = 0;
    info_stim1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6(trial_n, [11])) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    im1 = "b_4.png";
    im2 = "g_4.png";
    im3 = "p_4.png";
    im4 = "y_4.png";
    instr = `Well done! You gained ${points_won} points. There is no perfect number of points but try to always maximise them. \n Press a button to start the main game whenever you're ready.`

    text.setText(instr);
    image.setImage(im1);
    image_2.setImage(im2);
    image_3.setImage(im3);
    image_4.setImage(im4);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    green_frame.setOpacity(green_f);
    // keep track of which components have finished
    info_stim1Components = [];
    info_stim1Components.push(text);
    info_stim1Components.push(image);
    info_stim1Components.push(image_2);
    info_stim1Components.push(image_3);
    info_stim1Components.push(image_4);
    info_stim1Components.push(key_resp_2);
    info_stim1Components.push(green_frame);

    for (const thisComponent of info_stim1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function info_stim1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'info_stim1'-------
    // get current time
    t = info_stim1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index

      text.setAutoDraw(true);
    }


    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index

      image.setAutoDraw(true);
    }


    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index

      image_2.setAutoDraw(true);
    }


    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index

      image_3.setAutoDraw(true);
    }


    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index

      image_4.setAutoDraw(true);
    }


    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }


    // *green_frame* updates
    if (t >= 0.0 && green_frame.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      green_frame.tStart = t;  // (not accounting for frame time here)
      green_frame.frameNStart = frameN;  // exact frame index

      green_frame.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of info_stim1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function info_stim1RoutineEnd() {
  return async function () {
    //------Ending Routine 'info_stim1'-------
    for (const thisComponent of info_stim1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }

    key_resp_2.stop();
    // the Routine "info_stim1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    return Scheduler.Event.NEXT;
  };
}


var buttons;
var dur_fix;
var _key_resp_allKeys;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'fixation'-------
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    buttons = 0;
    dur_fix = 40;

    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(cross_fixation);
    fixationComponents.push(key_resp);

    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fixation'-------
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *cross_fixation* updates
    if (frameN >= 0 && cross_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross_fixation.tStart = t;  // (not accounting for frame time here)
      cross_fixation.frameNStart = frameN;  // exact frame index

      cross_fixation.setAutoDraw(true);
    }

    if (cross_fixation.status === PsychoJS.Status.STARTED && frameN >= dur_fix) {
      cross_fixation.setAutoDraw(false);
    }

    // *key_resp* updates
    if (frameN >= 0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED && frameN >= dur_fix) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd() {
  return async function () {
    //------Ending Routine 'fixation'-------
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }

    key_resp.stop();
    // the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    return Scheduler.Event.NEXT;
  };
}


var dur_cues;
var _key_resp_3_allKeys;
var cuesComponents;
function cuesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'cues'-------
    t = 0;
    cuesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    dur_cues = 120;
    if ((trial_n === 11)) {
        points_won = 0;
    }

    symbol_left.setImage(left);
    symbol_right.setImage(right);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    cuesComponents = [];
    cuesComponents.push(cross_stim2);
    cuesComponents.push(symbol_left);
    cuesComponents.push(symbol_right);
    cuesComponents.push(key_resp_3);

    for (const thisComponent of cuesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function cuesRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'cues'-------
    // get current time
    t = cuesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *cross_stim2* updates
    if (frameN >= 0 && cross_stim2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross_stim2.tStart = t;  // (not accounting for frame time here)
      cross_stim2.frameNStart = frameN;  // exact frame index

      cross_stim2.setAutoDraw(true);
    }

    if (cross_stim2.status === PsychoJS.Status.STARTED && frameN >= dur_cues) {
      cross_stim2.setAutoDraw(false);
    }

    // *symbol_left* updates
    if (frameN >= 0.0 && symbol_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      symbol_left.tStart = t;  // (not accounting for frame time here)
      symbol_left.frameNStart = frameN;  // exact frame index

      symbol_left.setAutoDraw(true);
    }

    if (symbol_left.status === PsychoJS.Status.STARTED && frameN >= dur_cues) {
      symbol_left.setAutoDraw(false);
    }

    // *symbol_right* updates
    if (frameN >= 0 && symbol_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      symbol_right.tStart = t;  // (not accounting for frame time here)
      symbol_right.frameNStart = frameN;  // exact frame index

      symbol_right.setAutoDraw(true);
    }

    if (symbol_right.status === PsychoJS.Status.STARTED && frameN >= dur_cues) {
      symbol_right.setAutoDraw(false);
    }

    // *key_resp_3* updates
    if (frameN >= 0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED && frameN >= 120) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of cuesComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var feed;
var feed_pos;
function cuesRoutineEnd() {
  return async function () {
    //------Ending Routine 'cues'-------
    for (const thisComponent of cuesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (typeof key_resp_3.keys === 'undefined') {
        msg = "Too slow";
        show_me_left = 0;
        show_me_right = 0;
        keep_me_left = 1;
        keep_me_right = 1;
        feed = left_rew;
        feed_pos = [1, (- 0.02)];
    } else {
        if (_pj.in_es6(key_resp_3.keys, "right")) {
            show_me_left = 0;
            show_me_right = 1;
            keep_me_left = 1;
            keep_me_right = 0;
            feed = right_rew;
            feed_pos = [0.06, (- 0.03)];
            res = 'rrr';
            msg = "";
            points_won = (points_won + right_rew_dbl);
            grand_total = (grand_total + right_rew_dbl);
        } else {
            if (_pj.in_es6(key_resp_3.keys, "left")) {
                show_me_left = 1;
                show_me_right = 0;
                keep_me_left = 0;
                keep_me_right = 1;
                feed = left_rew;
                feed_pos = [(- 0.06), (- 0.03)];
                msg = "";
                res = 'lll';
                points_won = (points_won + left_rew_dbl);
                grand_total = (grand_total + left_rew_dbl);
            } else {
                if (typeof key_resp_3.keys !== 'undefined') {
                    msg = "Wrong button";
                    show_me_left = 0;
                    show_me_right = 0;
                    keep_me_left = 1;
                    keep_me_right = 1;
                    feed = left_rew;
                    feed_pos = [1, (- 0.02)];
                }
            }
        }
    }
    if (((res === "lll") && (correct === 0))) {
        correct_count = (correct_count + 1);
    } else {
        if (((res === "rrr") && (correct === 1))) {
            correct_count = (correct_count + 1);
        }
    }

    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }

    key_resp_3.stop();
    // the Routine "cues" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    return Scheduler.Event.NEXT;
  };
}


var dur_sel;
var selection_animationComponents;
function selection_animationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'selection_animation'-------
    t = 0;
    selection_animationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if (((msg === "Wrong button") || (msg === "Too slow"))) {
        continueRoutine = false;
    } else {
        continueRoutine = true;
    }
    dur_sel = 50;

    s_left_3.setOpacity(keep_me_left);
    s_left_3.setImage(left);
    s_right_3.setOpacity(keep_me_right);
    s_right_3.setImage(right);
    s_if_left_3.setOpacity(show_me_left);
    s_if_left_3.setImage(left_selected);
    s_if_right_3.setOpacity(show_me_right);
    s_if_right_3.setImage(right_selected);
    // keep track of which components have finished
    selection_animationComponents = [];
    selection_animationComponents.push(cross_sel);
    selection_animationComponents.push(s_left_3);
    selection_animationComponents.push(s_right_3);
    selection_animationComponents.push(s_if_left_3);
    selection_animationComponents.push(s_if_right_3);

    for (const thisComponent of selection_animationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function selection_animationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'selection_animation'-------
    // get current time
    t = selection_animationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *cross_sel* updates
    if (frameN >= 0 && cross_sel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross_sel.tStart = t;  // (not accounting for frame time here)
      cross_sel.frameNStart = frameN;  // exact frame index

      cross_sel.setAutoDraw(true);
    }

    if (cross_sel.status === PsychoJS.Status.STARTED && frameN >= dur_sel) {
      cross_sel.setAutoDraw(false);
    }

    // *s_left_3* updates
    if (frameN >= 0 && s_left_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_left_3.tStart = t;  // (not accounting for frame time here)
      s_left_3.frameNStart = frameN;  // exact frame index

      s_left_3.setAutoDraw(true);
    }

    if (s_left_3.status === PsychoJS.Status.STARTED && frameN >= dur_sel) {
      s_left_3.setAutoDraw(false);
    }

    // *s_right_3* updates
    if (frameN >= 0.0 && s_right_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_right_3.tStart = t;  // (not accounting for frame time here)
      s_right_3.frameNStart = frameN;  // exact frame index

      s_right_3.setAutoDraw(true);
    }

    if (s_right_3.status === PsychoJS.Status.STARTED && frameN >= dur_sel) {
      s_right_3.setAutoDraw(false);
    }

    // *s_if_left_3* updates
    if (frameN >= 0.0 && s_if_left_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_if_left_3.tStart = t;  // (not accounting for frame time here)
      s_if_left_3.frameNStart = frameN;  // exact frame index

      s_if_left_3.setAutoDraw(true);
    }

    if (s_if_left_3.status === PsychoJS.Status.STARTED && frameN >= dur_sel) {
      s_if_left_3.setAutoDraw(false);
    }

    // *s_if_right_3* updates
    if (frameN >= 0.0 && s_if_right_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_if_right_3.tStart = t;  // (not accounting for frame time here)
      s_if_right_3.frameNStart = frameN;  // exact frame index

      s_if_right_3.setAutoDraw(true);
    }

    if (s_if_right_3.status === PsychoJS.Status.STARTED && frameN >= dur_sel) {
      s_if_right_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of selection_animationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function selection_animationRoutineEnd() {
  return async function () {
    //------Ending Routine 'selection_animation'-------
    for (const thisComponent of selection_animationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "selection_animation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    return Scheduler.Event.NEXT;
  };
}


var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.800000);
    // update component parameters for each repeat
    if (((msg === "Wrong button") || (msg === "Too slow"))) {
        continueRoutine = false;
    } else {
        continueRoutine = true;
    }

    s_left.setOpacity(keep_me_left);
    s_left.setImage(left);
    s_right.setOpacity(keep_me_right);
    s_right.setImage(right);
    s_if_left.setOpacity(show_me_left);
    s_if_left.setImage(left_selected);
    s_if_right.setOpacity(show_me_right);
    s_if_right.setImage(right_selected);
    text_2.setPos(feed_pos);
    text_2.setText(feed);
    text_5.setText(correct_count);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(cross_feed);
    feedbackComponents.push(s_left);
    feedbackComponents.push(s_right);
    feedbackComponents.push(s_if_left);
    feedbackComponents.push(s_if_right);
    feedbackComponents.push(text_2);
    feedbackComponents.push(text_5);

    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function feedbackRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'feedback'-------
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *cross_feed* updates
    if (t >= 0.0 && cross_feed.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross_feed.tStart = t;  // (not accounting for frame time here)
      cross_feed.frameNStart = frameN;  // exact frame index

      cross_feed.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cross_feed.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cross_feed.setAutoDraw(false);
    }

    // *s_left* updates
    if (t >= 0.0 && s_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_left.tStart = t;  // (not accounting for frame time here)
      s_left.frameNStart = frameN;  // exact frame index

      s_left.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (s_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      s_left.setAutoDraw(false);
    }

    // *s_right* updates
    if (t >= 0.0 && s_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_right.tStart = t;  // (not accounting for frame time here)
      s_right.frameNStart = frameN;  // exact frame index

      s_right.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (s_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      s_right.setAutoDraw(false);
    }

    // *s_if_left* updates
    if (t >= 0.0 && s_if_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_if_left.tStart = t;  // (not accounting for frame time here)
      s_if_left.frameNStart = frameN;  // exact frame index

      s_if_left.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (s_if_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      s_if_left.setAutoDraw(false);
    }

    // *s_if_right* updates
    if (t >= 0.0 && s_if_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_if_right.tStart = t;  // (not accounting for frame time here)
      s_if_right.frameNStart = frameN;  // exact frame index

      s_if_right.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (s_if_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      s_if_right.setAutoDraw(false);
    }

    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index

      text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }

    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index

      text_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd() {
  return async function () {
    //------Ending Routine 'feedback'-------
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var too_slowComponents;
function too_slowRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'too_slow'-------
    t = 0;
    too_slowClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.800000);
    // update component parameters for each repeat
    if (((msg === "Wrong button") || (msg === "Too slow"))) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }

    s_left_2.setOpacity(1);
    s_left_2.setImage(left);
    s_right_2.setOpacity(1);
    s_right_2.setImage(right);
    text_3.setText(msg);
    // keep track of which components have finished
    too_slowComponents = [];
    too_slowComponents.push(cross_slow);
    too_slowComponents.push(s_left_2);
    too_slowComponents.push(s_right_2);
    too_slowComponents.push(text_3);

    for (const thisComponent of too_slowComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function too_slowRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'too_slow'-------
    // get current time
    t = too_slowClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *cross_slow* updates
    if (t >= 0.0 && cross_slow.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross_slow.tStart = t;  // (not accounting for frame time here)
      cross_slow.frameNStart = frameN;  // exact frame index

      cross_slow.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cross_slow.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cross_slow.setAutoDraw(false);
    }

    // *s_left_2* updates
    if (t >= 0.0 && s_left_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_left_2.tStart = t;  // (not accounting for frame time here)
      s_left_2.frameNStart = frameN;  // exact frame index

      s_left_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (s_left_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      s_left_2.setAutoDraw(false);
    }

    // *s_right_2* updates
    if (t >= 0.0 && s_right_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      s_right_2.tStart = t;  // (not accounting for frame time here)
      s_right_2.frameNStart = frameN;  // exact frame index

      s_right_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (s_right_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      s_right_2.setAutoDraw(false);
    }

    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index

      text_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of too_slowComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function too_slowRoutineEnd() {
  return async function () {
    //------Ending Routine 'too_slow'-------
    for (const thisComponent of too_slowComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    msg = "";

    return Scheduler.Event.NEXT;
  };
}


var opacity_n;
var general_feedComponents;
function general_feedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'general_feed'-------
    t = 0;
    general_feedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    if ((correct_count > 60)) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    opacity_n = 1;
    msg_end = (("Task finished. Well Done! Total points won: " + grand_total.toString()) + "\n Ending experiment");

    text_6.setText(msg_end);
    // keep track of which components have finished
    general_feedComponents = [];
    general_feedComponents.push(text_6);

    for (const thisComponent of general_feedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function general_feedRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'general_feed'-------
    // get current time
    t = general_feedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index

      text_6.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of general_feedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function general_feedRoutineEnd() {
  return async function () {
    //------Ending Routine 'general_feed'-------
    for (const thisComponent of general_feedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((correct_count > 60)) {
        trials_3.finished = true;
    }

    return Scheduler.Event.NEXT;
  };
}


var endingComponents;
function endingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //------Prepare to start Routine 'ending'-------
    t = 0;
    endingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endingComponents = [];
    endingComponents.push(text_9);

    for (const thisComponent of endingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endingRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'ending'-------
    // get current time
    t = endingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index

      text_9.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_9.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endingRoutineEnd() {
  return async function () {
    //------Ending Routine 'ending'-------
    for (const thisComponent of endingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }


























  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
