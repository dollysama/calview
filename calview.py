import tkinter as tk
import calendar

app = tk.Tk()
app.title("Calendar")

tk.Label(app, text="Year").grid(row=0, column=0)
year = tk.Entry(app)
year.grid(row=0, column=1)

tk.Label(app, text="Month").grid(row=1, column=0)
month = tk.Entry(app)
month.grid(row=1, column=1)

result = tk.Label(app)
result.grid(row=3, column=0, columnspan=2)

def show():
    y = int(year.get())
    m = int(month.get())
    result.config(text=calendar.month(y, m))

tk.Button(app, text="Show", command=show).grid(row=2, column=0, columnspan=2)


app.mainloop()


