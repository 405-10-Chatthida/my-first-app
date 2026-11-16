import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7% และเปอร์เซ็น")
fullprice = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
sen = st.number_input("กรอกเปอร์เซ็นต์ส่วนลด (%):", min_value=0.0, max_value=100.0, value=0.0) 
discount = fullprice * sen / 100 
vaten = fullprice * 0.07
net_price = fullprice - vaten
fullprice_sen = f"ราคาสินค้า {fullprice:.2f} บาท ส่วนลด {sen:.2f}%" 
sen_ = discount 
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vaten:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.write("นางสาว ฉัตรธิดา ยศถานี เลขที่ 10  ม.4/5")
