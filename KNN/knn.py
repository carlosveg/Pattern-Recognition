from typing import List
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


class KNNClassifier():
    __classes = []
    __classifier = None

    def __init__(self, classes: List[List[int]], k=1) -> None:
        self.k = k
        self.__classes = classes
        self.__classifier = KNeighborsClassifier(k)

    def training(self, patterns: List[List[int]], classes: List[int]) -> int:
        self.patterns = patterns
        self.classes = classes
        self.__classifier.fit(patterns, classes)


if __name__ == '__main__':
    pass
