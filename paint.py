import pygame
import webbrowser

class Paint:
    @staticmethod
    def paint(screen, SCREEN_WIDTH, SCREEN_HEIGHT, pokemon_coordinates, running = False):

        drawing = False
        mod_draw = True
        pixels_rouges = [] 
        fond_origine = screen.copy()  # Capture du fond d'écran d'origine

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:  
                        mod_draw = not mod_draw  # Inverser l'état du mode dessin
                        print("Mode dessin activé", mod_draw)
                    if event.key == pygame.K_c and mod_draw: 
                        print("Nettoyage du dessin")
                        screen.blit(fond_origine, (0, 0)) 
                        pygame.display.flip()  
                        pixels_rouges = []  
                elif event.type == pygame.MOUSEBUTTONDOWN and mod_draw:
                    drawing = True
                elif event.type == pygame.MOUSEBUTTONUP and mod_draw:
                    drawing = False
                elif event.type == pygame.MOUSEMOTION and drawing and mod_draw:
                    pos = pygame.mouse.get_pos()  
                    if 0 <= pos[0] < SCREEN_WIDTH and 0 <= pos[1] < SCREEN_HEIGHT:  
                        couleur_origine = screen.get_at(pos) 
                        pygame.draw.circle(screen, (255, 0, 0), pos, 3)  
                        pixels_rouges.append((pos, couleur_origine))  
                        pygame.display.flip() 
                    
                    
                elif event.type == pygame.MOUSEBUTTONDOWN: # Logique de pokepedia
                    mouse_pos = pygame.mouse.get_pos()
                    for pokemon_info in pokemon_coordinates:
                        name_pokemon, coo_pokemon = pokemon_info
                        rect_pokemon = pygame.Rect(coo_pokemon)
                        if rect_pokemon.collidepoint(mouse_pos):
                            print("Nom du Pokémon:", name_pokemon)
                            webbrowser.open(f"https://www.pokepedia.fr/{name_pokemon}")
                

            pygame.display.update()
