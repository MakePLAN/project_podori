import pygame
import time

pygame.init()

display_width = 1024
display_height = 768
fps = 60

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
bright_red = (200, 0, 0)
green = (0, 255, 0)
bright_green = (0, 200, 0)
gray = (128, 128, 128)
bright_gray = (192, 192, 192)

scale_x = 0.45
scale_y = 0.5

car_width = 80
car_height = 160
car_start_x = 710
car_start_y = 400



sign_y = [100, 327, 554, 100, 327, 554]

wall_width = 50
midwall_width = wall_width * 2 - 20

#police car
carImg = pygame.image.load('images/police_car.png')

#battlecruiser
battleImg = pygame.image.load('images/battle_cruiser.png')


#blue car
blueImg = pygame.image.load('images/blue_car.png')

#mario kart
marioImg = pygame.image.load('images/mario_kart.png')



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption( 'A bit Racey')
clock = pygame.time.Clock() #measure frame per second

#sound
pygame.mixer.music.load("driving.mp3")
braking_sound = pygame.mixer.Sound("braking.wav")

cur_time = 0
pause = False

location_map = {}
lane_map = ["","","","","",""]
lane_y = [0,0,0,0,0,0]
lane_bool = [True, True, True, True, True, True]

car_list = ["battle_cruiser", "blue_car", "bus", "delivery_car", "mario_kart", "mcqueen_car", "truck", "police_car"]

def setup():
    global carImg,battleImg, blueImg, busImg

    #police car
    location_map["police_car"] = (80, 160, [0,0,0,0,710,0])
    carImg = pygame.transform.smoothscale(carImg, (80, 160))

    #battle cruiser
    location_map["battle_cruiser"] = (100, 160, [0,0,0,550,0,0])
    battleImg = pygame.transform.smoothscale(battleImg, (100, 160))

    #blue car
    location_map["blue_car"] = (120, 250, [0,0,0,0,0,845])
    blueImg = pygame.transform.smoothscale(blueImg, (120, 250))

    #bus
    location_map["bus"] = (100, 200, [0,0, 0, 0,0,0])


    #testing
    lane_map[3] = "battle_cruiser"
    lane_map[4] = "police_car"
    lane_map[5] = "blue_car"



    lane_y[4] = 400
    lane_bool[4] = False



def spawn_car( car_name, lane, loc_y=None, loc_x=None, angle=None): # function to spawn car
    x = location_map[car_name][2][lane]
    y = 0

    if loc_y == None:
        y = display_height + location_map[car_name][1]
        lane_y[lane] = y
    else:
        y = loc_y

    img = None
    if car_name == "police_car":
        x = loc_x
        img = carImg
        y = 400
        if angle != None:
            img = pygame.transform.rotate(img, angle)
    elif car_name == "battle_cruiser":
        img = battleImg
    elif car_name == "blue_car":
        img = blueImg


    #print(car_name, ": ", y)
    gameDisplay.blit( img, (x, y))  # blit - spawn the car


def spawn_wall():
    pygame.draw.rect(gameDisplay, gray, [0, 0, wall_width, display_height])
    pygame.draw.rect(gameDisplay, gray, [display_width - wall_width, 0, wall_width, display_height])
    pygame.draw.rect(gameDisplay, gray, [(display_width/2) - wall_width, 0, midwall_width, display_height])

def spawn_road():
    pygame.draw.rect(gameDisplay, bright_gray, [wall_width, 0, display_width - (2 * wall_width), display_height])
    pygame.draw.rect(gameDisplay, bright_gray, [wall_width, 0, display_width - (2 * wall_width), display_height])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def display_text(text, stime, duration):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects( text, largeText) # textsurf = text surface, textrect = rectange that contains the text
    TextRect.center = ((display_width / 2), (display_height / 4))
    gameDisplay.blit(TextSurf, TextRect)

    cur_time = int(time.localtime(time.time())[5])
    #print("stime: ", stime)
    #print("time: ", cur_time)
    if cur_time == 0:
        cur_time = 60
    if cur_time - duration >= stime:
        game_loop()

def things( thingx, thingy , thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def button(msg, x, y, w, h, inactive_color, active_color,action=None ):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 70)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)

def game_quit():
    pygame.quit()
    quit()

def display_speed(speed):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects("Speed: " + str(speed), largeText)
    TextRect.center = (100, 100)
    gameDisplay.blit(TextSurf, TextRect)

def game_over():
    pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)

    over = True

    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Crashed",largeText)
        TextRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(TextSurf, TextRect)

        button("Go!", 200, 450, 200, 100, green, bright_green, game_loop)
        button("Quit", 600, 450, 200, 100, red, bright_red, game_quit)


        pygame.display.update()
        clock.tick(15)

