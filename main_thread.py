#Copyright Xiaocheng Liang  xcliang@bu.edu

import InputModule_lxc
import Alert_module
import AiModule
import UserInterface_module
import time
import random
import threading

def runinput():
	bo = InputModule_lxc.readdata("./examplebo.txt")
	bp = InputModule_lxc.readdata("./examplebp.txt")
	pul = InputModule_lxc.readdata("./examplepul.txt")
	return bo, bp, pul

def runai(bo,bp, pul):
	'''''
	AI Module
	'''
	robot = AiModule.AiModule()
	robot.input_check(bo, bp, pul)
	predBloodOxygen, predBloodPressure, prePulse = robot.predict()

def runalert(bo,bp, pul):
	'''
	Alert Module
	'''
	Alt = Alert_module.Alert()
	for k in range(len(bo)):
	    boi = bo[k],0
	    bpi = bp[k],1
	    puli = pul[k],2
	    boa = Alt.Alert_for_three_categories_input(boi)
	    bpa = Alt.Alert_for_three_categories_input(bpi)
	    pula = Alt.Alert_for_three_categories_input(puli)

def runui(bo,bp, pul):
	'''''
	UserInterface Module
	'''''
	User = UserInterface_module.userInterface()
	User.getFromData(bo, bp, pul)

while 1:
	bo, bp, pul = runinput()
	t0 = threading.Thread(target = runinput)
	t1 = threading.Thread(target = runai, args=(bo, bp, pul,))
	t2 = threading.Thread(target = runalert, args=(bo, bp, pul,))
	t3 = threading.Thread(target = runui, args=(bo, bp, pul,))
	t0.start()
	t1.start()
	t2.start()
	t3.start()
	time.sleep(random.randint(2,4))