import streamlit as st
from openai import OpenAI
import os

# OpenAI 클라이언트 생성
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

# 제목
st.title("광영의 AI 챗봇")

# 설명
st.write("무엇이든 질문해보세요!")

# 질문 입력
question = st.text_input("질문을 입력하세요")

# 버튼
if st.button("질문하기"):

    if question:

        with st.spinner("AI가 답변을 준비 중입니다..."):

            try:
                response = client.responses.create(
                    model="gpt-5",
                    input=question
                )

                answer = response.output_text

                st.success("답변 완료!")
                st.write(answer)

            except Exception as e:
                st.error(f"오류 발생: {e}")

    else:
        st.warning("질문을 입력해주세요.")
