import pygame
import random
import sys
import time

pygame.init()
pygame.mixer.init()

# Screen
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stone Paper Scissor")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 50)

# Load Images
stone_img = pygame.image.load("stone.png")
paper_img = pygame.image.load("paper.png")
scissor_img = pygame.image.load("scissor.png")

stone_img = pygame.transform.scale(stone_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissor_img = pygame.transform.scale(scissor_img, (100, 100))

images = {
    "Stone": stone_img,
    "Paper": paper_img,
    "Scissor": scissor_img
}

# Load Sounds
win_sound = pygame.mixer.Sound("win.wav")
lose_sound = pygame.mixer.Sound("lose.wav")
click_sound = pygame.mixer.Sound("click.wav")

choices = ["Stone", "Paper", "Scissor"]

# Button class
class Button:
    def __init__(self, img, x, y, name):
        self.image = img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name

    def draw(self):
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Buttons
stone_btn = Button(stone_img, 80, 350, "Stone")
paper_btn = Button(paper_img, 250, 350, "Paper")
scissor_btn = Button(scissor_img, 420, 350, "Scissor")

# Game variables
result = ""
computer_choice = ""
show_animation = False

def countdown_animation():
    for i in ["3", "2", "1"]:
        screen.fill(WHITE)
        text = big_font.render(i, True, BLACK)
        screen.blit(text, (280, 200))
        pygame.display.update()
        pygame.time.delay(500)

def shake_animation():
    for _ in range(5):
        screen.fill(WHITE)
        offset = random.randint(-10, 10)
        screen.blit(images["Stone"], (200 + offset, 150))
        pygame.display.update()
        pygame.time.delay(100)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    title = big_font.render("Stone Paper Scissor", True, BLACK)
    screen.blit(title, (120, 30))

    # Show result
    if computer_choice:
        comp_img = images[computer_choice]
        screen.blit(comp_img, (250, 120))

    if result:
        res_text = font.render(result, True, BLACK)
        screen.blit(res_text, (220, 250))

    # Draw buttons
    stone_btn.draw()
    paper_btn.draw()
    scissor_btn.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if stone_btn.is_clicked(pos):
                user = "Stone"
            elif paper_btn.is_clicked(pos):
                user = "Paper"
            elif scissor_btn.is_clicked(pos):
                user = "Scissor"
            else:
                continue

            click_sound.play()

            countdown_animation()
            shake_animation()

            computer_choice = random.choice(choices)

            if user == computer_choice:
                result = "It's a Tie!"
            elif (user == "Stone" and computer_choice == "Scissor") or \
                 (user == "Paper" and computer_choice == "Stone") or \
                 (user == "Scissor" and computer_choice == "Paper"):
                result = "You Win!"
                win_sound.play()
            else:
                result = "You Lose!"
                lose_sound.play()

    pygame.display.update()