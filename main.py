import streamlit as st
import random

st.set_page_config(page_title="중3 자리배치", layout="centered")

st.title("🏫 중3 랜덤 자리배치")

# 처음 실행 시 자리 생성
if "seats" not in st.session_state:
    numbers = list(range(1, 21))
    random.shuffle(numbers)
    st.session_state.seats = numbers

# 랜덤 배치 버튼
if st.button("🎲 랜덤 배치"):
    numbers = list(range(1, 21))
    random.shuffle(numbers)
    st.session_state.seats = numbers

st.markdown("---")
st.subheader("📚 교탁")

seats = st.session_state.seats

# 5행 × 4열 출력
idx = 0
for r in range(5):
    cols = st.columns(4)
    for c in range(4):
        with cols[c]:
            st.button(
                str(seats[idx]),
                key=f"seat_{idx}",
                use_container_width=True,
                disabled=True,
            )
        idx += 1
