
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

        form_layout = QFormLayout()

        form_layout.addRow("Description:", self.description_input)
        form_layout.addRow("Amount:", self.amount_input)
        form_layout.addRow("Category:", self.category_input)

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addLayout(form_layout)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
