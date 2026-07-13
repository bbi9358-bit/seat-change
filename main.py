import streamlit as st
import random

st.set_page_config(page_title="중3 자리배치", layout="centered")

st.title("🏫 중3 랜덤 자리배치")

def make_seats():
    fixed = [2, 19]  # 앞줄 고정

    # 나머지 학생
    others = [i for i in range(1, 21) if i not in fixed]
    random.shuffle(others)

    # 앞줄의 나머지 두 자리
    front = fixed + others[:2]
    random.shuffle(front)  # 앞줄 안에서만 위치 랜덤

    # 나머지 자리
    back = others[2:]
    random.shuffle(back)

    return front + back


# 처음 실행
if "seats" not in st.session_state:
    st.session_state.seats = make_seats()

# 버튼
if st.button("🎲 랜덤 배치"):
    st.session_state.seats = make_seats()

st.markdown("---")
st.subheader("📚 교탁")

seats = st.session_state.seats

idx = 0
for r in range(5):
    cols = st.columns(4)
    for c in range(4):
        with cols[c]:
            st.button(
                str(seats[idx]),
                key=f"seat_{idx}",
                disabled=True,
                use_container_width=True,
            )
        idx += 1
