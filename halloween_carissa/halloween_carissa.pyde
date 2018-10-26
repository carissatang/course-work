def setup():
    size(640, 480)
    
def draw():
    background(255, 140, 0)
    noStroke()
    fill(255, 200, 100)
    ellipse(width/2, height/2, 300, 300)
    fill(0)
    triangle(-200, height, 320, 300, 840, height)
    rect(270, 200, 100, 120)
    triangle(250, 200, 320, 160, 390, 200)
