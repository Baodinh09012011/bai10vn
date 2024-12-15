import streamlit as s

with s.form("Mon an", clear_on_submit=False):
  bs = s.multiselect("Chọn bữa sáng: ", ["Bánh mì", "Bún riêu", "Phở bò", "Bánh canh"])
  btr = s.multiselect("Chọn bữa trưa: ", ["Cơm tấm", "Cơm gà", "Mì xào", "Nui"])
  bt = s.multiselect("Chọn bữa tối: ", ["Bún bò Huế", "Xôi mặn", "Bún chả cá", "Gà chiên"])
  submit = s.form_submit_button("Submit")

if submit:
  if not bs:
    s.warning("Bạn chưa chọn bữa sáng.")
  if not btr:
    s.warning("Bạn chưa chọn bữa trưa.")
  if not bt:
    s.warning("Bạn chưa chọn bữa tối.")
  if bs and btr and bt:
    s.success("Đã nộp thành công!")
    s.balloons()

s.write("Bua sang cua ban: ")
for i in range(len(bs)):
  s.write('-',bs[i])
s.write("Bua trua cua ban: ")
for i in range(len(btr)):
  s.write('-',btr[i])
s.write("Bua toi cua ban: ")
for i in range(len(bt)):
  s.write('-',bt[i])