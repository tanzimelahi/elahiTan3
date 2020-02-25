
fl=open("image6.ppm","w")
initialstr="P3\n500 500\n255\n"
data=list(range(250000))
initVal=0
while(initVal<len(data)):
    data[initVal]=["0","0","0"]
    initVal+=1
def plot(x,y,color):# color is a list
    x+=250
    y=250-y
    data[x+y*500]=color

#for the first two octants, the x0 must be smaller than x1
def firstoct(x0,y0,x1,y1,color):#oct 1 and 5
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=2*A+B
    while x<x1:
        plot(x,y,color)
        if d>=0:
            y+=1
            d=d+2*B
        x=x+1
        d=d+2*A
    plot(x1,y1,color)
def secondoct(x0,y0,x1,y1,color):#oct 2 and 6
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while y<y1:
        plot(x,y,color)
        if d<=0:
            d=d+2*A
            x+=1
        y=y+1
        d=d+2*B
    plot(x1,y1,color)
def thirdoct(x0,y0,x1,y1,color):#oct 3 and 7 remember the x0 and x1 hierarchy is reversed for this one
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while y<y1:
        plot(x,y,color)
        if d>=0:
            x=x-1
            d=d-2*A
        y=y+1
        d=d+2*B
    plot(x1,y1,color)
def fourthoct(x0,y0,x1,y1,color): #oct 4 and 8
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while x<x1:
        plot(x,y,color)
        if d<=0:
            y=y-1
            d=d-2*B
        x=x+1
        d=d+2*A
    plot(x1,y1,color)
def oneSlopePos(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while x<=x1:
        plot(x,y,color)
        x+=1
        y+=1

def oneSlopeNeg(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while x<=x1:
        plot(x,y,color)
        x+=1
        y-=1
def zeroSlope(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while(x<=x1):
        plot(x,y,color)
        x+=1
def undefinedSlope(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while y<=y1:
        plot(x,y,color)
        y+=1

def drawline(x0,y0,x1,y1,color):# whenever possible x0 must be greater than x1(left to right orientation)
    if(x0==x1):
        undefinedSlope(x0,y0,x1,y1,color)
    elif(y0==y1):
        zeroSlope(x0,y0,x1,y1,color)
    elif abs(x1-x0)>=abs(y1-y0):
        if y1>y0:
            firstoct(x0,y0,x1,y1,color)
        else:
            fourthoct(x0,y0,x1,y1,color)
    else:
        if y1>y0:
            secondoct(x0,y0,x1,y1,color)
        else:
            thirdoct(x1,y1,x0,y0,color)

    

for ls in data:
    for a in ls:
       initialstr+=a+" "
    initialstr+=" "

fl.write(initialstr)
print("image6.ppm")
fl.close()

