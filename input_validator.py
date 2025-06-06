class InputValidator:
    @staticmethod
    def validate_transaction(date, category, t_type, amount):
        if not date or not category or not t_type or not amount:
            return False
        try:
            int(amount)
        except ValueError:
            return False
        return True
