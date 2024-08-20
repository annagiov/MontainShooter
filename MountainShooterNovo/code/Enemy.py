#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_speed = ENTITY_SPEED.get(name, 5)
        self.initial_vertical_speed = self.vertical_speed
        self.moving_down = False

    def move(self):
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 5)

        if self.moving_down:
            self.rect.centery += self.vertical_speed * 2
            if self.rect.bottom >= WIN_HEIGHT:
                self.moving_down = False
        else:
            self.rect.centery -= self.vertical_speed
            if self.rect.top <= 0:
                self.moving_down = True
