from pygame import *

#background options:
WIDTH = 1500
HIEGHT = 700
display.set_caption("El-2ard team ghost game")
theme = int(input("choose theme [1:5] : "))
if theme == 1:
    bg=image.load("bg1.jpg")
elif theme == 2:
    bg=image.load("bg2.jpg")
elif theme == 3:
    bg=image.load("bg3.jpg")
elif theme == 4:
    bg=image.load("bg4.jpg")
else:
    bg=image.load("bg5.jpg")
window = display.set_mode((WIDTH,HIEGHT))
winner_hunter = image.load("untitled.png")
winner_ghost = image.load("untitled1.jpg")
bg=transform.scale(bg,(WIDTH,HIEGHT))
winner_hunter=transform.scale(winner_hunter,(WIDTH,HIEGHT))
winner_ghost=transform.scale(winner_ghost,(WIDTH,HIEGHT))

#charachters options:
ghost = image.load("ghost.png")
hunter = image.load("hunter.png")
hunter=transform.scale(hunter,(86,100))
ghost=transform.scale(ghost,(70,100))
hunter_looking = 0
clock = time.Clock()
CurrentTime = 0

#bullets:
Lbullets = []
class bullets:
    def __init__(self,x,y,direction):
        Lbullets.append(self)
        self.body = Rect(x , y+55 , 20 , 5)
        self.dirct = direction 
    def shoot(self):
        
        if self.dirct == 0:
            self.body.x -= 10
        elif self.dirct == 1:
            self.body.x += 10
        draw.rect(window,"yellow",bew.body)
        if self.body.x <= 0 or self.body.x >= WIDTH :
            Lbullets.remove(self)
    def hit(self,g):
        if g.colliderect(bew.body):
            window.blit(winner_hunter,(0,0))
            Lbullets.remove(self)
            CurrentTime = 0
            time.wait(500)

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
        hunter=transform.scale(hunter,(86,100))
        hunter_looking = 0
    if pkey[K_RIGHT] and x_h < WIDTH - 80:
        x_h += 4
        hunter = image.load("hunter_fliped.png")
        hunter=transform.scale(hunter,(86,100))
        hunter_looking = 1
    if pkey[K_SPACE] and len(Lbullets) <=1:
        bew = bullets(x_h,y_h,hunter_looking)
    for bew in Lbullets:
        bew.shoot()
        display.update()

    window.blit(bg,(0,0))
    window.blit(ghost,(x_g,y_g))

    #touching each other:
    g = Rect(x_g,y_g,55,70)
    window.blit(hunter,(x_h,y_h))
    h = Rect(x_h,y_h,60,70)
    if g.colliderect(h):    
        window.blit(winner_hunter,(0,0))
        CurrentTime = 0
        time.wait(500)
    for bew in Lbullets:
        bew.hit(g)
        
    CurrentTime = int(time.get_ticks() / 1000 - 2)
    if CurrentTime == 60:
        window.blit(winner_ghost, (0,0))
        time.wait(500)
        
    display.update()
          
quit()
