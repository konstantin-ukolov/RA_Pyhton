from PySide2.QtCore import Slot

from PySide2.QtSql import QSqlDatabase, QSqlTableModel

from PySide2.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QTableView,
    QLabel, QWidget, QPushButton,
    QFileDialog,
)

from AddEntryDialog import AddEntryDialog


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Desktop application')

        self._label = QLabel('Collection', self)

        self._open_button = QPushButton('Open')
        self._open_button.setToolTip('Choose the collection database')

        self._add_button = QPushButton('Add')
        self._add_button.setToolTip('Add a new entry into the collection')

        self._model = None
        self._view = QTableView(self)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self._label)
        horizontal_layout.addWidget(self._open_button)
        horizontal_layout.addWidget(self._add_button)

        layout = QVBoxLayout()
        layout.addLayout(horizontal_layout)
        layout.addWidget(self._view)

        self.setLayout(layout)

        self._open_button.clicked.connect(self.__open_collection)
        self._add_button.clicked.connect(self.__add_new_entry)

    @Slot()
    def __open_collection(self):
        collection = QFileDialog.getOpenFileName()[0]
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(collection)
        db.open()

        self._model = QSqlTableModel(self, db)
        self._model.setTable('objects')
        self._model.select()

        self._view.setModel(self._model)

    @Slot()
    def __add_new_entry(self):
        dialog = AddEntryDialog(self)

        if dialog.exec_() == AddEntryDialog.Accepted:
            entry = dialog.entry
            print(entry)
