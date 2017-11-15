import pygame
import random

BLACK = (23,23,23)
WHITE = (200,200,200)
YELLOW = (150,150,0)
GREEN = (0,200,0)
RED = (141,0,0)
BLUE = (130,250,236)

size = (600,630)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Asteroides")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Calibri",30,True,False)
#Imagens

player = pygame.image.load("Imagens/nave.png").convert()
player = pygame.transform.scale(player,(55,55))
player.set_colorkey(BLACK)

fundo = pygame.image.load("Imagens/telafundo.png").convert()
fundo = pygame.transform.scale(fundo,(size))

sound = pygame.mixer.Sound("Som/fire.wav")
sound.set_volume(1)
boom= pygame.mixer.Sound("Som/boom.wav")
smash = pygame.mixer.Sound("Som/smash.wav")
smash.set_volume(10)

explosao = pygame.image.load("Imagens/kaboom.png").convert()
explosao = pygame.transform.scale(explosao,(55,55))

meteoro = pygame.image.load("Imagens/meteoro.png").convert()
meteoro = pygame.transform.scale(meteoro,(90,90))

#Variavel Nave

x_speed = 0

x_nave = 300
y_nave = 540

#--------
#Função Meteoro

def meteoro1 (screen,x,y):
    global x_m1
    global y_m1

    screen.blit(meteoro,[x,y])

    if y_m1 <= 590:
        y_m1 += 6
    else:
        x_m1 = random.randint(1,100)
        y_m1 = 0

def meteoro2 (screen,x,y):
    global x_m2
    global y_m2

    screen.blit(meteoro,[x,y])

    if y_m2 <= 590:
        y_m2 += 5
    else:
        x_m2 = random.randint(110,230)
        y_m2 = 0

def meteoro3 (screen,x,y):
    global x_m3
    global y_m3

    screen.blit(meteoro,[x,y])

    if y_m3 <= 590:
        y_m3 += 5
    else:
        x_m3 = random.randint(240,360)
        y_m3 = 0

def meteoro4 (screen,x,y):
    global x_m4
    global y_m4

    screen.blit(meteoro,[x,y])

    if y_m4 <= 590:
        y_m4 += 6
    else:
        x_m4 = random.randint(370,490)
        y_m4 = 0

def meteoro5 (screen,x,y):
    global x_m5
    global y_m5

    screen.blit(meteoro,[x,y])

    if y_m5 <= 590:
        y_m5 += 5
    else:
        x_m5 = random.randint(500,590)
        y_m5 = 0
        
#Variavel Meteoro
x_m1 = random.randint(1,100)
y_m1 = -40

x_m2 = random.randint(110,230)
y_m2 = -10

x_m3 = random.randint(240,360)
y_m3 = 0

x_m4 = random.randint(370,490)
y_m4 = 20

x_m5 = random.randint(500,590)
y_m5 = -80


#------

#TIROS

yt = y_nave-20
t = 0
xt = x_nave+26

def tiro():
    global xt
    global yt
    global t

    pygame.draw.rect(screen,BLUE,[xt,yt,2,14],5)

    if yt >=0:
        yt -= 5

    else:
        yt = y_nave-20
        t = 0


#-------

#Jogador

vida = 3
pontos = 0

