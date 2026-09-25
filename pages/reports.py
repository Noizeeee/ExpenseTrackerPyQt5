from PyQt5.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QVBoxLayout
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

        # Put table into the Reports page
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)