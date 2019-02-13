#Copyright Xiaocheng Liang  xcliang@bu.edu

import InputModule_lxc
import Alert_module
import AiModule
import UserInterface_module

bo = InputModule_lxc.readdata("./examplebo.txt")
bp = InputModule_lxc.readdata("./examplebp.txt")
pul = InputModule_lxc.readdata("./examplepul.txt")

'''''
AI Module
'''
robot = AiModule.AiModule()
robot.input_check(bo, bp, pul)
predBloodOxygen, predBloodPressure, prePulse = robot.predict()

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

'''''
UserInterface Module
'''''
User = UserInterface_module.userInterface()
User.getFromData(bo, bp, pul)