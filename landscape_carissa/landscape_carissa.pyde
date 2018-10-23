#VARIABLES
cloud_one = 0
cloud_two = 0
sun = 0
c1 = color(0, 102, 180)
c2 = color(204, 102, 0)
redd = 135
greenn = 206
bluee = 250
num = 0

def setup():
    size(640, 480)
 
def draw():
    import time
    global cloud_one, cloud_two, sun, c1, c2, redd, greenn, bluee, num
    #BACKGROUND ANIMATION
    background(redd, greenn, bluee)
    if redd != 51 and num == 0:
        redd -= 1
    if greenn != 153 and num == 0:
        greenn -= 1
    if (redd <= 51 and greenn <= 153) or num == 1:
        num = 1
        if redd != 255:
            redd += 2
        if greenn != 140:
            greenn -= 1 
        if bluee != 0:
            bluee -= 4
    if (redd >= 255 and greenn <= 140 and bluee <= 0) or num == 2:
        num = 2
        if redd != 230:
            redd -= 1
        if greenn != 70:
            greenn -= 1
    if (redd <= 230 and greenn <= 70) or num == 3:
        num = 3
        if redd >= 52:
            redd -= 2
        if greenn >= 0:
            greenn -= 1
        if bluee <= 77:
            bluee += 5
        if redd <= 50:
            num = 4
    if num == 4:
        redd = 0
        greenn = 0
        bluee = 0
    print(redd, greenn, bluee, num)
    #SUN
    noStroke()
    fill(255, 255, 0)
    ellipse(320, sun, 100, 100)
    if sun >= 480:
        num = 0
        redd = 135
        greenn = 206
        bluee = 250
        sun = 0
    sun += 1.2
    print(sun)
    #CLOUDS
    fill(255)
    ellipse(cloud_one + 5, 55, 80, 40)
    ellipse(cloud_one - 50, 70, 90, 50)
    ellipse(cloud_one + 50, 70, 90, 50)
    ellipse(cloud_one - 5, 88, 80, 40)
    ellipse(cloud_two + 5, 45, 80, 40)
    ellipse(cloud_two - 50, 60, 90, 50)
    ellipse(cloud_two + 50, 60, 90, 50)
    ellipse(cloud_two - 5, 78, 80, 40)
    if cloud_one >= 640:
        cloud_one = 0
    if cloud_two >= 640:
        cloud_two = 0
    cloud_one += 1
    cloud_two += 3
    #GRASS
    fill(34, 139, 34)
    ellipse(320, 460, 700, 100)
    #HOUSE
    fill(139, 69, 19)
    rect(420, 360, 100, 80)
    triangle(400, 360, 540, 360, 470, 300)
