
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

from backend.date_manager import get_current_date

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200, 700)

        with open("styles/dashboard.qss", "r") as file:
            self.setStyleSheet(file.read())
        self.create_main()

    def create_main(self):
         # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Vertical layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        #Margin
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        #Header
        header = QWidget()
        header.setObjectName("header")
        
        header_layout = QHBoxLayout()
        header.setLayout(header_layout)

        #Margin
        header_layout.setContentsMargins(30, 0, 30, 0)
        header_layout.setSpacing(0)

        title = QLabel("EXPENSE TRACKER")
        title.setFont(QFont("Arial", 24, QFont.Bold))


        date = QLabel(f"Date: {get_current_date()}")
        date.setFont(QFont("Arial", 14))

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(date)
        header.setFixedHeight(100)
        main_layout.addWidget(header)


        # Left
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")

        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout()

        #Margin
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(40)
        
        sidebar.setLayout(sidebar_layout)

        #buttons
        dashboard_btn = QPushButton("Dashboard")
        reports_btn = QPushButton("Reports")
        add_expenses_btn = QPushButton("Add Expenses")

        dashboard_btn.setObjectName("sidebarButton")
        reports_btn.setObjectName("sidebarButton")
        add_expenses_btn.setObjectName("sidebarButton")

        for button in [dashboard_btn, reports_btn, add_expenses_btn]:
            button.setFixedHeight(100)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        sidebar_layout.addWidget(dashboard_btn)
        sidebar_layout.addWidget(reports_btn)
        sidebar_layout.addWidget(add_expenses_btn)

        sidebar_layout.setAlignment(Qt.AlignCenter)


        # Right
        content = QWidget()
        content.setObjectName("content")
        content_layout = QVBoxLayout()
        content.setLayout(content_layout)

        # Text
        label = QLabel("Expenses:")
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        content_layout.addWidget(label)

        #Body Layout for Left and Right Display
        body_layout = QHBoxLayout()
        body_layout.addWidget(sidebar)
        body_layout.addWidget(content)

        main_layout.addLayout(body_layout)


