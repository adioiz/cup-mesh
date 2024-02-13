import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev


def segment_image(img):
    """

    :param img: cup photo
    :return: cup segmentation and contours os the cup
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, threshold1=100, threshold2=200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #draw_con(contours[2], img)
    return contours, edges


def minimize_contours_points(contours):
    """

    :param contours: cup shape
    :return: less contours points for a better interpolation
    """
    unified_contours = None
    for idx, contour in enumerate(contours):
        if not idx == 2:
            if unified_contours is None:
                unified_contours = contour
            else:
                unified_contours = np.vstack((unified_contours, contour))

    idx = 0
    points = None
    while idx < len(unified_contours) - 1:
        distance = np.sqrt((unified_contours[idx + 1][0, 0] - unified_contours[idx][0, 0]) ** 2 + (
                unified_contours[idx + 1][0, 1] - unified_contours[idx][0, 1]) ** 2)
        while distance < 3 and idx < len(unified_contours) - 2:
            idx += 1
            distance = np.sqrt((unified_contours[idx + 1][0, 0] - unified_contours[idx][0, 0]) ** 2 + (
                        unified_contours[idx + 1][0, 1] - unified_contours[idx][0, 1]) ** 2)

        if points is None:
            points = unified_contours[idx]
        else:
            points = np.vstack((points, unified_contours[idx]))
        idx += 1
    return points


def interpolate_contours(points):
    """

    :param points:
    :return: spline interpolation of the points as x & y parameters
    """
    x, y = points[:, 0], points[:, 1]

    tck, u = splprep([x, y], s=1)
    unew = np.linspace(u.min(), u.max(), 1000)
    new_points = splev(unew, tck)

    return new_points[0], new_points[1]


def draw_con(contours, img):
    contour_image = img.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)

    plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB)), plt.title('Contours Drawn')
    plt.show()


def main():
    img = cv2.imread('cup.jpg')
    contours, edges = segment_image(img)
    points = minimize_contours_points(contours)
    x, y = interpolate_contours(points)

    plt.figure(figsize=(10, 5))
    plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR)), plt.title('Original image')
    plt.subplot(132), plt.imshow(cv2.cvtColor(edges, cv2.COLOR_RGB2BGR)), plt.title('cup edges')
    plt.subplot(133), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.plot(x, y, 'r-', linewidth=2), plt.title('Cup curve')
    plt.show()


