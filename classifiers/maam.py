from typing import List
import cv2
from sklearn.metrics import confusion_matrix, precision_score
from sklearn.neural_network import MLPClassifier


class MAAM():
    def __init__(self):
        self.__model = MLPClassifier(hidden_layer_sizes=(
            256, 128, 64), max_iter=200, activation="relu", solver="adam")

    def training(self, patterns: List[List], classes: List):
        self.__model.fit(patterns, classes)

    def classify(self, pattern: List):
        predict = self.__model.predict(pattern)[0]
        print(
            f"Dígito: {predict}")
        # cv2.imshow("Resultado", predict)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def estadistics(self, patterns_unknow: List[List], patterns: List[List]) -> None:
        predicts = self.__model.predict(patterns_unknow)
        matriz = confusion_matrix(predicts, patterns)
        print(f"Matriz de confusion: \n{ matriz }")
        precision = precision_score(predicts, patterns, average="macro")
        print(f"Precision score: \n{ precision * 100 }%")
