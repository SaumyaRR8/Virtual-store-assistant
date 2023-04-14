import pygame

# Define the store layout
store_layout = [    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]

# Define the map's dimensions
map_width = 400
map_height = 400

# Initialize Pygame
pygame.init()

# Create the canvas
canvas = pygame.display.set_mode((map_width, map_height))

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define aisle and shelf dimensions
aisle_width = map_width // len(store_layout[0])
aisle_height = map_height // len(store_layout)
shelf_width = aisle_width // 2
shelf_height = aisle_height // 2

# Draw the store layout on the canvas
for i in range(len(store_layout)):
    for j in range(len(store_layout[0])):
        aisle_x = j * aisle_width
        aisle_y = i * aisle_height
        if store_layout[i][j] == 1:
            pygame.draw.rect(canvas, black, (aisle_x, aisle_y, aisle_width, aisle_height), 0)
            shelf_x = aisle_x + aisle_width // 4
            shelf_y = aisle_y + aisle_height // 4
            pygame.draw.rect(canvas, white, (shelf_x, shelf_y, shelf_width, shelf_height), 0)

# Add labels
font = pygame.font.SysFont('Arial', 16)
for i in range(len(store_layout)):
    for j in range(len(store_layout[0])):
        aisle_x = j * aisle_width
        aisle_y = i * aisle_height
        if store_layout[i][j] == 1:
            aisle_label = font.render('Aisle {}'.format(len(store_layout)*i+j+1), True, white)
            aisle_label_rect = aisle_label.get_rect()
            aisle_label_rect.center = (aisle_x + aisle_width // 2, aisle_y + aisle_height // 2)
            canvas.blit(aisle_label, aisle_label_rect)

# Update the display
pygame.display.update()

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
