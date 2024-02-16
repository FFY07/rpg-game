import pygame

pygame.display.set_caption("Testing menu for character creation")
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((1280, 720))

cx = 1280 // 2
cy = 720 // 2

run = True

rect_list = []

def create_rect(start_x, start_y, start_width, start_height, offset):
    for _ in range(3):
        rect = pygame.Rect(start_x, start_y, start_width, start_height)
        rect_list.append(rect)
        start_y += offset

create_rect(57, 100, 853, 143, 213)
    
while run:

    pygame.display.update()
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    for rect in rect_list:
        pygame.draw.rect(screen, (255, 255, 255), rect, 3)
        print(f"topleft:{rect.topleft} | width: {rect.width} Height: {rect.height}")

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                for rect in rect_list:
                    rect.top -= 1
                
            if event.key == pygame.K_a:
                for rect in rect_list:
                    rect.left -= 1
                
            if event.key == pygame.K_s:
                for rect in rect_list:
                    rect.top += 1
                
            if event.key == pygame.K_d:
                for rect in rect_list:
                    rect.left += 1

            if event.key == pygame.K_UP:
                for rect in rect_list:
                    rect.height -= 1

            if event.key == pygame.K_LEFT:
                for rect in rect_list:
                    rect.width -= 1
                    
            if event.key == pygame.K_DOWN:
                for rect in rect_list:
                    rect.height += 1
                    
            if event.key == pygame.K_RIGHT:
                for rect in rect_list:
                    rect.width += 1
        
        if event.type == pygame.QUIT:
                run = False

pygame.quit()



        