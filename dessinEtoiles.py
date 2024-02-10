import pygame

class dessinEtoile:
    @staticmethod
    def drawStar(surface, color, center, size):
    # Définir les points de l'étoile
        outer_points = [
            (center[0], center[1] - size),  # point supérieur
            (center[0] + size * 0.3, center[1] - size * 0.3),  # point supérieur droit
            (center[0] + size, center[1]),  # point droit
            (center[0] + size * 0.3, center[1] + size * 0.3),  # point inférieur droit
            (center[0], center[1] + size),  # point inférieur
            (center[0] - size * 0.3, center[1] + size * 0.3),  # point inférieur gauche
            (center[0] - size, center[1]),  # point gauche
            (center[0] - size * 0.3, center[1] - size * 0.3)  # point supérieur gauche
        ]

        # Dessiner l'étoile en reliant les points
        pygame.draw.polygon(surface, color, outer_points)