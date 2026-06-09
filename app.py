# streamlit 라이브러리 불러오기
import streamlit as st
import time

# 웹페이지 제목 설정
st.title("광영의 AI 챗봇")

# 안내 문구 출력
st.write("궁금한 내용을 입력하고 버튼을 눌러보세요.")

# 사용자 질문 입력창 생성
question = st.text_input("질문을 입력하세요")

# 버튼 생성
if st.button("질문하기"):

    # 질문이 입력되었는지 확인
    if question:

        # 로딩 메시지 표시
        with st.spinner("AI가 답변을 준비 중입니다..."):
            # 2초 대기 (AI가 생각하는 것처럼 보이게 함)
            time.sleep(2)

        # 임시 답변 출력
        st.success("답변 완료!")

        st.write("### AI 답변")
        st.write(f"'{question}'에 대한 답변입니다.")
        st.write("현재는 테스트 버전입니다. 나중에 실제 AI API를 연결할 수 있습니다.")

    else:
        st.warning("질문을 먼저 입력해주세요.")
