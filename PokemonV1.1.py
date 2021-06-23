import pygame
from pygame.locals import *
from pygame import mixer
import sys
import random
import os
import time

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Impact', 40)


class Janela:  # Cria a Janela
    __alt = 0
    __lar = 0
    __cor = (0, 0, 0)

    def __init__(self, altura, largura):
        self.__alt = altura
        self.__lar = largura

    def get_dimensoes(self):
        return (self.__alt, self.__lar)

    def get_cor(self, R, G, B):
        x = (R, G, B)
        return x


w = Janela(800, 600)  # Cria a Janela
win = pygame.display.set_mode(w.get_dimensoes())
pygame.display.set_caption("Pokepy")

# importar Fundo
image = pygame.image.load("pokepyinicio.svg.png")
win.blit(image, (0, 0))
pygame.display.update()  # Atualização Da Aba Para Aparecer O Que For Adicionado
win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo

# Música
pygame.mixer.init()
pygame.init()
#pygame.mixer.music.load('depp.mp3')
#pygame.mixer.music.play()
#pygame.mixer.music.set_volume(1)
pygame.time.delay(2000)  # Delay Para A Visualização

rect_yChange = 50
t01 = pygame.Surface((560, 100))
t01.set_alpha(100)
t01.fill((240, 240, 240))
win.blit(t01, (125, rect_yChange))
pygame.display.update()  # Atualização Da Aba Para Aparecer O Que For Adicionado
PokemonChanged = False
while PokemonChanged == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
    # Escolher Pokemon
    # importar Botao1
    image = pygame.image.load("wartortleT.jpg")
    win.blit(image, (125, 50))

    # importar Botao2
    image = pygame.image.load("vulpix.jpg")
    win.blit(image, (125, 175))

    # importar Botao3
    image = pygame.image.load("snorlax.jpg")
    win.blit(image, (125, 300))

    # importar Botao4
    image = pygame.image.load("porygon.jpg")
    win.blit(image, (125, 425))

    if keys[K_UP]:
        rect_yChange -= 125
        if rect_yChange < 0:
            rect_yChange += 500
        # EfeitoSonoro
        #pygame.mixer.music.load("Baloon Alert.mp3")
        #pygame.mixer.music.play()
        #pygame.event.wait()
        time.sleep(0.1)

    if keys[K_DOWN]:
        rect_yChange += 125
        if rect_yChange > 500:
            rect_yChange -= 500
        # EfeitoSonoro
        #pygame.mixer.music.load("Baloon Alert.mp3")
        #pygame.mixer.music.play()
        #pygame.event.wait()
        time.sleep(0.1)

    win.blit(t01, (125, rect_yChange))
    pygame.display.update()  # Atualização Da Aba Para Aparecer O Que For Adicionado

    if rect_yChange == 50 and keys[K_RETURN]:
        Pokemon = "wartortle"
        win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
        PokemonChanged = True
    if rect_yChange == 175 and keys[K_RETURN]:
        Pokemon = "vulpix"
        win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
        PokemonChanged = True
    if rect_yChange == 300 and keys[K_RETURN]:
        Pokemon = "snorlax"
        win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
        PokemonChanged = True
    if rect_yChange == 425 and keys[K_RETURN]:
        Pokemon = "porygon"
        win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
        PokemonChanged = True

if Pokemon == "wartortle":
    class Wartortle:
        vida = 700

        def __init__(self, vida):
            self.vida = v

        def controladorvida(self, v):
            if self.vida <= 0:
                self.vida = 0
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                textsurface = myfont.render('You Lose', False, (250, 100, 250))
                win.blit(textsurface, (340, 80))
                pygame.display.update()
                time.sleep(10)
                exit(0)
        def AtaqueAdversario(self, v):
            self.vida -= random.randrange(0, 200)

        def Potion(self, v):
            self.vida += 50

        def BarraDeVida(self, v):
            if self.vida == 700:
                Barra = pygame.Surface((125, 12))
                Barra.fill((0, 255, 0))
            if self.vida <= 699:
                Barra = pygame.Surface((100, 12))
                Barra.fill((0, 255, 0))
            if self.vida < 500:
                Barra = pygame.Surface((75, 12))
                Barra.fill((0, 255, 0))
            if self.vida < 400:
                Barra = pygame.Surface((50, 12))
                Barra.fill((200, 200, 0))
            if self.vida < 100:
                Barra = pygame.Surface((25, 12))
                Barra.fill((255, 0, 0))
            if self.vida < 1:
                Barra = pygame.Surface((1, 12))
            win.blit(Barra, (445, 340))

