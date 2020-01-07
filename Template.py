import numpy as np
import cv2

class Template:
    def __init__(self, imageFile, advertFile, min_match_count, ratio):
        self.image = cv2.imread(imageFile,0) # template
        self.advert = cv2.imread(advertFile)
        self.orb = cv2.ORB_create()
        # imageBW = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        imageEqu = cv2.equalizeHist(self.image)
        self.kpTemplate, self.desTemplate = self.orb.detectAndCompute(imageEqu,None)
        # self.kpTemplate, self.desTemplate = self.orb.detectAndCompute(self.image,None)
        self.old_M = None
        self.old_dst = None
        self.skipped_count = 0
        self.MIN_MATCH_COUNT = min_match_count
        self.ratio = ratio

    def project_imageA_onto_imageB(self, imageA, imageB, homography, dst):
        warp = cv2.warpPerspective(imageA, homography, (imageB.shape[1],imageB.shape[0]))
        cv2.fillConvexPoly(imageB, dst.astype(int), 0, 16);
        imageB = imageB + warp;
        return imageB

    def distance(self, dst1, dst2):
        if dst1 is None or dst2 is None:
            return 31
        results1 = []
        for pt in dst1:
            results1.append((pt[0][0],pt[0][1]))

        results2 = []
        for pt in dst2:
            results2.append((pt[0][0],pt[0][1]))

        return max(np.linalg.norm(np.array(results1) - np.array(results2), axis=1))


    def processFrame(self, frame, frame_count):
        # if frame_count % 3 == 0:
        #     return self.project_imageA_onto_imageB(self.advert, frame, self.old_M, self.old_dst)
        frameBW = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frameEqu = cv2.equalizeHist(frameBW)
        # kpFrame, desFrame = self.orb.detectAndCompute(frame,None)
        kpFrame, desFrame = self.orb.detectAndCompute(frameEqu,None)

        FLANN_INDEX_KDTREE = 6
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(self.desTemplate,desFrame,k=2)

        good = []
        for m_n in matches:
          if len(m_n) != 2:
            continue
          (m,n) = m_n
          if m.distance < self.ratio*n.distance:
            good.append(m)

        if len(good)>self.MIN_MATCH_COUNT:
            src_pts = np.float32([ self.kpTemplate[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kpFrame[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
            matchesMask = mask.ravel().tolist()
            # print (M, matchesMask)
            h,w = self.image.shape
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            dst = cv2.perspectiveTransform(pts,M)
            max_distance = self.distance(dst, self.old_dst)
            if (max_distance > 30 and max_distance < 70) or (max_distance < 0):
                self.old_M = M
                self.old_dst = dst
                self.skipped_count = 0
            else:
                self.skipped_count += 1
            if self.skipped_count > 7:
                self.old_M = M
                self.old_dst = dst
                self.skipped_count = 0

            frame = self.project_imageA_onto_imageB(self.advert, frame, self.old_M, self.old_dst)

        else:
            # print ("Not enough matches are found - %d/%d" % (len(good),self.MIN_MATCH_COUNT))
            matchesMask = None

        return frame
