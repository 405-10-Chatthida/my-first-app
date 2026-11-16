import streamlit as st
st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")
fullprice = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0, value=1000.0)
sen = st.number_input("กรอกส่วนลด (%):", min_value=0.0, max_value=100.0, value=20.0)
st.divider()
discount = fullprice * sen / 100
vaten = (fullprice - discount) * 0.07
net_price = fullprice - discount + vaten
fullprice_sen = f"ราคาสินค้า {fullprice:.2f} บาท ส่วนลด {sen:.2f}%"
sen_ = discount
vat = vaten
net = net_price
st.write(f"• {fullprice_sen}")
st.write(f"• ส่วนลด ({sen:.0f}%): -{sen_:.2f} บาท")
st.write(f"• ราคาหลังหักส่วนลด: {fullprice - discount:.2f} บาท")
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +{vat:.2f} บาท")
st.markdown("---")
st.markdown(f"### • ราคาสุทธิที่ต้องจ่าย: {net:.2f} บาท")
st.divider()
st.write("นางสาว ฉัตรธิดา ยศถานี เลขที่ 10 ม.4/5")
