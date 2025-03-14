import pygame
import sys
from Entities import *
from datetime import datetime, timedelta

pygame.init()

WIDTH, HEIGHT = 1000, 600
DIAMETER = pow(1000**2 + 600**2,0.5)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CShot")

# Colors
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
DARK_BG = (30, 30, 30)
LIGHT_BORDER = (200, 200, 200)
AIM1_COLOR = (255, 0, 0)  
AIM2_COLOR = (0, 255, 0)  
AIM_SIZE = 2
AIM_SPEED = 1.5

# Fonts
TITLE_FONT = pygame.font.Font(None, 100)
BUTTON_FONT = pygame.font.Font(None, 50)
MUTE_FONT = pygame.font.Font(None, 35)
ERROR_FONT = pygame.font.Font(None, 40)
SCORE_FONT = pygame.font.Font(None, 30)
TIMER_FONT = pygame.font.Font(None, 40)

# Menu options
menu_options = [
    {"text": "Start Game", "color": LIGHT_BLUE, "hover_color": DARK_BLUE},
    {"text": "Leaderboard", "color": LIGHT_GREEN, "hover_color": DARK_GREEN},
    {"text": "Exit", "color": LIGHT_RED, "hover_color": DARK_RED},
]

# Music state
is_music_paused = False 

def play_background_music():
    try:
        pygame.mixer.music.load("Free Video Music-03.mp3")  
        pygame.mixer.music.set_volume(0.5) 
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Could not load music file: {e}")

