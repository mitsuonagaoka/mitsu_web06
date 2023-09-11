# streamlit run Font_show01.py

import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image
import os
import base64

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Connect to the SQLite database
conn = sqlite3.connect("./data/product30.db")
query = "SELECT * FROM t_出荷Data"
df = pd.read_sql_query(query, conn)
conn.close()

# Set column headers in Japanese
df.columns = ["番号", "品番", "出荷数", "注番", "出荷日", "出荷金額"]

# Streamlit UI
st.title("受注管理_出荷管理:")
image = Image.open('./data/猫.png')
st.image(image, width=100)

# Display data in dataframe
st.dataframe(df)

# A4（横）の新規PDFファイルを作成
output_directory = r"C:\Users\marom\Invoice"
pdf_filename = os.path.join(output_directory, "output.pdf")

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

doc = SimpleDocTemplate(pdf_filename, pagesize=landscape(A4), topMargin=20, bottomMargin=20)

# フォント指定・挿入
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

# Create PDF with borders
def create_pdf(dataframe):
    pdf_filename = os.path.join(os.path.dirname(__file__), "output.pdf")

    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, topMargin=20, bottomMargin=20)  # Set A4 size and margins
    data = [df.columns.tolist()] + df.values.tolist()

    # Register and set font
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
    p = canvas.Canvas("sample.pdf", pagesize=landscape(A4))
    p.setFont('HeiseiMin-W3', 12 * mm)

    # Add borders to the table
    table_style = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
                              ('FONTNAME', (0, 0), (-1, 0), "HeiseiMin-W3"),  # Use the specified font name
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('BACKGROUND', (0, 0), (-1, 0), colors.gray)])

    table = Table(data)
    table.setStyle(table_style)

    doc.build([table])

    return pdf_filename

pdf_file = create_pdf(df)

# Display PDF preview
st.title('PDF Preview')
with open(pdf_file, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
st.markdown(
    f'<embed src="data:application/pdf;base64,{base64_pdf}" width="800" height="600" type="application/pdf">',
    unsafe_allow_html=True)

# Remove the temporary sample.pdf file
# if os.path.exists("sample.pdf"):
#     os.remove("sample.pdf")





# import streamlit as st
# import sqlite3
# import pandas as pd
#
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, portrait, landscape
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.cidfonts import UnicodeCIDFont
# from reportlab.lib.units import mm
#
# import os
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib import colors
# import base64
# from PIL import Image
# from reportlab.pdfbase.ttfonts import TTFont
#
#
# # Connect to the SQLite database
# conn = sqlite3.connect("./data/product30.db")
# query = "SELECT * FROM t_出荷Data"
# df = pd.read_sql_query(query, conn)
# conn.close()
#
# # Set column headers in Japanese
# df.columns = ["番号", "品番", "出荷数", "注番", "出荷日", "出荷金額"]
#
# # st.title('Data Preview')
# st.title("受注管理_出荷管理:")
# image = Image.open('./data/猫.png')
# st.image(image, width=100)
#
#
# # Display data in dataframe
# st.dataframe(df)
#
# # # A4（横）の新規PDFファイルを作成　sample.pdf　output.pdf
# p = canvas.Canvas("sample.pdf", pagesize=landscape(A4))
#
# # Create PDF with borders
# def create_pdf(dataframe):
#     pdf_filename = os.path.join(os.path.dirname(__file__), "output.pdf")
#
#     doc = SimpleDocTemplate(pdf_filename, pagesize=A4, topMargin=20,
#                             bottomMargin=20)  # Set A4 size and margins
#     data = [df.columns.tolist()] + df.values.tolist()
#
#     # フォント指定・挿入
#     pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
#     p.setFont('HeiseiMin-W3', 12 * mm)
#
#     # Add borders to the table
#     table_style = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black),
#                               ('FONTNAME', (0, 0), (-1, 0), "HeiseiMin-W3"),  # Use the specified font name
#                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                               ('BACKGROUND', (0, 0), (-1, 0), colors.gray)])
#
#     table = Table(data)
#     table.setStyle(table_style)
#
#     doc.build([table])
#
#     return pdf_filename
#
# pdf_file = create_pdf(df)
#
# # 保存
# p.showPage()
# p.save()
#
# # Display PDF preview----------------------------------------------------------
# st.title('PDF Preview')
# with open(pdf_file, "rb") as f:
#     base64_pdf = base64.b64encode(f.read()).decode('utf-8')
# st.markdown(
#     f'<embed src="data:application/pdf;base64,{base64_pdf}" width="800" height="600" type="application/pdf">',
#     unsafe_allow_html=True)
#
# # 削除するファイルのパス
# file_path = "sample.pdf"
#
# # ファイルが存在するかチェックし、存在する場合は削除
# if os.path.exists(file_path):
#     os.remove(file_path)
