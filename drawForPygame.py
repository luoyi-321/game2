import pygame

color = {
    'skincolor':(255,203,162),
    'DskinColor':(188,152,120),
    'hair':(109,109,109),
    'hairRed':(109,100,100),
    'black':(0,0,0),
    'pinkyRed':(158,32,80),
    'shirtBody':(131,179,181),
    'Dshirtbody':(82,112,133),
    'Dblue' : (36,61,86),
    'white': (255,255,255)
    
}

def drawhead(center,window,faceSize,bodyCenter):
    # hair
    hairCenter = (center[0]-int(faceSize/2),center[1]-int(faceSize/1.5))
    
    pygame.draw.circle(window,color['hairRed'],hairCenter,int(faceSize/1.6))
    pygame.draw.circle(window,color['hairRed'],(center[0]+int(faceSize/2),hairCenter[1]),int(faceSize/1.6))
    # pygame.draw.ellipse(window,color['hairRed'],(hairCenter[0],hairCenter[1],center[0]+int(faceSize/2),hairCenter[1]))
    
     # eres
    pygame.draw.circle(window,color['pinkyRed'],(center[0]-faceSize,center[1]),int(faceSize/6))
    pygame.draw.circle(window,color['pinkyRed'],(center[0]+faceSize,center[1]),int(faceSize/6))
    
    # neck
    neckWidht = int((faceSize/2)+(faceSize/2))
    neckStartpoint = (center[0]-int(faceSize/2),center[1]+int(faceSize/2))
    neckEndpoint = bodyCenter
    
    pygame.draw.circle(window,color['white'],neckEndpoint,int(faceSize/1.4))
    pygame.draw.circle(window,color['hair'],neckEndpoint,int(faceSize/1.6))
    pygame.draw.line(window,color['skincolor'],center,neckEndpoint,neckWidht)
    ptss = [neckStartpoint, [neckStartpoint[0]+neckWidht,neckStartpoint[1]], [bodyCenter[0]-int(neckWidht/2),bodyCenter[1]]]
    pygame.draw.polygon(window,color['DskinColor'],ptss)
    
    # face
    pygame.draw.circle(window,color['skincolor'],center,faceSize)
    
    leftEye = (center[0]-int(faceSize/3),center[1]-int(faceSize/2))
    rightEye =(center[0]+int(faceSize/3),center[1]-int(faceSize/2))
    
    
    pygame.draw.circle(window,color['black'],leftEye,int(faceSize/6))
    pygame.draw.circle(window,color['black'],rightEye,int(faceSize/6))
    pygame.draw.line(window,color['black'],(rightEye[0]-int(faceSize/5),rightEye[1]-int(faceSize/5)),(rightEye[0]+int(faceSize/6),rightEye[1]-int(faceSize/6)),int(faceSize/8))
    pygame.draw.line(window,color['black'],(leftEye[0]-int(faceSize/5),leftEye[1]-int(faceSize/5)),(leftEye[0]+int(faceSize/6),leftEye[1]-int(faceSize/6)),int(faceSize/8))
    # nose
    pts = (center[0],center[1]-6),(center[0]-2,center[1]),(center[0],center[1]+2)
    pygame.draw.polygon(window,color['black'],pts)
    # # freshin
    Lfreshin = (center[0]-int(faceSize/3),center[1])
    Rfreshin = (center[0]+int(faceSize/3),center[1])
    
    pygame.draw.ellipse(window,color['pinkyRed'],(Lfreshin[0],Lfreshin[1],int(faceSize/6),int(faceSize/10)))
    pygame.draw.ellipse(window,color['pinkyRed'],(Rfreshin[0],Rfreshin[1],int(faceSize/6),int(faceSize/10)))
    # mouse
    
    contours = ((center[0]-int(faceSize/5),center[1]+int(faceSize/3)), (center[0],center[1]+int(faceSize/2)), (center[0]+int(faceSize/3),center[1]+int(faceSize/4)))
    pygame.draw.polygon(window, color['pinkyRed'], contours)
    
def drawHand(window,Rwrit,Lwrit,Relbow,Lelbow,Rshoulder,Lshoulder,handSize):
    handSize = handSize
    if handSize <= 0 :
        handSize = 2
    LhandPTS = (
        Lelbow,
        [Lwrit[0],Lwrit[1]]
    )
    RhandPTS = (
        Relbow,
        [Rwrit[0],Rwrit[1]]
    )
    
    pygame.draw.line(window,color['skincolor'],RhandPTS[0],RhandPTS[1],int(handSize*0.9))
    pygame.draw.line(window,color['skincolor'],LhandPTS[0],LhandPTS[1],int(handSize*0.9))
    
    
    LhandPTS = (
        Lshoulder,
        Lelbow,
    )
    RhandPTS = (
        Rshoulder,
        Relbow,
    )
    # pygame.draw.polylines(img = window,pts = [RhandPTS],isClosed = False,color = color['Dshirtbody'],thickness = handSize*2)    
    pygame.draw.line(window,color['Dshirtbody'],RhandPTS[0],RhandPTS[1],handSize)
    pygame.draw.line(window,color['Dshirtbody'],LhandPTS[0],LhandPTS[1],handSize)


def drawBody(Lshoulder,Rshoulder,Lhip,Rhip,facesize,window):
    pts = (Lshoulder,Rshoulder,Rhip,Lhip)
    pygame.draw.polygon(window,color['shirtBody'],pts)
    pass
def drawLeg(window,Lhip,Rhip,Rknee,Lknee,Rankle,Lankle,LegSize):
    LegsSize = LegSize
    hipSize = int(LegSize*0.9)
    if hipSize <= 0 :
        hipSize = 3
    isClose = False
    Lleg = (
        [Lhip[0],Lhip[1]+hipSize],
        Lknee,
        Lankle
    )
    Rleg = (
        [Rhip[0],Rhip[1]+hipSize],
        Rknee,
        Rankle
    )
    axesHeight  = int(Lhip[0]-Rhip[0])
    if axesHeight < 1 :
        axesHeight = 3
    pygame.draw.ellipse(window,color['Dblue'],(int(Rhip[0]),int(Rhip[1]),axesHeight,hipSize*2))
    pygame.draw.lines(window,color['Dblue'],isClose,Rleg,LegsSize)
    pygame.draw.lines(window,color['Dblue'],isClose,Lleg,LegsSize)