from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow

from CollectionsModel import CollectionsModel
from CollectionTableModel import CollectionTableModel
from ReminderApiProvider import ReminderApiProvider

from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._provider = ReminderApiProvider('http://localhost:8080')
        self._collections_model = CollectionsModel(self._provider)
        self._table_model = None

        self._ui.comboBox.setModel(self._collections_model)
        self._ui.comboBox.currentTextChanged.connect(self._set_collection)

        self._collections_model.update_model()
        self._set_collection(self._ui.comboBox.currentText())

    @Slot()
    def _set_collection(self, collection: str):
        self._table_model = CollectionTableModel(self._provider, collection)
        self._table_model.update_model()
        self._ui.tableView.setModel(self._table_model)
