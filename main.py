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

   # Crear el objeto Clock y variable dt (ANTES del gameloop)
   clock = pygame.time.Clock()  # Objeto para controlar los FPS
   dt = 0  # Variable para almacenar el tiempo delta (tiempo entre frames)

   running = True
   while running:
      # Manejo de eventos
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
      
      # Llenar la pantalla con color negro
      screen.fill("black")
      
      # (Aquí iría la lógica de tu juego, actualización de objetos, etc.)
      
      # Actualizar la pantalla (siempre al final del bucle)
      pygame.display.flip()

      # Controlar FPS y actualizar dt (DENTRO del gameloop, al final)
      dt = clock.tick(60) / 1000  # Controlar los FPS a 60 (60 FPS)

   # Salir del juego
   pygame.quit()

if __name__ == "__main__":
   main()