headX = 160
headY = 120
room = 0
starting_screen = True

def setup():
    global door_img, ghost_img, spookFont, defaultFont
    size(640, 480)
    noStroke()
    door_img = loadImage("door.png")
    ghost_img = loadImage("spooky ghosts.png")
    spookFont = createFont("Lucida Sans Demibold", 24)
    defaultFont = createFont("SansSerif.plain", 12)
    
def draw():
    global headX, headY, room, starting_screen, door1x
    
    if starting_screen:
        background(0)
        fill(255)
        text("You are stuck in a dark room", 120, 80)
        text("Find keys to escape", 120, 100)
        text("Click anywhere to continue...", 120, 440)
    
    elif room == 0:
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
        
        image(door_img, 480, 100, 45, 75)
        fill("#FFEFD5")
        ellipse(headX, headY, 50, 50)
        
        if(headX <= 10):
            headX = 10
        if(headY <= 10):
            headY = 10
        if(headY >= 470):
            headY = 470
        if(headX >= 630):
            headX = 630
        
    elif room == 1:
        background(0)
        image(ghost_img, 100, 100, 239, 210)
        textFont(spookFont)
        text("You've been spooked!", 320, 400)
        textFont(defaultFont)
        text("Press space to escape the spook", 360, 440)
        if keyPressed and key == ' ':
            room -= 1
        
def mousePressed():
    global starting_screen
    starting_screen = False
    
def keyPressed():
    global room, headX, headY
    if key == ' ' and room == 0 and headX in range(480, 525) and headY in range(100, 175):
        room = 1
    print(headX, headY, key)
    if key == ' ' and room == 1:
        room = 0
