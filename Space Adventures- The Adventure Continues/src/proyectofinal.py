# To change this template, choose Tools | Templates
# and open the template in the editor.

from pygame import *
import random
import pygame

class Joystick(object):
	def __init__(self):
		self.left = False
		self.right = False
		self.up = False
		self.down = False

joystick = Joystick()
joystick2 = Joystick()

class Personaje(pygame.sprite.Sprite):
        def __init__(self, x, y,imagen,imagen2):
		pygame.sprite.Sprite.__init__(self)
		self.image = image.load(imagen)
                self.bitmap = image.load(imagen)
                self.bitmap2 = image.load(imagen2)
		self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())
		self.velx = 5
		self.vely = 5
                self.valid = True


        def render(self):
		screen.blit(self.bitmap, (self.x, self.y))
                
        def render2(self):
		screen.blit(self.bitmap2, (self.x, self.y))

        def resetear(self,x,y):
                self.x=x
                self.y=y

        def canGoUp(self):
		return self.rect.y - self.vely >= 0

        def goUp(self):
		self.rect.y -= self.vely

        def canGoDown(self):
		return self.rect.bottom + self.vely < 600

        def goDown(self):
		self.rect.y += self.vely

        def canGoLeft(self):
		return self.rect.x - self.velx >= 0

        def goLeft(self):
		self.rect.x -= self.velx

        def canGoRight(self):
		return self.rect.right + self.velx < 800

        def goRight(self):
		self.rect.x += self.velx
class Jugadores:
        def __init__(self, x, y, imagen,imagen2):
		self.x = x
		self.y = y
		self.image = image.load(imagen)
                
                
                self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())
                self.valid = True
        def set_position(self, x, y):
		self.x = x
		self.y = y
        

def Colision( obj1, obj2 ):
    if obj1.valid and obj2.valid:
        return obj1.rect.colliderect( obj2.rect )
    else:
        return False

class Sprite:
	def __init__(self, x, y, imagen,sentido):
		self.x = x
		self.y = y
		self.bitmap = image.load(imagen)
		self.bitmap.set_colorkey((0,0,0))
                self.sentido = sentido
	def set_position(self, x, y):
		self.x = x
		self.y = y
        def set_sentido(self,sentido):
		self.sentido = sentido
	def render(self):
		screen.blit(self.bitmap, (self.x, self.y))

def game():

#aca van el llamado de las rocas
 a = random.randint(0, 3)
