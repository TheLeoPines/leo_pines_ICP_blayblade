import pygame as pg #Importing pygame as "pg"
from settings import * #Importing from a different made file to access on this file.
from pygame.sprite import Sprite #Importing the sprite command from pygame as "Sprite"

from os import path #using windows terminal

vec=pg.math.Vector2

#Collision
def collide_hit_rect(one,two):
     return one.hit_rect.colliderect(two.rect)

def collide_with_walls(sprite,group,dir):
    #Check for x collision
    if dir=='x':
        #Checking to see if we've collided with hitrects
        hits=pg.sprite.spritecollide(sprite,group,False,collide_hit_rect)
        if hits:
            #This line checks to see if we're to the left side of the wall
            if hits[0].rect.centerx>sprite.hit_rect.centerx:
                #Reposition the player(sprite) to the left side of the wall
                sprite.pos.x=hits[0].rect.left-sprite.hit_rect.width/2
            #This line checks to see if we're to the right side of the wall
            if hits[0].rect.centerx<sprite.hit_rect.centerx:
                #Reposition the player(sprite) to the right side of the wall
                sprite.pos.x=hits[0].rect.right+sprite.hit_rect.width/2
            sprite.vel.x=0
            sprite.hit_rect.centerx=sprite.pos.x

    #Checking for y collision 
    if dir=='y':
        #Checking to see if we've collided with hitrects
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            #This line checks to see if we're to the above of the wall
            if hits[0].rect.centery > sprite.hit_rect.centery:
                #Reposition the player(sprite) to the top of the wall
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            #This line checks to see if we're to the below of the wall
            if hits[0].rect.centery < sprite.hit_rect.centery:
                #Reposition the player(sprite)to the bottom of the wall
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y
        
    


class Player(Sprite):
    # Gives the player a sprite and sets the size and color of the sprites.
    def __init__(self,game,x,y):
        self.groups=game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game=game
        self.image=pg.Surface((TILESIZE,TILESIZE))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.hit_rect=PLAYER_HIT_RECT
        self.vel=vec(0,0)
        self.pos=vec(x*TILESIZE,y*TILESIZE)
        # self.vx, self.vy=0,0
        # self.x=x*TILESIZE
        # self.y=y*TILESIZE

    def get_keys(self):
        #reset v to zero
        #Listen for events specific to keys
        #change velocity based on which key is
        self.vel=vec(0,0) 
        # self.x, self.vy=0,0
        keys=pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]: #Clicking a goes left
            print("trying to go left...")
            self.vel.x=-PLAYER_SPEED
            # self.vx=-PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:#Clicking d goes right
            print("trying to go right...")
            self.vel.x=PLAYER_SPEED
            # self.vx=PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:#Clicking w goes up
            print("trying to go up...")
            self.vel.y=-PLAYER_SPEED
            # self.vy=-PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:#Clicking s goes down
            print("trying to go down...")
            self.vel.y=PLAYER_SPEED
            # self.vy=PLAYER_SPEED
        #Check to see if player is moving diagonal
        if self.vel.x!=0 and self.vel.y!=0:
            self.vel*=0.7071
        #   self.vel.normalize()
        
        # if self.vx!=0 and self.vy!=0:
        #     self.vx*=0.7071
        #     self.vy*=0.7071
    def update(self):
        #Outputing the position of the player.
        self.get_keys()
        self.rect.center=self.pos
        self.pos+=self.vel*self.game.dt
        self.hit_rect.centerx=self.pos.x
        collide_with_walls(self,self.game.all_walls,'x')
        self.hit_rect.centery=self.pos.y
        collide_with_walls(self,self.game.all_walls,'y')
        self.rect.center=self.hit_rect.center
        


#Inputing a wall
class Wall(Sprite):
    def __init__(self,game,x,y):
            self.groups=game.all_sprites, game.all_walls
            Sprite.__init__(self, self.groups)
            self.game=game
            self.image=pg.Surface((TILESIZE,TILESIZE))
            self.image.fill(BLUE)
            self.rect=self.image.get_rect()
            self.vx, self.vy=0,0
            self.x=x*TILESIZE
            self.y=y*TILESIZE
            self.rect.x=self.x
            self.rect.y=self.y
            print("wall initialized")
            print(self.rect.x)
            print(self.rect.y)
#inptuing a mob
class Mob(Sprite):
    def __init__(self,game,x,y):
            self.groups=game.all_sprites, game.all_mobs
            Sprite.__init__(self, self.groups)
            self.game=game
            self.image=pg.Surface((TILESIZE,TILESIZE))
            self.image.fill(RED)
            self.rect=self.image.get_rect()
            self.speed=1
            self.vx, self.vy=500,0
            self.x=x*TILESIZE
            self.y=y*TILESIZE
            self.rect.x=self.x
            self.rect.y=self.y
            print("mob initialized")
            print(self.rect.x)
            print(self.rect.y)
            
    
    def update(self):
        #Thanks pygame for the .right
        if self.rect.right>WIDTH or self.rect.x<0:
             print("Is this a bug>!>!")
             self.speed*=-1
             self.y+=TILESIZE
        self.x+=self.vx*self.game.dt*self.speed
        self.rect.x=self.x
        self.rect.y=self.y

         
    

            
    
    