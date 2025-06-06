import csv
import os
import chardet
from pathlib import Path

def get_transaction_file_path():
    app_dir = os.path.join(Path.home(), "Documents", "PayLog")
    os.makedirs(app_dir, exist_ok=True)
    return os.path.join(app_dir, "transactions.csv")

class FileManager:
    @staticmethod
    def save_to_csv(transactions, file_name=None):
        file_path = file_name or get_transaction_file_path()
        file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0
        with open(file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["날짜", "카테고리", "수입/지출", "금액", "메모"])
            for transaction in transactions:
                writer.writerow([transaction["date"], transaction["category"], transaction["type"], transaction["amount"], transaction["memo"]])

    @staticmethod
    def detect_encoding(file_path):
        with open(file_path, 'rb') as f:
            raw_data = f.read(10000)
        result = chardet.detect(raw_data)
        return result['encoding']

    @staticmethod
    def load_from_csv(file_name=None):
        transactions = []
        file_path = file_name or get_transaction_file_path()
        if os.path.exists(file_path):
            encoding = FileManager.detect_encoding(file_path)
            with open(file_path, mode="r", newline="", encoding=encoding) as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    try:
                        transactions.append({
                            "date": row[0],
                            "category": row[1],
                            "type": row[2],
                            "amount": int(row[3]) if row[3].isdigit() else 0,
                            "memo": row[4]
                        })
                    except (IndexError, ValueError):
                        print(f"잘못된 데이터 형식: {row}")
        return transactions