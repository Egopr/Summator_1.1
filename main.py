'''
Называю программу Adder - (рус. сумматор)
Содержит основные окна для работы.
'''

from PyQt5 import QtWidgets, uic
import sys



app = QtWidgets.QApplication(sys.argv)
windows = uic.loadUi("summator_0.1.ui")
windows.show()
sys.exit(app.exec())
