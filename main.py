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

znaki_a = ['imgs/a-1.png','imgs/a-2.png','imgs/a-3.png','imgs/a-4.png','imgs/a-5.png','imgs/a-6a.png','imgs/a-6b.png','imgs/a-6b.png','imgs/a-6c.png','imgs/a-6d.png','imgs/a-6e.png','imgs/a-7.png','imgs/a-8.png','imgs/a-9.png','imgs/a-10.png','imgs/a-11.png','imgs/a-11a.png','imgs/a-12.png','imgs/a-12b.png','imgs/a-12c.png','imgs/a-13.png','imgs/a-14.png','imgs/a-15.png','imgs/a-16.png','imgs/a-17.png','imgs/a-18a.png','imgs/a-18b.png','imgs/a-19.png','imgs/a-20.png','imgs/a-21.png','imgs/a-22.png','imgs/a-23.png','imgs/a-24.png','imgs/a-25.png','imgs/a-26.png','imgs/a-27.png','imgs/a-28.png','imgs/a-29.png','imgs/a-30.png','imgs/a-31.png','imgs/a-32.png','imgs/a-33.png','imgs/a-34.png',]
znaki_b = ['imgs/b-1.png','imgs/b-2.png']


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

        # Create a central widget and set a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        button_layout2 = QHBoxLayout()
        main_layout.addLayout(button_layout2)

        button_1 = QPushButton("Ist.")
        button_2 = QPushButton("Proj.")
        button_3 = QPushButton("MSIP")
        button_4 = QPushButton("GEO")
        button_layout2.addWidget(button_1)
        button_layout2.addWidget(button_2)
        button_layout2.addWidget(button_3)
        button_layout2.addWidget(button_4)

        button_3.clicked.connect(lambda: open_browser('MSIP'))
        button_4.clicked.connect(lambda: open_browser('GEO'))

        def open_browser(website):
            switcher = {
                'MSIP': 'https://msip.um.krakow.pl/kompozycje/?link=3fb9080586c6d4728333859b372acac5&config=config_plan.json',
                'GEO': 'https://mapy.geoportal.gov.pl/imap/Imgp_2.html?locale=en&gui=new&sessionID=7567238',
            }

            link = switcher.get(website)
            webbrowser.open(link)
            

        # Create a layout for buttons and add them to the main layout
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        # Add buttons 'A', 'B', 'C' to the button layout
        button_a = QPushButton("A")
        button_b = QPushButton("B")
        button_c = QPushButton("C")
        button_d = QPushButton("D")
        button_e = QPushButton("E")
        button_f = QPushButton("F")
        button_g = QPushButton("Linie")
        button_h = QPushButton("Inne")

        button_a.clicked.connect(lambda: on_button_a_clicked(grid_layout, 'A'))
        button_b.clicked.connect(lambda: on_button_a_clicked(grid_layout, 'B'))

        def on_button_a_clicked(grid_layout, newZnaki):
            self.clear_scroll_area(grid_layout)
            self.populate_scroll_area(newZnaki, grid_layout)
        
        button_layout.addWidget(button_a)
        button_layout.addWidget(button_b)
        button_layout.addWidget(button_c)
        button_layout.addWidget(button_d)
        button_layout.addWidget(button_e)
        button_layout.addWidget(button_f)
        button_layout.addWidget(button_g)
        button_layout.addWidget(button_h)

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
        print("Clicked image:", filename_no_extension)
        pyautogui.click(x=x_coord, y=y_coord)
        pyautogui.click(x=x_coord, y=y_coord)
        pyautogui.hotkey('ctrl', '3')
        pyautogui.press('backspace')
        pyautogui.typewrite(filename_no_extension)
        pyautogui.press('enter')
        pyautogui.moveTo(x_coord_center, y_coord_center)

    def clear_scroll_area(self, scroll_layout):
        print('clearing scroll area')
        while scroll_layout.count():
            item = scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def switch_case(self, argument):
        switcher = {
            'A': znaki_a,
            'B': znaki_b,
        }

        return switcher.get(argument)

    def populate_scroll_area(self, newZnaki, grid_layout):
        print('populating scroll area', newZnaki)

        populatedZnaki = self.switch_case(newZnaki)
        row = 0
        col = 0
        for file_name in populatedZnaki:
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
