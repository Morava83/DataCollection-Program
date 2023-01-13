# Simple Video Player and Questionaire Program for conducting research at Western University 
# July 13th, 2022
# By: Brian Morava  

from pyvidplayer import Video
import pygame, sys
from button import Button

responses = []
increment = 0
white = (255, 255, 255)
red = (255,0,0)
black = (0,0,0)

X = 1150
Y = 700

vid = Video("video.mp4")
vid.toggle_pause()
vid.set_size((X,Y))

pygame.init()
SCREEN = pygame.display.set_mode((X,Y))
pygame.display.set_caption('')

def question():
    
    font = pygame.font.Font('freesansbold.ttf', 22)
    
    #Question
    text = font.render('Which of the following responses best characterizes your mental state just before this section appeared?', True, red, black)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 4 - 100)

    #Option1 
    option1 = Button(image = None, pos=(X//2,325 - 165), text_input = "(1) Completely on task", font=pygame.font.Font('freesansbold.ttf', 25), base_color= "White", hovering_color="Green")
    #Option2 
    option2 = Button(image = None, pos=(X//2,450 - 165), text_input = "(2) Mostly  on task", font=pygame.font.Font('freesansbold.ttf', 25), base_color= "White", hovering_color="Green")
    #Option3
    option3 = Button(image = None, pos=(X//2,575 - 165), text_input = "(3) Both on task and on unrelated concerns", font=pygame.font.Font('freesansbold.ttf', 25), base_color= "White", hovering_color="Green")
    #Option4
    option4 = Button(image = None, pos=(X//2,535), text_input = "(4) Mostly on unrelated concerns", font=pygame.font.Font('freesansbold.ttf', 25), base_color= "White", hovering_color="Green")
    #Option5
    option5 = Button(image = None, pos=(X//2,660), text_input = "(5) Completely on unrelated concerns", font=pygame.font.Font('freesansbold.ttf', 25), base_color= "White", hovering_color="Green")
    
    while True:
        
        SCREEN.fill("black")
        MOUSE_POS = pygame.mouse.get_pos()
    
        SCREEN.blit(text,textRect)

        for button in [option1, option2, option3, option4, option5]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if option1.checkForInput(MOUSE_POS):
                    responses.append("Completely on task")
                    replayVid()
                elif option2.checkForInput(MOUSE_POS):
                    responses.append("Mostly  on task")
                    replayVid()
                elif option3.checkForInput(MOUSE_POS):
                    responses.append("Both on task and on unrelated concerns")
                    replayVid()
                elif option4.checkForInput(MOUSE_POS):
                    responses.append("Mostly on unrelated concerns")
                    replayVid()
                elif option5.checkForInput(MOUSE_POS):
                    responses.append("Completely on unrelated concerns")
                    replayVid()

        pygame.display.update()

def replayVid():
    global increment

    if increment >= (13.332*60):#change increment - 13.332
        
        font = pygame.font.Font('freesansbold.ttf', 32)
    
        #Response1
        response1 = font.render("Response #1: " + responses[0], True, white, black)
        response1Rect = response1.get_rect()
        response1Rect.center = (X // 2, 150)

        #Response2
        response2 = font.render("Response #2: " + responses[1], True, white, black)
        response2Rect = response2.get_rect()
        response2Rect.center = (X // 2, 350)

        #Response3
        response3 = font.render("Response #3: " + responses[2], True, white, black)
        response3Rect = response3.get_rect()
        response3Rect.center = (X // 2, 550)
        
        while True:
            vid.draw(SCREEN,(0,0))
            pygame.display.update()

            while True:
                SCREEN.fill("black")
                SCREEN.blit(response1,response1Rect)
                SCREEN.blit(response2,response2Rect)
                SCREEN.blit(response3,response3Rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
        

    else:
        isToggleOn = False
        vid.toggle_pause()#restart
        while True:
            vid.draw(SCREEN,(0,0))
            pygame.display.update()

            if (vid.get_pos() >= (13.332*60) + increment and not isToggleOn):#change time - 13.332
                    vid.toggle_pause()#stop for question
                    isToggleOn = True
                    increment += (6.666*60)#change time-6.666
                    question()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        

def playVideo():
    isToggleOn = False
    while True:
        vid.draw(SCREEN,(0,0))
        pygame.display.update()

        if (vid.get_pos() >= (6.666*60) and not isToggleOn):#change time - 6.666
            vid.toggle_pause()#stop for question 
            isToggleOn = True
            question()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def homeScreen():
    #Start Button 
    start = Button(image = None, pos=(X//2,Y//2), text_input = "START", font=pygame.font.Font('freesansbold.ttf', 40), base_color= "White", hovering_color="Green")

    while True:
        SCREEN.fill("black")
        MOUSE_POS = pygame.mouse.get_pos()

        start.changeColor(MOUSE_POS)
        start.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start.checkForInput(MOUSE_POS):
                    vid.toggle_pause()
                    playVideo()

        pygame.display.update()

homeScreen()