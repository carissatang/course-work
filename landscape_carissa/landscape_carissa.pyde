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
    global cloud_one, cloud_two, sun, c1, c2, redd, greenn, bluee, num
    #BACKGROUND ANIMATION
    background(redd, greenn, bluee)
    #blue to yellow
    if redd != 51 and num == 0:
        redd -= 1
    if greenn != 153 and num == 0:
        greenn -= 1
    #yellow to orange
    if (redd <= 51 and greenn <= 153) or num == 1:
        num = 1
        if redd != 255:
            redd += 2
        if greenn != 140:
            greenn -= 1 
        if bluee != 0:
            bluee -= 4
    #orange to red
    if (redd >= 255 and greenn <= 140 and bluee <= 0) or num == 2:
        num = 2
        if redd != 230:
            redd -= 1
        if greenn != 70:
            greenn -= 1
    #red to purple
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
    #purple to black
    if num == 4:
        redd = 0
        greenn = 0
        bluee = 0
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
    sun += 1.3
    #CLOUDS
    fill(255)
    #cloud one
    ellipse(cloud_one + 5, 55, 80, 40)
    ellipse(cloud_one - 50, 70, 90, 50)
    ellipse(cloud_one + 50, 70, 90, 50)
    ellipse(cloud_one - 5, 88, 80, 40)
    #cloud two
    ellipse(cloud_two + 5, 45, 80, 40)
    ellipse(cloud_two - 50, 60, 90, 50)
    ellipse(cloud_two + 50, 60, 90, 50)
    ellipse(cloud_two - 5, 78, 80, 40)
    if cloud_one >= 640:
        cloud_one = 0
    if cloud_two >= 640:
        cloud_two = 0
    cloud_one += 1
    cloud_two += 2
    #GRASS
    fill(34, 139, 34)
    ellipse(100, 500, 700, 200)
    ellipse(600, 500, 700, 200)
    #HOUSE
    fill(139, 69, 19)
    rect(420, 360, 100, 80)
    #roof
    triangle(400, 360, 540, 360, 470, 300)
    #chimney
    rect(495, 315, 20, 50)
