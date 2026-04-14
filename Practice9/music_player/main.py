import pygame
from player import play, stop, next_track, back_track

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 50)

play_text = "P = play"
stop_text = "S = stop"
next_text = "N = next track"
back_text = "B = previous track"
exit_text = "Q = quit"

tracks_t = ["Kairat Nurtas - Ол сен емес", "Градусы - Кто ты"]
selected_track_text = tracks_t[0]

play_text_surface = font.render(play_text, True, (0, 0, 0))
stop_text_surface = font.render(stop_text, True, (0, 0, 0))
next_text_surface = font.render(next_text, True, (0, 0, 0))
back_text_surface = font.render(back_text, True, (0, 0, 0))
exit_text_surface = font.render(exit_text, True, (0, 0, 0))
selected_track_surface = font.render(selected_track_text, True, (0, 0, 0))
play_text_rect = play_text_surface.get_rect(center=(400, 100))
stop_text_rect = stop_text_surface.get_rect(center=(400, 150))
next_text_rect = next_text_surface.get_rect(center=(400, 200))
back_text_rect = back_text_surface.get_rect(center=(400, 250))
exit_text_rect = exit_text_surface.get_rect(center=(400, 300))
selected_track_rect = selected_track_surface.get_rect(center=(400, 450))

tracks = ["Practice9/music_player/music/Kairosh.mp3", "Practice9/music_player/music/gradusi.mp3"]

selected_track = tracks[0]

# pygame.mixer.music.load("Practice9/music_player/music/Kairosh.mp3")
# pygame.mixer.music.load("Practice9/music_player/music/gradusi.mp3")
# pygame.mixer.music.play()

pos = 0

is_paused = False

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play(selected_track)
            elif event.key == pygame.K_s:
                stop(is_paused)
                is_paused = stop(is_paused)
                print(is_paused)
            elif event.key == pygame.K_n:
                pos, selected_track, selected_track_surface, selected_track_rect = next_track(tracks, pos, tracks_t)
            elif event.key == pygame.K_b:
                pos, selected_track, selected_track_surface, selected_track_rect = back_track(tracks, pos, tracks_t)
            elif event.key == pygame.K_q:
                run = False
                
    
    screen.fill((255, 255, 255))
    screen.blit(play_text_surface, play_text_rect)
    screen.blit(stop_text_surface, stop_text_rect)
    screen.blit(next_text_surface, next_text_rect)
    screen.blit(back_text_surface, back_text_rect)
    screen.blit(exit_text_surface, exit_text_rect)
    screen.blit(selected_track_surface, selected_track_rect)

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()