import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from main_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        self.comboBox.addItems([item[0] for item in cur.execute("SELECT type FROM coffee").fetchall()])
        self.pushButton.clicked.connect(self.run)

    def run(self):
        cur = self.con.cursor()
        result = cur.execute(f"""SELECT * FROM coffee WHERE id = {self.comboBox.currentIndex() + 1}""").fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))



def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
