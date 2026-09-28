from PyQt5.QtWidgets import (
    QComboBox,
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

from PyQt5.QtCore import Qt

from backend.expense_manager import get_all_expenses, update_expenses, delete_expense

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

            self.table.item(row, 0).setData(
                Qt.UserRole,
                expense["id"]
            )
        #Buttons
        update_btn = QPushButton("Update")
        update_btn.clicked.connect(self.update_expense)

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(self.delete_expenses)

        button_container = QWidget()
        button_container_layout = QHBoxLayout()
        button_container_layout.addWidget(delete_btn)
        button_container_layout.addWidget(update_btn)

        button_container.setLayout(button_container_layout)

        #Fields
        search_container = QWidget()
        search_container_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Input the description")
        
        search_btn = QPushButton("Search")
        search_container_layout.addWidget(search_input)
        search_container_layout.addWidget(search_btn)

        search_container.setLayout(search_container_layout)

        self.description_input = QLineEdit()
        self.description_input.setFixedWidth(500)
        self.description_input.setPlaceholderText("Enter description")

        self.amount_input = QLineEdit()
        self.amount_input.setFixedWidth(500)
        self.amount_input.setPlaceholderText("Enter amount")

        self.category_input = QComboBox()
        self.category_input.setFixedWidth(500)
        self.category_input.addItems([
            "Food",
            "Transportation",
            "Bills",
            "Shopping",
            "Entertainment",
            "Other"
        ])

        # Put table into the Reports page
        layout = QVBoxLayout()
        layout.addWidget(search_container)
        layout.addWidget(self.table)
        layout.addWidget(self.description_input)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.category_input)
        layout.addWidget(button_container)
        self.setLayout(layout)

        #Select Row Input on QLine
        self.table.itemSelectionChanged.connect(self.input_row)

    def input_row(self):
        selected_row = self.table.currentRow()

        description = self.table.item(selected_row, 1).text()
        amount = self.table.item(selected_row, 3).text()
        category = self.table.item(selected_row, 2).text()

        self.description_input.setText(description)
        self.amount_input.setText(amount)
        self.category_input.setCurrentText(category)

    def update_expense(self):

        selected_row = self.table.currentRow()

        if selected_row == -1:
            print("No row selected")
            return

        expense_id = self.table.item(
            selected_row, 0
        ).data(Qt.UserRole)

        # Get the NEW values from the input fields
        description = self.description_input.text()
        category = self.category_input.currentText()
        amount = self.amount_input.text()

        print("ID:", expense_id)
        print("Description:", description)
        print("Category:", category)
        print("Amount:", amount)

        result = update_expenses(
            expense_id,
            description,
            category,
            amount
        )

        print("Update result:", result)

    def delete_expenses(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            print("No row selected")
            return

        expense_id = self.table.item(
            selected_row, 0
        ).data(Qt.UserRole)

        print("Deleting ID:", expense_id)

        result = delete_expense(expense_id)

        print("Delete result:", result)

        self.table.removeRow(selected_row)