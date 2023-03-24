import pygame
pygame.init() # 파이게임을 실행하기위한 초기화 

# 창 생성을 위한 창의 크기 조절 
screen_width = 480
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption("피하기 게임")

# 배경 불러오기 
background = pygame.image.load("C:/Users/swl/Desktop/prac/pygame/img/background.png")

# 캐릭터 만들기 
character = pygame.image.load("C:/Users/swl/Desktop/prac/pygame/img/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos =  screen_height - character_height


# 이동위치 변수 생성 
to_x = 0
speed = 0.3 
clock = pygame.time.Clock()

# 내려오는 적 
character = pygame.transform.scale(character,(60,150))

start_ticks = pygame.time.get_ticks()

running =True # 게임 진행 여부에 대한 변수 
while running :  # 근데 시발 이벤트 입력받는건 if문으로 받음 되지않나? 왜 for문으로 받지 
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #파이게임을 멈출시 종료  
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0            
    
    character_x_pos += to_x * dt
   
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
         character_x_pos = screen_width - character_width

    # 화면에 그리기 
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos)) 

    pygame.display.update()

