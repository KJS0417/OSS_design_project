import tkinter as tk
from tkinter import ttk

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("PayLog")
        self.root.geometry("600x600")

    def create_input_section(self):
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        date_label = ttk.Label(input_frame, text="날짜 (YYYY-MM-DD):")
        date_label.grid(row=0, column=0)
        date_entry = ttk.Entry(input_frame)
        date_entry.grid(row=0, column=1)

        category_label = ttk.Label(input_frame, text="카테고리:")
        category_label.grid(row=1, column=0)
        category_entry = ttk.Entry(input_frame)
        category_entry.grid(row=1, column=1)

        type_label = ttk.Label(input_frame, text="수입/지출:")
        type_label.grid(row=2, column=0)
        type_combobox = ttk.Combobox(input_frame, values=["수입", "지출"])
        type_combobox.grid(row=2, column=1)

        amount_label = ttk.Label(input_frame, text="금액:")
        amount_label.grid(row=3, column=0)
        amount_entry = ttk.Entry(input_frame)
        amount_entry.grid(row=3, column=1)

        memo_label = ttk.Label(input_frame, text="메모:")
        memo_label.grid(row=4, column=0)
        memo_entry = ttk.Entry(input_frame)
        memo_entry.grid(row=4, column=1)

        add_button = ttk.Button(input_frame, text="추가")
        add_button.grid(row=5, columnspan=2)

        chart_button = ttk.Button(input_frame, text="차트 보기")
        chart_button.grid(row=6, columnspan=2, pady=5)

        return date_entry, category_entry, type_combobox, amount_entry, memo_entry, add_button, chart_button