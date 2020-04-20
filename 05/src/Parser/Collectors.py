from abc import abstractmethod
from collections import Counter


class AbstractCollector(object):
    @abstractmethod
    def push(self, word: str):
        pass

    @abstractmethod
    def save(self):
        pass


class PrintCollector(AbstractCollector):
    def push(self, word: str):
        print(word)

    @abstractmethod
    def save(self):
        pass


class WordCountCollector(AbstractCollector):
    def __init__(self,):
        self._filename = None
        self._ignore_case = False
        self._words = Counter()

    def configure(self, options: dict):
        self._ignore_case = options.get('ignore_case', False)
        self._filename = options['output']

    def push(self, word: str):
        self._words.update([word.lower() if self._ignore_case else word])

    def save(self):
        with open(str(self._filename), 'w') as f:
            for key, value in self._results():
                f.write(f'{key}: {value}\n')

    def _results(self):
        return reversed(sorted(self._words.items(), key=lambda x: x[1]))
