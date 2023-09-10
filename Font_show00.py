from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import mm

# A4（横）の新規PDFファイルを作成
p = canvas.Canvas("sample.pdf", pagesize=landscape(A4))

# フォント指定・挿入
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
p.setFont('HeiseiMin-W3', 24*mm)
p.drawString(30*mm, 115*mm, 'このフォントは')
p.drawString(50*mm, 85*mm, 'HeiseiMin-W3です。')

# 保存
p.showPage()
p.save()
