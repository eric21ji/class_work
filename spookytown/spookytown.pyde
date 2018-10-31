headX = 160
headY = 120
room = 0
rooms_visited = 0

def setup():
    global door_img, ghost_img, doot, care_bear, pumpkin, spookFont, defaultFont, winFont
    size(640, 480)
    noStroke()
    door_img = loadImage("door.png")
    ghost_img = loadImage("spooky ghosts.png")
    doot = loadImage("doot.png")
    care_bear = loadImage("care bears.jpg")
    pumpkin = loadImage("pumpkin.jpg")
    spookFont = createFont("Lucida Sans Demibold", 24)
    defaultFont = createFont("SansSerif.plain", 12)
    winFont = createFont("Lucida Sans Demibold", 48)
    
def draw():
    global headX, headY, room, starting_screen
    
    if room == 0:
        background(0)
        fill(255)
        text("You are stuck in a dark room", 120, 80)
        text("Try to check out different rooms", 120, 100)
        text("Click anywhere to continue...", 120, 440)
    
    elif room == 1:
        if(keyPressed):
            if key == 'w':
                headY -= 3
            if key == 's':
                headY += 3
            if key == 'a':
                headX -= 3
            if key == 'd':
                headX += 3
        background(0)
        
        image(door_img, 480, 60, 45, 75)
        image(door_img, 480, 180, 45, 75)
        image(door_img, 480, 300, 45, 75)
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
        
    elif room == 2:
        background(0)
        image(ghost_img, 100, 100, 239, 210)
        fill(255)
        textFont(spookFont)
        text("You've been spooked!", 320, 400)
        textFont(defaultFont)
        text("Press space to escape the spook", 360, 440)
        
    elif room == 3:
        background(0)
        image(doot, 40, 40, 512, 288)
        fill(255)
        textFont(spookFont)
        text("doot", 360, 400)
        textFont(defaultFont)
        text("Press space to return to the main room", 360, 440)
        
    elif room == 4:
        background(255)
        image(care_bear, 40, 40, 229, 280)
        fill(0)
        textFont(spookFont)
        text("nothing to see here...", 320, 400)
        textFont(defaultFont)
        text("Press space to pretend this never happened", 360, 440)
        
    elif room == 5:
        background(0)
        textFont(defaultFont)
        fill(255)
        text("After visiting all the rooms, you start to feel tired.", 100, 100)
        text("You close your eyes and wake up from the nightmare", 100, 115)
        text("that was this awful game.", 100, 130)
        text("Press space to continue...", 400, 360)
    
    elif room == 6:
        background(0)
        fill("#FF8C00")
        textFont(winFont)
        text("HAPPY HALLOWEEN!", 50, 100)
        image(pumpkin, width/2 - 180, height/2-50, 360, 248)
        
        
def mousePressed():
    global room
    if room == 0:
        room = 1
    
def keyPressed():
    global room, headX, headY, rooms_visited
    if room == 1 and headX in range(480, 525) and headY in range(60, 135):
        room = 2
        headX = width/2
        headY = height/2
    elif key == ' ' and room == 2:
        room = 1
        rooms_visited += 1
    elif room == 1 and headX in range(480, 525) and headY in range(180, 255):
        room = 3
        headX = width/2
        headY = height/2
    elif room == 3 and key == ' ':
        room = 1
        rooms_visited += 1
    elif room == 1 and headX in range(480, 525) and headY in range(300, 375):
        room = 4
        headX = width/2
        headY = height/2
    elif room == 4 and key == ' ':
        room = 1
        rooms_visited += 1
    elif room == 1 and rooms_visited == 3:
        room = 5
    elif room == 5 and key == ' ':
        room = 6
