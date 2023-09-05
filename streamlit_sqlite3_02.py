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


# データベースに接続
db_name = './data/product30.db'
conn = sqlite3.connect(db_name)
c = conn.cursor()

menu = ["総合生産管理", "受注管理1", "出荷管理2", "在庫管理3", "注文管理4", "顧客管理5"]
submenu1 = ["受注1検索0", "受注1追加1", "受注1編集2", "受注1削除3"]
submenu2 = ["出荷2検索0", "出荷2追加1", "出荷2編集2", "出荷2削除3", "出荷2金額表示4"]
submenu3 = ["在庫3検索0", "在庫3追加1", "在庫3編集2", "在庫3削除3"]
submenu4 = ["注文4検索0_品番_注番", "注文4追加1_日付", '期間別請求書表示', 'invoice表示']
submenu5 = ["顧客5検索0", "顧客5追加1", "顧客5編集2", "顧客5削除3"]

# サイドバーにメニューを表示
choice = st.sidebar.selectbox("Menu", menu)

def Output_report20():
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

# /////選択されたメニューに応じて、選択肢を表示//////////////////////////////////
if choice == "受注管理1":
    # st.sidebar.markdown("Select a submenu:")
    submenu_choice = st.sidebar.selectbox("", submenu1)

    # 選択されたサブメニューの情報を表示
    if submenu_choice == "受注1検索0":
        st.title('findings10 ')
        # findings10()
    elif submenu_choice == "受注1追加1":
        st.title('addings11 ')
        # addings11()
    elif submenu_choice == "受注1編集2":
        st.title('changes12 ')
        # changes12()
    elif submenu_choice == "受注1削除3":
        st.title('deletes13')
        # deletes13()

elif choice == "出荷管理2":
    st.sidebar.markdown("Select a submenu:")
    submenu_choice = st.sidebar.selectbox("", submenu2)

    # 選択されたサブメニューの情報を表示
    if submenu_choice == "出荷2検索0":
        Output_report20()
        # findings20()
    elif submenu_choice == "出荷2追加1":
        st.title('addings21')
        # addings21()
    elif submenu_choice == "出荷2編集2":
        st.title('changes22')
        # changes22()
    elif submenu_choice == "出荷2削除3":
        st.title('deletes23')
        # deletes23()
    elif submenu_choice == "出荷2金額表示4":
        st.title('showamount24')
        # showamount24()

elif choice == "在庫管理3":
    st.sidebar.markdown("Select a submenu:")
    submenu_choice = st.sidebar.selectbox("", submenu3)

    # 選択されたサブメニューの情報を表示
    if submenu_choice == "在庫3検索0":
        st.title('finding30')
        # finding30()
    elif submenu_choice == "在庫3追加1":
        st.title('adding31')
        # adding31()
    elif submenu_choice == "在庫3編集2":
        st.title('changes32')
        # changes32()
    elif submenu_choice == "在庫3削除3":
        st.title('delete33')
        # delete33()

if choice == "注文管理4":
    st.sidebar.markdown("Select a submenu:")
    submenu_choice = st.sidebar.selectbox("", submenu4)

    # 選択されたサブメニューの情報を表示
    if submenu_choice == "注文4検索0_品番_注番":
        st.title('findings40()')
        # findings40()
    elif submenu_choice == "注文4追加1_日付":
        st.title('addings41()')
        # addings41()
    elif submenu_choice == "受注データ表示":
        st.title('show_data42()')
        # show_data42()
    elif submenu_choice == "期間別請求書表示":
        st.title('show_invoice43')
        # show_invoice43()
    elif submenu_choice == "invoice表示":
        st.title('invoice_show44')
        # invoice_show44()

elif choice == "顧客管理5":
    st.sidebar.markdown("Select a submenu:")
    submenu_choice = st.sidebar.selectbox("", submenu5)

    # 選択されたサブメニューの情報を表示
    if submenu_choice == "顧客5検索0":
        st.title('findings50')
        # findings50()
    elif submenu_choice == "顧客5追加1":
        st.title('addings51')
        # addings51()
    elif submenu_choice == "顧客5編集2":
        st.title('changes52')
        # changes52()
    elif submenu_choice == "顧客5削除3":
        st.title('deletes53')
        # deletes53()


if choice == "総合生産管理":
    # title‘画像を表示する
    st.caption("受注管理1:")
    image = Image.open('./data/猫.png')
    st.image(image, width=70)

    st.caption("出荷管理2:")
    image1 = Image.open('./data/牛.png')
    st.image(image1, width=70)

    st.caption("在庫管理3:")
    image1 = Image.open('./data/犬.png')
    st.image(image1, width=70)

    st.caption("注文管理4:")
    image1 = Image.open('./data/猪.png')
    st.image(image1, width=70)

    st.caption("顧客管理5:")
    image1 = Image.open('./data/狐.png')
    st.image(image1, width=70)
