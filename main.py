#coding:utf-8
import pygame

#Resolution de la surface
resolution = (640, 480)
#  pour le tuple color (R,G,B)
blue_color = (80, 150, 155)
black_color = (0,0,0)

# Init Pygame
pygame.init()

#Titre de la surface
pygame.display.set_caption("My first Pygame App")

# Création de la surface 
screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)

#Passage de la couleur sur screen
screen.fill(blue_color)

#Dessin d'une ligne (surface, color, position dep, position arr, bordure)
pygame.draw.line(screen, black_color, [10, 10], [100, 100], 5)

#Rect(left, top, width, height)
rect_form = pygame.Rect(200,200, 150, 200)
#Dessin un rectangle (surface, color, ObjRect, bordure)
pygame.draw.rect(screen, black_color, rect_form, 5)

#Dessin d'un cercle (surface, color, [position du cercle], rayon, bordure)
pygame.draw.circle(screen, black_color, [250, 100], 50, 5)

#Coordonnée pour poligone 
coords = [(50, 250), (100, 350), (150, 150)]
#Dessin d'un polygone (surface, color, position des points..., bordure)
pygame.draw.polygon(screen, black_color, coords, 5)

#Raffraichissement pour affichage
pygame.display.flip()

# Boucle infinit pour la surface
launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            