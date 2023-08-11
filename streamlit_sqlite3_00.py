import streamlit as st
import sqlite3
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os

# Set character encoding
import locale

locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

# Connect to the SQLite database
conn = sqlite3.connect("product30.db")
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


# Create PDF with borders
def create_pdf(dataframe):
    pdf_filename = os.path.join(os.path.dirname(__file__), "output.pdf")

    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, topMargin=20,
                            bottomMargin=20)  # Set A4 size and margins
    data = [df.columns.tolist()] + df.values.tolist()

    # Add borders to the table HGRGE.TTC
    table_style = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('BACKGROUND', (0, 0), (-1, 0), colors.gray)])

    table = Table(data)
    table.setStyle(table_style)

    doc.build([table])

    return pdf_filename


pdf_file = create_pdf(df)

# Display PDF download link
st.title('PDF Preview')
st.markdown(f"Download [PDF File]({pdf_file})")

# streamlit run streamlit_sqlte300.py