if Pokemon == "vulpix":
    class Vulpix:
        vida = 500

        def __init__(self, vida):
            self.vida = v

        def controladorvida(self, v):
            if self.vida <= 0:
                self.vida = 0
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                textsurface = myfont.render('You Lose', False, (250, 100, 250))
                win.blit(textsurface, (340, 80))
                pygame.display.update()
                time.sleep(10)
                exit(0)
        def AtaqueAdversario(self, v):
            self.vida -= random.randrange(0, 200)

        def Potion(self, v):
            self.vida += 50

        def BarraDeVida(self, v):
            if self.vida == 500:
                Barra = pygame.Surface((125, 12))
                Barra.fill((0, 255, 0))
            if self.vida < 500:
                Barra = pygame.Surface((100, 12))
                Barra.fill((0, 255, 0))
            if self.vida < 400:
                Barra = pygame.Surface((75, 12))
                Barra.fill((0, 255, 0))
            if self.vida < 300:
                Barra = pygame.Surface((50, 12))
                Barra.fill((200, 200, 0))
            if self.vida < 200:
                Barra = pygame.Surface((25, 12))
                Barra.fill((255, 0, 0))
            if self.vida < 1:
                Barra = pygame.Surface((1, 12))
            win.blit(Barra, (445, 340))

if Pokemon == "snorlax":
    class Snorlax:
        vida = 1000

        def __init__(self, vida):
            self.vida = v

        def controladorvida(self, v):
            if self.vida <= 0:
                self.vida = 0
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                textsurface = myfont.render('You Lose', False, (250, 100, 250))
                win.blit(textsurface, (340, 80))
                pygame.display.update()
                time.sleep(10)
                exit(0)
        def AtaqueAdversario(self, v):
            self.vida -= random.randrange(0, 200)

        def Potion(self, v):
            self.vida += 50

        def Sleep(self, v):
            textsurface = myfont.render('Snorlax Usa Sleep', False, (250, 100, 250))
            win.blit(textsurface, (50, 100))
            self.vida += 80

        def BarraDeVida(self, v):
            if self.vida >= 1000:
                Barra = pygame.Surface((125, 12))
                Barra.fill((0, 255, 0))
            if self.vida <= 999:
                Barra = pygame.Surface((100, 12))
                Barra.fill((0, 255, 0))
            if self.vida <= 600:
                Barra = pygame.Surface((75, 12))
                Barra.fill((0, 255, 0))
            if self.vida <= 500:
                Barra = pygame.Surface((50, 12))
                Barra.fill((200, 200, 0))
            if self.vida <= 300:
                Barra = pygame.Surface((25, 12))
                Barra.fill((255, 0, 0))
            if self.vida <= 0:
                Barra = pygame.Surface((1, 12))
            win.blit(Barra, (445, 340))

if Pokemon == "porygon":
    class Porygon:
        vida = 500

        def __init__(self, vida):
            self.vida = v

        def controladorvida(self, v):
            if self.vida <= 0:
                self.vida = 0
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                textsurface = myfont.render('You Lose', False, (250, 100, 250))
                win.blit(textsurface, (340, 80))
                pygame.display.update()
                time.sleep(10)
                exit(0)
        def AtaqueAdversario(self, v):
            self.vida -= random.randrange(0, 200)

        def Potion(self, v):
            self.vida += 50

        def BarraDeVida(self, v):
            if self.vida == 500:
                Barra = pygame.Surface((125, 12))
                Barra.fill((0, 255, 0))
            if self.vida < 500:
                Barra = pygame.Surface((100, 12))
                Barra.fill((0, 255, 0))
            if self.vida < 400:
                Barra = pygame.Surface((75, 12))
                Barra.fill((0, 255, 0))
            if self.vida < 300:
                Barra = pygame.Surface((50, 12))
                Barra.fill((200, 200, 0))
            if self.vida < 200:
                Barra = pygame.Surface((25, 12))
                Barra.fill((255, 0, 0))
            if self.vida < 1:
                Barra = pygame.Surface((1, 12))
            win.blit(Barra, (445, 340))

