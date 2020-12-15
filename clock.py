# Clock
# Rohan Deswal
# rohan.deswal22@gmail.com
import pygame
import math
import time
from random import randint
pygame.init()

display_width = 600
display_height = 600

tw = int(display_width/2)
th = int(display_height/2)
lw = 1

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('CLOCK')

clock = pygame.time.Clock()

pos = pygame.mouse.get_pos()

def change_range(OldValue,OldMin,OldMax,NewMin,NewMax):
    return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin

class Star:
    
    def __init__(self):
        
        self.x = randint(5,display_width) 
        self.y = randint(5,display_height)
        self.z = randint(5,display_width)
        self.pz = 1
        self.maxspeed = 30
        
    def update(self,second):
        speed = int(change_range(second+2,0,59,0,self.maxspeed))
        self.z-=speed
        if self.z <= 5:
            self.z = randint(0,display_width)           
    def show(self):
        
        sx = int(change_range((self.x/(self.z+0.001)),0,1,0,display_width))
        sy = int(change_range((self.y/(self.z+0.001)),0,1,0,display_height))
        
        px = int(change_range((self.x/(self.pz+0.001)),0,1,0,display_width))
        py = int(change_range((self.y/(self.pz+0.001)),0,1,0,display_height))
        self.pz = self.z 
        pygame.draw.line(gameDisplay,(255,255,255),(display_width - (tw - sx),display_height - (th - sy)),(display_width - (tw - px),display_height - (th - py)),lw)
        pygame.draw.line(gameDisplay,(255,255,255),((tw - sx),display_height - (th - sy)),((tw - px),display_height - (th - py)),lw)
        pygame.draw.line(gameDisplay,(255,255,255),(display_width - (tw - sx),(th - sy)),(display_width - (tw - px),(th - py)),lw)
        pygame.draw.line(gameDisplay,(255,255,255),((tw - sx),(th - sy)),((tw - px),(th - py)),lw)
            
def gameLoop():

    crashed = False

    stars = []
    for i in range(0,400):
        star = Star()
        stars.append(star)


    w = 100
    h = 100

    a,b = math.radians(90),math.radians(450)

    x = display_width/2 + 100
    y = display_height/2 

    def  show_time(time,x,y):
        font = pygame.font.Font('font.ttf',70)
        text = font.render(time,True,(255,255,255))
        gameDisplay.blit(text,(x,y))
        
    radius = 150
    start = math.radians(90)

    back = (0,0,0)

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    crashed = True

        _time = time.localtime()
        minute = _time.tm_min
        hour = _time.tm_hour % 12
        second =  _time.tm_sec
        time_showing = (str(hour) if hour >= 10 else str('0') + str(hour)) + '.' + (str(minute) if minute >= 10 else str('0') + str(minute)) + '.' + (str(second) if second >= 10 else str('0') + str(second))
                    
        gameDisplay.fill(back)

        for i in range(0,len(stars)):
            stars[i].show()
            stars[i].update(second)
    
        pygame.draw.circle(gameDisplay,back,(int(display_width/2 + 100),int(display_height/2)),10)
        pygame.draw.circle(gameDisplay,(245,222,179),(int(display_width/2 + 100),int(display_height/2)),10,2)
        
        end_second = (((second - 0) * (math.radians(360) - 0)) / (60 - 0)) + 0 + start
        end_minute = (((minute - 0) * (math.radians(360) - 0)) / (60 - 0)) + 0 + start
        end_hour = (((hour - 0) * (math.radians(360) - 0)) / (12 - 0)) + 0 + start

        len_sec = (((second - 0) * (display_height - 0)) / (60 - 0)) + 0
        len_min = (((minute - 0) * (display_height - 0)) / (60 - 0)) + 0 
        len_hour = (((hour - 0) * (display_height - 0)) / (12 - 0)) + 0
        
        pygame.draw.arc(gameDisplay,(255,100,150),[display_width/2 - 100,display_height/2 - 200,400,400],a,b,5)
        pygame.draw.arc(gameDisplay,back,[display_width/2 - 100,display_height/2 - 200,400,400],start,math.radians(540) - end_second,5)
            
        pygame.draw.arc(gameDisplay,(100,255,150),[display_width/2 - 90,display_height/2 - 190,380,380],a,b,5)
        pygame.draw.arc(gameDisplay,back,[display_width/2 - 90,display_height/2 - 190,380,380],start,math.radians(540) - end_minute,5)

        pygame.draw.arc(gameDisplay,(150,100,255),[display_width/2 - 80,display_height/2 - 180,360,360],a,b,5)
        pygame.draw.arc(gameDisplay,back,[display_width/2 - 80,display_height/2 - 180,360,360],start,math.radians(540) - end_hour,5)

        angle_s = end_second - start + math.radians(-88)
        angle_m = end_minute - start + math.radians(-90)
        angle_h = end_hour - start + math.radians(-90)
        
        xs = x + (math.cos((angle_s)) * radius - 10)
        ys = y + (math.sin((angle_s)) * radius - 10)

        xm = x + (math.cos((angle_m)) * (radius - 20))
        ym = y + (math.sin((angle_m)) * (radius - 20))

        xh = x + (math.cos((angle_h)) * (radius - 40))
        yh = y + (math.sin((angle_h)) * (radius - 40))
        
        pygame.draw.line(gameDisplay,(255,100,150),(x,y),(xs,ys),5)
        pygame.draw.line(gameDisplay,(100,255,150),(x,y),(xm,ym),5)
        pygame.draw.line(gameDisplay,(150,100,255),(x,y),(xh,yh),5)

        pygame.draw.rect(gameDisplay,(255,100,150),[130,display_height - int(len_sec),50,len_sec])
        pygame.draw.rect(gameDisplay,(100,255,150),[70,display_height - int(len_min),50,len_min])
        pygame.draw.rect(gameDisplay,(150,100,255),[10,display_height - int(len_hour),50,len_hour])

        show_time(time_showing,display_width/2 - (60) + 100,display_height/2)
        show_time(str(hour) if hour >= 10 else str('0') + str(hour),15,display_height - 100)
        show_time(str(minute) if minute >= 10 else str('0') + str(minute),75,display_height - 100)
        show_time(str(second) if second >= 10 else str('0') + str(second),135,display_height - 100)
        
        pygame.display.update()
        clock.tick(60)
        
gameLoop()
pygame.display.quit()
