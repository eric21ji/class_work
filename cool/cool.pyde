headX = 160
headY = 120

def setup():
    size(640, 480)
    noStroke()
def draw():
    global headX, headY
    
    if(keyPressed):
        if key == 'w':
            headY -= 2
        if key == 's':
            headY += 2
        if key == 'a':
            headX -= 2
        if key == 'd':
            headX += 2
    background(0)
    
    fill("#FFEFD5")
    ellipse(headX, headY, 50, 50)
    
    fill(255)
    text("you have been poisoned...", 40, 440)
    
    if(headX <= 10):
        headX = 10
    if(headY <= 10):
        headY = 10
    if(headY >= 470):
        headY = 470
    if(headX >= 630):
        headX = 630
