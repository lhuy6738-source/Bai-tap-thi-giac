import matplotlib.pyplot as pit
import numpy as rp
import cv2 as cv
import numpy as np


def read_imgge_form_github(url):
    req = request.urlopen(url)
    arr = np.asanyarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecpde(arr, cv.IMREAD_COLOR)
    return img

def add_gauss_noise():
    mean = 0
    sigma = 20
    noise = np.random.normal(mean, sigma, img.shape)
    img_n = np.clip(img + noise, 0, 255).astype(np.uint8)
    return img_n

def add_peper_noise(img, amount=0.02):
    noisy = img.copy()
    num_pixels = int(amount*img.size)

    # white
    cords = [np.random.randint(0, i-1, num_pixels) fpr 1 in img.shapee]
    noisy[cords[0], cords[1]] = 255

    # black
    cords = [np.random.randint(0, i-1, num_pixels) fpr 1 in img.shapee]
    noisy[cords[0], cords[1]] = 0

    return noisy

def restore_img(img_noise):
    _img = cv.GaussianBlur(img_noise, (6,6), 0)
    return _img


if __name__=="__main__":
    #url = "https://raw.githubusercontent.com/opencv/opencv/refs/heads/4.x/samples/data/lena.jpg"
    url ="https://raw.githubusercontent.com/udacity/CarND-LaneLines-P1/master/test_images/solidWhiteCurve.jpg"
     # print(read_image_from_github(url))
    img = read_image_from_github(url)
  
    img_bw = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ed1 = cv.Canny(img, 100,200)
    h, w = ed1.shape
    mask = np.zeros_like(ed1)
    poly = np.array([[ (0,h), (w,h),(w//2+50, h//2),(w//2 - 50, h//2)]], dtype=np.int32)
    cv.fillPoly(mask, poly, 255)
    roi = cv.bitwise_and(ed1, mask)
    img2 = np.concatenate((ed1, roi), axis=1)
    cv.imshow("ROI", img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    lines = cv.HoughLinesP(roi,
                           rho=1.0,
                           theta=np.pi/180, 
                           threshold=50,
                           minLineLength=50,
                           maxLineGap=150)
    lane_img = img.copy()
    if lines is not None:
        for line in lines:
            x1,y1, x2, y2 = line[0]
            cv.line(lane_img, (x1,y1), (x2,y2), (0, 0, 255 ),2)
    cv.imshow("img2", lane_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# ed1 = cv.Canny(img, 100,200)
    # ed2 = cv.Canny(img_bw, 100, 200)
    # cbimg = np.concatenate((ed1, ed2), axis=1)
    # cv.imshow("edge",cbimg)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # cv.imshow("perfect condition",img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    # edge_img1 = cv.Canny(img, 100, 200)
    # cv.imshow("edge detection",edge_img1)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    img = read_imgge_form_github(url)
    img2 = add_gauss_noise(img)
    img3 = add_peper_noise(img)
    #combine_img = np.concatenate((img, img2), axis=1)
    #cv.imshow("combine imges",combine_img)
    #cv.imshow("peper", img3)
    img4 = restore_img(img3)
    img5 = restore_img(img2)

    cv.waiKey(0)
    cv.destroyallWindows()
    combine_img = np.concatenate((img3, img4), axis=1)
    cv.imshow("combine images",combine_img)
    cv.waitKey(0)
    cv. destroyAllWindows()


    img6 = cv.blur()
    img7 = cv.medianBlur()


    combine_img = np.concatenate((img, img3, img2, img7), axis=1)
    cv.imshow("combine images",combine_img)
    cv.waitKey(0)
    cv. destroyAllWindows()
