import streamlit as st
import time

# Thiết lập tiêu đề
st.title("Một Lời Tỏ Tình")

# Hiệu ứng nhấp nháy
st.markdown("""
<style>
.blink {
    animation: blink-animation 1s steps(5, start) infinite;
}
@keyframes blink-animation {
    to {
        visibility: hidden;
    }
}
h2 {
    color: #FF6347;  /* Màu đỏ */
}
</style>
""", unsafe_allow_html=True)

# Nội dung tỏ tình
st.markdown("<h2 class='blink'>Bin à, anh yêu em!</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px; color: #555;'>Anh muốn nói rằng em là ánh sáng trong cuộc đời anh.</p>
<p style='font-size: 20px; color: #555;'>Em có muốn trở thành bạn gái của anh không?</p>
""", unsafe_allow_html=True)

# Nút bấm
if st.button("Có, em yêu anh!"):
    st.success("Yay! Anh rất hạnh phúc khi em đồng ý!")
elif st.button("Xin lỗi, không phải lúc này."):
    st.warning("Cái này vẫn là đồng ý mà khác màu thui bé iu    !")

# Phần âm nhạc (nếu có)
st.audio("sound/sound.mp3", format="audio/mp3", start_time=0) 