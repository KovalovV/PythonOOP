from os import execlp
import re


class Text:
    def __init__(self, path):
        self.__path = path
        self.__text = ''
        self.__symbols = 0
        self.__words = 0
        self.__sentences = 0

    def __str__(self):
        return f'Amout of symbols in text: {self.__symbols}\nAmout of words in text: {len(self.__words)}\nAmout of sentences in text: {len(self.__sentences)}'

    def read_file(self):
        with open(self.__path, "r") as file:
            self.__text = file.read()
            self.__symbols = len(self.__text)
            self.__words = re.findall(r'[a-zA-Z-\']+', self.__text)
            self.__sentences = re.split(r'[.!?]+', self.__text)
            self.__sentences.pop()
            file.close()


def main():
    try:
        test = Text("C:/MinGW/bin/cpp/Python/2/text.txt")
        test.read_file()
        print(test)
        return 'All is good!'
    except:
        return 'Something went wrong!'

print(main())