#aca va cuando inicializa las rocas
 piedra1 = Sprite(200, 500, 'imagenes/roca21.png',a)
 a = random.randint(0, 3)
 piedra2 = Sprite(10, 100, 'imagenes/roca21.png',a)
 a = random.randint(0, 3)
 piedra3 = Sprite(550, 590, 'imagenes/roca31.png',a)
 myFont = pygame.font.SysFont("Comic Sans MS", 20)
 texto1 = myFont.render("Vidas P1:", 1, (0, 0, 255))
 texto3 = myFont.render("Vidas P2:", 1, (0, 0, 255))
 rocas = pygame.mixer.Sound("sonidos/rocas.WAV")
 salir=0
 vidas1 = 6
 vidas2 = 6

 while salir == 0:
    screen.fill(0);
    texto2 = myFont.render(str(vidas1), 1, (0, 0, 255))
    texto4 = myFont.render(str(vidas2), 1, (0, 0, 255))

    screen.blit(player.image, player.rect)
    screen.blit(player2.image, player2.rect)
    readInput();
    updateState();
    screen.blit(texto1, (10, 10))
    screen.blit(texto2, (100, 10))
    screen.blit(texto3, (250, 10))
    screen.blit(texto4, (340, 10))

    if piedra1.sentido==0:
            piedra1.y-=5
            piedra1.render()
    if piedra1.sentido==1:
            piedra1.y+=5
            piedra1.render()
    if piedra1.y<10:
            piedra1.sentido=1
            piedra1.y+=5
    if piedra1.y>590:
            piedra1.sentido=0
            piedra1.y-=5

    if piedra1.sentido==2:
            piedra1.x-=5
            piedra1.render()
    if piedra1.sentido==3:
            piedra1.x+=5
            piedra1.render()
    if piedra1.x<10:
            piedra1.sentido=3
            piedra1.x+=5
    if piedra1.x>780:
            piedra1.sentido=2
            piedra1.x-=5

    if piedra2.sentido==0:
            piedra2.y-=5
            piedra2.render()
    if piedra2.sentido==1:
            piedra2.y+=5
            piedra2.render()
    if piedra2.y<10:
            piedra2.sentido=1
            piedra2.y+=5
    if piedra2.y>590:
            piedra2.sentido=0
            piedra2.y-=5

    if piedra2.sentido==2:
            piedra2.x-=5
            piedra2.render()
    if piedra2.sentido==3:
            piedra2.x+=5
            piedra2.render()
    if piedra2.x<10:
            piedra2.sentido=3
            piedra2.x+=5
    if piedra2.x>780:
            piedra2.sentido=2
            piedra2.x-=5

    if piedra3.sentido==0:
            piedra3.y-=5
            piedra3.render()
    if piedra3.sentido==1:
            piedra3.y+=5
            piedra3.render()
    if piedra3.y<10:
            piedra3.sentido=1
            piedra3.y+=5
    if piedra3.y>590:
            piedra3.sentido=0
            piedra3.y-=5

    if piedra3.sentido==2:
            piedra3.x-=5
            piedra3.render()
    if piedra3.sentido==3:
            piedra3.x+=5
            piedra3.render()
    if piedra3.x<10:
            piedra3.sentido=3
            piedra3.x+=5
    if piedra3.x>780:
            piedra3.sentido=2
            piedra3.x-=5

    if Colision(player,player2):
        vidas1+=1
        vidas2+=1
        player. __init__(150,260,'imagenes/astro1.png','imagenes/astro2.png')
        player2. __init__(648,200,'imagenes/marciano1.png','imagenes/extra3.png')
        # ACA VA EL CODIGO DE LAS PIEDRAS PARA QUE COMIENCE DE NUEVO
        a = random.randint(0, 3)
        #aca va cuando inicializa las rocas
        piedra1 = Sprite(200, 500, 'imagenes/roca21.png',a)
        a = random.randint(0, 3)
        piedra2 = Sprite(10, 100, 'imagenes/roca21.png',a)
        a = random.randint(0, 3)
        piedra3 = Sprite(550, 590, 'imagenes/roca31.png',a)

        
    rocax=Personaje(piedra1.x,piedra1.y,'imagenes/roca21.png','imagenes/roca21.png')
    rocax2=Personaje(piedra2.x,piedra2.y,'imagenes/roca21.png','imagenes/roca21.png')



    if Colision(rocax2,rocax):
            if piedra1.sentido==0:
                piedra1.sentido=random.choice((1,2,3))
                piedra1.y+=5
                rocas.play()
            else:
                piedra1.sentido=random.choice((0,2,3))
                piedra1.y-=5
                rocas.play()
            if piedra2.sentido==0:
                piedra2.sentido=random.choice((1,2,3))
                piedra2.x+=5
                rocas.play()
            else:
                piedra2.sentido=random.choice((0,2,3))
                piedra2.x-=5
                rocas.play()

    rocax=Personaje(piedra3.x,piedra3.y,'imagenes/roca31.png','imagenes/roca21.png')
    rocax2=Personaje(piedra2.x,piedra2.y,'imagenes/roca21.png','imagenes/roca21.png')

    if Colision(rocax2,rocax):
            if piedra3.sentido==0:
                piedra3.sentido=random.choice((1,2,3))
                piedra3.y+=5
                rocas.play()
            else:
                piedra3.sentido=random.choice((0,2,3))
                piedra3.y-=5
                rocas.play()
            if piedra2.sentido==0:
                piedra2.sentido=random.choice((1,2,3))
                piedra2.x+=5
                rocas.play()
            else:
                piedra2.sentido=random.choice((0,2,3))
                piedra2.x-=5
                rocas.play()

    rocax=Personaje(piedra1.x,piedra1.y,'imagenes/roca21.png','imagenes/roca21.png')
    rocax2=Personaje(piedra3.x,piedra3.y,'imagenes/roca31.png','imagenes/roca21.png')

    if Colision(rocax2,rocax):
            if piedra1.sentido==0:
                piedra1.sentido=random.choice((1,2,3))
                piedra1.y+=5
                rocas.play()
            else:
                piedra1.sentido=random.choice((0,2,3))
                piedra1.y-=5
                rocas.play()
            if piedra3.sentido==0:
                piedra3.sentido=random.choice((1,2,3))
                piedra3.x+=5
                rocas.play()
            else:
                piedra3.sentido=random.choice((0,2,3))
                piedra3.x-=5
                rocas.play()

    if vidas1==0:
        salir=1

    if vidas2==0:
        salir=1


    rocax=Personaje(piedra1.x,piedra1.y,'imagenes/roca21.png','imagenes/roca21.png')
    rocax2=Personaje(piedra2.x,piedra2.y,'imagenes/roca21.png','imagenes/roca21.png')
    rocax3=Personaje(piedra3.x,piedra3.y,'imagenes/roca31.png','imagenes/roca21.png')

    if Colision(rocax,player):
        if vidas1>=1:
            player. __init__(150,260,'imagenes/astro1.png','imagenes/astro2.png')
            vidas1-=1
    if Colision(rocax2,player):
        if vidas1>=1:
            player. __init__(150,260,'imagenes/astro1.png','imagenes/astro2.png')
            vidas1-=1

    if Colision(rocax3,player):
        if vidas1>=1:
            player. __init__(150,260,'imagenes/astro1.png','imagenes/astro2.png')
            vidas1-=1

    if Colision(rocax,player2):
        if vidas2>=1:
            player2. __init__(648,200,'imagenes/marciano1.png','imagenes/extra3.png')
            vidas2-=1
    if Colision(rocax2,player2):
        if vidas2>=1:
            player2. __init__(648,200,'imagenes/marciano1.png','imagenes/extra3.png')
            vidas2-=1

    if Colision(rocax3,player2):
        if vidas2>=1:
            player2. __init__(648,200,'imagenes/marciano1.png','imagenes/extra3.png')
            vidas2-=1

    display.update()
    clock.tick(tempo)



