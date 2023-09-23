from pygame import *
init()
from random import *
screen = display.set_mode((1200, 750))
display.set_caption('Ping Pong')
encendido = True
finish = False
screen.fill((0, 255, 0)) 

class Objeto(sprite.Sprite):
	def __init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion):
		sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.ancho = ancho
		self.largo = largo
		self.direccionx = direccionx
		self.direcciony = direcciony
		self.puntuacion = puntuacion

	def DibujarObjeto(self):
		draw.rect(screen, (255,255,255), (self.x,self.y,self.ancho,self.largo))

class Personaje(Objeto):
	def __init__(self, x, y, ancho, largo, direccionx , direcciony, puntuacion):
		Objeto.__init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion)
		
	def Movimiento(self):
		x = self.x
		y = self.y
		keys = key.get_pressed()
		if keys[K_DOWN]==1:
			y1 = y
			y = y + 20
			self.y = y
			if y > 625:
				self.y = y1
		if keys[K_UP]==1:
			y1 = y
			y = y -20
			self.y = y
			if y < 5:
				self.y = y1
		self.DibujarObjeto()
	
	def check_colisiones(sprite1, sprite2):
		xsprite1 = sprite1.x
		ysprite1 = sprite1.y
		anchosprite1 = sprite1.ancho
		largosprite1 = sprite1.largo
		xsprite2 = sprite2.x
		ysprite2 = sprite2.y
		anchosprite2 = sprite2.ancho
		largosprite2 = sprite2.largo
		if (ysprite1 + largosprite1) > ysprite2 and ysprite1 < (ysprite2 + largosprite2) and (xsprite1 + anchosprite1) > xsprite2 and xsprite1 < (xsprite2 + anchosprite2):
			return True

class Enemigo(Objeto):
	def __init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion):
		Objeto.__init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion)

	def Movimiento(self):
		if self.y <= 0:
			self.direcciony = 1
		elif self.y + self.largo >= 750:
			self.direcciony = - 1
		self.y = self.y + (10 * self.direcciony)
		self.DibujarObjeto()
		
class Bola(Objeto):
	def __init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion):
		Objeto.__init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion)
	
	def Movimiento(self):
		if self.direccionx == 1:
			self.x = self.x + 10
			if self.direcciony == -1:
				self.y = self.y - 5
			else:
				self.y = self.y + 5
		elif self.direccionx == -1:
			self.x = self.x - 10
			if self.direcciony == -1:
				self.y = self.y - 5
			else:
				self.y = self.y + 5
		self.DibujarObjeto()

	def Golpear_personaje(self, personaje):
		if Personaje.check_colisiones(self, personaje) == True:
			self.direccionx = 1

	def Golpear_enemigo(self, personaje):
		if Personaje.check_colisiones(self, personaje) == True:
			self.direccionx = -1
	
	def Puntuar(self, protagonista, enemigo):
		if self.y == 0 or self.y == 700:
			self.direcciony = - self.direcciony
		elif self.x == 1200:
			protagonista.puntuacion = protagonista.puntuacion + 1
			self.x = 550
			self.y = 350
			self.direccionx = - self.direccionx
		elif self.x == 0:
			enemigo.puntuacion = enemigo.puntuacion + 1
			self.x = 550
			self.y = 350
			self.direccionx = - self.direccionx

class Bloque(Objeto):
	def __init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion):
		Objeto.__init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion)

	def Rebotar(self, bola):
		if Personaje.check_colisiones(self, bola) == True:
			bola.direccionx = -1
			self.x = self.x + 5000

	def Reaparecer(self):
		if self.x > 5000:
			self.x = self.x - 5000

font = font.Font('freesansbold.ttf', 20)
textPuntuacion = font.render('Marcador: '+ str('0 - 0'), True, (0, 255, 0),  (0, 0, 0))
textRectPuntuacion = textPuntuacion.get_rect()
textRectPuntuacion.x = 550
textRectPuntuacion.y = 10

protagonista = Personaje(10, 300, 20, 120, 1, 1, 0)
enemigo1 = Enemigo(1170,400,20,120, 1, 1, 0)
enemigo2 = Enemigo(1170,200,20,120, -1, -1, 0)
bola = Bola(550,350,40,40, 1, 1, 0)
bloque1 = Bloque(1050,0,50,50, 1, 1, 0)
bloque2 = Bloque(1050,50,50,50, 1, 1, 0)
bloque3 = Bloque(1050,700,50,50, 1, 1, 0)
bloque4 = Bloque(1050,650,50,50, 1, 1, 0)
bloque5 = Bloque(1050,275,50,50, 1, 1, 0)
bloque6 = Bloque(1050,325,50,50, 1, 1, 0)
bloque7 = Bloque(1050,375,50,50, 1, 1, 0)
bloque8 = Bloque(1050,425,50,50, 1, 1, 0)

while encendido:
	if finish == False:
		screen.fill((0, 255, 0))
		protagonista.Movimiento()
		enemigo1.Movimiento()
		bola.Movimiento()
		bola.Golpear_personaje(protagonista)
		bola.Golpear_enemigo(enemigo1)
		bola.Puntuar(protagonista, enemigo1)
		enemigo2.Movimiento()
		bola.Golpear_enemigo(enemigo2)
		if protagonista.puntuacion >= 2:
			bloque1.DibujarObjeto()
			bloque1.Rebotar(bola)
			bloque1.Reaparecer()
			bloque2.DibujarObjeto()
			bloque2.Rebotar(bola)
			bloque2.Reaparecer()
			if protagonista.puntuacion >= 5:
				bloque3.DibujarObjeto()
				bloque3.Rebotar(bola)
				bloque3.Reaparecer()
				bloque4.DibujarObjeto()
				bloque4.Rebotar(bola)
				bloque4.Reaparecer()
				if protagonista.puntuacion >= 8:
					bloque5.DibujarObjeto()
					bloque5.Rebotar(bola)
					bloque5.Reaparecer()
					bloque6.DibujarObjeto()
					bloque6.Rebotar(bola)
					bloque6.Reaparecer()
					bloque7.DibujarObjeto()
					bloque7.Rebotar(bola)
					bloque7.Reaparecer()
					bloque8.DibujarObjeto()
					bloque8.Rebotar(bola)
					bloque8.Reaparecer()
		textPuntuacion = font.render('Marcador: '+ str(protagonista.puntuacion) + ' - ' + str(enemigo1.puntuacion), True, (0, 255, 0),  (0, 0, 0))
		screen.blit(textPuntuacion, textRectPuntuacion)
		time.delay(15)
		if protagonista.puntuacion == 10:
			finish = True
		elif enemigo1.puntuacion == 10:
			finish = True
	elif finish == True:
		if protagonista.puntuacion >= 10:
			victoria = image.load("win.png")
			screen.blit(victoria, (375, 100))
		elif enemigo1.puntuacion >= 10:
			victoria = image.load("lose.png")
			screen.blit(victoria, (300, 50))
	for evento in event.get():
		if evento.type==QUIT:
			encendido=False
	display.flip()