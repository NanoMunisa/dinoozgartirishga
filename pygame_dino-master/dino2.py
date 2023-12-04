import pygame
import os


# pygame initsalizatsiya qilish
pygame.init()

#Ekran sozlamalari
ScreenHeight = 600
ScreenWidth  = 1200

# ekranni sozlamalarini qullash
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))


#yurish rasmlari yuklab olamiz
Running = [pygame.image.load(os.path.join("dino/Dino", "DinoRun1.png")), pygame.image.load(os.path.join("dino/Dino", "DinoRun2.png"))]

#sakrash rasmlari yuklab olamiz
Jumping = pygame.image.load(os.path.join("dino/Dino", "DinoJump.png"))

#pastlash rasmlari yuklab olish
Dunking = [pygame.image.load(os.path.join("dino/Dino", "DinoDuck1.png")), pygame.image.load(os.path.join("dino/Dino", "DinoDuck2.png"))]

Small_cactus = [pygame.image.load(os.path.join("dino/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("dino/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("dino/Cactus", "SmallCactus3.png")) ]
Large_cactus = [pygame.image.load(os.path.join("dino/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("dino/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("dino/Cactus", "LargeCactus3.png")),  ]

Bird         = [pygame.image.load(os.path.join("dino/Bird", "Bird1.png")),
                pygame.image.load(os.path.join("dino/Bird", "Bird2.png")),]

Cloud        = pygame.image.load(os.path.join("dino/Other", "Cloud.png"))


BG           = pygame.image.load(os.path.join("dino/Other", "Track.png"))



# boshlaymiz


# dino classi
class Dinosaur:
    x_pos = 80
    y_pos = 310
    y_pos_duck = 340
    Jump_Vel = 8.5

    def __init__(self):
        self.duck_img = Dunking
        self.run_img = Running
        self.jump_img = Jumping

        # dino holati
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        # qiyinlik darajasi
        self.step_index = 0
        self.jump_vel = self.Jump_Vel
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()

        #dino pozitsiyasi
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    # dinoni holatini yangilash metodi
    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        

        if self.step_index >= 10:
            self.step_index = 0
        

        if userInput[pygame.K_UP] and not self.dino_jump: 
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False


    #dino pasayishi
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y  = self.y_pos_duck
        self.step_index +=1
    

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index +=1




    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.Jump_Vel:
            self.dino_jump = False
            self.jump_vel = self.Jump_Vel 

    


    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y) )





def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        screen.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(screen)
        player.update(userInput)


        clock.tick(30)
        pygame.display.update()
         



         









main()




#972286210 Nusrat 




