import pygame
import requests
import os


name = 'map.png'
URL = 'http://static-maps.yandex.ru/1.x/'
ll = [37.530887, 55.7033118]
l = 'sat'
spn = [0.002, 0.002]
lastll = [34, 34]

def get_image():
    image = requests.get(URL, params=get_params())
    if image:
        return image
    print(image.content)

def checkState():
    return lastll != ll

def load_image(image):
    with open('map.png', 'wb') as f:
        f.write(image.content)

def show_image(screen):
    screen.blit(pygame.transform.scale(pygame.image.load('map.png'), (width, height)), (0, 0))

def get_params():
    return {'ll': f"{ll[0]},{ll[1]}", "spn": f"{spn[0]},{spn[1]}", 'l': type_map}

pygame.init()
size = width, height = 600, 465
screen = pygame.display.set_mode(size)
running = 1
FPS = 10
type_maps = ['sat', 'map', 'map,skl,trf']
type_map = 'sat'
clock = pygame.time.Clock()
print(ll[0] + spn[0] * width / 2, abs(ll[0] - spn[0] * height / 2))
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = 0
        elif ev.type == pygame.KEYDOWN:  
            if ev.key == pygame.K_PAGEUP:
                spn[0] -= spn[0] / 2
                spn[1] -= spn[1] / 2
            elif ev.key == pygame.K_PAGEDOWN:
                spn[0] += spn[0] / 2
                spn[1] += spn[1] / 2
            elif ev.key == pygame.K_UP:
                ll[1] += spn[1] / 10
            elif ev.key == pygame.K_DOWN:
                ll[1] -= spn[1] / 10
            elif ev.key == pygame.K_RIGHT:
                ll[0] += spn[1] / 10
            elif ev.key == pygame.K_LEFT:
                ll[0] -= spn[1] / 10
            elif ev.key == pygame.K_1:
                type_map = type_maps[0]
            elif ev.key == pygame.K_2:
                type_map = type_maps[1]
            elif ev.key == pygame.K_3:
                type_map = type_maps[2]
    
    if checkState():
        image = get_image()
        if image:
            screen.fill((0, 0, 0))
            load_image(image)
            show_image(screen)
            lastll = ll[:]
    print(ll)
    pygame.display.flip()
    clock.tick(FPS)

os.remove(name)
