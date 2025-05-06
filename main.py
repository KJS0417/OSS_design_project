import tkinter as tk
from ui import UI
from chart import Chart
from login_window import LoginWindow

class App:
    def __init__(self, root):
        self.root = root
        self.ui = UI(root)
        self.date_entry, self.category_entry, self.type_combobox, self.amount_entry, self.memo_entry, self.add_button, self.chart_button = self.ui.create_input_section()
        self.chart_button.config(command=self.show_chart)

    def show_chart(self):
        # 더미 데이터
        dummy_transactions = [
            {"date": "2025-01-15", "type": "수입", "amount": 300000},
            {"date": "2025-01-20", "type": "지출", "amount": 100000},
            {"date": "2025-02-10", "type": "수입", "amount": 250000},
            {"date": "2025-02-18", "type": "지출", "amount": 150000},
        ]
        chart = Chart(dummy_transactions)
        chart.generate_monthly_bar_chart()

def launch_app():
    main_root = tk.Tk()
    App(main_root)
    main_root.mainloop()

if __name__ == "__main__":
    login_root = tk.Tk()
    LoginWindow(login_root, launch_app)
    login_root.mainloop()
