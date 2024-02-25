from pygame import *
from random import choice
font.init()

#створи вікно гри
TILESIZE = 45
AAA = 500
MAP_WIDTH, MAP_HEIGHT = 15, 15
WIDTH, HEIGHT = TILESIZE*MAP_WIDTH, TILESIZE*MAP_HEIGHT
FPS = 60

font1 = font.SysFont('Roboto', 30)
font2 = font.SysFont('Roboto', 30)


window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Labirinth')
clock = time.Clock() #game timer

bg = image.load("floor_bg.png")
bg = transform.scale(bg, (WIDTH, HEIGHT)) #resize bg




treasure_img = image.load("chest.png")

wall1_img = image.load('wall1.png')
wall2_img = image.load('wall2.png')
wall3_img = image.load('wall3.png')
wall4_img = image.load('wall4.png')
wall5_img = image.load('wall5.png')
wall6_img = image.load('wall6.png')
wall7_img = image.load('wall7.png')
wall8_img = image.load('wall8.png')
floor_img = image.load('floor.png')
corner1_img = image.load('corner1.png')
corner2_img = image.load('corner2.png')
corner3_img = image.load('corner3.png')
corner4_img = image.load('corner4.png')
bb_img = image.load('black_block.png')
sf_img = image.load('sight_field.png')
bed_img = image.load('bed.png')
shelf_img = image.load('shelfes.png')
lfurniture = image.load('livingroom_furinture.png')
chest_highlited = image.load('chest-highlited.png')
kfurn_img = image.load('kitchen-interior.png')

