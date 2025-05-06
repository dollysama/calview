from tkinter import ttk
import tkinter as tk
import calendar
from datetime import datetime


class CalView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cal Viewer")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        frm = ttk.Frame(root)
        frm.pack(pady=10)

        yr = datetime.now().year
        if yr < 1947 or yr > 2150: yr = 1947
        self.yr_var = tk.IntVar(value=yr)
        ttk.Label(frm, text="Yr:").grid(row=0, column=0, padx=5)
        self.yr_spin = ttk.Spinbox(frm, from_=1947, to=2150, textvariable=self.yr_var, width=6)
        self.yr_spin.grid(row=0, column=1, padx=5)

        mth = datetime.now().month
        self.mth_var = tk.IntVar(value=mth)
        ttk.Label(frm, text="Mth:").grid(row=0, column=2, padx=5)
        self.mth_spin = ttk.Spinbox(frm, from_=1, to=12, textvariable=self.mth_var, width=4)
        self.mth_spin.grid(row=0, column=3, padx=5)

        self.go_btn = ttk.Button(frm, text="GO", command=self.show_cal)
        self.go_btn.grid(row=0, column=4, padx=10)

        self.txt = tk.Text(root, width=35, height=10, font=("Courier", 12))
        self.txt.pack(pady=10)

    def show_cal(self):
        yr = self.yr_var.get()
        mth = self.mth_var.get()
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatmonth(yr, mth)
        self.txt.delete("1.0", tk.END)
        self.txt.insert(tk.END, cal_str)
