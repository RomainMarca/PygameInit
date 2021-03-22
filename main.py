#coding:utf-8
import pygame

#Resolution de la surface
resolution = (1600, 900)
# Tuple color (R,G,B, Alpha)
blue_color = (0, 75, 155)
black_color = (0,0,0)
white_color = (255, 255, 255)
red_color = (255, 0, 0)

FRAMERATE = 60

# Init Pygame
pygame.init()

#Initialisation du tps
clock = pygame.time.Clock()

#Titre de la surface
pygame.display.set_caption("My first Pygame App")

# Création de la surface 
screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)


# Récupérer image en créer un surface
sonicImg = pygame.image.load("img/sonic.jpg")
mushroomImg = pygame.image.load("img/mushroom.png")
#Convertion de l'image 
sonicImg.convert()
#Avec gestion de la transparence
mushroomImg.convert_alpha()

#Charger TextPolicy "SYSTEM" SysFont("namePolicy", taille, True/False bold, True/False Italic)
arial_font = pygame.font.SysFont("arial", 30)
#Charger TextPolicy Font("namePolicy", taille)
other_font = pygame.font.Font("font/Sweet Talk.otf", 100)
#Donner un text a la police render("TEXTE", True/False lissage, color, BackgroudColor)
text = arial_font.render("Hello World !", True, blue_color)
text2 = other_font.render("Hello Moon !", True, red_color)


# Boucle infinit pour la surface
launched = True
while launched:
    
    ### Corps du program ###

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

    #Affiche le texte sur la surface blit(texte, [coordonnée du point haut gauche de l'image X,Y])
    screen.blit(text, [550, 100])
    screen.blit(text2, [550, 140])


    # Accède aux event de Pygame
    for event in pygame.event.get():
        #Gestion de la croix
        if event.type == pygame.QUIT:
            launched = False
        
        # Ecoute Touche Escape
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                launched = False
        
        # Affiche les dimension nde la surface apres avoir récupéré celle ci
        if event.type == pygame.VIDEORESIZE:
            screen.fill(white_color)
            other_font = pygame.font.Font("font/Sweet Talk.otf", 100)
            text2 = other_font.render("{}x{}".format(event.w, event.h), True, red_color)
            screen.blit(text2, [550, 140])
        
        """
        # Affiche sur le terminal la postion de la souris dans la surface
        if event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))
        """

    # Vitesse de raffraichissement    
    clock.tick(FRAMERATE)

    #Raffraichissement pour affichage
    pygame.display.flip()
   