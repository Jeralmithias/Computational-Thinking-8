###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")
q1 = codesters.Square(100,100,200, 'white')
q2 = codesters.Square(-100,100,200, 'blue')
q3 = codesters.Square(-100,-100,200, 'red')
q4 = codesters.Square(100,-100,200, 'black')


s1 = codesters.Sprite("Screenshot 2025-03-14 9.10.17 AM (1).png", 100,100,)
s1.set_size(0.6)
s2 = codesters.Sprite("striped-sailboat.png",-100,100)
s2.set_size(0.3)
s3 = codesters.Sprite("download.png", -100,-100)
s3.set_size(0.6)
s4 = codesters.Sprite("W.png", 100,-100)
s4.set_size(0.6)