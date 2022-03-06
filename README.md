This repository contains projects related to computer vision and image processing.

**Sift Keypoint Detection and Panorama Creation-**
Python version - 3.4.2.17
Avg Running time: 30 sec

Method 1- keypoints_and_descriptors(image)

This method is used to retrieve the key points and the descriptors from the left and right images.
It returns the key points and the descriptors.

Method 2- calculate_knn(left_des,right_des)

This method is used to calculate 2 nearest neighbors taking the left and right descriptors.
It takes the descriptors from method 1 as input. 
This method returns a map of left indeces and right indeces and a list of the descriptors mapping

Method 3 - calculate_cross_check(knn_left,knn_right)

This method is used to calculate the crosscheck. It takes the map returned by method 2 as input and retrieves the descreptors and calculates cross_check based on the values.

Method 4 - calculate_ratio_testing_array(knn_left,vals_left,threshhold,left_img_kp,right_img_kp):

This method is used to calculate ratio testing based on threshold. It discards the pairs which do not have the distance criterion.
It returns the list of left and right keypoints which can be used to find the homography.

Method 5 -
calculate_homography_using_ransac_new(key_points_left,key_points_right)

This method is used to calculate the homography matrix using ransac problem. 
The parameters used are 
•	K = 5000 iterations
•	N= 4 number of random points
•	T =5 test residual distance
Method 6- calculate_homography(lpoints,rpoints)

This method takes random points and calculates the homography using singular value decomposition.
This method returns the final homography based on the best set which is calculated based on inliers received by RANSAC method.

After receiving the homography matrix the right image is transformed using cv2.perspectiveTransform() and the corners are extracted and the homography matrix is translated.
Wrap perspective is used to wrap the right image and left image is pasted at the beginning of the right image.

The wraped image is our output.


