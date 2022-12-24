from typing import List
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, precision_score


class KNNClassifier():
    __classifier = None

    def __init__(self, k=1) -> None:
        self.__classifier = KNeighborsClassifier(n_neighbors=k)

    def training(self, patterns: List[List[int]], classes: List[int]) -> int:
        self.__classifier.fit(patterns, classes)

    def classify(self, pattern: List[List]) -> None:
        print(
            f"El patron {pattern[0][::-1]} pertenece a la clase {self.__classifier.predict(pattern)[0]}")

    def estadistics(self, patterns_unknow: List[List], patterns: List[List]) -> None:
        predicts = self.__classifier.predict(patterns_unknow)
        matriz = confusion_matrix(predicts, patterns)
        print(f"Matriz de confusion: \n{ matriz }")
        precision = precision_score(predicts, patterns, average="macro")
        print(f"Precision score: \n{ precision * 100 }%")
