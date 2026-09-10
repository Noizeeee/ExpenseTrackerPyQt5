
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QSpacerItem,
    QSizePolicy
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200, 700)
        self.create_main()

    def create_main(self):
         # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main horizontal layout
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Left
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        #buttons
        dashboard_btn = QPushButton("Dashboard")
        expenses_btn = QPushButton("Expenses")
        income_btn = QPushButton("Income")

        dashboard_btn.setFixedSize(150, 100)
        expenses_btn.setFixedSize(150, 100)
        income_btn.setFixedSize(150, 100)

        sidebar_layout.addWidget(dashboard_btn)
        sidebar_layout.addWidget(expenses_btn)
        sidebar_layout.addWidget(income_btn)

        sidebar_layout.setAlignment(Qt.AlignCenter)


        # Right
        content = QWidget()

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)


