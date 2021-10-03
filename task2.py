###############
##Design the function "calibrate" to  return 
# (1) intrinsic_params: should be a list with four elements: [f_x, f_y, o_x, o_y], where f_x and f_y is focal length, o_x and o_y is offset;
# (2) is_constant: should be bool data type. False if the intrinsic parameters differed from world coordinates. 
#                                            True if the intrinsic parameters are invariable.
#It is ok to add other functions if you need
###############
import numpy as np
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, TERM_CRITERIA_EPS, TERM_CRITERIA_MAX_ITER, \
    findChessboardCorners, cornerSubPix, drawChessboardCorners

def calculate_A(x,y,world_coordinates):
#   Retrieve X coordinates from world coordinates
    X=world_coordinates[:,0,0]
#   Retrieve Y coordinates from world coordinates
    Y=world_coordinates[:,0,1]
#   Retrieve Z coordinates from world coordinates    
    Z=world_coordinates[:,0,2]
    n=x.size
    A=[]
#   Calculating A based on preliminary 3
    for i in range(0,2*n):
        if(i%2==0):
            index=int(i/2)
            a=[X[index],Y[index],Z[index],1,0,0,0,0,-x[index]*X[index],-x[index]*Y[index],-x[index]*Z[index],-x[index]]
            A.append(a)
        else:
            index=int(i/2)
            a=[0,0,0,0,X[index],Y[index],Z[index],1,-y[index]*X[index],-y[index]*Y[index],-y[index]*Z[index],-y[index]]
            A.append(a)
    return np.array(A)

def retrieve_intrensic_paramaters(A):
#     Using SVD decomposing A into U Sigma and V.T
    l,m,V_Transpose=np.linalg.svd(A)
    M=V_Transpose[11]
    lambda_for_rot = M[8:11];
#     Calculating Lambda based on prilimnary 1
    lambda_scalar = 1/np.sqrt(lambda_for_rot[0]**2 + lambda_for_rot[1]**2 + lambda_for_rot[2]**2)
    M = lambda_scalar * M
    a=M.reshape(3,4).dot(np.array([40,0,10,1]))
# Calculating m1,m2,m3,m4 
    m1=np.array(M[0:3]).reshape(3,1)
    m2=np.array(M[4:7]).reshape(3,1)
    m3=np.array(M[8:11]).reshape(3,1)
    m4=np.array([M[3],M[7],M[11]]).reshape(3,1)
#     Calculating intrensic paramaters
    o_x=m1.T.dot(m3)[0,0]
    o_y=m2.T.dot(m3)[0,0]
    f_x=np.sqrt(m1.T.dot(m1)-np.power(o_x,2))[0,0]
    f_y=np.sqrt(m2.T.dot(m2)-np.power(o_y,2))[0,0]
    return [f_x,f_y,o_x,o_y]
    

def calibrate(imgname):
    #......
    #......
    criteria = (TERM_CRITERIA_EPS + TERM_CRITERIA_MAX_ITER, 30, 0.1)
#     reading the image 
    image=imread(imgname,1)
#     converting into grey image
    gray=cvtColor(image,COLOR_BGR2GRAY)
#     retrieving the corners
    retval, corners = findChessboardCorners(image,(9,4))
    #Manually Deleting the Z axis points from the image system
    corners=np.delete(corners,[4,13,22,31],0)
#     refining the coordinates
    corners_refined = cornerSubPix(gray,corners, (5,5), (-1,-1), criteria)
#     This commented code is used to plot the points on the image
#     print(corners_refined)
#     drawChessboardCorners(image,(8,4),corners,retval)
#     checkboard_image = line(image, (1197,845), (0, 0), (0, 255, 0), 1)
#     imshow('img',checkboard_image)
#     waitKey(1)
    
    world_coordinates=np.array([[[40,0,10]],[[30,0,10]],[[20,0,10]],[[10,0,10]],[[0,10,10]],[[0,20,10]],[[0,30,10]],[[0,40,10]],[[40,0,20]],[[30,0,20]],[[20,0,20]],[[10,0,20]],[[0,10,20]],[[0,20,20]],[[0,30,20]],[[0,40,20]],[[40,0,30]],[[30,0,30]],[[20,0,30]],[[10,0,30]],[[0,10,30]],[[0,20,30]],[[0,30,30]],[[0,40,30]],[[40,0,40]],[[30,0,40]],[[20,0,40]],[[10,0,40]],[[0,10,40]],[[0,20,40]],[[0,30,40]],[[0,40,40]]])
    x=corners_refined[:,0,0]
    y=corners_refined[:,0,1]
    A=calculate_A(x,y,world_coordinates)
    intrensic_params=retrieve_intrensic_paramaters(A)
    #translating worldcoordinates with (10,10,10)
    world_coordinates+=10
    A=calculate_A(x,y,world_coordinates)
    intrensic_params_Changes=retrieve_intrensic_paramaters(A)
    is_constant=True
    
    return intrensic_params,is_constant
          

if __name__ == "__main__":
    intrinsic_params, is_constant = calibrate('checkboard.png')
    print(intrinsic_params)
    print(is_constant)