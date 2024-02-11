import pygame

class Paint:
    @staticmethod
    def paint(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        running = True
        drawing = False
        pixels_rouges = [] 
        fond_origine = screen.copy()  # Capture du fond d'écran d'origine

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    drawing = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    drawing = False
                elif event.type == pygame.MOUSEMOTION and drawing:
                    pos = pygame.mouse.get_pos()  
                    if 0 <= pos[0] < SCREEN_WIDTH and 0 <= pos[1] < SCREEN_HEIGHT:  # Vérifier si la position est à l'intérieur des limites de la fenêtre
                        couleur_origine = screen.get_at(pos) 
                        pygame.draw.circle(screen, (255, 0, 0), pos, 3)  
                        pixels_rouges.append((pos, couleur_origine))  
                        pygame.display.flip() 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c: 
                        screen.blit(fond_origine, (0, 0)) 
                        pygame.display.flip()  
                        pixels_rouges = []  

            pygame.display.update()
