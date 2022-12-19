from typing import List


class KNNClassifier():
    __classes = []

    def __init__(self, classes: List[List[int]], k=1) -> None:
        self.k = k
        self.__classes = classes

    def learning(self, patterns: List[List[int]], classes: List[int]) -> int:
        self.patterns = patterns
        self.classes = classes


if __name__ == '__main__':
    pass
