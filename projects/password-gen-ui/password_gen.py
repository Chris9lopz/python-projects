import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("My First App")
        # Show Window
        self.show()


app = qtw.QApplication([])
mw = MainWindow()

# Run App
app.exec_()
