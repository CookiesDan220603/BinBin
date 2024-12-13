import streamlit as st

# Thiết lập tiêu đề
st.set_page_config(page_title="Tỏ Tình với bé Bin", page_icon="❤️")

# Thiết lập giao diện
st.markdown("""
<style>
body {
    background-color: #ffebcd;  /* Màu nền nhẹ nhàng */
    font-family: 'Arial', sans-serif;
}
.header {
    text-align: center;
    margin: 20px;
    color: #FF4500;  /* Màu cam rực rỡ */
}
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
.content {
    text-align: center;
    font-size: 24px;
    color: #2E8B57;  /* Màu xanh lá */
    font-weight: bold;
}
.button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}
.button-container button {
    margin: 0 10px;
    padding: 10px 20px;
    font-size: 18px;
    background-color: #FF69B4;  /* Màu hồng */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.button-container button:hover {
    background-color: #FF1493;  /* Màu hồng đậm khi hover */
}
</style>
""", unsafe_allow_html=True)

# Tiêu đề
st.markdown("<h1 class='header'>Một Lời Tỏ Tình Đặc Biệt</h1>", unsafe_allow_html=True)

# Nội dung tỏ tình
st.markdown("<h2 class='blink'>Bin à, anh yêu em!</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='content'>
    <p>Em là ánh sáng trong cuộc đời anh.</p>
    <p>Hãy để anh khùng với em nhó baby!</p>
</div>
""", unsafe_allow_html=True)

# Nút bấm
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
if st.button("Có, em yêu Anh!", key="yes"):
    st.success("Yay! Anh rất hạnh phúc khi em đồng ý!")
    
if st.button("Xin lỗi, không phải lúc này.", key="no"):
    st.warning("Anh vẫn sẽ lôi em theo cùng thôi baby, đừng có mơ!")
st.markdown("</div>", unsafe_allow_html=True)

# Phần âm nhạc tự động phát

# Hình ảnh (nếu bạn có)
st.image("img/chụt chụt.jpg", use_container_width=True)  # Thay đổi đường dẫn hình ảnh nếu cần
st.audio("sound/sound.mp3", format="audio/mp3", start_time=0)
