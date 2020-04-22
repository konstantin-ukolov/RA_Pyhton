from PySide2.QtCore import (
    Slot, Qt,
    QAbstractListModel, QModelIndex,
)

from ReminderApiProvider import ReminderApiProvider


class CollectionsModel(QAbstractListModel):
    def __init__(self, provider, parent=None):
        super().__init__(parent)
        self._api: ReminderApiProvider = provider
        self._collections = list()

        self.update_model()

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self._collections)

    def data(self, index, role=Qt.DisplayRole):
        return self._collections[index.row()] \
            if role == Qt.DisplayRole and index.row() < self.rowCount() else None

    @Slot()
    def update_model(self):
        collections = self._api.get_collections()

        if collections != self._collections:
            self.beginResetModel()
            self._collections = collections
            self.endResetModel()
