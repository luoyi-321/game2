import pygame
import os
import mediapipe as mp
import random 
import speech_recognition as sr
import cv2
from poseDectectionForPygame import detectPose
import math
import time



# pygame 
pygame.init()
WIDTH , HEIGHT = 1080 , 780
COLOR = {"RED_COLOR":(255,0,0),
         "WHITE_COLOR":(255,255,255)}
screen = pygame.display.set_mode((WIDTH , HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join("sniperGme","pic","pic","BG.jpg"),),(WIDTH,HEIGHT))
scoop = pygame.image.load("sniperGme\pic\pic\scope.png")
scoop = pygame.transform.scale(scoop,(scoop.get_width()/4,scoop.get_height()/4))
main_font = pygame.font.SysFont("Courier Regular",50)
title_font = pygame.font.SysFont("Courier Regular",30)
score = 2
bg = cv2.imread("sniperGme\pic\pic\scope.png")
bg = cv2.resize(bg,(WIDTH,HEIGHT))
# mediapipe
mp_pose = mp.solutions.pose
pose_image = mp_pose.Pose(static_image_mode = True,min_detection_confidence=0.5, model_complexity = 1)
pose_video = mp_pose.Pose(static_image_mode = True,min_detection_confidence=0.7, model_complexity = 1)
mp_drawing = mp.solutions.drawing_utils

def getcoordimate(obj,image):
    x = int(obj.x * image[0])
    y = int(obj.y * image[1])
    return x, y

# def detectPose(image, pose,window):
#     imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = pose.process(imageRGB)
#     landmarks = results.pose_landmarks
#     pos = []
#     # pos = landmarks.landmark[mp_pose.PoseLandmark.NOSE]
#     if landmarks:
#         for Lmark in mp_pose.PoseLandmark:
#             partBody = landmarks.landmark[Lmark]
#             pos.append((partBody.x*WIDTH,partBody.y*HEIGHT))
#             pygame.draw.circle(window,(255,222,196),(partBody.x*WIDTH,partBody.y*HEIGHT),10)
#         R_wirt = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
#         R_pinky = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        
#         pygame.draw.line(window,(255,222,0),(R_wirt.x*WIDTH,R_wirt.y*HEIGHT),(R_pinky.x*WIDTH,R_pinky.y*HEIGHT),3)
def distance(pointOne:list,pointTwo:list):
    return math.dist(pointOne,pointTwo)

 
def coolision(point1,point2):
    if distance(point1,point2) < 60:
        return True
    return False       

class Scoop:
    def __init__(self,position):
        self.position = position
        self.state = False
        self.img = pygame.image.load("sniperGme\pic\pic\scope.png")
        
        self.mask = pygame.mask.from_surface(self.img)
    def draw(self,window):
        scoop = pygame.transform.scale(self.img,(self.img.get_width()/4,self.img.get_height()/4))
        window.blit(scoop,self.position)
    def changPosition(self):
        self.position = random.choice([(300,300),(400,200),(500,300),(400,600)])
    def Shoot(self,headPosition):
        isHit = False
        if coolision(self.position,headPosition):
            isHit = True
        self.img = pygame.image.load("sniperGme\pic\pic\shooted.png")
        return isHit
        
        
class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,window):
        pygame.draw.rect(window,COLOR["RED_COLOR"],(self.x-40,self.y,20,50))
        pygame.draw.polygon(window,COLOR["RED_COLOR"],((self.x-40,self.y-5),(self.x-30,self.y-40),(self.x-20,self.y-5)))
        

run = True

vidio = cv2.VideoCapture(0)

live_Label = main_font.render(f"SCORE: {score}",1,COLOR["RED_COLOR"])
def main():
    # speech reconition
    # r = sr.Recognizer()
    #             #启用麦克风
    # mic = sr.Microphone()
    FPS = 60
    run = True
    bullets = []
    for i in range(3):
        position = random.choice([(300,300),(400,200),(500,300),(400,600)])
        bullet = Bullet(WIDTH-(30*i),50)
        bullet.scoop = Scoop(position)
        bullets.append(bullet)
    clock = pygame.time.Clock()
    count = 0
    while run:
        headPosition:list
        clock.tick(FPS)
        
        
        # print(count)   
        # with mic as source:
    #降噪
            # r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            # print("wo:",r.recognize_sphinx(audio))
            
        # key Event
        # print(results)
        # if scoopStop:
            # bullets.remove(bullet)
        
        currentBullet =  bullets[0]
        if count == 100 and not currentBullet.scoop.state:
            currentBullet.scoop.changPosition()
            count = 0
        
        # frame = cv2.transpose(frame)
        # frame = cv2.flip(frame)
        # frame = pygame.surfarray.make_surface(frame)
        screen.blit(BG,(0,0))
        res ,frame = vidio.read()
        frame = cv2.flip(frame,1)
        frame =  cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if res:
            headPosition  = detectPose(frame,screen,draw=True)
            print(headPosition)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    currentBullet.scoop.Shoot(headPosition)
                    bullets.remove(currentBullet)
                    currentBullet.scoop.draw(screen)
                    time.sleep(5)
                    currentBullet.scoop.state = True
                    if len(bullets) <= 0:
                        run = False
        currentBullet.scoop.draw(screen)
        screen.blit(live_Label,(50,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for bullet in bullets:
            bullet.draw(screen)    
        pygame.display.update()
        count += 1
        

def main_menu():
    run = True
    while run:
        screen.blit(BG,(0,0))
        
        title_label = title_font.render("Press the Mouse to begin...", 1,COLOR["WHITE_COLOR"])
        screen.blit(title_label,(WIDTH/2 - title_label.get_width()/2,350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()
if __name__ == '__main__':
    main_menu()