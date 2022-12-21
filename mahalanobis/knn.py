from typing import List
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


class KNNClassifier():
    __classifier = None

    def __init__(self, classes: List[List[int]], k=1) -> None:
        self.k = k
        self.classes = classes
        self.__classifier = KNeighborsClassifier(n_neighbors=k)

    def training(self, patterns: List[List[int]], classes: List[int]) -> int:
        self.__classifier.fit(patterns, classes)


if __name__ == '__main__':
    pass
