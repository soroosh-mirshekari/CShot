import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CShot")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (0, 100, 0)
LIGHT_RED = (255, 182, 193)
DARK_RED = (139, 0, 0)
YELLOW = (245, 210, 34)
GRAY = (100, 100, 100)
CUSTOM_RED = (245, 93, 34)

TITLE_FONT = pygame.font.Font(None, 100)
BUTTON_FONT = pygame.font.Font(None, 50)
MUTE_FONT = pygame.font.Font(None, 35)

menu_options = [
    {"text": "Start Game", "color": LIGHT_BLUE, "hover_color": DARK_BLUE},
    {"text": "Leaderboard", "color": LIGHT_GREEN, "hover_color": DARK_GREEN},
    {"text": "Exit", "color": LIGHT_RED, "hover_color": DARK_RED},
]


is_music_paused = False 

def play_background_music():
    try:
        pygame.mixer.music.load("Free Video Music-03.mp3")  
        pygame.mixer.music.set_volume(0.5) 
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Could not load music file: {e}")

def draw_menu(selected=None):
    
    for y in range(HEIGHT):
        pygame.draw.line(screen, (YELLOW[0], YELLOW[1] - int(y / 5), YELLOW[2]), (0, y), (WIDTH, y))

   
    title_surface = TITLE_FONT.render("CShot", True, CUSTOM_RED)
    screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 50))

 
    button_rects = []
    for index, option in enumerate(menu_options):
        rect_x, rect_y = WIDTH // 2 - 150, 200 + index * 100
        rect_width, rect_height = 300, 60
        color = option["hover_color"] if selected == index else option["color"]

        pygame.draw.rect(screen, GRAY, (rect_x + 5, rect_y + 5, rect_width, rect_height), border_radius=15)
        pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height), border_radius=15)

        text_surface = BUTTON_FONT.render(option["text"], True, WHITE)
        screen.blit(text_surface, (rect_x + rect_width // 2 - text_surface.get_width() // 2,
                                   rect_y + rect_height // 2 - text_surface.get_height() // 2))

        button_rects.append(pygame.Rect(rect_x, rect_y, rect_width, rect_height))

   
    mute_button_rect = pygame.Rect(20, HEIGHT - 60, 100, 40)  
    pygame.draw.rect(screen, DARK_RED, mute_button_rect, border_radius=10)  
    mute_text = "Mute" if not is_music_paused else "Unmute"
    mute_surface = MUTE_FONT.render(mute_text, True, WHITE)
    screen.blit(mute_surface, (mute_button_rect.centerx - mute_surface.get_width() // 2,
                               mute_button_rect.centery - mute_surface.get_height() // 2))

    pygame.display.flip()
    return button_rects, mute_button_rect

def main_menu():
    global is_music_paused 
    running = True
    selected = None
    while running:
        button_rects, mute_button_rect = draw_menu(selected)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                for index, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        selected = index
                        break
                else:
                    selected = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mute_button_rect.collidepoint(mouse_pos):
                    if is_music_paused:
                        pygame.mixer.music.unpause()
                        is_music_paused = False
                    else:
                        pygame.mixer.music.pause()
                        is_music_paused = True
                for index, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        if index == 0:  
                            start_game()
                        elif index == 1:  
                            leaderboard()
                        elif index == 2:
                            running = False
                            pygame.quit()
                            sys.exit()
        pygame.display.flip()

def start_game():
    print("Start Game")
    pygame.time.wait(400)

def leaderboard():
    print("Leaderboard")
    pygame.time.wait(400)

if __name__ == "__main__":
    play_background_music() 
    main_menu()
