import sys
import pyautogui
import webbrowser

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QGridLayout, QScrollArea

# //// GET THE SAVED CLICKING COORDS
from config import read_config
x_coord, y_coord, x_coord_center, y_coord_center, geometry_x, geometry_y, geometry_size_x, geometry_size_y = read_config()

from imageLabel import ImageLabel

image_files = ['imgs/a-1.png','imgs/b-1.png','imgs/b-2.png']  # Example list, replace with your list

from getImages import getImages

znaki = getImages('imgs/')
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )

        # Set window geometry to top-left corner
        self.setGeometry(geometry_x, geometry_y, geometry_size_x, geometry_size_y)

        self.setStyleSheet("background-color: #333333; color: #CCCCCC")

        # Create a central widget and set a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Main utility buttons ROW
        button_layout2 = QHBoxLayout()
        main_layout.addLayout(button_layout2)

        utility_buttons = ["Ist.","Proj.","MSIP","GEO", 'Serwer']
        utility_functions = {
            "MSIP": lambda: open_browser('https://msip.um.krakow.pl/kompozycje/?link=3fb9080586c6d4728333859b372acac5&config=config_plan.json'),
            "GEO": lambda: open_browser('https://mapy.geoportal.gov.pl/imap/Imgp_2.html?locale=en&gui=new&sessionID=7567238'),
            'Ist.': lambda: open_browser(''),
            'Proj.': lambda: open_browser(''),
            'Serwer': lambda: open_browser(''),
        }

        for utility in utility_buttons:
            button = QPushButton(utility)
            button.clicked.connect(utility_functions[utility])
            button_layout2.addWidget(button)

        def open_browser(website):
            webbrowser.open(website)
            

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        button_texts = ["A", "B", "C", "D", "E", "F", "Linie", "Inne"]
        button_functions = {
            "A": lambda: on_button_a_clicked(grid_layout, znaki['a']),
            "B": lambda: on_button_a_clicked(grid_layout, znaki['b']),
            "C": lambda: on_button_a_clicked(grid_layout, 'C'),
            "D": lambda: on_button_a_clicked(grid_layout, 'D'),
            "E": lambda: on_button_a_clicked(grid_layout, 'E'),
            "F": lambda: on_button_a_clicked(grid_layout, 'F'),
            "Linie": lambda: on_button_a_clicked(grid_layout, 'Linie'),
            "Inne": lambda: on_button_a_clicked(grid_layout, 'Inne')
        }

        for text in button_texts:
            button = QPushButton(text)
            button.clicked.connect(button_functions[text])
            button_layout.addWidget(button)


        def on_button_a_clicked(grid_layout, buttonType):
            print(buttonType)
            self.clear_scroll_area(grid_layout)
            self.populate_scroll_area(buttonType, grid_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Allow scroll area to resize with its contents
        
        main_layout.addWidget(scroll_area)
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        scroll_layout = QVBoxLayout(scroll_widget)
        grid_layout = QGridLayout()
        scroll_layout.addLayout(grid_layout)

        quit_layout = QHBoxLayout()
        quit_button = QPushButton("Wyjdź")
        quit_button.clicked.connect(self.close)
        quit_layout.addWidget(quit_button)
        main_layout.addLayout(quit_layout)

        self.setMinimumSize(100, 150)

    def on_image_clicked(self, filename):
        filename_no_extension = filename.replace('imgs/', '').replace('.png', '')
        pyautogui.click(x=x_coord, y=y_coord)
        pyautogui.click(x=x_coord, y=y_coord)
        pyautogui.hotkey('ctrl', '3')
        pyautogui.press('backspace')
        pyautogui.typewrite(filename_no_extension)
        pyautogui.press('enter')
        pyautogui.moveTo(x_coord_center, y_coord_center)

    def clear_scroll_area(self, scroll_layout):
        while scroll_layout.count():
            item = scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def populate_scroll_area(self, newZnaki, grid_layout):
        row = 0
        col = 0
        for file_name in newZnaki:
            filename_no_extension = file_name.replace('imgs/', '').replace('.png', '')
            name_label = QLabel(filename_no_extension)
            name_label.setAlignment(QtCore.Qt.AlignCenter)
            image_label = ImageLabel(file_name)

            pixmap = QtGui.QPixmap(file_name)
            image_label.setPixmap(pixmap.scaled(80, 80, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation))

            grid_layout.addWidget(name_label, row, col, alignment=QtCore.Qt.AlignCenter)
            grid_layout.addWidget(image_label, row + 1, col, alignment=QtCore.Qt.AlignCenter)
            grid_layout.setVerticalSpacing(5)

            col += 1
            if col == 4:
                col = 0
                row += 2

            image_label.clicked.connect(self.on_image_clicked)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    sys.exit(app.exec_())
