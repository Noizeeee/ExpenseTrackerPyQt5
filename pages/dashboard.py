
import sys

#Matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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

    def create_dashboard(self):
        #Grid for Three Cards
        Cards = QWidget()
        cards_layout = QHBoxLayout()
        Cards.setLayout(cards_layout)

        cards_layout.setContentsMargins(20, 20, 20, 20)
        cards_layout.setSpacing(20)

        # Left Card
        total_expenses = QFrame()
        total_expenses.setObjectName("expenseCard")
        total_expenses_layout = QVBoxLayout()

        total_expenses_title = QLabel("Total Expenses")
        total_expenses_value = QLabel("₱88,250")

        total_expenses_layout.addWidget(total_expenses_title)
        total_expenses_layout.addWidget(total_expenses_value)

        total_expenses.setLayout(total_expenses_layout)

        # Center Card
        monthly_expenses = QFrame()
        monthly_expenses.setObjectName("expenseCard")
        monthly_expenses_layout = QVBoxLayout()

        monthly_expenses_title = QLabel("This Month")
        monthly_expenses_value = QLabel("₱8,250")

        monthly_expenses_layout.addWidget(monthly_expenses_title)
        monthly_expenses_layout.addWidget(monthly_expenses_value)

        monthly_expenses.setLayout(monthly_expenses_layout)


        # Right Card
        average_daily = QFrame()
        average_daily.setObjectName("expenseCard")
        average_daily_layout = QVBoxLayout()

        average_daily_title = QLabel("Avg. Daily")
        average_daily_value = QLabel("₱275")

        average_daily_layout.addWidget(average_daily_title)
        average_daily_layout.addWidget(average_daily_value)

        average_daily.setLayout(average_daily_layout)


        # Add cards
        cards_layout.addWidget(total_expenses, 1)
        cards_layout.addWidget(monthly_expenses, 1)
        cards_layout.addWidget(average_daily, 1)

        self.content_layout.addWidget(Cards)

        #Grid for Two Graphs
        Grid = QWidget()
        grid_layout = QGridLayout()

        grid_layout.setContentsMargins(20, 20, 20, 20)
        grid_layout.setSpacing(20)


        #Left Graph
        graph = self.create_graph()
        grid_layout.addWidget(graph, 1, 0)

        #Right Graph
        grid_layout.addWidget(QPushButton("Right"), 1, 1)

        #Set Column Size
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)
        Grid.setLayout(grid_layout)
        self.content_layout.addWidget(Grid)

    def create_main(self):
        # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Vertical layout
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        #Margin
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

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
        self.main_layout.addWidget(header)


        # Left
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")

        self.sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout()

        #Margin
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(40)
        
        self.sidebar.setLayout(sidebar_layout)

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

        #Body Layout for Left and Right Display
        body_layout = QHBoxLayout()
        body_layout.addWidget(self.sidebar)
        body_layout.addWidget(self.content)

        self.main_layout.addLayout(body_layout)

        self.show_page("dashboard")


    def create_graph(self):
        figure = Figure(figsize=(5, 3))
        canvas = FigureCanvas(figure)

        canvas.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )


        months = ["Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"]
        expenses = [500, 200, 1000, 3000, 2000, 0, 0, 0, 0, 2000, 7000, 300]

        # Left graph
        ax = figure.add_subplot(111)

        ax.bar(months, expenses)

        ax.tick_params(axis="x", rotation=45)

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        ax.set_xticklabels(months)
        ax.set_yticks([0, 1000, 2000, 3000, 4000, 5000, 6000])

        ax.set_title("Expense Trend")
        ax.set_xlabel("Month")
        ax.set_ylabel("Expenses")
        figure.tight_layout()
        
        return canvas

    def show_page(self, page):
        # Remove the current content
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

        # Add new content
        if page == "dashboard":
            self.create_dashboard()

        elif page == "reports":
            label = QLabel("Reports")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont("Arial", 24, QFont.Bold))
            
            self.content_layout.addWidget(label)

        elif page == "add_expenses":
            label = QLabel("Add Expenses")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont("Arial", 24, QFont.Bold))
                        
            self.content_layout.addWidget(label)