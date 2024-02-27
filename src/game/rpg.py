from renpy.compat import *
import pygame_sdl2 as pygame


def show():
    RED = (255,0,0)  # 红色，使用RGB颜色
    radius = 20 # 半径
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.draw.circle(window,RED,(200,300),radius)
    pygame.display.update()  # 刷新屏幕
    while True:
        pass

def main():
	pass

if __name__ == "__main__":
	main()
