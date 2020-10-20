def thinningGuoHallIteration(img, _iter):
    rows,cols = img.shape
    marker = np.zeros((rows, cols), np.uint8)
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            p2 = img[i-1,j]
            p3 = img[i-1,j+1]
            p4 = img[i,j+1]
            p5 = img[i+1,j+1]
            p6 = img[i+1,j]
            p7 = img[i+1,j-1]
            p8 = img[i,j-1]
            p9 = img[i-1,j-1]
            C  = (np.invert(np.array(p2, dtype=np.uint8)) ^ (p3 | p4)) + (np.invert(np.array(p4, dtype=np.uint8)) ^ (p5 | p6)) + (np.invert(np.array(p6, dtype=np.uint8)) ^ (p7 | p8)) + (np.invert(np.array(p8, dtype=np.uint8)) ^ (p9 | p2))
            N1 = (p9 | p2) + (p3 | p4) + (p5 | p6) + (p7 | p8)
            N2 = (p2 | p3) + (p4 | p5) + (p6 | p7) + (p8 | p9)
            N = N1 if N1 < N2 else N2
            m = ((p6 | p7 | np.invert(np.array(p9, dtype=np.uint8))) & p8) if _iter == 0 else ((p2 | p3 | np.invert(np.array(p5, dtype=np.uint8))) & p4)
            if (C == 252 & (N >= 253 & N <= 254) ^ m == 0):
                marker[i,j] = 255
#             else:
#                 print(m)
            
    result_img = cv2.bitwise_and(img, ~marker)
            
    return result_img
    
    
    def thinningGuoHall(img):
#     ret, im = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    im = np.zeros(img.shape,np.uint8)
    prev = np.zeros(img.shape,np.uint8)
    diff = np.zeros(img.shape,np.uint8)
    
    im = img.copy()    
    done = False
    while( not done):
        im = thinningGuoHallIteration(im, 0)
        im = thinningGuoHallIteration(im, 1)
        diff = cv2.absdiff(im, prev)
        prev = im.copy()
        num = cv2.countNonZero(diff)
        if num==0:
            done = True
        
    return im
