import pygame
import pygame_gui

class GUI:

    def __init__(self):
        pygame.init()

        # Declaring object dimensions - width x height
        self.window_size = (800, 600)
        self.tile_size = (60, 60)
        self.initial_board_pos = (50, 50)

        # Window title
        pygame.display.set_caption('Sudoku Solver')
        
        # Background settings
        self.background = pygame.Surface(self.window_size)
        self.background.fill(pygame.Color('#111111'))
        
        self.window_surface = pygame.display.set_mode(self.window_size)
        self.manager = pygame_gui.UIManager(self.window_size)


    def run(self):
        # Infinite loop running the program until closed
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            time_delta = clock.tick(60)/1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                

                self.manager.process_events(event)
            
            self.manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            pygame.display.update()


    def drawBoard(self):

        X, Y = self.initial_board_pos

        