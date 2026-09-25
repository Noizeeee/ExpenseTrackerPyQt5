from backend.expense_manager import add_expenses
from PyQt5.QtWidgets import (
    QSizePolicy,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QMessageBox
)

from PyQt5.QtCore import Qt
from backend.date_manager import get_current_date

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
        self.clear_button = QPushButton("Clear")

        self.add_button.clicked.connect(self.save_expense)
        self.clear_button.clicked.connect(self.clear)

        #SIZING
        self.description_input.setFixedWidth(500)
        self.amount_input.setFixedWidth(500)
        self.category_input.setFixedWidth(500)


        button_layout = QHBoxLayout()
        self.add_button.setFixedWidth(100)
        self.clear_button.setFixedWidth(100)

        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.add_button)

        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(100)

        form_layout = QFormLayout()

        form_layout.addRow("Description:", self.description_input)
        form_layout.addRow("Amount:", self.amount_input)
        form_layout.addRow("Category:", self.category_input)

        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setFormAlignment(Qt.AlignCenter)


        layout = QVBoxLayout()
        layout.addWidget(title, alignment=Qt.AlignCenter)
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        container = QWidget()
        container.setObjectName("container")
        container.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(container)

        main_layout.setContentsMargins(50, 50, 50, 50)

        self.setLayout(main_layout)

    #For Button
    def save_expense(self):
        date = get_current_date()
        description = self.description_input.text().strip()
        amount = self.amount_input.text().strip()
        category = self.category_input.currentText()

        #Validate Fields
        if not description:
            QMessageBox.warning(
                    self,
                    "Invalid Input",
                    "Please enter a description."
                )
            self.description_input.setFocus()
            return
        
        if not amount or not amount.isdigit():
            QMessageBox.warning(
            self,
            "Invalid Input",
            f"{amount} is not a valid amount!"
        )
            self.clear()
            self.amount_input.setFocus()
            return
        
        try:
            add_expenses(date, description, category, amount)
            self.clear()
            QMessageBox.information(
                        self,
                        "Expense Tracker",
                        "Expense added succesfully!"
                    )
        except Exception as e:
            print(f"Error: {e}")

    def clear(self):
        self.description_input.clear()
        self.amount_input.clear()
        self.category_input.setCurrentIndex(0)
