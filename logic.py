logic.py
#code responsible for when a button is clicked
import csv

from gui import *

class Logic(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_checkout.clicked.connect(lambda :self.submit())
        self.button_edit.clicked.connect(lambda: self.change())

    def submit(self):
        """
        Process submitted quantities and calculate totals
        Handle also input validation and store data

        """

        try:
            number1 = int(self.input_quantitywater.text())
            number2 = int(self.input_quantitysandwich.text())
            number3 = int(self.input_quantitycookie.text())

            if number1 <= 0 or number2 <= 0 or number3 <= 0:
                self.clear_total_labels()
                self.label_message.setText('All values must be positive')
            else:
                total1 = number1 * 1
                self.label_total1.setText(f'${total1:.2f}')

                total2 = number2 * 4
                self.label_total2.setText(f'${total2:.2f}')

                total3 = number3 * 1.50
                self.label_total3.setText(f'${total3:.2f}')

                total4 = total1 + total2 + total3
                self.label_total4.setText(f'${total4:.2f}')

                self.input_quantitywater.setReadOnly(True)
                self.input_quantitysandwich.setReadOnly(True)
                self.input_quantitycookie.setReadOnly(True)

                self.label_message.setText('')

            with open ('data.csv' , 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([number1, number2, number3])


        except(ValueError):
            self.label_message.setText('Enter whole numeric value')
            self.clear_total_labels()



    def clear_total_labels(self):
        """
        Clear the total label
        """
        self.label_total1.clear()
        self.label_total2.clear()
        self.label_total3.clear()
        self.label_total4.clear()

    def clear_input_fields(self):
        """clear the input field"""
        self.input_quantitycookie.clear()
        self.input_quantitysandwich.clear()
        self.input_quantitywater.clear()

    def change(self):
        """
        allow editing of input field and reset the message
        """
        self.input_quantitywater.setReadOnly(False)
        self.input_quantitysandwich.setReadOnly(False)
        self.input_quantitycookie.setReadOnly(False)

        self.input_quantitywater.setFocus()
        self.label_message.setText('')

