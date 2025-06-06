class TransactionManager:
    def __init__(self):
        self.transactions = []
        self.total_income = 0
        self.total_expense = 0
    
    def add_transaction(self, date, category, t_type, amount, memo):
        transaction = {
            "date": date,
            "category": category,
            "type": t_type,
            "amount": int(amount),
            "memo": memo
        }
        self.transactions.append(transaction)
        if t_type == "수입":
            self.total_income += int(amount)
        elif t_type == "지출":
            self.total_expense += int(amount)
        return transaction  # 새로 추가된 항목만 반환

    def get_transactions(self):
        return self.transactions

    def get_total_income(self):
        return self.total_income

    def get_total_expense(self):
        return self.total_expense