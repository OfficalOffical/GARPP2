import req
import bresenham



def newFeasibleEdge(M,V):
    vY = V[req.randrange(len(V))]
    vT = req.randrange(1, M + 1)
    i = 0


    while True:
        while(i < len(V)):
            if(vT == V[i]):
                vT = req.randrange(1, M + 1)
                i=-1
                print("hololo")
            i+=1
        if(vT != vY):
            break



    vX = 1
    tempDist = 0

    tempX,tempY=req.deTransport(6,vY)
    temp1X,temp1Y=req.deTransport(6,vT)

    C = bresenham.bresenham( tempX, tempY, temp1X, temp1Y )
    TC = req.toTransport(6,C)


    for x in range( len( TC ) ):
        if (req.isFeasible( 6, vY, TC[x] )):
            if (tempDist < req.maxDist( 6, vY, TC[x] )):
                tempDist = req.maxDist( 6, vY, TC[x] )
                vX = TC[x]

    return vY,vX


