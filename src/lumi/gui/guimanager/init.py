import sys

from PyQt5 import QtWidgets
from guimanager.core import Ui_Dialog
from guimanager.eventhandler import GUIEventHandler

class ApplicationWindow(QtWidgets.QWidget, Ui_Dialog, GUIEventHandler):
    
    def _construct_qapplication(self):
        self.app = QtWidgets.QApplication(sys.argv)

    def _setup_ui(self):
        self.setup_ui_dialog()  
        for index, tabname in enumerate(['tab', 'tabddd']):
            self.setup_tab_structure_with_index_and_name(index, tabname)
        self.set_buddies()   
        self.retranslate_ui_dialog()

    def __init__(self):
        self._construct_qapplication()
        super(ApplicationWindow, self).__init__()

        self._setup_ui()
        self.route_callbacks_to_objects()
    
    def run(self):
        self.show()
        sys.exit(self.app.exec_())