# AugmentedReality

## Approach

### 1. Identify keypoints and descriptors 

Used the ORB keypoint detector and descriptor to identify the object. It is based on the algorithm introduced by Ethan Rublee, Vincent Rabaud, Kurt Konolige and Gary Bradski in their 2011 paper titled "ORB: an efficient alternative to SIFT or SURF". ORB combines FAST keypoint detector and BRIEF descriptor to identify keypoints and descriptors. Their approach is based on the idea of Intensity Centroid: A corner's intensity is offset from its center and this can be used to compute orientation. In addition, they add a learning step to the BRIEF algorithm resulting in better descriptors that works better even with rotation. 

### 2. Find Matches 

Used FLANN search to find matches. This is based on the paper by Marius Muja, and David G. Lowe, titled, "Fast Approximate Nearest Neighbors with Automatic Algorithm Configuration" published in 2009. The basic premise here is to find Fast Approximate Nearest Neighbors by automatic selection of optimal algorithm based on factors like structure of dataset and required precision. 

### 3. Identify Good Matches

With the FLANN search, get a set of matches. Then used the distance ratio method from David Lowe's 2004 paper Distinctive Image Features from Scale-Invariant Keypoints, to identify the good matches and drop the bad ones. This is based on comparing distance of the closest neighbor to that of the second closest neighbor and is that is less than a predefined ration, then classify the match as good. This ratio is setup as a tuning parameter for each template and varies each scenario. 

### 4. Find homography and Do perspective transformation 

Calculated homography with the matched points. With the homography, did a perspective transform to find the final 4 points of the identified object. 

### 5. Project image on to the identified object 

With the homography identified in the previous step, and the polygon points to be replaced, did a perspective warp of the replacement image and place the image on to the video frame. 

### 6. Smooth the resulting projection

Initial results were very choppy with the replaced image flickering and moving too frequently and not smoothly. First tried to average the findings over the last n findings and replacing. While that was smooth, it did not fit exactly correctly in the image with gaps between the replacing image and replaced image. 

Set a threshold and if the quantum of change was between the upper and lower bounds of the threshold then, updated the image on the frame. Otherwise, the image was not changed. This resulted in a smoother image transition. The quantum of change was calculated as the maximum of Euclidean distance change between the points. 

### 7. Multiple Object Search

Refactored the code with classes to test how the above algorithm works on multiple object detection at the same time. Refactored code was able to find multiple images albeit with a significant performance impact of about 40% per additional image search. 

Performance Statistics
======================

Perf Run |Number  of Frames in the video|Number Of Runs|Total Number of Frames processed|Time Taken |Time per frame (ms) |Frames per second 
---------|------------------------------|--------------|--------------------------------|-----------|--------------------|-------------------- 
Run 1 - 1 Image Search|496|3|1488|80.8|54.301|18.4158
Run 2 - 1 Image Search|583|3|1749|82.46|47.1469|21.2102
Run 3 - 2 Image Search|728|3|2184|154|70.5128|14.1818


On average, for single object detection, the frame rate achievable was 20. I tried to tune the code to reduce the time, and get the frame rate up to at least 30. One approach that worked was skipping every third frame and not processing. This worked relatively smooth and provide about 30% improvement in time and helped push the average FPS to 30. 

These can be validated by running PerfTest.py

Results and Improvements
========================
![Demo1](/Demo1.gif)

![Demo2](/Demo2.gif)

There were some cases where the process was not performing well. The following are the improvement areas that I could think of: 

1. Especially with glossy objects, whose appearance changed with the lighting and the camera angle, seemed to perform worse. I also identified that the lighting of the template image affects the results esp., if the lighting in the video is different or changes. I tried to use equalized histograms of the images to detect keypoints. This improved the performance a bit, but there is still improvements to be done in this regard. 

2. I had initially tried implementing Camshift algorithm in this program. While it worked, it seemed to perform slower with lots of errors. But there should be someway to use a similar algorithm like Camshift to track the objects and limiting the amount of search to be done. 

3. Every additional search add about 40% more time required. In practical applications this will not be acceptable at all. May be a better practical application will use a machine learning algorithm to classify the type or object like book, car etc, and then we do feature detection identify the specific object. 

References
==========

1. Ethan Rublee, Vincent Rabaud, Kurt Konolige, Gary Bradski. ORB: an efficient alternative to SIFT or SURF, 2011

2. Marius Muja, David G. Lowe. Fast Approximate Nearest Neighbors with Automatic Algorithm Configuration, 2009

3. Distinctive Image Features from Scale-Invariant Keypoints David G. Lowe, 2004
