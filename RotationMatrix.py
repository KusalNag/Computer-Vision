###############
##Design the function "findRotMat" to  return 
# 1) rotMat1: a 2D numpy array which indicates the rotation matrix from xyz to XYZ 
# 2) rotMat2: a 2D numpy array which indicates the rotation matrix from XYZ to xyz 
#It is ok to add other functions if you need
###############

import numpy as np
import cv2

def findRotMat(alpha, beta, gamma):
    
    rotMat1= rotationMatrix(gamma,beta,alpha)
    rotMat2=rotationMatrix(360-alpha,360-beta,360-gamma)
    
    
    return (rotMat1,rotMat2)

def rotationMatrix(alpha,beta,gamma):
    
    #Convert degrees to radians
    a=np.pi/180*alpha
    b=np.pi/180*beta
    c=np.pi/180.*gamma
    #First rotation along z axes
    yaw1=np.array([[np.cos(a),-np.sin(a),0],[np.sin(a),np.cos(a),0],[0,0,1]])
    #second rotation along x axes 
    roll=np.array([[1,0,0],[0,np.cos(b),-np.sin(b)],[0,np.sin(b),np.cos(b)]])
    #Third rotation along z axes
    yaw2=np.array([[np.cos(c),-np.sin(c),0],[np.sin(c),np.cos(c),0],[0,0,1]])
    return np.matmul((np.matmul(yaw1,roll)),yaw2)


if __name__ == "__main__":
    alpha = 45
    beta = 30
    gamma = 60
    rotMat1, rotMat2 = findRotMat(alpha, beta, gamma)
    print(rotMat1)
    print(rotMat2)
    


