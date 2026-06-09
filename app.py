import streamlit as st
import os
# google 이름 공간 충돌을 완전히 회피하는 최신 정석 임포트 문법
from google.genai import Client

# 1. Render 시스템 환경 변수에서 직접 키 가져오기 (보안 유지)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    try:
        # 공식 가이드에 따른 최신 클라이언트 초기화
        client = Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        st.error(f"클라이언트 초기화 실패: {e}")
else:
    st.error("Render 설정(Environment)에서 GEMINI_API_KEY를 찾을 수 없습니다!")

# 웹사이트 제목 구성
st.title("🤖 광영의 AI 스마트 비서")
st.write("무엇이든 물어보세요! 구글 Gemini 엔진이 즉시 답변해 드립니다.")

# 2. 사용자가 질문을 입력할 창
user_input = st.text_input("질문이나 요청 사항을 입력하세요:", placeholder="예: 직장인을 위한 시간 관리 팁 3가지 알려줘")

# 3. 답변 생성 버튼
if st.button("AI에게 물어보기"):
    if user_input:
        with st.spinner("AI 비서가 답변을 생각하고 있습니다..."):
            try:
                # 2026년 기준 가장 완벽하게 작동하는 정식 텍스트 생성 문법
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=user_input,
                )
                
                st.success("💡 AI 비서의 답변이 완료되었습니다!")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("질문을 먼저 입력해주세요!")
