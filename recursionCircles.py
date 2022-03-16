from processing import *

def setup():
  size(500, 150)
  frameRate(1)
  fill(0, 0, 0)
   
  
def recursiveCircle(x, size, count):
  if count == 0:
    return
  ellipse(x,75,size,size)
  
  recursiveCircle(x+size/1.2, size*(2/3), count-1)
  
  

def draw():
  background(200, 50, 40)
  recursiveCircle(75, 150, 20)
  
  
run()
