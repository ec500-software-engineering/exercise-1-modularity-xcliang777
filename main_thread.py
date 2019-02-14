#Copyright Xiaocheng Liang  xcliang@bu.edu

import InputModule_lxc
import Alert_module
import AiModule
import UserInterface_module
import time
import random
import threading

def run():
	bo = InputModule_lxc.readdata("./examplebo.txt")
	bp = InputModule_lxc.readdata("./examplebp.txt")
	pul = InputModule_lxc.readdata("./examplepul.txt")

	robot = AiModule.AiModule()
	robot.input_check(bo, bp, pul)
	predBloodOxygen, predBloodPressure, prePulse = robot.predict()

	Alt = Alert_module.Alert()
	for k in range(len(bo)):
	    boi = bo[k],0
	    bpi = bp[k],1
	    puli = pul[k],2
	    boa = Alt.Alert_for_three_categories_input(boi)
	    bpa = Alt.Alert_for_three_categories_input(bpi)
	    pula = Alt.Alert_for_three_categories_input(puli)
	print(boa)
	print(bpa)
	print(pula)

	User = UserInterface_module.userInterface()
	User.getFromData(bo, bp, pul)

while True:
	for i in range(5):
		t = threading.Thread(target = run)
		t.start()
		time.sleep(random.randint(2,4))