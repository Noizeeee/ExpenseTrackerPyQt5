from PyQt5.QtWidgets import (
    QLineEdit,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout
)

from backend.expense_manager import get_all_expenses


class reports(QWidget):

    def __init__(self):
        super().__init__()

        self.create_table()

    def create_table(self):

        self.table = QTableWidget()

        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels([
            "Date",
            "Description",
            "Category",
            "Amount"
        ])

        # Select entire row
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        # Only one row at a time
        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        # Stretch columns
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        # Get expenses
        expenses = get_all_expenses()

        self.table.setRowCount(len(expenses))

        for row, expense in enumerate(expenses):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(str(expense["date"]))
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(str(expense["description"]))
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(str(expense["category"]))
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(str(expense["amount"]))
            )

        update_btn = QPushButton("Update")
        delete_btn = QPushButton("Delete")

        #Buttons
        button_container = QWidget()
        button_container_layout = QHBoxLayout()
        button_container_layout.addWidget(update_btn)
        button_container_layout.addWidget(delete_btn)

        button_container.setLayout(button_container_layout)

        #Fields
        search_input = QLineEdit()
        search_input.setPlaceholderText("Input the description")

        # Put table into the Reports page
        layout = QVBoxLayout()
        layout.addWidget(search_input)
        layout.addWidget(self.table)
        layout.addWidget(button_container)

        self.setLayout(layout)