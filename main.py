#coding:utf-8
import pygame

#Resolution de la surface
resolution = (1600, 900)
#  pour le tuple color (R,G,B, Alpha)
blue_color = (80, 150, 155)
black_color = (0,0,0)
white_color = (255, 255, 255)

# Init Pygame
pygame.init()

#Titre de la surface
pygame.display.set_caption("My first Pygame App")

# Création de la surface 
screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)


# Récupérer image en créer un surface
sonicImg = pygame.image.load("sonic.jpg")
mushroomImg = pygame.image.load("mushroom.png")
#Convertion de l'image 
sonicImg.convert()
#Avec gestion de la transparence
mushroomImg.convert_alpha()



# Boucle infinit pour la surface
launched = True
while launched:
    # Accède aux event de Pygame
    for event in pygame.event.get():
        #Gestion de la croix
        if event.type == pygame.QUIT:
            launched = False
        
        # Ecoute Touche Escape
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                launched = False

    ### Corps du program

    #Passage de la couleur a screen
    screen.fill(white_color)

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


    #Affiche image sur la surface blit(img, [coordonnée du point haut gauche de l'image X,Y])
    screen.blit(sonicImg, [500, 200]) 
    screen.blit(mushroomImg, [200, 500])


    #Raffraichissement pour affichage
    pygame.display.flip()
   