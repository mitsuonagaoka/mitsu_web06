# 例としてPDFファイルを生成
import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
pdf_file = "output.pdf"
create_pdf(df, pdf_file)


# input
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, portrait, landscape
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.cidfonts import UnicodeCIDFont
# from reportlab.lib.units import mm
#
# # A4（横）の新規PDFファイルを作成
# p = canvas.Canvas("sample.pdf", pagesize=landscape(A4))
#
# # フォント指定・挿入
# pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
# p.setFont('HeiseiMin-W3', 24*mm)
# p.drawString(30*mm, 115*mm, 'このフォントは')
# p.drawString(50*mm, 85*mm, 'HeiseiMin-W3です。')
#
# # 保存
# p.showPage()
# p.save()

# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, portrait
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# import webbrowser
#
# # 源真ゴシック（ http://jikasei.me/font/genshin/）
# GEN_SHIN_GOTHIC_MEDIUM_TTF = "./fonts/GenShinGothic-Monospace-Medium.ttf"
#
# # 白紙をつくる（A4縦）
# FILENAME = 'HelloWorld.pdf'
# c = canvas.Canvas(FILENAME, pagesize=portrait(A4))
#
# # フォント登録
# pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC_MEDIUM_TTF))
# font_size = 20
# c.setFont('GenShinGothic', font_size)
#
# # 真ん中に文字列描画
# width, height = A4  # A4用紙のサイズ
# c.drawCentredString(width / 2, height / 2 - font_size * 0.4, 'こんにちは、世界！')
#
# # Canvasに書き込み
# c.showPage()
# # ファイル保存
# c.save()
#
# # ブラウザーで表示
# webbrowser.open(FILENAME)
