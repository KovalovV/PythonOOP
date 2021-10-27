from os import execlp
import re


class Text:
    def __init__(self, path):
        self.__path = path
        self.__text = ''

    def __str__(self):
        return f'Amout of symbols in text: {self.__symbols}\nAmout of words in text: {len(self.__words)}\nAmout of sentences in text: {len(self.__sentences)}'

    def reading(self):
        self.__text = ''
        with open(self.__path, "r") as file:
            self.__text = file.read()

    def read__symbols(self):
        if not len(self.__text):
            self.reading()
        self.__symbols = len(self.__text)

    def read__words(self):
        if not len(self.__text):
            self.reading()
        self.__words = re.findall(r'[a-zA-Z-\']+', self.__text)

    def read__sentences(self):
        if not len(self.__text):
            self.reading()
        self.__sentences = re.split(r'[.!?]+', self.__text)
        self.__sentences.pop()


def main():
    try:
        test = Text("C:/MinGW/bin/cpp/Python/2/text.txt")
        test.read__symbols()
        test.read__words()
        test.read__sentences()
        print(test)
        return ' #All is good!'
    except OSError:
        return ' #Problem with opening file!'

print(main())
