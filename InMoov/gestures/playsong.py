# -- coding: utf-8 --

def playsong(data):
  i01.startedGesture()
  if (data == "can i have your attention"): # Могу ли я привлечь ваше внимание
    i01.mouth.speak("ok you have my attention")
    #i01.mouth.speak(u"Хорошо, что я привлёк ваше внимание")
    stopit()
    i01.mouth.speak("electro funk inmoov")
    #i01.mouth.speak(u"Электо функции Инмоова")
    i01.setHeadSpeed(1.0,1.0)
    i01.setArmSpeed("left",1.0,1.0,1.0,1.0)
    i01.setArmSpeed("right",1.0,1.0,1.0,1.0)
    i01.setHandSpeed("left",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setHandSpeed("right",1.0,1.0,1.0,1.0,1.0,1.0)
    i01.setTorsoSpeed(1.0,1.0,1.0)
    #for x in range(5):
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    sleep(2)
    i01.moveHead(110,80)
    sleep(2)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveTorso(90,90,90)
    fullspeed()
    i01.giving()
    sleep(5)
    i01.armsFront()
    sleep(4)
    fullspeed()
    i01.daVinci()
    sleep(5)
    surrender()
    sleep(6)
    i01.giving()
    sleep(6)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    sleep(3)
    i01.moveHead(60,90)
    fingerright()
    sleep(3)
    i01.moveHead(110,80)
    fingerleft()
    relax()
    i01.moveTorso(90,90,90)
    sleep(3)
    fullspeed()
    sleep(3)
    madeby()
    relax()
    sleep(5)
    i01.disable()
  i01.finishedGesture()

  
   


