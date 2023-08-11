import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import webbrowser

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Generator")

        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("id", "番号", "品番", "出荷数", "注番", "出荷日", "出荷金額")
        self.tree.heading("id", text="ID")
        self.tree.heading("番号", text="番号")
        self.tree.heading("品番", text="品番")
        self.tree.heading("出荷数", text="出荷数")
        self.tree.heading("注番", text="注番")
        self.tree.heading("出荷日", text="出荷日")
        self.tree.heading("出荷金額", text="出荷金額")
        self.tree.pack()

        self.load_button = tk.Button(root, text="Load Data", command=self.load_data)
        self.load_button.pack()

        self.generate_button = tk.Button(root, text="Generate PDF", command=self.generate_pdf)
        self.generate_button.pack()

    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("./data/product30.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM t_出荷Data")
        data = cursor.fetchall()
        for row in data:
            self.tree.insert("", "end", values=row)
        conn.close()

    def generate_pdf(self):
        df = pd.DataFrame(self.tree.get_children())
        df.columns = ["id", "番号", "品番", "出荷数", "注番", "出荷日", "出荷金額"]

        pdf_filename = "output.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)

        c.drawString(100, 750, "PDF Report")

        y_start = 700
        for index, row in df.iterrows():
            c.drawString(100, y_start, f"ID: {row['id']}, 番号: {row['番号']}, 出荷数: {row['出荷数']},"
                                       f" 注番: {row['注番']}, 出荷日: {row['出荷日']}, 出荷金額: {row['出荷金額']}")
            y_start -= 20

        c.save()

        # Open PDF in default PDF viewer
        webbrowser.open(pdf_filename)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
