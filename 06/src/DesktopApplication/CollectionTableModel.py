from PySide2.QtCore import (
    Slot, Qt,
    QAbstractTableModel, QModelIndex,
    QTimer,
)

from ReminderApiProvider import ReminderApiProvider


class CollectionTableModel(QAbstractTableModel):
    __update_timeout = 10_000
    __columns = ['original', 'translation', 'transcription']

    def __init__(self, provider, collection, parent=None):
        super().__init__(parent)
        self._api: ReminderApiProvider = provider
        self._collection = collection
        self._objects = list()
        self._timer = QTimer(self)

        self._timer.timeout.connect(self.update_model)

        self._timer.start(self.__update_timeout)
        self.update_model()

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.__columns)

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self._objects)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row, column = index.row(), index.column()

            if row < self.rowCount() and column < self.columnCount():
                return self.__get_display_data(row, column)

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        return self.__columns[section] \
                if orientation == Qt.Horizontal and role == Qt.DisplayRole \
                else None

    def object(self, row):
        return self._objects[row]

    @Slot()
    def update_model(self):
        objects = self._api.get_objects(self._collection)

        if objects != self._objects:
            self.beginResetModel()
            self._objects = objects
            self.endResetModel()

    def __get_display_data(self, row: int, column: int) -> str:
        try:
            return self._objects[row][self.__columns[column]]
        except KeyError:
            return 'NULL'
