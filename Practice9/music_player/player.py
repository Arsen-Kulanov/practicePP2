import pygame

pygame.init()
font = pygame.font.Font(None, 50)

def play(selected_track):
    pygame.mixer.music.load(selected_track)
    pygame.mixer.music.play()

def stop(is_paused):
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
        return is_paused
    else:
        pygame.mixer.music.pause()
        is_paused = True
        return is_paused

def next_track(tracks, pos, tracks_t):
    pos = (pos + 1) % len(tracks)

    selected_track = tracks[pos]
    selected_track_text = tracks_t[pos]

    selected_track_surface = font.render(selected_track_text, True, (0, 0, 0))
    selected_track_rect = selected_track_surface.get_rect(center=(400, 450))

    return pos, selected_track, selected_track_surface, selected_track_rect

def back_track(tracks, pos, tracks_t):
    pos = (pos - 1) % len(tracks)

    selected_track = tracks[pos]
    selected_track_text = tracks_t[pos]

    selected_track_surface = font.render(selected_track_text, True, (0, 0, 0))
    selected_track_rect = selected_track_surface.get_rect(center=(400, 450))

    return pos, selected_track, selected_track_surface, selected_track_rect