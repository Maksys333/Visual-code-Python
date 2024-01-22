from typing import Any
from pygame import *

green = (12,166,6)
background = (130, 200, 0)

window = display.set_mode((750, 700))
window.fill(green) 
win_weight = 750
win_height = 700

class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image=transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, x_speed, y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        # Спершу рух по горизонталі
        if self.rect.x <= win_weight - 80 and lion.x_speed > 0 or lion.rect.x >=0 and lion.x_speed < 0:
            self.rect.x += self.x_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: # йдено праворуч, правий край персонажа впритул до лівого краю стіни
            for p in platforms_touched:
                self.rect.right = min(self.rect.right,
                                    p.rect.left) # якщо торкнулися відразу кількох, то правий край мінімальний 13 можливих
        elif self.x_speed < 0: # йдемо ліворуч, ставимо лівий край персонажа впритул до правого краю стіни
            for p in platforms_touched:
                self.rect.left = max(self.rect.left,
                                    p.rect.right) # якщо торкнулися кількох стін, то лівий край максимальний
        if self.rect.y <= win_height - 80 and lion.y_speed > 0 or lion.rect.y >= 0 and lion.y_speed < 0: 
            self.rect.y += self.y_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: # йдемо вниз
            for p in platforms_touched:
                self.y_speed = 0
                # Перевіряємо, яка з платформ знизу найвища, вирівняємося по ній, запам'ятовуємо її як свою опору:
                if p.rect.top < self.rect.bottom: 
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: # йдемо вгору  
            for p in platforms_touched:
                self.y_speed = 0 # при зіткненні зі стіной вертикальна швидкість гаситься self.rect.top = max(self.rect.top,
                self.rect.top = max(self.rect.top,
                                 p.rect.bottom) # вирівнюємо верхній край по нижніх краях стінок, на які наїхали

wall_1 = GameSprite('wall.jpg', 20, 800, 400, 150)
wall_2 = GameSprite('wall.jpg', 300, 20, 110, 335)
wall_3 = GameSprite('wall.jpg', 300, 20, 0, 520)
wall_4 = GameSprite('wall.jpg', 300, 20, 0, 150)
wall_5 = GameSprite('wall.jpg', 20, 140, 600, 0)
wall_6 = GameSprite('wall.jpg', 300, 20, 550, 405)
wall_7 = GameSprite('wall.jpg', 20, 140, 580, 560)
barriers = sprite.Group()
barriers.add(wall_1)
barriers.add(wall_2)
barriers.add(wall_3)
barriers.add(wall_4)
barriers.add(wall_5)
barriers.add(wall_6)
barriers.add(wall_7)

lion = Player('lion.png', 100, 200 - 80, 80, 550, 0, 0)
enemy = GameSprite("hunter.png", 80, 80, 600, 300)
treasures = GameSprite("treasures.png", 80, 80, 630, 570)
speed_runa = GameSprite("steak.png", 80, 80, 40, 40)
god_mode = GameSprite("premium.png", 80, 80, 650, 20)

beef1 = GameSprite("beef.png", 80, 80, 270, 220)
beef2 = GameSprite("beef.png", 80, 80, 50, 400)
beef3 = GameSprite("beef.png", 80, 80, 459, 585)
beef4 = GameSprite("beef.png", 80, 80, 270, 570)

meat = sprite.Group()
meat.add(beef1)
meat.add(beef2)
meat.add(beef3)
meat.add(beef4)

m_speed_x = -5
meat_sum = 0
player_speed = 10
speed_active = False
god_mode_active = False

window = display.set_mode((750, 700))
window.fill(background) 
run = True
while run:
    time.delay(50)
    window.fill(green)
    for e in event.get():
        if e.type == QUIT:
            run = False

    keys = key.get_pressed()
    if keys[K_a]:
        lion.x_speed = -player_speed
    elif keys[K_d]:
        lion.x_speed = player_speed
    else:
        lion.x_speed = 0
    if keys[K_w]:
        lion.y_speed = -player_speed
    elif keys[K_s]:
        lion.y_speed = player_speed
    else:
        lion.y_speed = 0
    
    wall_1.reset()
    wall_2.reset()
    wall_3.reset()
    wall_4.reset()
    wall_5.reset()
    wall_6.reset()
    wall_7.reset()
    lion.reset()
    enemy.reset()
    treasures.reset()
    if not god_mode_active:
        god_mode.reset()
    if not speed_active:
        speed_runa.reset()
    barriers.draw(window)
    platform_touch = sprite.spritecollide(lion, barriers, False)

    if sprite.collide_rect(lion, speed_runa):
        player_speed = 15
        speed_active = True

    if sprite.collide_rect(lion, god_mode):
        god_mode_active = True

    if sprite.collide_rect(lion, enemy) and god_mode_active == False:
        run = False
        #обчислюємо ставлення
        meat.remove(meat)
        img_lose = image.load('background_game_over.jpg')
        window.fill((255, 255, 255))
        window.blit(transform.scale(img_lose, (win_weight, win_height)), (0, 0))
    
    if sprite.collide_rect(lion, treasures):
        run = False
        meat.remove(meat)
        img_win = image.load('background_win.jpg')
        window.fill((255, 255, 255))
        window.blit(transform.scale(img_win, (win_weight, win_height)), (0, 0))
    
    enemy.rect.x += m_speed_x
    if sprite.collide_rect(enemy, wall_2) or enemy.rect.x > win_weight - 80:
        m_speed_x *= -1
    
    meat.draw(window)
    
    for beef in meat:
        if sprite.collide_rect(lion, beef):
            meat.remove(beef)
            meat_sum += 1
    
    display.set_caption(f'Кількість шматків: {meat_sum}')
    
    speed_runa.update()
    enemy.update()
    treasures.update()
    lion.update()
    time.delay(50)
    display.update()
