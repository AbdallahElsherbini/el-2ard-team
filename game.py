from pygame import *

#background options:
WIDTH = 1500
HIEGHT = 700
window = display.set_mode((WIDTH,HIEGHT))
display.set_caption("ghost game")
bg=image.load("BG.jpeg")
winner_hunter = image.load("untitled.png")
winner_ghost = image.load("untitled1.jpg")
bg=transform.scale(bg,(WIDTH,HIEGHT))
winner_hunter=transform.scale(winner_hunter,(WIDTH,HIEGHT))
winner_ghost=transform.scale(winner_ghost,(WIDTH,HIEGHT))


#charachters options:
ghost = image.load("ghost.png")
hunter = image.load("hunter.png")
hunter=transform.scale(hunter,(70,100))
ghost=transform.scale(ghost,(70,100))
clock = time.Clock()
CurrentTime = 0


x_g = 50
y_g = HIEGHT/2
x_h = 1350
y_h = HIEGHT/2
running = True
while running:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            running = False

    pkey =key.get_pressed()
    if pkey[K_w] and y_g > 0:
        y_g -= 5
    if pkey[K_s] and y_g < HIEGHT-90:
        y_g += 5
    if pkey[K_a] and x_g > 0 :
        x_g -= 5
        ghost = image.load("ghost_fliped.png")
        ghost=transform.scale(ghost,(70,100))
    if pkey[K_d] and x_g < WIDTH-80: 
        x_g += 5
        ghost = image.load("ghost.png")
        ghost=transform.scale(ghost,(70,100))

    if pkey[K_UP] and y_h > 0:
        y_h -= 4
    if pkey[K_DOWN] and y_h < HIEGHT - 100:
        y_h += 4
    if pkey[K_LEFT] and x_h > 0 :
        x_h -= 4
        hunter = image.load("hunter.png")
        hunter=transform.scale(hunter,(70,100))
    if pkey[K_RIGHT] and x_h < WIDTH - 80:
        x_h += 4
        hunter = image.load("hunter_fliped.png")
        hunter=transform.scale(hunter,(70,100))

    
    window.blit(bg,(0,0))
    window.blit(ghost,(x_g,y_g))

    #touching each other:
    g = Rect(x_g,y_g,70,100)
    window.blit(hunter,(x_h,y_h))
    h = Rect(x_h,y_h,70,100)
    if g.colliderect(h):    
        window.blit(winner_hunter,(0,0))
        CurrentTime = 0
        time.wait(500)
        
    CurrentTime = int(time.get_ticks() / 1000 - 2)
    if CurrentTime == 60:
        window.blit(winner_ghost, (0,0))
        time.wait(500)
    
        
    display.update()
    
       
quit()





