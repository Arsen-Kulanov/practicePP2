import pygame
import math
from datetime import datetime

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    canvas = pygame.Surface((800, 600))
    canvas.fill((0, 0, 0))

    font = pygame.font.SysFont(None, 32)

    mode = 'blue'
    tool = 'brush'
    brush_size = 5

    drawing = False
    start_pos = None
    last_pos = None

    text_mode = False
    text = ""
    text_pos = None

    def color():
        if mode == 'red':
            return (255, 0, 0)
        if mode == 'green':
            return (0, 255, 0)
        return (0, 0, 255)

    def flood_fill(surf, x, y, target, repl):
        if target == repl:
            return
        stack = [(x, y)]
        w, h = surf.get_size()
        while stack:
            cx, cy = stack.pop()
            if 0 <= cx < w and 0 <= cy < h:
                if surf.get_at((cx, cy))[:3] == target:
                    surf.set_at((cx, cy), repl)
                    stack.append((cx+1, cy))
                    stack.append((cx-1, cy))
                    stack.append((cx, cy+1))
                    stack.append((cx, cy-1))

    def draw_rect(s, a, b, c):
        x = min(a[0], b[0])
        y = min(a[1], b[1])
        w = abs(a[0] - b[0])
        h = abs(a[1] - b[1])
        pygame.draw.rect(s, c, (x, y, w, h), brush_size)

    def draw_circle(s, a, b, c):
        r = int(((b[0]-a[0])**2 + (b[1]-a[1])**2) ** 0.5)
        pygame.draw.circle(s, c, a, r, brush_size)

    def draw_square(s, a, b, c):
        size = min(abs(b[0]-a[0]), abs(b[1]-a[1]))
        x, y = a
        if b[0] < a[0]:
            x -= size
        if b[1] < a[1]:
            y -= size
        pygame.draw.rect(s, c, (x, y, size, size), brush_size)

    def draw_rtriangle(s, a, b, c):
        p1 = a
        p2 = (a[0], b[1])
        p3 = b
        pygame.draw.polygon(s, c, [p1, p2, p3], brush_size)

    def draw_etriangle(s, a, b, c):
        side = abs(b[0] - a[0])
        h = int((math.sqrt(3)/2) * side)
        p1 = a
        p2 = (a[0] + side, a[1])
        p3 = (a[0] + side//2, a[1] - h)
        pygame.draw.polygon(s, c, [p1, p2, p3], brush_size)

    def draw_rhombus(s, a, b, c):
        cx = (a[0] + b[0]) // 2
        cy = (a[1] + b[1]) // 2
        w = abs(b[0] - a[0]) // 2
        h = abs(b[1] - a[1]) // 2
        p1 = (cx, cy - h)
        p2 = (cx + w, cy)
        p3 = (cx, cy + h)
        p4 = (cx - w, cy)
        pygame.draw.polygon(s, c, [p1, p2, p3, p4], brush_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                mods = pygame.key.get_mods()

                if mods & pygame.KMOD_CTRL and event.key == pygame.K_s:
                    name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
                    pygame.image.save(canvas, name)

                if text_mode:
                    if event.key == pygame.K_ESCAPE:
                        text_mode = False
                        text = ""
                    elif event.key == pygame.K_RETURN:
                        img = font.render(text, True, color())
                        canvas.blit(img, text_pos)
                        text_mode = False
                        text = ""
                    else:
                        text += event.unicode
                    continue

                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                elif event.key == pygame.K_1:
                    brush_size = 2
                elif event.key == pygame.K_2:
                    brush_size = 5
                elif event.key == pygame.K_3:
                    brush_size = 10

                elif event.key == pygame.K_4:
                    tool = 'brush'
                elif event.key == pygame.K_5:
                    tool = 'rect'
                elif event.key == pygame.K_6:
                    tool = 'circle'
                elif event.key == pygame.K_7:
                    tool = 'eraser'
                elif event.key == pygame.K_8:
                    tool = 'line'
                elif event.key == pygame.K_9:
                    tool = 'fill'
                elif event.key == pygame.K_0:
                    tool = 'text'
                elif event.key == pygame.K_q:
                    tool = 'square'
                elif event.key == pygame.K_w:
                    tool = 'rtriangle'
                elif event.key == pygame.K_e:
                    tool = 'etriangle'
                elif event.key == pygame.K_t:
                    tool = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tool == 'fill':
                    x, y = event.pos
                    target = canvas.get_at((x, y))[:3]
                    flood_fill(canvas, x, y, target, color())

                elif tool == 'text':
                    text_mode = True
                    text_pos = event.pos
                    text = ""

                else:
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

                if tool == 'rect':
                    draw_rect(canvas, start_pos, event.pos, color())
                elif tool == 'circle':
                    draw_circle(canvas, start_pos, event.pos, color())
                elif tool == 'line':
                    pygame.draw.line(canvas, color(), start_pos, event.pos, brush_size)
                elif tool == 'square':
                    draw_square(canvas, start_pos, event.pos, color())
                elif tool == 'rtriangle':
                    draw_rtriangle(canvas, start_pos, event.pos, color())
                elif tool == 'etriangle':
                    draw_etriangle(canvas, start_pos, event.pos, color())
                elif tool == 'rhombus':
                    draw_rhombus(canvas, start_pos, event.pos, color())

        if drawing and tool == 'brush':
            mx, my = pygame.mouse.get_pos()
            pygame.draw.line(canvas, color(), last_pos, (mx, my), brush_size)
            last_pos = (mx, my)

        if drawing and tool == 'eraser':
            mx, my = pygame.mouse.get_pos()
            pygame.draw.circle(canvas, (0, 0, 0), (mx, my), 20)

        screen.blit(canvas, (0, 0))

        if drawing and tool == 'line':
            pygame.draw.line(screen, color(), start_pos, pygame.mouse.get_pos(), brush_size)

        if text_mode:
            img = font.render(text, True, color())
            screen.blit(img, text_pos)

        pygame.display.flip()
        clock.tick(60)

main()