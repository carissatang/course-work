sun = 0
red = 135
green = 206
blue = 250
num = 0
cloud_x = 0

def setup():
    size(640, 480)
    
def sunset():
    global red, green, blue, num, sun
    #blue to yellow
    if red != 51 and num == 0:
        red -= 1
    if green != 153 and num == 0:
        green -= 1
    #yellow to orange
    if (red <= 51 and green <= 153) or num == 1:
        num = 1
        if red != 255:
            red += 2
        if green != 140:
            green -= 1 
        if blue != 0:
            blue -= 4
    #orange to red
    if (red >= 255 and green <= 140 and blue <= 0) or num == 2:
        num = 2
        if red != 230:
            red -= 1
        if green != 70:
            green -= 1
    #red to purple
    if (red <= 230 and green <= 70) or num == 3:
        num = 3
        if red >= 52:
            red -= 2
        if green >= 0:
            green -= 1
        if blue <= 77:
            blue += 5
        if red <= 50:
            num = 4
    #purple to black
    if num == 4:
        red = 0
        green = 0
        blue = 0
    #sun
    noStroke()
    fill(255, 255, 0)
    ellipse(320, sun, 100, 100)
    sun += 1.3
    if sun >= 480:
        num = 0
        red = 135
        green = 206
        blue = 250
        sun = 0
        
def clouds(cloud_x, cloud_y):
    fill(255)
    ellipse(cloud_x, cloud_y - 15, 80, 40)
    ellipse(cloud_x - 45, cloud_y, 90, 50)
    ellipse(cloud_x + 45, cloud_y, 90, 50)
    ellipse(cloud_x, cloud_y + 18, 80, 40)

def grass(x, y):
    fill(34, 139, 34)
    ellipse(x, y, 700, 200)

def house():
    fill(139, 69, 19)
    rect(420, 360, 100, 80)
    triangle(400, 360, 540, 360, 470, 300)
    rect(495, 315, 20, 50)

def draw():
    background(red, green, blue)
    global cloud_x
    
    if cloud_x >= 640:
        cloud_x = 0
    cloud_x += 1
    
    sunset()
    clouds(cloud_x, 80)
    grass(100, 500)
    grass(600, 500)
    house()
