import tkinter as tk
from tkinter import messagebox
from transaction_manager import TransactionManager
from file_manager import FileManager
from chart import Chart
from input_validator import InputValidator
from ui import UI
from login_window import LoginWindow

class App:
    def __init__(self, root):
        self.root = root
        self.transaction_manager = TransactionManager()
        self.file_manager = FileManager()
        self.chart = None
        self.ui = UI(root)
        
        loaded_transactions = self.file_manager.load_from_csv()
        self.transaction_manager.transactions = loaded_transactions
        
        self.date_entry, self.category_entry, self.type_combobox, self.amount_entry, self.memo_entry, self.add_button, self.chart_button = self.ui.create_input_section()

        self.add_button.config(command=self.add_transaction)
        self.chart_button.config(command=self.show_chart)

    def add_transaction(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        t_type = self.type_combobox.get()
        amount = self.amount_entry.get()
        memo = self.memo_entry.get()

        if InputValidator.validate_transaction(date, category, t_type, amount):
            new_transaction = self.transaction_manager.add_transaction(date, category, t_type, amount, memo)
            self.file_manager.save_to_csv([new_transaction])
        else:
            messagebox.showwarning("입력 오류", "모든 항목을 입력하고, 금액은 숫자만 입력해주세요.")

    def show_chart(self):
        self.chart = Chart(self.transaction_manager.get_transactions())
        self.chart.generate_monthly_bar_chart()

def launch_app():
    main_root = tk.Tk()
    app = App(main_root)
    main_root.mainloop()

if __name__ == "__main__":
    login_root = tk.Tk()
    LoginWindow(login_root, launch_app)
    login_root.mainloop()