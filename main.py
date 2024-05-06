'''
Называю программу Adder - (рус. сумматор)
Содержит основные окна для работы.
'''


from PyQt5 import QtWidgets
import adder
import sys



app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = adder.Ui_Form()
ui.setupUi(window)
window.show()
sys.exit(app.exec())












