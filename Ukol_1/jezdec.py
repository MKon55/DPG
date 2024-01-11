import pygame
import sys
import os

#Inicializace Pygame
pygame.init()

#Cesta k novému pracovnímu adresáři - nutno nastavit vlastní 
new_working_directory = r"C:\Users\misap\Desktop\DPG\Ukol_1"

#Změna pracovního adresáře
os.chdir(new_working_directory)

# Definice barev
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Velikost okna a šachovnice
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

#Inicializace okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Šachovnice s jezdcem')

#Funkce pro vykreslení šachovnice
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
#Funkce pro načtení obrázku jezdce
def load_knight_image():
    return pygame.image.load("knight.png").convert_alpha()

#Načtení obrázku jezdce
knight_image = load_knight_image()

#Funkce pro vykreslení jezdce
def draw_knight(row, col):
    screen.blit(knight_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

#Počáteční pozice jezdce
knight_row, knight_col = 5, 5

#Funkce pro výpočet platných tahů jezdce
def valid_moves(row, col):
    moves = []

    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    for move in knight_moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
            moves.append((new_row, new_col))

    return moves

#Hlavní smyčka hry
running = True
selected = False  #Zda jezdce vybrán
selected_moves = []  #Seznam platných tahů pro vybrané pole

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_col = mouseX // SQUARE_SIZE
            clicked_row = mouseY // SQUARE_SIZE

            #Kontrola, zda myš byla kliknuta na jezdce
            if selected:
                #Kontrola, zda kliknuté pole je mezi platnými tahy
                if (clicked_row, clicked_col) in selected_moves:
                    knight_row, knight_col = clicked_row, clicked_col
                    selected = False
                    selected_moves = []
                else:
                    selected = False
                    selected_moves = []
            else:
                #Kontrola, zda kliknuté pole obsahuje jezdce
                if (clicked_row, clicked_col) == (knight_row, knight_col):
                    selected = True
                    selected_moves = valid_moves(knight_row, knight_col)

    keys = pygame.key.get_pressed()

    if selected:
        screen.fill(BLACK)
        draw_board()

        for move in selected_moves:
            pygame.draw.rect(screen, (0, 255, 0), (move[1] * SQUARE_SIZE, move[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        draw_knight(knight_row, knight_col)
        pygame.display.flip()
    else:
        if keys[pygame.K_UP] and (knight_row - 1, knight_col) in valid_moves(knight_row, knight_col):
            knight_row -= 1
        if keys[pygame.K_DOWN] and (knight_row + 1, knight_col) in valid_moves(knight_row, knight_col):
            knight_row += 1
        if keys[pygame.K_LEFT] and (knight_row, knight_col - 1) in valid_moves(knight_row, knight_col):
            knight_col -= 1
        if keys[pygame.K_RIGHT] and (knight_row, knight_col + 1) in valid_moves(knight_row, knight_col):
            knight_col += 1

        screen.fill(BLACK)
        draw_board()
        draw_knight(knight_row, knight_col)
        pygame.display.flip()

pygame.quit()
sys.exit()