class Adversario:
    vida = 800

    def __init__(self, vida):
        self.vida = v

    def controladorvida(self, v):
        if self.vida < 0:
            self.vida = 0
            win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
            textsurface = myfont.render('You Win', False, (250, 100, 250))
            win.blit(textsurface, (340, 80))
            pygame.display.update()
            time.sleep(10)
            exit(0)

    def BarraDeVida(self, v):
        if self.vida == 800:
            Barra = pygame.Surface((125, 12))
            Barra.fill((0, 255, 0))
        if self.vida <= 799:
            Barra = pygame.Surface((100, 12))
            Barra.fill((0, 255, 0))
        if self.vida < 600:
            Barra = pygame.Surface((75, 12))
            Barra.fill((0, 255, 0))
        if self.vida <= 400:
            Barra = pygame.Surface((50, 12))
            Barra.fill((200, 200, 0))
        if self.vida <= 200:
            Barra = pygame.Surface((25, 12))
            Barra.fill((255, 0, 0))
        if self.vida < 1:
            Barra = pygame.Surface((1, 12))
        win.blit(Barra, (345, 65))

    def Bite(self, v):
        self.vida -= 40
        textsurface = myfont.render('Wartortle Usa Bite', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
    def HydroPump(self, v):
        textsurface = myfont.render('Wartortle Usa HydroPump', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 80
    def IceBeam(self, v):
        textsurface = myfont.render('Wartortle Usa IceBeam', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 90
    def WaterGun(self, v):
        textsurface = myfont.render('Wartortle Usa WaterGun', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 40
    def Ember(self, v):
        textsurface = myfont.render('Vulpix Usa Ember', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 40
    def Flamethrower(self, v):
        textsurface = myfont.render('Vulpix Usa Flamethrower', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 90
    def Incinerate(self, v):
        textsurface = myfont.render('Vulpix Usa Incinerate', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 60
    def MysticalFire(self, v):
        textsurface = myfont.render('Vulpix Usa MysticalFire', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 75
    def BodySlam(self, v):
        textsurface = myfont.render('Snorlax Usa Slam', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 85
    def GigaImpact(self, v):
        textsurface = myfont.render('Snorlax Usa GigaImpact', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 150
    def Crunch(self, v):
        textsurface = myfont.render('Snorlax Usa Crunch', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 80
    def Psybeam(self, v):
        textsurface = myfont.render('Porygon Usa Psybeam', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 65
    def HyperBeam(self, v):
        textsurface = myfont.render('Porygon Usa HyperBeam', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 150
    def DreamEater(self, v):
        textsurface = myfont.render('Porygon Usa DreamEater', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 100
        #EasterEgg
        image = pygame.image.load("Jorge.JPG")
        win.blit(image, (0, 475))
    def ShadowBall(self, v):
        textsurface = myfont.render('Porygon Usa ShadowBall', False, (250, 100, 250))
        win.blit(textsurface, (10, 100))
        self.vida -= 80

#MenuDeBatalha
if PokemonChanged:

    time.sleep(0.25)

    # importar BotaoFight
    image = pygame.image.load("fight.png")
    win.blit(image, (0, 475))

    # importar BotaoBag
    image = pygame.image.load("bag.png")
    win.blit(image, (275, 475))

    rect_x = 14
    t = pygame.Surface((240, 80))
    t.set_alpha(100)
    t.fill((250, 0, 0))
    win.blit(t, (rect_x, 481))

    pygame.display.update()  # Atualização Da Aba Para Aparecer O Que For Adicionado

    clock = pygame.time.Clock()
    FPS = clock.tick(40)  # Limite de FPS

    # Inicia o Menu Do Jogo
    while PokemonChanged == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.event.pump()
        keys = pygame.key.get_pressed()
        win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo

        itens = False
        fight = False

        # importar BotaoFight
        image = pygame.image.load("fight.png")
        win.blit(image, (0, 475))

        # importar BotaoBag
        image = pygame.image.load("bag.png")
        win.blit(image, (275, 475))

        kadabra = pygame.image.load("kadabra.png")
        kadabra = pygame.transform.scale(kadabra, (300, 250))
        win.blit(kadabra, (475, 25))

        barra = pygame.image.load("BarraClear.png")
        barra = pygame.transform.scale(barra, (250, 75))
        barra2 = pygame.image.load("BarraClear.png")
        barra2 = pygame.transform.scale(barra2, (250, 75))
        win.blit(barra, (250, 25))
        win.blit(barra2, (350, 300))

        if Pokemon == "wartortle":
            wartortle = pygame.image.load("wartortle-back.png")
            wartortle = pygame.transform.scale(wartortle, (300, 250))
            win.blit(wartortle, (150, 200))
            Wartortle.BarraDeVida(Wartortle, 0)
            Adversario.BarraDeVida(Adversario, 0)

        if Pokemon == "vulpix":
            vulpix = pygame.image.load("vulpix-back.png")
            vulpix = pygame.transform.scale(vulpix, (280, 250))
            win.blit(vulpix, (135, 195))
            Vulpix.BarraDeVida(Vulpix, 0)
            Adversario.BarraDeVida(Adversario, 0)

        if Pokemon == "snorlax":
            snorlax = pygame.image.load("snorlax-back.png")
            snorlax = pygame.transform.scale(snorlax, (255, 225))
            win.blit(snorlax, (143, 225))
            Snorlax.BarraDeVida(Snorlax, 0)
            Adversario.BarraDeVida(Adversario, 0)

        if Pokemon == "porygon":
            porygon = pygame.image.load("porygon-back.png")
            porygon = pygame.transform.scale(porygon, (255, 240))
            win.blit(porygon, (143, 225))
            Porygon.BarraDeVida(Porygon, 0)
            Adversario.BarraDeVida(Adversario, 0)

        if keys[K_RIGHT]:
            rect_x += 275
            if rect_x > 550:
                rect_x -= 825
            #EfeitoSonoro
            #pygame.mixer.music.load("Baloon Alert.mp3")
            #pygame.mixer.music.play()
            #pygame.event.wait()
            time.sleep(0.25)

            t = pygame.Surface((240, 80))
            t.set_alpha(100)
            t.fill((250, 0, 0))
            win.blit(t, (rect_x, 481))

        if keys[K_LEFT]:
            rect_x -= 275
            if rect_x < 0:
                rect_x += 550
            #EfeitoSonoro
            #pygame.mixer.music.load("Baloon Alert.mp3")
            #pygame.mixer.music.play()
            #pygame.event.wait()
            time.sleep(0.25)

        t = pygame.Surface((240, 80))
        t.set_alpha(100)
        t.fill((250, 0, 0))
        win.blit(t, (rect_x, 481))

        pygame.display.update()  # Atualização Da Aba Para Aparecer O Que For Adicionado

        if keys[K_RETURN] and rect_x == 289:
            win.fill(w.get_cor(50, 50, 200))  # Redesenha O Fundo
            # importar Botao1
            image = pygame.image.load("grade.png")
            win.blit(image, (125, 50))
            textsurface = myfont.render('Potion', False, (250, 100, 250))
            win.blit(textsurface, (340, 80))
            itens = True
            break
            pygame.display.update()  # Atualização Da Aba Para Aparecer O Que For Adicionado

        if keys[K_RETURN] and rect_x == 14:
            win.fill(w.get_cor(50, 50, 200))
            fight = True
            break

        pygame.display.update()

'''--------------------------------------------MenuDosAtaques---------------------------------------------------------------------------'''

rect_xFight = 148
rect_yFight = 412
Ataque = pygame.Surface((247, 80))
Ataque.set_alpha(50)
Ataque.fill((255, 0, 0))
win.blit(Ataque, (rect_xFight, rect_yFight))
pygame.display.update()
while fight:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo

    if fight:

        if Pokemon == "wartortle":
            wartortle = pygame.image.load("wartortle-back.png")
            wartortle = pygame.transform.scale(wartortle, (300, 250))
            win.blit(wartortle, (150, 200))
            win.blit(kadabra, (475, 25))
            Wartortle.BarraDeVida(Wartortle, 0)
            Adversario.BarraDeVida(Adversario, 0)
            win.blit(barra, (250, 25))
            win.blit(barra2, (350, 300))

            # importar Botao1
            image = pygame.image.load("botao.png")
            win.blit(image, (145, 410))
            textsurface = myfont.render('Water Gun', False, (50, 50, 200))
            win.blit(textsurface, (185, 430))

            # importar Botao2
            image = pygame.image.load("botao.png")
            win.blit(image, (400, 410))
            textsurface = myfont.render('Hydro Pump', False, (50, 50, 200))
            win.blit(textsurface, (430, 430))
            # importar Botao3
            image = pygame.image.load("botao.png")
            win.blit(image, (145, 500))
            textsurface = myfont.render('Bite', False, (0, 0, 0))
            win.blit(textsurface, (240, 520))
            # importar Botao4
            image = pygame.image.load("botao.png")
            win.blit(image, (400, 500))
            textsurface = myfont.render('Ice Beam', False, (70, 70, 150))
            win.blit(textsurface, (460, 520))

            '------------1 Ataque------------'
            if rect_xFight == 148 and rect_yFight == 412 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo

                wartortle = pygame.image.load("wartortle-back.png")
                wartortle = pygame.transform.scale(wartortle, (300, 250))
                win.blit(wartortle, (200, 150))
                win.blit(kadabra, (425, 75))
                Wartortle.BarraDeVida(Wartortle, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.WaterGun(Adversario, 0)
                Wartortle.AtaqueAdversario(Wartortle, 0)
                Adversario.controladorvida(Adversario, 0)
                Wartortle.controladorvida(Wartortle, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Water Gun', False, (50, 50, 200))
                win.blit(textsurface, (185, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Hydro Pump', False, (50, 50, 200))
                win.blit(textsurface, (430, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Bite', False, (0, 0, 0))
                win.blit(textsurface, (240, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Ice Beam', False, (70, 70, 150))
                win.blit(textsurface, (460, 520))

                pygame.display.update()
                time.sleep(0.3)

            '------------2 Ataque------------'
            if rect_xFight == 398 and rect_yFight == 412 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo

                wartortle = pygame.image.load("wartortle-back.png")
                wartortle = pygame.transform.scale(wartortle, (300, 250))
                win.blit(wartortle, (200, 150))
                win.blit(kadabra, (425, 75))
                Wartortle.BarraDeVida(Wartortle, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.HydroPump(Adversario, 0)
                Wartortle.AtaqueAdversario(Wartortle, 0)
                Adversario.controladorvida(Adversario, 0)
                Wartortle.controladorvida(Wartortle, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Water Gun', False, (50, 50, 200))
                win.blit(textsurface, (185, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Hydro Pump', False, (50, 50, 200))
                win.blit(textsurface, (430, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Bite', False, (0, 0, 0))
                win.blit(textsurface, (240, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Ice Beam', False, (70, 70, 150))
                win.blit(textsurface, (460, 520))

                pygame.display.update()
                time.sleep(0.3)

            '------------3 Ataque------------'
            if rect_xFight == 148 and rect_yFight == 500 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo

                wartortle = pygame.image.load("wartortle-back.png")
                wartortle = pygame.transform.scale(wartortle, (300, 250))
                win.blit(wartortle, (200, 150))
                win.blit(kadabra, (425, 75))
                Wartortle.BarraDeVida(Wartortle, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.Bite(Adversario, 0)
                Wartortle.AtaqueAdversario(Wartortle, 0)
                Adversario.controladorvida(Adversario, 0)
                Wartortle.controladorvida(Wartortle, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Water Gun', False, (50, 50, 200))
                win.blit(textsurface, (185, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Hydro Pump', False, (50, 50, 200))
                win.blit(textsurface, (430, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Bite', False, (0, 0, 0))
                win.blit(textsurface, (240, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Ice Beam', False, (70, 70, 150))
                win.blit(textsurface, (460, 520))

                pygame.display.update()
                time.sleep(0.3)

            '------------4 Ataque------------'
            if rect_xFight == 398 and rect_yFight == 500 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                wartortle = pygame.image.load("wartortle-back.png")
                wartortle = pygame.transform.scale(wartortle, (300, 250))
                win.blit(wartortle, (200, 150))
                win.blit(kadabra, (425, 75))
                Wartortle.BarraDeVida(Wartortle, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.IceBeam(Adversario, 0)
                Wartortle.AtaqueAdversario(Wartortle, 0)
                Adversario.controladorvida(Adversario, 0)
                Wartortle.controladorvida(Wartortle, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Water Gun', False, (50, 50, 200))
                win.blit(textsurface, (185, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Hydro Pump', False, (50, 50, 200))
                win.blit(textsurface, (430, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Bite', False, (0, 0, 0))
                win.blit(textsurface, (240, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Ice Beam', False, (70, 70, 150))
                win.blit(textsurface, (460, 520))

                pygame.display.update()
                time.sleep(0.3)

        if Pokemon == "vulpix":
            vulpix = pygame.image.load("vulpix-back.png")
            vulpix = pygame.transform.scale(vulpix, (280, 250))
            win.blit(vulpix, (135, 195))
            win.blit(kadabra, (475, 25))
            Vulpix.BarraDeVida(Vulpix, 0)
            Adversario.BarraDeVida(Adversario, 0)
            win.blit(barra, (250, 25))
            win.blit(barra2, (350, 300))

            # importar Botao1
            image = pygame.image.load("botao.png")
            win.blit(image, (145, 410))
            textsurface = myfont.render('Ember', False, (250, 0, 0))
            win.blit(textsurface, (210, 430))

            # importar Botao2
            image = pygame.image.load("botao.png")
            win.blit(image, (400, 410))
            textsurface = myfont.render('Flamethrower', False, (250, 0, 0))
            win.blit(textsurface, (415, 430))
            # importar Botao3
            image = pygame.image.load("botao.png")
            win.blit(image, (145, 500))
            textsurface = myfont.render('Incinerate', False, (250, 0, 0))
            win.blit(textsurface, (190, 520))
            # importar Botao4
            image = pygame.image.load("botao.png")
            win.blit(image, (400, 500))
            textsurface = myfont.render('Mystical Fire', False, (250, 0, 0))
            win.blit(textsurface, (425, 520))

            '------------1 Ataque------------'
            if rect_xFight == 148 and rect_yFight == 412 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                vulpix = pygame.image.load("vulpix-back.png")
                vulpix = pygame.transform.scale(vulpix, (280, 250))
                win.blit(vulpix, (185, 145))
                win.blit(kadabra, (425, 75))
                Vulpix.BarraDeVida(Vulpix, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.Ember(Adversario, 0)
                Vulpix.AtaqueAdversario(Vulpix, 0)
                Adversario.controladorvida(Adversario, 0)
                Vulpix.controladorvida(Vulpix, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Ember', False, (250, 0, 0))
                win.blit(textsurface, (210, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Flamethrower', False, (250, 0, 0))
                win.blit(textsurface, (415, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Incinerate', False, (250, 0, 0))
                win.blit(textsurface, (190, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Mystical Fire', False, (250, 0, 0))
                win.blit(textsurface, (425, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------2 Ataque------------'
            if rect_xFight == 398 and rect_yFight == 412 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                vulpix = pygame.image.load("vulpix-back.png")
                vulpix = pygame.transform.scale(vulpix, (280, 250))
                win.blit(vulpix, (185, 145))
                win.blit(kadabra, (425, 75))
                Vulpix.BarraDeVida(Vulpix, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.Flamethrower(Adversario, 0)
                Vulpix.AtaqueAdversario(Vulpix, 0)
                Adversario.controladorvida(Adversario, 0)
                Vulpix.controladorvida(Vulpix, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Ember', False, (250, 0, 0))
                win.blit(textsurface, (210, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Flamethrower', False, (250, 0, 0))
                win.blit(textsurface, (415, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Incinerate', False, (250, 0, 0))
                win.blit(textsurface, (190, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Mystical Fire', False, (250, 0, 0))
                win.blit(textsurface, (425, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------3 Ataque------------'
            if rect_xFight == 148 and rect_yFight == 500 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                vulpix = pygame.image.load("vulpix-back.png")
                vulpix = pygame.transform.scale(vulpix, (280, 250))
                win.blit(vulpix, (185, 145))
                win.blit(kadabra, (425, 75))
                Vulpix.BarraDeVida(Vulpix, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.Incinerate(Adversario, 0)
                Vulpix.AtaqueAdversario(Vulpix, 0)
                Adversario.controladorvida(Adversario, 0)
                Vulpix.controladorvida(Vulpix, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Ember', False, (250, 0, 0))
                win.blit(textsurface, (210, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Flamethrower', False, (250, 0, 0))
                win.blit(textsurface, (415, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Incinerate', False, (250, 0, 0))
                win.blit(textsurface, (190, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Mystical Fire', False, (250, 0, 0))
                win.blit(textsurface, (425, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------4 Ataque------------'
            if rect_xFight == 398 and rect_yFight == 500 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                vulpix = pygame.image.load("vulpix-back.png")
                vulpix = pygame.transform.scale(vulpix, (280, 250))
                win.blit(vulpix, (185, 145))
                win.blit(kadabra, (425, 75))
                Vulpix.BarraDeVida(Vulpix, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.MysticalFire(Adversario, 0)
                Vulpix.AtaqueAdversario(Vulpix, 0)
                Adversario.controladorvida(Adversario, 0)
                Vulpix.controladorvida(Vulpix, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Ember', False, (250, 0, 0))
                win.blit(textsurface, (210, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Flamethrower', False, (250, 0, 0))
                win.blit(textsurface, (415, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Incinerate', False, (250, 0, 0))
                win.blit(textsurface, (190, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Mystical Fire', False, (250, 0, 0))
                win.blit(textsurface, (425, 520))

                pygame.display.update()
                time.sleep(0.3)

        if Pokemon == "snorlax":
            snorlax = pygame.image.load("snorlax-back.png")
            snorlax = pygame.transform.scale(snorlax, (255, 225))
            win.blit(snorlax, (143, 225))
            win.blit(kadabra, (475, 25))
            Snorlax.BarraDeVida(Snorlax, 0)
            Adversario.BarraDeVida(Adversario, 0)
            win.blit(barra, (250, 25))
            win.blit(barra2, (350, 300))

            # importar Botao1
            image = pygame.image.load("botao.png")
            win.blit(image, (145, 410))
            textsurface = myfont.render('Sleep', False, (0, 50, 50))
            win.blit(textsurface, (220, 430))

            # importar Botao2
            image = pygame.image.load("botao.png")
            win.blit(image, (400, 410))
            textsurface = myfont.render('Body Slam', False, (250, 50, 50))
            win.blit(textsurface, (440, 430))
            # importar Botao3
            image = pygame.image.load("botao.png")
            win.blit(image, (145, 500))
            textsurface = myfont.render('Giga Impact', False, (0, 0, 0))
            win.blit(textsurface, (170, 520))
            # importar Botao4
            image = pygame.image.load("botao.png")
            win.blit(image, (400, 500))
            textsurface = myfont.render('Crunch', False, (0, 0, 0))
            win.blit(textsurface, (460, 520))

            '------------1 Ataque------------'
            if rect_xFight == 148 and rect_yFight == 412 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                snorlax = pygame.image.load("snorlax-back.png")
                snorlax = pygame.transform.scale(snorlax, (255, 225))
                win.blit(snorlax, (153, 250))
                win.blit(kadabra, (425, 75))
                Snorlax.BarraDeVida(Snorlax, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Snorlax.Sleep(Snorlax, 0)
                Snorlax.AtaqueAdversario(Snorlax, 0)
                Adversario.controladorvida(Adversario, 0)
                Snorlax.controladorvida(Snorlax, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Sleep', False, (0, 50, 50))
                win.blit(textsurface, (220, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Body Slam', False, (250, 50, 50))
                win.blit(textsurface, (440, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Giga Impact', False, (0, 0, 0))
                win.blit(textsurface, (170, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Crunch', False, (0, 0, 0))
                win.blit(textsurface, (460, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------2 Ataque------------'
            if rect_xFight == 398 and rect_yFight == 412 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                snorlax = pygame.image.load("snorlax-back.png")
                snorlax = pygame.transform.scale(snorlax, (255, 225))
                win.blit(snorlax, (153, 200))
                win.blit(kadabra, (425, 75))
                Snorlax.BarraDeVida(Snorlax, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.BodySlam(Adversario, 0)
                Snorlax.AtaqueAdversario(Snorlax, 0)
                Adversario.controladorvida(Adversario, 0)
                Snorlax.controladorvida(Snorlax, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Sleep', False, (0, 50, 50))
                win.blit(textsurface, (220, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Body Slam', False, (250, 50, 50))
                win.blit(textsurface, (440, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Giga Impact', False, (0, 0, 0))
                win.blit(textsurface, (170, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Crunch', False, (0, 0, 0))
                win.blit(textsurface, (460, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------3 Ataque------------'
            if rect_xFight == 148 and rect_yFight == 500 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                snorlax = pygame.image.load("snorlax-back.png")
                snorlax = pygame.transform.scale(snorlax, (255, 225))
                win.blit(snorlax, (153, 200))
                win.blit(kadabra, (425, 75))
                Snorlax.BarraDeVida(Snorlax, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.GigaImpact(Adversario, 0)
                Snorlax.AtaqueAdversario(Snorlax, 0)
                Adversario.controladorvida(Adversario, 0)
                Snorlax.controladorvida(Snorlax, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Sleep', False, (0, 50, 50))
                win.blit(textsurface, (220, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Body Slam', False, (250, 50, 50))
                win.blit(textsurface, (440, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Giga Impact', False, (0, 0, 0))
                win.blit(textsurface, (170, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Crunch', False, (0, 0, 0))
                win.blit(textsurface, (460, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------4 Ataque------------'
            if rect_xFight == 398 and rect_yFight == 500 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                snorlax = pygame.image.load("snorlax-back.png")
                snorlax = pygame.transform.scale(snorlax, (255, 225))
                win.blit(snorlax, (153, 200))
                win.blit(kadabra, (425, 75))
                Snorlax.BarraDeVida(Snorlax, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.Crunch(Adversario, 0)
                Snorlax.AtaqueAdversario(Snorlax, 0)
                Adversario.controladorvida(Adversario, 0)
                Snorlax.controladorvida(Snorlax, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Sleep', False, (0, 50, 50))
                win.blit(textsurface, (220, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Body Slam', False, (250, 50, 50))
                win.blit(textsurface, (440, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Giga Impact', False, (0, 0, 0))
                win.blit(textsurface, (170, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Crunch', False, (0, 0, 0))
                win.blit(textsurface, (460, 520))

                pygame.display.update()
                time.sleep(0.3)

        if Pokemon == "porygon":
            porygon = pygame.image.load("porygon-back.png")
            porygon = pygame.transform.scale(porygon, (255, 240))
            win.blit(porygon, (143, 225))
            win.blit(kadabra, (475, 25))
            Porygon.BarraDeVida(Porygon, 0)
            Adversario.BarraDeVida(Adversario, 0)
            win.blit(barra, (250, 25))
            win.blit(barra2, (350, 300))

            # importar Botao1
            image = pygame.image.load("botao.png")
            win.blit(image, (145, 410))
            textsurface = myfont.render('Psybeam', False, (200, 0, 100))
            win.blit(textsurface, (200, 430))

            # importar Botao2
            image = pygame.image.load("botao.png")
            win.blit(image, (400, 410))
            textsurface = myfont.render('Hyper Beam', False, (50, 0, 250))
            win.blit(textsurface, (435, 430))
            # importar Botao3
            image = pygame.image.load("botao.png")
            win.blit(image, (145, 500))
            textsurface = myfont.render('Dream Eater', False, (100, 50, 50))
            win.blit(textsurface, (175, 520))
            # importar Botao4
            image = pygame.image.load("botao.png")
            win.blit(image, (400, 500))
            textsurface = myfont.render('Shadow Ball', False, (100, 0, 250))
            win.blit(textsurface, (430, 520))

            '------------1 Ataque------------'
            if rect_xFight == 148 and rect_yFight == 412 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                porygon = pygame.image.load("porygon-back.png")
                porygon = pygame.transform.scale(porygon, (255, 240))
                win.blit(porygon, (193, 185))
                win.blit(kadabra, (425, 75))
                Porygon.BarraDeVida(Porygon, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.Psybeam(Adversario, 0)
                Porygon.AtaqueAdversario(Porygon, 0)
                Adversario.controladorvida(Adversario, 0)
                Porygon.controladorvida(Porygon, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Psybeam', False, (200, 0, 100))
                win.blit(textsurface, (200, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Hyper Beam', False, (50, 0, 250))
                win.blit(textsurface, (435, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Dream Eater', False, (100, 50, 50))
                win.blit(textsurface, (175, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Shadow Ball', False, (100, 0, 250))
                win.blit(textsurface, (430, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------2 Ataque------------'
            if rect_xFight == 398 and rect_yFight == 412 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                porygon = pygame.image.load("porygon-back.png")
                porygon = pygame.transform.scale(porygon, (255, 240))
                win.blit(porygon, (193, 185))
                win.blit(kadabra, (425, 75))
                Porygon.BarraDeVida(Porygon, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.HyperBeam(Adversario, 0)
                Porygon.AtaqueAdversario(Porygon, 0)
                Adversario.controladorvida(Adversario, 0)
                Porygon.controladorvida(Porygon, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Psybeam', False, (200, 0, 100))
                win.blit(textsurface, (200, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Hyper Beam', False, (50, 0, 250))
                win.blit(textsurface, (435, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Dream Eater', False, (100, 50, 50))
                win.blit(textsurface, (175, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Shadow Ball', False, (100, 0, 250))
                win.blit(textsurface, (430, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------3 Ataque------------'
            if rect_xFight == 148 and rect_yFight == 500 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                porygon = pygame.image.load("porygon-back.png")
                porygon = pygame.transform.scale(porygon, (255, 240))
                win.blit(porygon, (193, 185))
                win.blit(kadabra, (425, 75))
                Porygon.BarraDeVida(Porygon, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.DreamEater(Adversario, 0)
                Porygon.AtaqueAdversario(Porygon, 0)
                Adversario.controladorvida(Adversario, 0)
                Porygon.controladorvida(Porygon, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Psybeam', False, (200, 0, 100))
                win.blit(textsurface, (200, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Hyper Beam', False, (50, 0, 250))
                win.blit(textsurface, (435, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Dream Eater', False, (100, 50, 50))
                win.blit(textsurface, (175, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Shadow Ball', False, (100, 0, 250))
                win.blit(textsurface, (430, 520))

                pygame.display.update()
                time.sleep(0.3)
            '------------4 Ataque------------'
            if rect_xFight == 398 and rect_yFight == 500 and keys[K_RETURN]:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                porygon = pygame.image.load("porygon-back.png")
                porygon = pygame.transform.scale(porygon, (255, 240))
                win.blit(porygon, (193, 185))
                win.blit(kadabra, (425, 75))
                Porygon.BarraDeVida(Porygon, 0)
                Adversario.BarraDeVida(Adversario, 0)
                Adversario.ShadowBall(Adversario, 0)
                Porygon.AtaqueAdversario(Porygon, 0)
                Adversario.controladorvida(Adversario, 0)
                Porygon.controladorvida(Porygon, 0)
                win.blit(barra, (250, 25))
                win.blit(barra2, (350, 300))

                # importar Botao1
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 410))
                textsurface = myfont.render('Psybeam', False, (200, 0, 100))
                win.blit(textsurface, (200, 430))

                # importar Botao2
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 410))
                textsurface = myfont.render('Hyper Beam', False, (50, 0, 250))
                win.blit(textsurface, (435, 430))
                # importar Botao3
                image = pygame.image.load("botao.png")
                win.blit(image, (145, 500))
                textsurface = myfont.render('Dream Eater', False, (100, 50, 50))
                win.blit(textsurface, (175, 520))
                # importar Botao4
                image = pygame.image.load("botao.png")
                win.blit(image, (400, 500))
                textsurface = myfont.render('Shadow Ball', False, (100, 0, 250))
                win.blit(textsurface, (430, 520))

                pygame.display.update()
                time.sleep(0.3)

        kadabra = pygame.image.load("kadabra.png")
        kadabra = pygame.transform.scale(kadabra, (300, 250))
        win.blit(kadabra, (475, 25))

        if keys[K_RIGHT]:
            rect_xFight += 250
            if rect_xFight > 398:
                rect_xFight -= 500
            #EfeitoSonoro
            #pygame.mixer.music.load("Baloon Alert.mp3")
            #pygame.mixer.music.play()
            #pygame.event.wait()
            time.sleep(0.25)

        if keys[K_LEFT]:
            rect_xFight -= 250
            if rect_xFight < 148:
                rect_xFight += 500
            #EfeitoSonoro
            #pygame.mixer.music.load("Baloon Alert.mp3")
            #pygame.mixer.music.play()
            #pygame.event.wait()
            time.sleep(0.25)

        if keys[K_UP]:
            rect_yFight -= 88
            if rect_yFight < 400:
                rect_yFight += 175
            #EfeitoSonoro
            #pygame.mixer.music.load("Baloon Alert.mp3")
            #pygame.mixer.music.play()
            #pygame.event.wait()
            time.sleep(0.25)

        if keys[K_DOWN]:
            rect_yFight += 88
            if rect_yFight > 550:
                rect_yFight -= 175
            #EfeitoSonoro
            #pygame.mixer.music.load("Baloon Alert.mp3")
            #pygame.mixer.music.play()
            #pygame.event.wait()
            time.sleep(0.25)

        win.blit(Ataque, (rect_xFight, rect_yFight))
        pygame.display.update()
'''------------------------------------------Bag------------------------------------------------------------------------'''

'''rect_y = 50
t2 = pygame.Surface((560, 100))
t2.set_alpha(100)
t2.fill((250, 0, 0))
win.blit(t2, (125, rect_y))
pygame.display.update()

cont = 1'''
while itens:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
    if itens:
        textsurface = myfont.render('Em Manutenção...', False, (250, 100, 250))
        win.blit(textsurface, (340, 80))
        pygame.display.update()
        '''# importar Botao1
        image = pygame.image.load("grade.png")
        win.blit(image, (125, 50))
        textsurface = myfont.render('Potion', False, (250, 100, 250))
        win.blit(textsurface, (340, 80))

        if cont:
            cont += 1
            Wartortle.Potion(Wartortle, 0)
            if cont > 5:
                win.fill(w.get_cor(50, 50, 255))  # Redesenha O Fundo
                textsurface = myfont.render('Acabaram As Suas Poçôes!', False, (250, 100, 250))
                win.blit(textsurface, (125, 50))
                pygame.display.update()
                time.sleep(5)

        if keys[K_UP]:
            rect_y -= 1000
            if rect_y < 0:
                rect_y += 1000
            time.sleep(0.25)

        if keys[K_DOWN]:
            rect_y += 1000
            if rect_y > 0:
                rect_y -= 1000
            time.sleep(0.25)

        win.blit(t2, (125, rect_y))
        pygame.display.update()  # Atualização Da Aba Para Aparecer O Que For Adicionado'''
