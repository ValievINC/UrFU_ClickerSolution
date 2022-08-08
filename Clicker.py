import pygame
import sys


# Константы
left_mouse_button = 1
FPS = 60
display_width = 1280
display_height = 720


# Глобальные переменные
clicks = 0
click_power = 1
power_price = 10


# Инициализация всего
pygame.init()
window = pygame.display
window.set_caption("UrFU Clicker")
urfu_image = pygame.image.load("UrFU.png")
power_image = pygame.image.load("plus_blue.png")
screen = window.set_mode((display_width, display_height))
clock = pygame.time.Clock()


# Рисуем логотип
def draw():
    screen.fill("white")
    screen.blit(urfu_image, (395, 127))
    screen.blit(power_image, (10, 285))


# Рисуем количество кликов
def draw_click_count():
    font = pygame.font.SysFont('arial', 36)
    text = font.render(f'Кликов: {clicks}', True, 'black')
    center = text.get_rect(center=(display_width/2, 100))
    screen.blit(text, center)


# Рисуем силу крика
def draw_click_power():
    font = pygame.font.SysFont('arial', 24)
    text = font.render(f'Сила клика: {click_power}', True, 'black')
    center = text.get_rect(center=(85, 265))
    screen.blit(text, center)


# Рисуем цену буста
def draw_power_price():
    font = pygame.font.SysFont('arial', 24)
    text = font.render(f'Цена буста: {power_price}', True, 'black')
    center = text.get_rect(center=(85, 455))
    screen.blit(text, center)


# Непосредственно геймплей циклом True
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == left_mouse_button:
            mouse_position = pygame.mouse.get_pos()
            # Клик по логотипу
            if mouse_position[0] in range(395, 885) and mouse_position[1] in range(127, 593):
                clicks += click_power
            # Покупка буста
            elif mouse_position[0] in range(10, 160) and mouse_position[1] in range(285, 435):
                if clicks >= power_price:
                    click_power += 1
                    clicks -= power_price
                    power_price = round(power_price * 1.5)
        # Выход
        if event.type == pygame.QUIT:
            sys.exit()

    draw()
    draw_click_count()
    draw_click_power()
    draw_power_price()
    # Без update не будет отрисовки
    pygame.display.update()