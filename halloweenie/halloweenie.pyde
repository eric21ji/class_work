player_x = 160
player_y = 120
room = 0
rooms_visited = 0
pumpkin_y = 480
red_ball_y = 440

def setup():
    global door_img, ghost_img, doot, care_bear, pumpkin, spookFont, defaultFont, endFont
    size(640, 480)
    noStroke()
    #load sprites and images
    door_img = loadImage("door.png")
    ghost_img = loadImage("spooky ghosts.png")
    doot = loadImage("doot.png")
    care_bear = loadImage("care bears.jpg")
    pumpkin = loadImage("pumpkin.jpg")
    #load fonts for different situations
    spookFont = createFont("Lucida Sans Demibold", 24)
    defaultFont = createFont("SansSerif.plain", 12)
    endFont = createFont("Lucida Sans Demibold", 48)
    
def draw():
    global player_x, player_y, room, pumpkin_y, red_ball_y
    
    if room == 0: #Starting screen
        background(0) #black
        fill(255) #white
        text("There are a couple of doors here", 120, 80)
        text("Check out the other rooms", 120, 100)
        text("Click anywhere to continue...", 120, 440)
    
    elif room == 1: #Main room
        if(keyPressed): #player movement
            if key == 'w': 
                player_y -= 3 #player moves up
            if key == 's':
                player_y += 3 #player moves down
            if key == 'a':
                player_x -= 3 #player moves left
            if key == 'd':
                player_x += 3 #player moves right
        background(0)
        
        #makes doors
        image(door_img, 480, 60, 45, 75) #ghost room - top door
        image(door_img, 480, 180, 45, 75) #doot room - centre right door
        image(door_img, 480, 300, 45, 75) #care bear room - bottom door
        
        if rooms_visited >= 3: #adds special door to main room
            image(door_img, 120, 180, 45, 75) #red ball room - centre left door
            
        #draw player
        fill("#FFEFD5") #peach
        ellipse(player_x, player_y, 50, 50) #head
        fill(0)
        ellipse(player_x - 7, player_y - 7, 5, 5) #eyes
        ellipse(player_x + 7, player_y - 7, 5, 5)
        rect(player_x-7, player_y + 10, 14, 1) #mouth
        
        #borders, so that the player cannot travel beyond these points
        if(player_x <= 10):
            player_x = 10
        if(player_y <= 10):
            player_y = 10
        if(player_y >= 470):
            player_y = 470
        if(player_x >= 630):
            player_x = 630    
            
        
    elif room == 2: #ghost room
        background(0)
        image(ghost_img, 100, 100, 239, 210) #display ghosts
        fill(255) #white
        textFont(spookFont)
        text("You've been spooked!", 320, 400)
        textFont(defaultFont)
        text("Press space to escape the spook", 360, 440)

    elif room == 3: #doot room
        background(0)
        image(doot, 40, 40, 512, 288) #display doot
        fill(255) #white
        textFont(spookFont)
        text("doot", 360, 400)
        textFont(defaultFont)
        text("Press space to return to the main room", 360, 440)
        
    elif room == 4: #care bear room
        background(255)
        image(care_bear, 40, 40, 229, 280) #display care bear
        fill(0)
        textFont(spookFont)
        text("terrifying", 320, 400)
        textFont(defaultFont)
        text("Press space to return to the main room", 320, 440)

    elif room == 6: #almost end screen
        background(0)
        textFont(defaultFont)
        fill(255)
        text("Woah. You found an exit", 100, 100)
        text("I think you won", 100, 115)
        text("yeah", 100, 130)
        text("Press space to continue...", 400, 360)
    
    elif room == 7: #happy halloween screen
        background(0)
        fill("#FF8C00")
        textFont(endFont)
        text("HAPPY HALLOWEEN!", 50, 100)
        image(pumpkin, width/2 - 180, pumpkin_y, 360, 248) #draw flying pumpkin
        pumpkin_y -= 2 #moves pumpking up
        if(pumpkin_y <= 190): #make sure pumpkin stays once it reaches a certain point
            pumpkin_y = 190
    elif room == 8: #evil red ball race
        if(keyPressed): #controls player movement
            if key == 'w':
                player_y -= 3
            if key == 's':
                player_y += 3
            if key == 'a':
                player_x -= 3
            if key == 'd':
                player_x += 3
        background(0)
        
        #draw door
        image(door_img, 100, 100, 45, 75)
        #draw player
        fill("#FFEFD5") #peach
        ellipse(player_x, player_y, 50, 50)
        fill(0)
        ellipse(player_x - 7, player_y - 7, 5, 5)
        ellipse(player_x + 7, player_y - 7, 5, 5)
        rect(player_x-7, player_y + 10, 14, 1)
        #draw evil red ball
        fill(148, 15, 15)
        ellipse(122.5, red_ball_y, 75, 75)
        fill(255)
        text("The evil red ball is coming to get you!", 80, 400)
        text("Reach the door first!", 80, 415)

        red_ball_y -= 1.45 #moves the ball upwards
    
        #borders
        if(player_x <= 10):
            player_x = 10
        if(player_y <= 10):
            player_y = 10
        if(player_y >= 470):
            player_y = 470
        if(player_x >= 630):
            player_x = 630  
            
        if red_ball_y <= 175 : #player lose, since ball reaches door
            room = 13
            
    elif room == 13: #losing screen
        background(0)
        textFont(endFont)
        text("YOU LOSE", 80, 120)
        textFont(defaultFont)
        text("Click anywhere to start again", 80, 400)
        red_ball_y = 440
        
def mousePressed():
    global room
    if room == 0:
        room = 1 #exit starting screen
    if room == 13:
        room = 0 #restart game
    
def keyPressed():
    global room, player_x, player_y, rooms_visited
    if room == 1 and player_x in range(480, 525) and player_y in range(60, 135): #moves to room 2
        room = 2
        #reset playerposition
        player_x = width/2
        player_y = height/2
    elif key == ' ' and room == 2: #return to main room
        room = 1
        rooms_visited += 1
    elif room == 1 and player_x in range(480, 525) and player_y in range(180, 255): #move to room 3
        room = 3
        #reset player position
        player_x = width/2
        player_y = height/2
    elif room == 3 and key == ' ': #return to main room
        room = 1
        rooms_visited += 1
    elif room == 1 and player_x in range(480, 525) and player_y in range(300, 375): #move to room 4
        room = 4
        #reset player position
        player_x = width/2
        player_y = height/2
    elif room == 4 and key == ' ': #return to main room
        room = 1
        rooms_visited += 1
    elif room == 1 and rooms_visited >= 3 and player_x in range(120, 165) and player_y in range(180, 255): #move to almost end screen
        room = 8
        #move player position 
        player_x = 480
        player_y = 320
    elif room == 6 and key == ' ': #move to halloween screen
        room = 7
    elif room == 8 and player_x in range(100, 145) and player_y in range(100, 175): #move to room 6
        room = 6
