import math
import pygame as pg
from pygame.math import Vector3 as v3
from pygame.math import Vector2 as v2
from typing import List

# >> Functions
def calculate_x(pos : v3 ,rot : v3) -> float:
    return (
        pos.y * math.sin(rot.x) * math.sin(rot.y) * math.cos(rot.z) - 
        pos.z * math.cos(rot.x) * math.sin(rot.y) * math.cos(rot.z) + 
        pos.y * math.cos(rot.x) * math.sin(rot.z) + 
        pos.z * math.sin(rot.x) * math.sin(rot.z) + 
        pos.x * math.cos(rot.y) * math.cos(rot.z)
    )
def calculate_y(pos : v3 ,rot : v3) -> float:
    return (
        pos.y * math.cos(rot.x) * math.cos(rot.z) + 
        pos.z * math.sin(rot.x) * math.cos(rot.z) - 
        pos.y * math.sin(rot.x) * math.sin(rot.y) * math.sin(rot.z) + 
        pos.z * math.cos(rot.x) * math.sin(rot.y) * math.sin(rot.z) - 
        pos.x * math.cos(rot.y) * math.sin(rot.z)
    )
def calculate_z(pos : v3 ,rot : v3) -> float:
    return (
        pos.z * math.cos(rot.x) * math.cos(rot.y) - 
        pos.y * math.sin(rot.x) * math.cos(rot.y) + 
        pos.x * math.sin(rot.y)
    )

def calculate_point(pos : v3 ,rot : v3) -> v3:
    return v3(
        calculate_x(pos ,rot)
        ,calculate_y(pos ,rot)
        ,calculate_z(pos ,rot) + DISTANCE_FROM_CAM
    )
def convert_to_screen(pos : v3) -> v2:
        ooz: float = 1 / pos.z

        xp = int(SCREEN_WIDTH / 2 + PIXEL_PER_UNIT * ooz * pos.x)
        yp = int(SCREEN_HEIGHT / 2 + PIXEL_PER_UNIT * ooz * pos.y)

        return v2(xp ,yp)

# >> Classes

class Cube:
    def __init__(self ,size : float ,position : v3 = v3() ,rotation : v3 = v3()) -> None:
        self.size: float = size
        self.position: v3 = position
        self.rotation: v3 = rotation

    def draw(self) -> None:
        a: float = -.5 * self.size
        b: float = .5 * self.size

        point1 : v2 = convert_to_screen(calculate_point(v3(a,b,a) ,self.rotation) + self.position)
        point2 : v2 = convert_to_screen(calculate_point(v3(a,b,b) ,self.rotation) + self.position)
        point3 : v2 = convert_to_screen(calculate_point(v3(b,b,b) ,self.rotation) + self.position)
        point4 : v2 = convert_to_screen(calculate_point(v3(b,b,a) ,self.rotation) + self.position)
        point5 : v2 = convert_to_screen(calculate_point(v3(a,a,a) ,self.rotation) + self.position)
        point6 : v2 = convert_to_screen(calculate_point(v3(a,a,b) ,self.rotation) + self.position)
        point7 : v2 = convert_to_screen(calculate_point(v3(b,a,b) ,self.rotation) + self.position)
        point8 : v2 = convert_to_screen(calculate_point(v3(b,a,a) ,self.rotation) + self.position)

        pg.draw.line(screen ,(255 ,255 ,255) ,point1 ,point2)
        pg.draw.line(screen ,(255 ,255 ,255) ,point1 ,point4)
        pg.draw.line(screen ,(255 ,255 ,255) ,point1 ,point5)
        pg.draw.line(screen ,(255 ,255 ,255) ,point2 ,point3)
        pg.draw.line(screen ,(255 ,255 ,255) ,point2 ,point6)
        pg.draw.line(screen ,(255 ,255 ,255) ,point3 ,point4)
        pg.draw.line(screen ,(255 ,255 ,255) ,point8 ,point4)
        pg.draw.line(screen ,(255 ,255 ,255) ,point3 ,point7)
        pg.draw.line(screen ,(255 ,255 ,255) ,point8 ,point7)
        pg.draw.line(screen ,(255 ,255 ,255) ,point6 ,point7)
        pg.draw.line(screen ,(255 ,255 ,255) ,point5 ,point8)
        pg.draw.line(screen ,(255 ,255 ,255) ,point5 ,point6)
class Pyramid:
    def __init__(self ,height : float = 10 ,base_size : float = 10 ,position : v3 = v3() ,rotation : v3 = v3()) -> None:
        self.height: float = height
        self.base_size: float = base_size
        self.position: v3 = position
        self.rotation: v3 = rotation

    def draw(self) -> None:
            a: float = -.5 * self.base_size
            b: float = .5 * self.base_size
            h: float = .5 * self.height

            point1 : v2 = convert_to_screen(calculate_point(v3(a,h,b) ,self.rotation) + self.position)
            point2 : v2 = convert_to_screen(calculate_point(v3(b,h,b) ,self.rotation) + self.position)
            point3 : v2 = convert_to_screen(calculate_point(v3(a,h,a) ,self.rotation) + self.position)
            point4 : v2 = convert_to_screen(calculate_point(v3(b,h,a) ,self.rotation) + self.position)
            point5 : v2 = convert_to_screen(calculate_point(v3(0,-h,0) ,self.rotation) + self.position)

            pg.draw.line(screen ,(255 ,255 ,255) ,point1 ,point2)
            pg.draw.line(screen ,(255 ,255 ,255) ,point1 ,point3)
            pg.draw.line(screen ,(255 ,255 ,255) ,point1 ,point5)
            pg.draw.line(screen ,(255 ,255 ,255) ,point2 ,point4)
            pg.draw.line(screen ,(255 ,255 ,255) ,point2 ,point5)
            pg.draw.line(screen ,(255 ,255 ,255) ,point3 ,point4)
            pg.draw.line(screen ,(255 ,255 ,255) ,point3 ,point5)
            pg.draw.line(screen ,(255 ,255 ,255) ,point4 ,point5)

class Scene:
    def __init__(self) -> None:
        self.gameObjects : List[object] = []

    def create(self ,gameObject : object):
        self.gameObjects.append(gameObject)

    def draw(self) -> None:
        for gameObject in self.gameObjects:
            gameObject.draw() # type: ignore
         

# >> Variables
# > Constants
DISTANCE_FROM_CAM = 60
FPS = 120
PIXEL_PER_UNIT = 500
CUBE_OFFSET = 75

# > Dynamic
screen: pg.Surface  = pg.display.set_mode((1920 ,1080))
SCREEN_WIDTH ,SCREEN_HEIGHT= screen.get_size()

# Scene
game = Scene()

big_cube = Cube(30 ,v3(0 ,0 ,0) ,v3())

pyramid = Pyramid(45 ,30 ,v3(0 ,-CUBE_OFFSET//2 ,0) ,v3())
pyramid_n = Pyramid(-45 ,30 ,v3(0 ,CUBE_OFFSET//2 ,0) ,v3())

game.create(big_cube)
game.create(pyramid)
game.create(pyramid_n)

running : bool = True
clock = pg.time.Clock()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0,0,0))

    game.draw()

    pg.display.flip()

    big_cube.rotation += v3(0 ,0.01 ,0)
    pyramid.rotation += v3(0 ,.01 ,0)
    pyramid_n.rotation += v3(0 ,.01 ,0)
    clock.tick(FPS)

pg.quit()
exit()