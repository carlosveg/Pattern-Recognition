import os
from typing import List
import pandas as pd
import cv2
import csv


def getImagesFromPath(path: str) -> List[str]:
    contentPath = os.listdir(
        f"{os.getcwd()}/{path}")
    # print(contentPath)
    contentPath = list(
        map(lambda item: f"{path}{item}", contentPath))

    return contentPath


def getImages(paths: List, typeOpen: int = 1) -> List:
    images = []

    for path in paths:
        images.append(cv2.imread(path, typeOpen))

    return images


def getTrainingData(images_zones: List, original_image) -> List[List[int]]:
    width, height, _ = original_image.shape
    training_data = []

    for image_index, image in enumerate(images_zones):
        for x in range(int(width*0.1), int(width*0.9)):
            for y in range(height):
                if int(image[x, y][0]) * int(original_image[x, y][0]) == 0:
                    (b, g, r) = original_image[x, y]
                    training_data.append([b, g, r, image_index + 1])

    return training_data


def writeInCsv(filename: str, headers: List[str], data: List) -> None:
    with open(filename, 'w', encoding='UTF-8', newline='') as data_file:
        writer = csv.writer(data_file)

        writer.writerow(headers)
        writer.writerows(data)


def adapterTrainingData(filename: str, X_train: any, y_train: any) -> List[List]:
    fullData = pd.read_csv(filename)
    patterns = fullData[X_train]
    classes = fullData[y_train]

    return patterns, classes


def doAll(filename: str) -> List[List]:
    images = getImages(
        ["assets/image/cielo.png", "assets/image/boscosa.png", "assets/image/suelo.png"])
    training_data = getTrainingData(
        images, cv2.imread("assets/image/3-regiones.png"))

    writeInCsv(filename, ['b', 'g', 'r', "clase"], training_data)
    data_adapted = adapterTrainingData(filename, ['b', 'g', 'r'], "clase")

    return data_adapted