def game_unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def game_pause():

    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Paused",largeText)
        TextRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(TextSurf, TextRect)

        button("Back", 200, 450, 200, 100, green, bright_green, game_unpause)
        button("Quit", 600, 450, 200, 100, red, bright_red, game_quit)


        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Project Podori",largeText)
        TextRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 200, 450, 200, 100, green, bright_green, game_loop)
        button("Quit", 600, 450, 200, 100, red, bright_red, game_quit)


        pygame.display.update()
        clock.tick(15)

def game_loop():
    global stime, pause

    pygame.mixer.music.play(-1)
    pygame.mixer.music.pause()

    x = car_start_x
    y = car_start_y

    x_change = 0

    sign_speed = 0

    thing_startx = 300
    thing_starty = 0 - display_height
    thing_speed = 7

    thing_width = 100
    thing_height = 100

    gameExit = False
    crashed = False

    key_state = 0
    # 0 = idle
    # 1 = increasing speed
    # 2 = decreasing speed

    angle = 0

    sound_state = 0

    check = False

    while not gameExit:

        for event in pygame.event.get(): #event handling loop
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    angle += 5
                if event.key == pygame.K_RIGHT:
                    angle -= 5
                if event.key == pygame.K_UP:
                    key_state = 1
                if event.key == pygame.K_DOWN:
                    key_state = 3
                if event.key == pygame.K_p:
                    pause = True
                    game_pause()
                if event.key == pygame.K_n:
                    x_change -= 5
                if event.key == pygame.K_m:
                    x_change += 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_n or event.key == pygame.K_m:
                    x_change = 0
                if event.key == pygame.K_UP:
                    key_state = 2
            #print(event)

        if angle < 0:
            angle = 355
        elif angle > 360:
            angle = 5

        #print("angle: ", angle)

        x += x_change

        gameDisplay.fill(white)

        spawn_road()
        spawn_wall()

        # checking wall collision
        if (x > (display_width - wall_width - car_width) or x < wall_width) or (
                (display_width / 2) - wall_width <= x <= (
                display_width / 2) - wall_width + midwall_width) and not crashed:
            stime = int(time.localtime(time.time())[5])
            crashed = True

        # right road
        sign_size = 20
        sign_first = 150 + display_width / 2
        sign_second = 150 * 2 + display_width / 2
        sign_third = 150
        sign_fourth = 150 * 2


        if key_state == 1:
            sign_speed += 0.5
        if key_state == 2:
            sign_speed -= 0.25
        if key_state == 3:
            if check == True:
                pygame.mixer.Sound.play(braking_sound)
                check = False
            sign_speed -= 1
        if sign_speed < 0:
            sign_speed = 0
            key_state = 0
        #print("Speed: ", sign_speed)

        if int(sign_speed) == 0:
            pygame.mixer.music.stop()

            sound_state = 1
        else:
            if sound_state == 0:
                pygame.mixer.music.unpause()
                check = True
            else:
                pygame.mixer.music.play(-1)
                sound_state = 0

        display_speed(int(sign_speed))
        gap = 100
        #sign1_y = i * gap + ((display_height - 200) / 4) * i
        #sign2_y = i * gap + ((display_height - 200) / 4) * i

        for i in range(0, 3):
            pygame.draw.rect(gameDisplay, white, [sign_first, sign_y[i] , sign_size,
                                                  (display_height - 200) / 4])
            pygame.draw.rect(gameDisplay, white, [sign_second, sign_y[i+3], sign_size,
                                                  (display_height - 200) / 4])
            pygame.draw.rect(gameDisplay, white, [sign_third, sign_y[i], sign_size,
                                                  (display_height - 200) / 4])
            pygame.draw.rect(gameDisplay, white, [sign_fourth, sign_y[i + 3], sign_size,
                                                  (display_height - 200) / 4])

        for i in range(0, 6):
            sign_y[i] += sign_speed
            if sign_y[i] > display_height:
                sign_y[i] = 0


        #spawn police car
        spawn_car("police_car", 4, lane_y[4], x, angle ) #spawn the car



        #spawn left car
        if lane_bool[3]:
            spawn_car("battle_cruiser", 3)
            lane_bool[3] = False
        else:
            spawn_car("battle_cruiser", 3, lane_y[3])
            lane_y[3] -= 10
            if (lane_y[3] + location_map["battle_cruiser"][1]) < 0:
                lane_bool[3] = True


        #spawn right car
        if lane_bool[5]:
            spawn_car("blue_car", 5)
            lane_bool[5] = False
        else:
            spawn_car("blue_car", 5, lane_y[5])
            lane_y[5] -= 10
            if ( lane_y[5] + location_map["blue_car"][1]) < 0:
                lane_bool[5] = True


        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        if thing_starty > display_height:
            thing_starty = 0 - display_height

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx+thing_width:
                crashed = True


        if crashed:
            x_change = 0
            game_over()
            #display_text("You Crahsed", stime, 2)

        pygame.display.update()
        #update = update that one part or the entire surface
        #filp = update the entire surface always

        clock.tick(fps) #set frame per second

setup()
game_intro()
game_loop()
pygame.quit() #quit pygame
quit()
