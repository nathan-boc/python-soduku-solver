import pygame
import pygame_gui


pygame.init()


# Declaring object dimensions
window_size = (800, 600)
tile_size = (50, 50)


# Window title
pygame.display.set_caption('Sudoku Solver')
window_surface = pygame.display.set_mode(window_size)

# Background settings
background = pygame.Surface(window_size)
background.fill(pygame.Color('#111111'))

manager = pygame_gui.UIManager(window_size)

# Window objects
hello_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((350, 275), (100, 50)), 
                                            text = 'Say Hello', 
                                            manager = manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    print('Hello World!')

        manager.process_events(event)
    
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()