#Programa

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -4
            elif event.key == pygame.K_RIGHT:
                x_speed = 4
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0

    if x_nave>0 and x_nave<545:
        x_nave += x_speed
    if x_nave<=0:
        x_nave+=4
    elif x_nave>= 545:
        x_nave-=4

    #carregar fundo
    screen.blit(fundo,(0,0))

    #meteoro
    
    meteoro1(screen,x_m1,y_m1)
    meteoro2(screen,x_m2,y_m2)
    meteoro3(screen,x_m3,y_m3)
    meteoro4(screen,x_m4,y_m4)
    meteoro5(screen,x_m5,y_m5)

    #nave
    
    screen.blit(player,[x_nave,y_nave])
    
    #Colisao Meteoro-Nave

    if x_m1<= x_nave+55 and x_m1+85>= x_nave:
        if y_nave - (y_m1+70)<= 1:
            vida -=1
            x_m1 = random.randint(1,100)
            y_m1 = -40
            boom.play()
            screen.blit(explosao,[x_nave,y_nave])
            pygame.time.delay(300)

    if x_m2<= x_nave+55 and x_m2+85>= x_nave:
        if y_nave - (y_m2+70) <= 1:
            vida -= 1
            x_m2 = random.randint(110,230)
            y_m2 = -10
            boom.play()
            screen.blit(explosao,[x_nave,y_nave])
            pygame.time.delay(300)

    if x_m3<= x_nave+55 and x_m3+85>= x_nave:
        if y_nave - (y_m3+70) <= 1:
            vida -= 1
            x_m3 = random.randint(240,360)
            y_m3 = 0
            boom.play()
            screen.blit(explosao,[x_nave,y_nave])
            pygame.time.delay(300)

    if x_m4<= x_nave+55 and x_m4+85>= x_nave:
        if y_nave - (y_m4+70) <= 1:
            vida -=1
            x_m4 = random.randint(370,490)
            y_m4 = 20
            boom.play()
            screen.blit(explosao,[x_nave,y_nave])
            pygame.time.delay(200)

    if x_m5<= x_nave+55 and x_m5+85>= x_nave:
        if y_nave - (y_m5+70)<=1:
            vida -=1
            x_m5 = random.randint(500,590)
            y_m5 = -80
            boom.play()
            screen.blit(explosao,[x_nave,y_nave])
            pygame.time.delay(300)

    #tiro

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if t == 0:
                xt = x_nave+26
                sound.play()
            t = 1

    if t == 1:
        tiro()

    #colisao tiro

    if t == 1:
        
        if x_m1<= xt+1 and x_m1+90>= xt:
            if yt - (y_m1+77) <= 1:
                pontos += 1
                t = 0
                yt = y_nave - 20
                x_m1 = random.randint(1,100)
                y_m1 = -40
                smash.play()
                
        
        if x_m2<= xt+1 and x_m2+90>=xt:
            if yt - (y_m2+77)<= 1:
                pontos += 1
                t = 0
                yt = y_nave - 20

                x_m2 = random.randint(110,230)
                y_m2 = -10
                smash.play()

        if x_m3<= xt+1 and x_m3+90>=xt:
            if yt - (y_m3+77) <= 1:
                pontos += 1
                t = 0
                yt = y_nave-20

                x_m3 = random.randint(240,360)
                y_m3 = 0
                smash.play()

        if x_m4<= xt+1 and x_m4+90>=xt:
            if yt - (y_m4+77) <= 1:
                pontos += 1
                t = 0
                yt = y_nave-20

                x_m4 = random.randint(370,490)
                y_m4 = 20
                smash.play()

        if x_m5<= xt+1 and x_m5+90>=xt:
            if yt - (y_m5+77) <= 1:
                pontos += 1
                t = 0
                yt = y_nave-20

                x_m5 = random.randint(500,590)
                y_m5 = -80
                smash.play()

    #pontos
    text = font.render(str(pontos),True,BLUE)
    screen.blit(text,[560,20])

    #game over
    if vida == -1:
        pygame.time.delay(1500)
        break
    
    if vida == 3:
        pygame.draw.rect(screen,GREEN,[0,610,600,20],0)
    elif vida == 2:
        pygame.draw.rect(screen,YELLOW,[0,610,400,20],0)

    elif vida == 1:
        pygame.draw.rect(screen,RED,[0,610,200,20],0)

    elif vida <= 0:
        font = pygame.font.SysFont("Calibri",50,True,False)
        gameover = font.render("GAME OVER",True,RED)
        screen.blit(gameover,[175,280])
        vida = -1

    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

print("--------------------------------")
print("\nGAME OVER")
print()

score = []
nome = input("Digite seu nome: ")
aux = [nome,"Pontos: "+str(pontos)]
score.append(aux)
print()
for i in score:
    print(i)


