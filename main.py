# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   running = True
   while running:
      # Manejo de eventos
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
      
      # 1. Llenar la pantalla con color negro
      screen.fill("black")
      
      # (Aquí iría la lógica de tu juego, actualización de objetos, etc.)
      
      # 2. Actualizar la pantalla (siempre al final del bucle)
      pygame.display.flip()

   # Salir del juego
   pygame.quit()

if __name__ == "__main__":
   main()