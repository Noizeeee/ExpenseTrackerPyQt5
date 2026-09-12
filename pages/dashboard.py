
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
    QSizePolicy,
    QButtonGroup
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
        self.dashboard_btn = QPushButton("Dashboard")
        self.reports_btn = QPushButton("Reports")
        self.add_expenses_btn = QPushButton("Add Expenses")

        self.dashboard_btn.setObjectName("sidebarButton")
        self.reports_btn.setObjectName("sidebarButton")
        self.add_expenses_btn.setObjectName("sidebarButton")

        for button in [self.dashboard_btn, self.reports_btn, self.add_expenses_btn]:
            button.setFixedHeight(100)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            button.setCheckable(True)

        #Create button Group
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.dashboard_btn)
        self.button_group.addButton(self.reports_btn)
        self.button_group.addButton(self.add_expenses_btn)

        #ONLY ONE Button active at a time
        self.button_group.setExclusive(True)

        self.dashboard_btn.setChecked(True)

        #Button Function
        self.dashboard_btn.clicked.connect(
            lambda: self.show_page("dashboard")
        )

        self.reports_btn.clicked.connect(
                    lambda: self.show_page("reports")
        )

        self.add_expenses_btn.clicked.connect(
                    lambda: self.show_page("add_expenses")
        )

        sidebar_layout.addWidget(self.dashboard_btn)
        sidebar_layout.addWidget(self.reports_btn)
        sidebar_layout.addWidget(self.add_expenses_btn)

        sidebar_layout.setAlignment(Qt.AlignCenter)


        # Right
        self.content = QWidget()
        self.content.setObjectName("content")
        self.content_layout = QVBoxLayout()
        self.content.setLayout(self.content_layout)

        #Grid for Three Box
        Grid = QWidget()
        grid_layout = QGridLayout()
        grid_layout.addWidget(QPushButton("Left"), 1, 0)
        grid_layout.addWidget(QPushButton("Middle"), 1, 1)
        grid_layout.addWidget(QPushButton("Right"), 1, 2)
        Grid.setLayout(grid_layout)
        self.content_layout.addWidget(Grid)

        # Text
        label = QLabel("Expenses:")
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.content_layout.addWidget(label)

        #Body Layout for Left and Right Display
        body_layout = QHBoxLayout()
        body_layout.addWidget(sidebar)
        body_layout.addWidget(self.content)

        main_layout.addLayout(body_layout)

    def show_page(self, page):
        # Remove the current content
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

        # Add new content
        if page == "dashboard":
            label = QLabel("Dashboard")

        elif page == "reports":
            label = QLabel("Reports")

        elif page == "add_expenses":
            label = QLabel("Add Expenses")

        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 24, QFont.Bold))

        self.content_layout.addWidget(label)


#Add DASHBOARD ELEMENTS