def draw_menu(selected=None):
    # Draw gradient background
    for y in range(HEIGHT):
        pygame.draw.line(screen, (YELLOW[0], YELLOW[1] - int(y / 5), YELLOW[2]), (0, y), (WIDTH, y))

    # Draw title
    title_surface = TITLE_FONT.render("CShot", True, CUSTOM_RED)
    screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 50))

    # Draw menu buttons
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

    # Draw mute button
    mute_button_rect = pygame.Rect(20, HEIGHT - 60, 100, 40)  
    pygame.draw.rect(screen, DARK_RED, mute_button_rect, border_radius=10)  
    mute_text = "Mute" if not is_music_paused else "Unmute"
    mute_surface = MUTE_FONT.render(mute_text, True, WHITE)
    screen.blit(mute_surface, (mute_button_rect.centerx - mute_surface.get_width() // 2,
                               mute_button_rect.centery - mute_surface.get_height() // 2))

    pygame.display.flip()
    return button_rects, mute_button_rect

def get_player_names():
    input_box1 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 40)
    input_box2 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 10, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color1 = color_inactive
    color2 = color_inactive
    active1 = False
    active2 = False
    text1 = ''
    text2 = ''
    font = pygame.font.Font(None, 32)
    error_message = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active1 = not active1
                    active2 = False
                elif input_box2.collidepoint(event.pos):
                    active2 = not active2
                    active1 = False
                else:
                    active1 = False
                    active2 = False
                color1 = color_active if active1 else color_inactive
                color2 = color_active if active2 else color_inactive
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        if text1.strip() == "" or text2.strip() == "":  # Check if either name is empty
                            error_message = "Both player names must be filled!"
                        else:
                            error_message = ''
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode
                elif active2:
                    if event.key == pygame.K_RETURN:
                        if text1.strip() == "" or text2.strip() == "":  # Check if either name is empty
                            error_message = "Both player names must be filled!"
                        else:
                            error_message = ''
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode

        # Draw gradient green background
        for y in range(HEIGHT):
            gradient_green = (0, min(255, 100 + int(y / HEIGHT * 155)), 0)  # Gradient from dark to light green
            pygame.draw.line(screen, gradient_green, (0, y), (WIDTH, y))

        # Draw input boxes
        txt_surface1 = font.render(text1, True, BLACK)
        txt_surface2 = font.render(text2, True, BLACK)
        width1 = max(200, txt_surface1.get_width() + 10)
        width2 = max(200, txt_surface2.get_width() + 10)
        input_box1.w = width1
        input_box2.w = width2
        screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)

        # Draw labels
        label1 = font.render("Player 1:", True, WHITE)
        label2 = font.render("Player 2:", True, WHITE)
        screen.blit(label1, (input_box1.x - 100, input_box1.y + 5))
        screen.blit(label2, (input_box2.x - 100, input_box2.y + 5))

        # Send error message
        if error_message:
            error_surface = ERROR_FONT.render(error_message, True, DARK_RED)
            screen.blit(error_surface, (WIDTH // 2 - error_surface.get_width() // 2, HEIGHT // 2 + 70))

        pygame.display.flip()

    return text1, text2

def player_shots(aim, targets):
    aim.shot()
    for target in targets:
        if aim.check_collision(target): # Collision check
            target.random_placement()
            return True
    return False 

def score_scale(aim):
    aim_xy = aim.xy_axis()
    shot_xy = aim.last_shot()
    x = aim_xy[0] - shot_xy[0]
    y = aim_xy[1] - shot_xy[1]
    distance = pow(x**2 + y**2,0.5)

    if DIAMETER > distance > DIAMETER - 233: return 5
    elif DIAMETER - 233 > distance > DIAMETER - 466: return 4
    elif DIAMETER - 466 > distance > DIAMETER - 699: return 3
    elif DIAMETER - 699 > distance > DIAMETER - 932: return 2
    else : return 1

def start_game():
    player1_name, player2_name = get_player_names()

    BORDER_THICKNESS = 5

    # Create Aim objects
    aim_1 = Aim(BORDER_THICKNESS, WIDTH, HEIGHT, screen, AIM_SPEED, AIM_SIZE, AIM1_COLOR, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
    aim_2 = Aim(BORDER_THICKNESS, WIDTH, HEIGHT, screen, AIM_SPEED, AIM_SIZE, AIM2_COLOR, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    # Create Targets
    target_1 = Target(BORDER_THICKNESS, WIDTH, HEIGHT, screen)
    target_2 = Target(BORDER_THICKNESS, WIDTH, HEIGHT, screen)
    target_3 = Target(BORDER_THICKNESS, WIDTH, HEIGHT, screen)
    targets = [target_1, target_2, target_3]
    timer = TimerTarget(BORDER_THICKNESS, WIDTH, HEIGHT, screen)
    ammo = AmmoTarget(BORDER_THICKNESS, WIDTH, HEIGHT, screen)

    # Randomly place aims and targets
    aim_1.random_placement()
    aim_2.random_placement()
    for target in targets:
        target.random_placement()
    ammo.random_placement()
    timer.random_placement()

    # Initialize shot counters
    player1_shots = 15 
    player2_shots = 15

    # players score
    score1 = 0
    score2 = 0
    player1_missed = True
    player2_missed = True

    # Initialize timers
    player1_timer = timedelta(seconds=60) 
    player2_timer = timedelta(seconds=60)
    start_time = datetime.now()

    ammo_activated = False
    timer_activated = False
    ammo_used = False
    timer_used = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player1_shots > 0 and player1_timer.total_seconds() > 0:  # Check for spacebar press
                    if player_shots(aim_1, targets):
                        if player1_missed:
                            score1 += score_scale(aim_1)
                        else: score1 += score_scale(aim_1) + 2
                        player1_missed = False
                    else: player1_missed = True

                    # check if player hits ammo box 
                    if ammo_activated and aim_1.check_collision(ammo):
                        ammo_used = True
                        player1_shots += 6

                    # check if player hits timer
                    if timer_activated and aim_1.check_collision(timer):
                        timer_used = True
                        player1_timer += timedelta(seconds=15)

                    player1_shots -= 1

                if event.key == pygame.K_KP_0 and player2_shots > 0 and player2_timer.total_seconds() > 0:  # check for 0 keypad press
                    if player_shots(aim_2, targets):
                        if player2_missed:
                            score2 += score_scale(aim_2)
                        else: score2 += score_scale(aim_2) + 2
                        player2_missed = False
                    else: player2_missed = True

                    # check if player hits ammo box 
                    if ammo_activated and aim_2.check_collision(ammo):
                        ammo_used = True
                        player2_shots += 6

                    # check if player hits timer
                    if timer_activated and aim_2.check_collision(timer):
                        timer_used = True
                        player2_timer += timedelta(seconds=15)

                    player2_shots -= 1

        if player1_shots <= 5 and player2_shots <= 5:
            ammo_activated = True

        if player1_timer.seconds <= 30 and player2_timer.seconds <= 30:
            timer_activated = True

        # Update timers
        elapsed_time = datetime.now() - start_time
        player1_timer -= elapsed_time
        player2_timer -= elapsed_time
        start_time = datetime.now()
        if player1_timer.total_seconds() <= 0: player1_timer = timedelta(seconds=0)
        if player2_timer.total_seconds() <= 0: player2_timer = timedelta(seconds=0)

        # Get pressed keys
        keys = pygame.key.get_pressed()
        aim_1.press_key(keys)
        aim_2.press_key(keys)

        # Draw background
        screen.fill(DARK_BG)

        # Draw player names, shot counts, and timers
        font = pygame.font.Font(None, 25)
        player1_text = font.render(f"Player 1: {player1_name} - Bullets: {player1_shots} - Timer: {player1_timer.seconds} - Score: {score1}", True, LIGHT_GREEN)
        screen.blit(player1_text, (20, 20))
        player2_text = font.render(f"Player 2: {player2_name} - Bullets: {player2_shots} - Timer: {player2_timer.seconds} - Score: {score2}", True, LIGHT_BLUE)
        screen.blit(player2_text, (WIDTH - 380, 20))  

        # Check if time is up or both players are out of shots
        if (player1_timer.total_seconds() <= 0 and player2_timer.total_seconds() <= 0) or (player1_shots <= 0 and player2_shots <= 0) or (player1_timer.total_seconds() <= 0 and player2_shots <= 0) or (player2_timer.total_seconds() <= 0 and player1_shots <= 0):
            running = False
            print("Game Over!")
            print(f"{player1_name} shots: {15 - player1_shots}")
            print(f"{player2_name} shots: {15 - player2_shots}")

        # Draw objects
        aim_1.draw()
        aim_2.draw()
        for target in targets:
            target.draw()
        
        if not ammo_used and ammo_activated:
            ammo.draw()
        if not timer_used and timer_activated:
            timer.draw()
        
        # Update the display
        pygame.display.flip()

def leaderboard():
    print("Leaderboard")
    pygame.time.wait(400)

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

if __name__ == "__main__":
    play_background_music() 
    main_menu()