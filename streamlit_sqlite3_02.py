# streamlit run streamlit_sqlite3_02.py

import streamlit as st
import sqlite3
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os
import base64
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
import locale

from PIL import Image


# Connect to the SQLite database
conn = sqlite3.connect("./data/product30.db")
# Read data from the table
query = "SELECT * FROM t_出荷Data"
df = pd.read_sql_query(query, conn)
# Close the database connection
conn.close()

# Set column headers in Japanese
df.columns = ["番号", "品番", "出荷数", "注番", "出荷日", "出荷金額"]

st.title('Data Preview')

# Display data in dataframe
st.dataframe(df)

# フォントファイルがアプリのディレクトリ内の fonts ディレクトリにある場合のパス
# font_path = "fonts/msgothic.ttc"

font_path = "C:\Windows\Fonts\msgothic.ttc"

# Register custom font
pdfmetrics.registerFont(TTFont("msgothic", font_path))
addMapping("msgothic", 0, 0, "msgothic")


# Create PDF with borders
def create_pdf(dataframe):
    pdf_filename = os.path.join(os.path.dirname(__file__), "output.pdf")

    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, topMargin=20,
                            bottomMargin=20)  # Set A4 size and margins
    data = [df.columns.tolist()] + df.values.tolist()

    # Add borders to the table
    table_style = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                              ('FONTNAME', (0, 0), (-1, 0), "msgothic"),  # Use the specified font name
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('BACKGROUND', (0, 0), (-1, 0), colors.gray)])

    table = Table(data)
    table.setStyle(table_style)

    doc.build([table])

    return pdf_filename


pdf_file = create_pdf(df)

# Display PDF preview
st.write('Hellow World')
st.write('Display PDF')
st.title('PDF Preview')
with open(pdf_file, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
st.markdown(
    f'<embed src="data:application/pdf;base64,{base64_pdf}" width="800" height="600" type="application/pdf">',
    unsafe_allow_html=True)

# Display PDF download link
st.markdown(f"Download [PDF File]({pdf_file})")

# 受注管理1と猫.pngを横に並べる。
st.caption("受注管理1111:")
image = Image.open('./data/猫.png')
st.image(image, width=70)
