#!/usr/bin/env python3

import os
import random
import cv2
import numpy as np

def motionBlur(image, degree = 60, angle = 135):
    image = np.array(image)

    # 这里生成任意角度的运动模糊kernel的矩阵，degree越大，模糊程度越高
    M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
    motion_blur_kernel = np.diag(np.ones(degree))
    motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))

    motion_blur_kernel = motion_blur_kernel / degree
    blurred = cv2.filter2D(image, -1, motion_blur_kernel)

    # Convert to uint8
    cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
    return np.array(blurred, dtype = np.uint8)

def shiftImage(img, topPosition, resolution):
    M = np.float32([[1, 0, 0],[0, 1, topPosition]])
    return cv2.warpAffine(img, M, resolution)

def addImage(img1, img2, height, ratio, shift):
    dst = img1.copy()
    thresholdL = int(height * ratio)
    thresholdH = int(height * ratio + shift)
    for i in range(thresholdL):
        dst[i] = img2[i]
    for i in range(thresholdL, thresholdH):
        alpha = (thresholdH - i) / shift
        beta = (i - thresholdL) / shift
        dst[i] = img2[i] * alpha + img1[i] * beta
    return dst.astype(np.uint8)

if __name__ == "__main__":
    folder = input("请输入图片所在文件夹") or "src"
    fps = int(input("请输入视频帧率") or 24)
    fpp = int(input("请输入每张图片持续的帧数") or 3)
    width = int(input("请输入视频横向分辨率") or 1920)
    height = int(input("请输入视频纵向分辨率") or 1080)
    resolution = (width, height)
    shift = height / (fpp + 1) / 2

    imgArray = os.listdir(folder)
    random.shuffle(imgArray)
    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    videoWriter = cv2.VideoWriter("save.mp4", fourcc, fps, resolution)
    back = np.zeros((height, width, 3), np.uint8)

    for i, img in enumerate(imgArray):
        temp = cv2.imread(os.path.join(folder, img))
        if not isinstance(temp, np.ndarray):
            print("Failed to read:", img)
            continue
        h, w, _ = temp.shape
        if h / w > height / width:
            H = int(h * width / w) # Fit width
            resized = cv2.resize(temp, (width, H), interpolation = cv2.INTER_AREA)
            delta = int((H - height) / 2)
            cropped = resized[delta:delta + height, :]
        else:
            W = int(w * height / h) # Fit height
            resized = cv2.resize(temp, (W, height), interpolation = cv2.INTER_AREA)
            delta = int((W - width) / 2)
            cropped = resized[: , delta:delta + width]

        print("Frame", i, "of", len(imgArray), "start")
        videoWriter.write(back)
        for j in range(fpp - 1):
            ratio = (j + 1) / fpp
            front_blur = motionBlur(cropped, int(60 * (1 - ratio)))
            front = shiftImage(front_blur, (ratio - 1) * height + shift, resolution)
            print(str(int(ratio * 100)) + "%")
            videoWriter.write(addImage(back, front, height, ratio, shift))
        back = cropped

    videoWriter.write(back)
    videoWriter.release()
