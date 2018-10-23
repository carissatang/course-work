# while loop
# increase a variable
# use draw() for animation

cloud_one = 0
cloud_two = 0
sun = 640

def setup():
    size(640, 480)
 
def draw():
    global cloud_one, cloud_two, sun
    background(135, 206, 250)
    if cloud_one >= 640:
        cloud_one = 0
    if cloud_two >= 640:
        cloud_two = 0
    cloud_one += 1
    cloud_two += 3
    noStroke()
    fill(200, 180, 0)
    ellipse(320, sun, 100, 100)
    if sun <= 0:
        sun = 640
    sun -= 1
    fill(255)
    ellipse(cloud_one + 5, 55, 80, 40)
    ellipse(cloud_one - 50, 70, 90, 50)
    ellipse(cloud_one + 50, 70, 90, 50)
    ellipse(cloud_one - 5, 88, 80, 40)
    ellipse(cloud_two + 5, 45, 80, 40)
    ellipse(cloud_two - 50, 60, 90, 50)
    ellipse(cloud_two + 50, 60, 90, 50)
    ellipse(cloud_two - 5, 78, 80, 40)
    fill(50, 150, 50)
    ellipse(320, 460, 700, 100)
    fill(165, 82, 42)
    rect(420, 360, 100, 80)


    
    
