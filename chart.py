import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
from tkinter import messagebox

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

class Chart:
    def __init__(self, transactions):
        self.transactions = transactions

    def generate_monthly_bar_chart(self):
        monthly_data = defaultdict(lambda: {"수입": 0, "지출": 0})

        # 월별 수입/지출 합산
        for t in self.transactions:
            try:
                month = datetime.strptime(t["date"], "%Y-%m-%d").strftime("%Y-%m")
                monthly_data[month][t["type"]] += t["amount"]
            except Exception as e:
                print(f"날짜 파싱 오류: {t['date']} -> {e}")

        if not monthly_data:
            messagebox.showwarning("차트 없음", "차트 데이터를 불러올 수 없습니다. 거래 내역이 없습니다.")
            return

        # 월 정렬
        sorted_months = sorted(monthly_data.keys())

        income_values = [monthly_data[m]["수입"] for m in sorted_months]
        expense_values = [monthly_data[m]["지출"] for m in sorted_months]

        x = range(len(sorted_months))
        width = 0.35

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar([i - width / 2 for i in x], income_values, width=width, label="수입", color='skyblue')
        ax.bar([i + width / 2 for i in x], expense_values, width=width, label="지출", color='salmon')

        ax.set_xlabel("월")
        ax.set_ylabel("금액")
        ax.set_title("월별 수입/지출")
        ax.set_xticks(x)
        ax.set_xticklabels(sorted_months, rotation=45)
        ax.legend()
        ax.grid(True)

        plt.tight_layout()
        plt.show()