sprites = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, width=60, height=60, x=100, y=250):
        super().__init__()
        self.hp = 100
        self.image = transform.scale(sprite_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = mask.from_surface(self.image)
        sprites.add(self)
    def draw(self, window):
        window.blit(self.image, self.rect)

class SightField(sprite.Sprite):
    def __init__(self, sprite_image, width=500, height=500, x=100, y=250):
        super().__init__()
        sprites.remove(self)
        self.image = transform.scale(sprite_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        sprites.add(self)
    def draw(self, window):
        window.blit(self.image, self.rect)

sight_field = SightField(sf_img, 2500,2500, 0,0)

class Player(GameSprite):
    
    def __init__(self, sprite_image, width=15, height=15, x=100, y=250):
        super().__init__(sprite_image,TILESIZE,TILESIZE, x, y)
        sprites.remove(self)
        self.speed = 2
        self.images = {
            "down": [image.load('a1.png'), image.load('a2.png')],
            "right": [image.load('a4.png'), image.load('a5.png')],
            "left": [image.load('a6.png'), image.load('a7.png')],
            "up": [image.load('a8.png'), image.load('a3.png')],
            'idle': [image.load('idle1.png'), image.load('idle2.png')]  # Assuming a3 is also the up sprite
        }
        
        self.direction = "down"
        self.frame = 0
        self.last_update = time.get_ticks()
        self.frame_rate = 200  # milliseconds per frame

    def update(self):
        global hp_text
        now = time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame = (self.frame + 1) % 2  # Cycle through the frames
            self.image = self.images[self.direction][self.frame]
            self.mask = mask.from_surface(self.image)
        self.old_pos = self.rect.x, self.rect.y
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            sight_field.rect.y -= self.speed
            self.direction = "up"
        if keys[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
            sight_field.rect.y += self.speed
            self.direction = "down"
        if keys[K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
            sight_field.rect.x -= self.speed
            self.direction = "left"
        if keys[K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            sight_field.rect.x += self.speed
            self.direction = "right"
        collidelist = sprite.spritecollide(self, walls, False, sprite.collide_mask)
        if len(collidelist) > 0:
            self.rect.x, self.rect.y = self.old_pos
            sight_field.rect.centerx, sight_field.rect.centery = self.old_pos
        collidelist = sprite.spritecollide(self, others, False, sprite.collide_mask)
        if len(collidelist) > 0:
            self.rect.x, self.rect.y = self.old_pos
            sight_field.rect.centerx, sight_field.rect.centery = self.old_pos
        

    def draw(self, window):
        
        window.blit(self.image , self.rect)
        


walls = sprite.Group()
class Wall1(GameSprite):
    def __init__(self, x, y):
        super().__init__(wall1_img, TILESIZE, TILESIZE, x, y)      
        walls.add(self)

class Wall2(GameSprite):
    def __init__(self, x, y):
        super().__init__(wall2_img, TILESIZE, TILESIZE, x, y)      
        walls.add(self)

class Wall3(GameSprite):
    def __init__(self, x, y):
        super().__init__(wall3_img, TILESIZE, TILESIZE, x, y)      
        walls.add(self)

class Wall4(GameSprite):
    def __init__(self, x, y):
        super().__init__(wall4_img, TILESIZE, TILESIZE, x, y)      
        walls.add(self)

class Wall5(GameSprite):
    def __init__(self, x, y):
        super().__init__(wall5_img, TILESIZE, TILESIZE+1, x, y)      
        walls.add(self)

class Wall6(GameSprite):
    def __init__(self, x, y):
        super().__init__(wall6_img, TILESIZE, TILESIZE, x, y)      
        walls.add(self)


class Wall7(GameSprite):
    def __init__(self, x, y):
        super().__init__(wall7_img, TILESIZE, TILESIZE, x, y)      
        walls.add(self)
class Wall8(GameSprite):
    def __init__(self, x, y):
        super().__init__(wall8_img, TILESIZE, TILESIZE, x, y)      
        walls.add(self)
others=sprite.Group()
class Other(GameSprite):
    def __init__(self,sprite_img, width, height, x, y):
        super().__init__(sprite_img,width, height, x, y)      
        others.add(self)

player = Player(image.load('idle1.png'), TILESIZE, TILESIZE)

finish_text = font2.render('Game Over!', True, (255, 0, 15))
treasure = None
collision_block = None
hole1 = None
def start_level(level):
    global collision_block, hole1, treasure

    with open(level, 'r') as file:
        x, y = 0, 0
        map = file.readlines()

        # for row in map:
        #     for symbol in map:
        #         if symbol == ' ' or symbol == '' or symbol == 'f':
        #             GameSprite(floor_img,TILESIZE,TILESIZE,x,y)
        #         x+=TILESIZE
        #     y+= TILESIZE
        # x, y = 0,0
        for row in map:
            
            for symbol in row:

                if symbol == '1':
                    Wall1(x, y)
                if symbol == '2':
                    Wall2(x,y)
                if symbol == '3':
                    Wall3(x,y)
                elif symbol == '(':
                    GameSprite(image.load('floor3.png'), TILESIZE, TILESIZE,x,y)
                elif symbol == 'H':
                    GameSprite(image.load('floor_hole3.png'), TILESIZE, TILESIZE,x,y)
                elif symbol == 'P':
                    player.rect.x = x
                    player.rect.y = y
                    player.start_x, player.start_y = player.rect.x, player.rect.y
                    sight_field.rect.centerx = x
                    sight_field.rect.centery = y
                elif symbol == 't':
                    
                    treasure = Other(treasure_img, TILESIZE, TILESIZE+45, x, y)
                elif symbol == '4':
                    Wall4(x,y)
                elif symbol == '5':
                    Wall5(x,y)
                elif symbol == '6':
                    Wall6(x,y)
                elif symbol == '7':
                    Wall7(x,y)
                elif symbol == '!':
                    GameSprite(bb_img, TILESIZE,TILESIZE,x,y)
                    GameSprite(corner1_img, TILESIZE-15, TILESIZE-15, x,y)
                    
                elif symbol == "@":
                    GameSprite(bb_img, TILESIZE,TILESIZE,x,y)

                    GameSprite(corner2_img, TILESIZE-15, TILESIZE-15, x+15,y)
                elif symbol == '#':
                    GameSprite(bb_img, TILESIZE,TILESIZE,x,y)
                    GameSprite(corner3_img, TILESIZE-15, TILESIZE-15,x,y)
                elif symbol == '$':
                    GameSprite(bb_img, TILESIZE,TILESIZE,x,y)
                    GameSprite(corner4_img, TILESIZE-15, TILESIZE-15,x+15,y+15)

                elif symbol == '8':
                    Wall8(x,y)
                elif symbol == 'b':
                    GameSprite(bb_img, TILESIZE, TILESIZE,x,y)
                elif symbol == 'B':
                    bed = Other(bed_img,TILESIZE+45, TILESIZE+120, x+5,y)
                elif symbol == 's':
                    shelf = Other(shelf_img, TILESIZE,TILESIZE+25,x,y)
                elif symbol == 'l':
                    lfurn = Other(lfurniture, TILESIZE+155, TILESIZE+35,x,y)
                elif symbol == 'k':
                    kfurn = Other(kfurn_img, TILESIZE+100, TILESIZE+35,x, -5)
                elif symbol == 'h':
                    
                    hole1 = GameSprite(image.load('floor_hole1.png'), TILESIZE, TILESIZE, x,y)
                elif symbol == 'a':
                    Other(image.load('abandoned_shelf.png'), TILESIZE, TILESIZE+50, x,y)
                elif symbol == ')':
                    Other(image.load('barrels.png'), TILESIZE+70, TILESIZE+45, x,y)
                elif symbol == 'A':
                    Other(image.load('abandoned_table.png'), TILESIZE+25, TILESIZE+35, x,y)
                elif symbol == 'C':
                   
                    collision_block=GameSprite(image.load('collision_block.png'), TILESIZE, TILESIZE, x,y)

            
                x += TILESIZE
            y+=TILESIZE
            x = 0


start_level('map2.txt')
finish = False
while True:
#оброби подію «клік за кнопкою "Закрити вікно"»
    for e in event.get():
        if e.type == QUIT:
            quit()
    
    window.blit(bg, (0,0))
    sprites.draw(window)
    others.draw(window)
    if not finish == True:
        player.update()
        sight_field.update()
    if player.hp <= 0:
        finish = True
    if sprite.collide_rect(player, collision_block):
        print('avc')
        for s in sprites:
            s.kill()
        
        start_level('map2.txt')
    elif sprite.collide_rect(player, hole1):
        for s in sprites:
            s.kill()
        start_level('map3.txt')        
    
    if sprite.collide_rect(player, treasure):        
        finish = True
        finish_text = font2.render('U Won!', True, (255, 0, 15))
    if finish:
        window.blit(finish_text, (500, 500))
    player.draw(window)
    sight_field.draw(window)
    display.update()
    clock.tick(FPS)