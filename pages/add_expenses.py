from backend.expense_manager import add_expenses
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QFormLayout
)


class AddExpenses(QWidget):
    def __init__(self):
        super().__init__()

        title = QLabel("Add Expenses")

        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter description")

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")

        self.category_input = QComboBox()
        self.category_input.addItems([
            "Food",
            "Transportation",
            "Bills",
            "Shopping",
            "Entertainment",
            "Other"
        ])

        self.add_button = QPushButton("Add Expense")

        self.add_button.clicked.connect(self.save_expense)

        form_layout = QFormLayout()

        form_layout.addRow("Description:", self.description_input)
        form_layout.addRow("Amount:", self.amount_input)
        form_layout.addRow("Category:", self.category_input)

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addLayout(form_layout)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def save_expense(self):
        description = self.description_input.text()
        amount = self.amount_input.text()
        category = self.category_input.currentText()

        try:
            add_expenses(description, category, amount)
        except Exception as e:
            print(f"Error: {e}")