def readInput():
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()

		if event.type == KEYDOWN:
			if event.key == K_UP:
				joystick.up = True
			elif event.key == K_DOWN:
				joystick.down = True
			elif event.key == K_LEFT:
				joystick.left = True
			elif event.key == K_RIGHT:
				joystick.right = True
                        elif event.key == pygame.K_e:
                                #salir = 1
                                print "aaahhh"
                                game();
                        elif event.key == pygame.K_ESCAPE:
                            exit();


		if event.type == KEYUP:
			if event.key == K_UP:
				joystick.up = False
			elif event.key == K_DOWN:
				joystick.down = False
			elif event.key == K_LEFT:
				joystick.left = False
			elif event.key == K_RIGHT:
				joystick.right = False


                if event.type == KEYDOWN:
			if event.key == K_w:
				joystick2.up = True
			elif event.key == K_s:
				joystick2.down = True
			elif event.key == K_a:
				joystick2.left = True
			elif event.key == K_d:
				joystick2.right = True
                        elif event.key == pygame.K_e:
                                #salir = 1
                                print "aaahhh"
                                game();
                        elif event.key == pygame.K_ESCAPE:
                            exit();

		if event.type == KEYUP:
			if event.key == K_w:
				joystick2.up = False
			elif event.key == K_s:
				joystick2.down = False
			elif event.key == K_a:
				joystick2.left = False
			elif event.key == K_d:
				joystick2.right = False

def updateState():


	if joystick.up:
		if player.canGoUp():
			player.goUp()

	elif joystick.down:
		if player.canGoDown():
			player.goDown()


	if joystick.left:
		if player.canGoLeft():
			player.goLeft()

	elif joystick.right:
		if player.canGoRight():
			player.goRight()


        if joystick2.up:
		if player2.canGoUp():
			player2.goUp()

	elif joystick2.down:
		if player2.canGoDown():
			player2.goDown()


	if joystick2.left:
		if player2.canGoLeft():
			player2.goLeft()

	elif joystick2.right:
		if player2.canGoRight():
			player2.goRight()

init()

screen = display.set_mode((800,600))
display.set_caption('SPACE BATTLE')

#fondo = pygame.mixer.Sound("sonidos/killers_human(2)-Part 1.wav")


salir = 0
tempo = 70 #Esta es la variable del tiempo para ir incrementando cuando se pase de nivel
clock = pygame.time.Clock()
#fondo.play(999,)



myFont = pygame.font.SysFont("Comic Sans MS", 20)
player = Personaje(150,260,'imagenes/astro1.png','imagenes/astro2.png')
player2 = Personaje(648,200,'imagenes/marciano1.png','imagenes/extra3.png')

while salir == 0:
    screen.fill(0);
    texto22 = myFont.render("SPACE BATTLE ", 1, (250, 50, 50))
    texto24 = myFont.render("Presione E para Comenzar " , 1, (0, 0, 255))
    texto20 = myFont.render("Presione Esc para Salir " , 1, (0, 0, 255))
    texto6 = myFont.render("Movimiento Marciano" , 1, (255, 255, 255))
    texto7 = myFont.render("Arriba: W" , 1, (0, 0, 255))
    texto8 = myFont.render("Abajo: S" , 1, (0, 0, 255))
    texto9 = myFont.render("Izquierda: A" , 1, (0, 0, 255))
    texto10 = myFont.render("Derecha: D" , 1, (0, 0, 255))

    texto11 = myFont.render("Movimiento Astronauta" , 1, (255, 255, 255))
    texto12 = myFont.render("Arriba: ^ " , 1, (0, 0, 255))
    texto13 = myFont.render("Abajo: v" , 1, (0, 0, 255))
    texto14 = myFont.render("Izquierda: <- " , 1, (0, 0, 255))
    texto15 = myFont.render("Derecha: ->" , 1, (0, 0, 255))

    readInput();
    updateState();

    screen.blit(texto22, (300,100))
    screen.blit(texto24, (245, 150))
    screen.blit(texto20, (245, 350))
    #screen.blit(texto6, (500, 500))

    screen.blit(texto6, (150,200))
    screen.blit(texto7, (150, 220))
    screen.blit(texto8, (150, 240))
    screen.blit(texto9, (150, 260))
    screen.blit(texto10, (150, 280))

    screen.blit(texto11, (450,200))
    screen.blit(texto12, (450, 220))
    screen.blit(texto13, (450, 240))
    screen.blit(texto14, (450, 260))
    screen.blit(texto15, (450, 280))

    display.update()
    clock.tick(tempo)

