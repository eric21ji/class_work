import random

"""
This program starts off by drawing three stars (make sure it works).
Do the following in steps:
1. Increase the number of stars to 5.
2. Rather than calling an ellipse function for each star, 
   create a while loop with an index variable to draw them.
3. Rather than manually adding stars, create a for loop that will add 100
   stars to the stars_x and stars_y lists with random x/y coordinates.
4. Create a for loop to increase the x location ever so slightly to make the 
   stars move across the sky.
5. Within the draw loop, use the list.append() method on both lists to 
   periodically add another star. Add the star off-screen and let it move into view.
   - You need to limit the number of times per second a new star is added, or there
     will be too many created (60 per second). Use frameCount % 60 == 0 to create one every 60 frames.
6. If any particular star has moved out of view, remove it from the lists. Use list.pop(index) to remove
   the appropriate coordinates.
7. Convert the two coordinate lists into a 2-dimensional list called 'stars'. The general structure will be:
   stars = [[x1, y2], [x2, y2], [x3, y3]]
   stars[0]     # the first star as a list of coordinates [x1, y1]
   stars[0][0]  # the first star's x coordinate, x1
   stars[0][1]  # the first star's y coordinate, y1
"""
stars = []
for i in range(101):
    stars.append([random.randint(1, 640), random.randint(1, 480)])

def setup():
    size(640, 480)

def draw():
    background(0)
    
    # draw stars
    noStroke()
    fill(255)
    
    #draw stars
    for star in range(len(stars)):
        ellipse(stars[star][0], stars[star][1], 5, 5)
    
    #move stars
    for star in range(len(stars)):
        stars[star][0] += 1
    
    #pop stars
    for star in range(len(stars)-1, 0, -1):  #move in reverse, otherwise index out of bounds when a coordinate is popped from the list
        if stars[star-1][0] >= width + 5:
            stars.pop(star-1)
            
    #add new star every second
    if frameCount % 60 == 0:
        stars.append([0, random.randint(1, height)])
