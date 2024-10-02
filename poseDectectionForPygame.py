
import matplotlib.pyplot as plt
import mediapipe as mp
from drawForPygame import drawBody,drawHand,drawhead,drawLeg
import cv2

mp_pose = mp.solutions.pose
pose_video = mp_pose.Pose(static_image_mode = False, model_complexity = 1,min_detection_confidence=0.7)

def getcoordimate(obj,image):
    x = int(obj.x * image[0])
    y = int(obj.y * image[1])
    return x, y

def detectPose(image,window, pose = pose_video, draw=False, display=False,headPosition =[0,0]):
    height,width,_ = image.shape
    
    window = window
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(imageRGB)
    if results.pose_landmarks and draw:
        nose = results.pose_landmarks.landmark[0]
        noseCenter = (getcoordimate(nose,(width,height)))
        # print(noseCenter)
        
        Lshoulder = (getcoordimate(results.pose_landmarks.landmark[11],(width,height)))
        Rshoulder = (getcoordimate(results.pose_landmarks.landmark[12],(width,height)))
        Rwrit = (getcoordimate(results.pose_landmarks.landmark[16],(width,height)))
        Lwrit = (getcoordimate(results.pose_landmarks.landmark[15],(width,height)))
        Relbow = (getcoordimate(results.pose_landmarks.landmark[14],(width,height)))
        Lelbow = (getcoordimate(results.pose_landmarks.landmark[13],(width,height)))
        
        Lhip = (getcoordimate(results.pose_landmarks.landmark[23],(width,height)))
        Rhip= (getcoordimate(results.pose_landmarks.landmark[24],(width,height)))
        # print(Lshoulder)
        Lknee = (getcoordimate(results.pose_landmarks.landmark[25],(width,height)))
        Rknee = (getcoordimate(results.pose_landmarks.landmark[26],(width,height)))
        
        Lankle = (getcoordimate(results.pose_landmarks.landmark[27],(width,height)))
        Rankle = (getcoordimate(results.pose_landmarks.landmark[28],(width,height)))
        # leftEye = results.pose_landmarks.landmark[2]
        # rightEye = results.pose_landmarks.landmark[5]
        leftEre = results.pose_landmarks.landmark[7]
        rightEre = results.pose_landmarks.landmark[8]
        
        facesize1 = int((leftEre.x*width)-((nose.x*width)))
        facesize= int(((nose.x*width))-(rightEre.x*width))
        if facesize+20 < facesize1:
            facesize=facesize1
        if facesize <= 0 :
            facesize = 10
        # print(facesize)
        headPosition = (noseCenter[0]+facesize,noseCenter[1]+facesize)
        # hair
        bodyCenter = (int((Lshoulder[0]+Rshoulder[0])/2),int((Lshoulder[1]+Rshoulder[1])/2))
        if int(facesize/2) < 1 :
            facesize = 4
        drawLeg(window,Lhip,Rhip,Rknee,Lknee,Rankle,Lankle,facesize)
        drawBody(Lshoulder,Rshoulder,Lhip,Rhip,facesize,window)
        drawhead(noseCenter,window,facesize,bodyCenter)
        drawHand(window,Rwrit,Lwrit,Relbow,Lelbow,Rshoulder,Lshoulder,facesize)
    if display:
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title('Original Image');plt.axis('off')
        plt.subplot(122);plt.imshow(window[:,:,::-1]);plt.title('Output Image');plt.axis('off')
    else:
        return headPosition
    
