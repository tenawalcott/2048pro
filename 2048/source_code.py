# -*- coding: utf-8 -*-
# !/usr/bin/python
"""
Name: 2048 pro
Author: Ding Yipeng
Created on 9 Jun 2019
"""

import pygame
import sys
from pygame.locals import *
import random
import time


class Game:
	def __init__(self, size, num):
		self.size = size
		self.number = [[0 for i in range(size+1)]for j in range(size+1)]
		self.score = 0
		self.num = num
		self.add()
		self.add()

	def add(self):
		while True:
			ran = random.randint(0, self.size**2-1)
			if self.number[ran//self.size][ran % self.size] == 0:
				self.number[ran//self.size][ran % self.size] = self.num
				self.score = self.score+self.num
				break

	def adjust(self):
		flag = False
		for a in self.number:
			temp = []
			k = 0
			for b in a:
				if b != 0:
					if b != k:
						temp.append(b)
						k = b
					else:
						temp.append(temp.pop()*num)
						k = 0
			len_t = len(temp)
			for i in range(self.size-len_t):
				temp.append(0)
			for j in range(self.size):
				if a[j] != temp[j]:
					flag = True
					a[j] = temp[j]
		return flag

	def unclock_route(self):
		self.number = [[self.number[i][j] for i in range(self.size)] for j in reversed(range(self.size))]

	def clock_route(self):
		self.number = [[self.number[i][j] for i in reversed(range(self.size))] for j in range(self.size)]

	def up(self):
		self.unclock_route()
		if self.adjust():
			self.add()
		self.clock_route()

	def down(self):
		self.clock_route()
		if self.adjust():
			self.add()
		self.unclock_route()

	def left(self):
		if self.adjust():
			self.add()

	def right(self):
		self.clock_route()
		self.clock_route()
		if self.adjust():
			self.add()
		self.unclock_route()
		self.unclock_route()

	def over(self):
		for i in range(self.size):
			for j in range(self.size):
				if self.number[i][j] == 0:
					return False
		for i in range(self.size):
			for j in range(self.size-1):
				if self.number[i][j] == self.number[i][j+1]:
					return False
				if self.number[j][i] == self.number[j+1][i]:
					return False
		return True


def start(number, size):
	font1 = pygame.font.Font("simfang.ttf", 70)
	font2 = pygame.font.Font("simfang.ttf", 30)
	length = 385//size
	block = [pygame.Surface((length, length))for i in range(size+1)]
	for i in range(size):
		block[i].fill((0, 0, 0) if i % 2 != 0 else (255, 255, 255))
	score_block = pygame.Surface((384,170))
	score_block.fill((255, 255, 255))
	for i in range(size):
		for j in range(size):
			screen.blit(game.number[i][j] == 0 and block[(i+j)%2] or block[2+(i+j) % 2], (length*j, length*i))
			if game.number[i][j] != 0:
				text = font1.render(str(game.number[i][j]), True, (255, 0, 255))
				rect = text.get_rect()
				rect.center = (length*j+length/2, length*i+length/2)
				screen.blit(text, rect)
	name_block = pygame.Surface((384, 150))
	name_block.fill((255, 255, 255))
	screen.blit(name_block, (0, 384))
	text = font2.render("制作： 丁一芃", True, (0, 0, 0))
	rect = text.get_rect()
	rect.center = (384//2, 384+200)
	screen.blit(text, rect)
	screen.blit(name_block, (0, 384))
	text = font2.render("bgm:Cassete - 2048", True, (0, 0, 0))
	rect = text.get_rect()
	rect.center = (384//2, 384+230)
	screen.blit(text, rect)
	screen.blit(score_block, (0, 384))
	text = font2.render((
		"Game over with score {}".format(game.score) if game.over() else "Score {}".format(game.score)),
		True, (0, 0, 0))
	rect = text.get_rect()
	rect.center = (384//2, 384+150/2)
	screen.blit(text, rect)
	pygame.display.update()	


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Cassete - 2048.mp3")
screen = pygame.display.set_mode((384, 640))
pygame.display.set_caption("2048 Pro")
image_bg = pygame.image.load('bg.jpg')
screen.blit(image_bg, (0, 0))
pygame.display.flip()
while True:
	pygame.mixer.music.play()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN and 99 <= event.pos[0] <= 283 and 529 <= event.pos[1] <= 569:
			image_2 = pygame.image.load("1.jpg")
			screen.blit(image_2, (0, 0))
			pygame.display.flip()
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						if 54 <= event.pos[0] <= 62 and 340 <= event.pos[1] <= 370:
							image_tick = pygame.image.load("tick.png")
							screen.blit(image_tick, (58, 352))
							font = pygame.font.Font("simfang.ttf", 20)
							text = font.render("请输入3至6的整数", True, (0, 0, 0))
							rect = text.get_rect()
							rect.center = (177, 530)
							screen.blit(text, rect)
							pygame.display.update()
							num = 2
						if (50 <= event.pos[0] <= 70) and (380 <= event.pos[1] <= 400):
							image_tick = pygame.image.load("tick.png")
							screen.blit(image_tick, (58, 390))
							num = 3
							font = pygame.font.Font("simfang.ttf", 20)
							text = font.render("Please enter the number between 3 and 6", True, (0, 0, 0))
							rect = text.get_rect()
							rect.center = (177, 530)
							screen.blit(text, rect)
							pygame.display.update()
					keys = pygame.key.get_pressed()
					if keys[K_3]:
						font = pygame.font.Font("simfang.ttf", 20)
						text = font.render("3", True, (0, 0, 0))
						rect = text.get_rect()
						rect.center = (207, 486)
						screen.blit(text, rect)
						pygame.display.update()
						size = 3
						game = Game(size, num)
						time.sleep(2)
						while True:
							start(num,size)
							clock = pygame.time.Clock()
							clock.tick(10)
							for event in pygame.event.get():
								if event.type == QUIT:
									sys.exit()
								keys = pygame.key.get_pressed()
								if keys[K_UP]:
									game.up()
								if keys[K_DOWN]:
									game.down()
								if keys[K_LEFT]:
									game.left()
								if keys[K_RIGHT]:
									game.right()
							if game.over():
								start(num, size)
								break
					if keys[K_4]:
						font = pygame.font.Font("simfang.ttf", 20)
						text = font.render("4", True, (0, 0, 0))
						rect = text.get_rect()
						rect.center = (207, 486)
						screen.blit(text, rect)
						pygame.display.update()
						size = 4
						game = Game(size, num)
						while True:
							start(num, size)
							clock = pygame.time.Clock()
							clock.tick(10)
							for event in pygame.event.get():
								if event.type == QUIT:
									sys.exit()
								keys = pygame.key.get_pressed()
								if keys[K_UP]:
									game.up()
								if keys[K_DOWN]:
									game.down()
								if keys[K_LEFT]:
									game.left()
								if keys[K_RIGHT]:
									game.right()
							if game.over():
								start(num, size)
								break
					if keys[K_5]:
						font = pygame.font.Font("simfang.ttf", 20)
						text = font.render("5", True, (0, 0, 0))
						rect = text.get_rect()
						rect.center = (207, 486)
						screen.blit(text, rect)
						pygame.display.update()
						size = 5
						game = Game(size, num)
						while True:
							start(num, size)
							clock = pygame.time.Clock()
							clock.tick(10)
							for event in pygame.event.get():
								if event.type == QUIT:
									sys.exit()
								keys = pygame.key.get_pressed()
								if keys[K_UP]:
									game.up()
								if keys[K_DOWN]:
									game.down()
								if keys[K_LEFT]:
									game.left()
								if keys[K_RIGHT]:
									game.right()
							if game.over():
								start(num, size)
								break
					if keys[K_6]:
						font = pygame.font.Font("simfang.ttf",20)
						text = font.render("6", True, (0, 0, 0))
						rect = text.get_rect()
						rect.center = (207, 486)
						screen.blit(text, rect)
						pygame.display.update()
						size = 6
						game = Game(size, num)
						while True:
							start(num, size)
							clock = pygame.time.Clock()
							clock.tick(10)
							for event in pygame.event.get():
								if event.type == QUIT:
									sys.exit()
								keys = pygame.key.get_pressed()
								if keys[K_UP]:
									game.up()
								if keys[K_DOWN]:
									game.down()
								if keys[K_LEFT]:
									game.left()
								if keys[K_RIGHT]:
									game.right()
							if game.over():
								start(num, size)
								break
					if event.type == QUIT:
						sys.exit()
			pygame.time.delay(3000)
