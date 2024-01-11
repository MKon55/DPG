import pygame
import random

#Inicializace Pygame
pygame.init()

#Barvy
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)

#Velikost okna
sirka_okna = 600
vyska_okna = 400

#Nastavení okna
okno = pygame.display.set_mode((sirka_okna, vyska_okna))
pygame.display.set_caption('Starý dobrý had :-) ')

#Hodiny
hodiny = pygame.time.Clock()

#Velikost bloku hada
velikost_bloku = 10
rychlost_hada = 10

#Fonty
font_styl = pygame.font.SysFont("comicsansm", 25)
font_skore = pygame.font.SysFont("comicsansms", 35)

#Výpis skóre
def Vase_skore(skore):
    hodnota = font_skore.render("Vaše skóre: " + str(skore), True, BLACK)
    okno.blit(hodnota, [0, 0])

#Vykreslení hada
def nase_had(velikost_bloku, seznam_hada):
    for x in seznam_hada:
        pygame.draw.rect(okno, GREEN, [x[0], x[1], velikost_bloku, velikost_bloku])

#Výpis zprávy
def zprava(msg, barva):
    zprava = font_styl.render(msg, True, barva)
    okno.blit(zprava, [sirka_okna / 10, vyska_okna / 3])

#Hlavní herní smyčka
def herniSmycka():
    konec_hry = False
    konec_hry_text = False

    #Pozice a pohyb hada
    x1 = sirka_okna / 2
    y1 = vyska_okna / 2

    x1_zmena = 0
    y1_zmena = 0

    seznam_hada = []
    delka_hada = 1

    jidlo_x = round(random.randrange(0, sirka_okna - velikost_bloku) / 10.0) * 10.0
    jidlo_y = round(random.randrange(0, vyska_okna - velikost_bloku) / 10.0) * 10.0

    # Hlavní herní smyčka
    while not konec_hry:

        #Hra skončila, zobrazí se zpráva
        while konec_hry_text == True:
            okno.fill(WHITE)
            zprava("Stiskněte C-pro znovu nebo Q-pro ukončení", RED)
            Vase_skore(delka_hada - 1)
            pygame.display.update()

            #Reakce na klávesy
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        konec_hry = True
                        konec_hry_text = False
                    if event.key == pygame.K_c:
                        herniSmycka()

        #Zpracování událostí
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                konec_hry = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_zmena = -velikost_bloku
                    y1_zmena = 0
                elif event.key == pygame.K_RIGHT:
                    x1_zmena = velikost_bloku
                    y1_zmena = 0
                elif event.key == pygame.K_UP:
                    y1_zmena = -velikost_bloku
                    x1_zmena = 0
                elif event.key == pygame.K_DOWN:
                    y1_zmena = velikost_bloku
                    x1_zmena = 0

        #Kontrola zda-li had narazil do hranice okna
        if x1 >= sirka_okna or x1 < 0 or y1 >= vyska_okna or y1 < 0:
            konec_hry_text = True

        x1 += x1_zmena
        y1 += y1_zmena
        okno.fill(WHITE)

        #Vykreslení jídla
        pygame.draw.rect(okno, RED, [jidlo_x, jidlo_y, velikost_bloku, velikost_bloku])

        #Přidání nové pozice do seznamu hada
        hlava_hada = []
        hlava_hada.append(x1)
        hlava_hada.append(y1)
        seznam_hada.append(hlava_hada)

        #Ořezání seznamu hada
        if len(seznam_hada) > delka_hada:
            del seznam_hada[0]

        #Kontrola, zda-li had narazil sám do sebe
        for x in seznam_hada[:-1]:
            if x == hlava_hada:
                konec_hry_text = True

        #Vykreslení hada do okna
        nase_had(velikost_bloku, seznam_hada)

        #Výpis skóre
        Vase_skore(delka_hada - 1)

        pygame.display.update()

        #Přidání nového jídla po sežrání
        if x1 == jidlo_x and y1 == jidlo_y:
            jidlo_x = round(random.randrange(0, sirka_okna - velikost_bloku) / 10.0) * 10.0
            jidlo_y = round(random.randrange(0, vyska_okna - velikost_bloku) / 10.0) * 10.0
            delka_hada += 1

            #Konec hry po sežrání určitého počtu jídel
            if delka_hada >= 10:
                konec_hry_text = True

        #Omezení rychlosti hry
        hodiny.tick(rychlost_hada)

    pygame.quit()
    quit()

#Spuštění herní smyčky
herniSmycka()
