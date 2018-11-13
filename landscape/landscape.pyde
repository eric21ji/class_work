import random
snow_y = [100, 0, -30, -50, -100, 40, 140, -140, 200, -200, 70, -70, 20, -280, -180, -240, 24, 57, 13, -93, -152, 14, -50, -123]
snow_x = []
hat_x = [95, 105]
hat_y = [257, 227, 249]

for snowflake in range(24):
    snow_x.append(random.randint(1,640))

def setup():
    size(640, 480)
    noStroke()
    
def draw():
    background("#00BFFF") #sky blue
    
    draw_snowman()
    draw_hat()
    draw_tree()
    draw_ground()
    draw_snowflakes()
                        
def draw_snowflakes():
    global snow_x, snow_y
    #move the snowflakes down
    for snowflake in range(len(snow_y)):
        snow_y[snowflake] += 2 
    fill("#F0F0EC") #snowy white
    #drawing snowflakes
    for coord in range(len(snow_x)):
        ellipse(snow_x[coord], snow_y[coord], 5, 5)
    #cycle snowflakes to the top
    for coord in range(len(snow_x)):
        if snow_y[coord] >= 424:
            snow_y[coord] = -10
            snow_x[coord] = random.randint(1, 640)
            
def draw_ground():
    #dirt
    fill(87, 59, 12) #brown
    rect(-10, 440, 650, 40)
    #snow
    fill("#F0F0EC") #snowy white
    rect(-10, 420, 650, 20)
    
def draw_tree():
    #log
    fill("#53350A")
    rect(440, 180, 30, 240)
    #snow
    fill(255, 255, 255)
    triangle(455, 162, 398, 220, 512, 220)
    triangle(455, 195, 388, 255, 522, 255)
    triangle(455, 225, 378, 295, 532, 295)
    triangle(455, 265, 368, 330, 542, 330)
    #leaves
    fill("#01796f")
    triangle(455, 165, 400, 220, 510, 220)
    triangle(455, 200, 390, 255, 520, 255)
    triangle(455, 230, 380, 295, 530, 295)
    triangle(455, 270, 370, 330, 540, 330)
    
def draw_snowman():
    #arms
    fill(87, 59, 12)#brown
    rect(140, 310, 50, 5)
    rect(50, 310, 50, 5)
    #body
    fill(255, 255, 255)#white
    ellipse(120, 385, 80, 80)
    ellipse(120, 330, 65, 65)
    ellipse(120, 285, 50, 50)
    #nose
    fill("#ed9121")
    triangle(116, 290, 120, 286, 128, 297)
    #eyes
    fill(0, 0, 0)
    ellipse(110, 280, 7, 7)
    ellipse(130, 280, 7, 7)
    fill("#36454f")
    ellipse(110, 280, 5, 5)
    ellipse(130, 280, 5, 5)
    #buttons
    fill("#36454f")
    for y in range(315, 346, 15):
        ellipse(120, y, 6, 6)
    #mohawk
    fill("#554838")
    ellipse(120, 253, 10, 25)
    ellipse(118, 253, 10, 25)
    ellipse(122, 253, 10, 25)
    
def draw_hat():
    #draw hat
    fill(5, 0, 5)
    rect(hat_x[0], hat_y[0], 50, 10)
    rect(hat_x[1], hat_y[1], 30, 35)
    fill("#82172B")
    rect(hat_x[1], hat_y[2], 30, 8)
    #control flying hat
    if(keyPressed == True):
        if(key == 'w'):
            for coord in range(len(hat_y)): hat_y[coord] -= 1
        if(key == 's'):
            for coord in range(len(hat_y)): hat_y[coord] += 1
        if(key == 'a'):
            for coord in range(len(hat_x)): hat_x[coord] -= 1
        if(key == 'd'):
            for coord in range(len(hat_x)): hat_x[coord] += 1
            
