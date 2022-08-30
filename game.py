from pygame import *
WIDTH = 1500
HIEGHT = 700
window = display.set_mode((WIDTH,HIEGHT))
display.set_caption("ghost game")
window.fill("grey")
ghost = image.load("ghost.png")
hunter = image.load("clipart939914.png")
hunter=transform.scale(hunter,(70,100))
ghost=transform.scale(ghost,(70,100))
clock = time.Clock()
bg=image.load("BG.jpeg")
winner = image.load("untitled.png")
bg=transform.scale(bg,(WIDTH,HIEGHT))
winner=transform.scale(winner,(WIDTH,HIEGHT))

x_g = 50
y_g = 50
x_h = 200
y_h = 250
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
    if pkey[K_d] and x_g < WIDTH-80: 
        x_g += 5

    if pkey[K_UP] and y_h > 0:
        y_h -= 4
    if pkey[K_DOWN] and y_h < HIEGHT - 100:
        y_h += 4
    if pkey[K_LEFT] and x_h > 0 :
        x_h -= 4
    if pkey[K_RIGHT] and x_h < WIDTH - 80:
        x_h += 4

    
    window.blit(bg,(0,0))
    window.blit(ghost,(x_g,y_g))
    g = Rect(x_g,y_g,70,100)
    window.blit(hunter,(x_h,y_h))
    h = Rect(x_h,y_h,70,100)
    if g.colliderect(h):    
        window.blit(winner,(0,0))
        
        
    
        
    display.update()
    
       
quit()





