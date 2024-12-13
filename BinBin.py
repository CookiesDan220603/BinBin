import streamlit as st

# CSS for heart shape
heart_css = """
<style>
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

.heart {
    position: relative;
    width: 100px;
    height: 100px;
    background: red;
    transform: rotate(-45deg);
    margin: 50px auto;
}

.heart:before,
.heart:after {
    content: "";
    position: absolute;
    width: 100px;
    height: 100px;
    background: red;
    border-radius: 50%;
}

.heart:before {
    top: -50px;
    left: 0;
}

.heart:after {
    left: 50px;
    top: 0;
}

.text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 16px;
    animation: blink 1s infinite;
}
</style>
"""

# HTML for heart and text
heart_html = """
<div class="heart">
    <div class="text">ANH YÊU BIN</div>
</div>
"""

# Streamlit app
st.title("Anh Yêu Bin Lắm")
st.markdown(heart_css, unsafe_allow_html=True)
st.markdown(heart_html, unsafe_allow_html=True)