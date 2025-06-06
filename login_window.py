import tkinter as tk
from tkinter import messagebox
import os
from pathlib import Path

def get_password_file_path():
    app_dir = os.path.join(Path.home(), "Documents", "PayLog")
    os.makedirs(app_dir, exist_ok=True)
    return os.path.join(app_dir, "password.txt")

class LoginWindow:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        self.root.title("로그인")
        self.root.geometry("300x150")

        if not os.path.exists(get_password_file_path()):
            self.setup_password_ui()
        else:
            self.login_ui()

    def setup_password_ui(self):
        tk.Label(self.root, text="처음 사용입니다.\n비밀번호를 설정하세요:").pack(pady=10)
        self.new_pw_entry = tk.Entry(self.root, show="*")
        self.new_pw_entry.pack()
        self.new_pw_entry.bind("<Return>", self.save_password)
        tk.Button(self.root, text="저장", command=self.save_password).pack(pady=10)

    def save_password(self, event=None):
        pw = self.new_pw_entry.get()
        if pw:
            with open(get_password_file_path(), "w") as f:
                f.write(pw)
            messagebox.showinfo("성공", "비밀번호가 설정되었습니다.")
            self.root.destroy()
            self.on_success()
        else:
            messagebox.showwarning("경고", "비밀번호를 입력해주세요.")

    def login_ui(self):
        tk.Label(self.root, text="비밀번호를 입력하세요:").pack(pady=10)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        self.password_entry.bind("<Return>", self.check_password)
        tk.Button(self.root, text="확인", command=self.check_password).pack(pady=10)

    def check_password(self, event=None):
        entered_pw = self.password_entry.get()
        with open(get_password_file_path(), "r") as f:
            saved_pw = f.read().strip()
        if entered_pw == saved_pw:
            self.root.destroy()
            self.on_success()
        else:
            messagebox.showerror("오류", "비밀번호가 틀렸습니다.")
