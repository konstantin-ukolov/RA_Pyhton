from enum import Enum


class Error(Enum):
    INVALID_METHOD_PARAMS = 1
    INVALID_TIME_PERIOD = 2
    SOURCE_IS_NOT_READY = 3
    UNKNOWN_SOURCE = 4
    UNKNOWN_MODEL = 5
    UNKNOWN_ERROR = 6


class AnalyzerError(Exception):
    def __init__(self, error_code=Error.UNKNOWN_ERROR):
        self._error_code = error_code

    @property
    def error_code(self) -> Error:
        return self._error_code

    @property
    def details(self) -> dict:
        return {}


class InvalidMethodParameter(AnalyzerError):
    def __init__(self, param):
        super().__init__(Error.INVALID_METHOD_PARAMS)
        self._param = param

    @property
    def details(self) -> dict:
        return {
            'required param': self._param
        }


class InvalidTimePeriod(AnalyzerError):
    def __init__(self, begin, end):
        super().__init__(Error.INVALID_TIME_PERIOD)
        self._begin = begin
        self._end = end

    @property
    def details(self) -> dict:
        return {
            'begin': self._begin,
            'end': self._end,
        }


class DataSourceIsNotReady(AnalyzerError):
    def __init__(self, source):
        super().__init__(Error.SOURCE_IS_NOT_READY)
        self._source = source

    @property
    def details(self) -> dict:
        return {
            'source': self._source
        }


class UnknownDataSource(AnalyzerError):
    def __init__(self, source):
        super().__init__(Error.UNKNOWN_SOURCE)
        self._source = source

    @property
    def details(self) -> dict:
        return {
            'source': self._source
        }


class UnknownModel(AnalyzerError):
    def __init__(self, model):
        super().__init__(Error.UNKNOWN_MODEL)
        self._model = model

    @property
    def details(self) -> dict:
        return {
            'model': self._model
        }