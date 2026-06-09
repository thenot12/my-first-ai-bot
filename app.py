import streamlit as st
import google.generativeai as genai
import os

# 1. 시스템 환경 변수에서 키 가져오기
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    # [치트키] 렌더의 구버전 라이브러리가 자꾸 v1beta 통로를 고집할 때, 최신 v1 통로를 바라보도록 강제 리셋
    os.environ["STREAMLIT_GOOGLE_ENTRYPOINT_VERSION"] = "v1" 
else:
    st.error("Render 설정(Environment)에서 GEMINI_API_KEY를 찾을 수 없습니다!")

st.title("🤖 광영의 AI 스마트 비서")
st.write("무엇이든 물어보세요! 구글 Gemini 엔진이 즉시 답변해 드립니다.")

user_input = st.text_input("질문이나 요청 사항을 입력하세요:", placeholder="예: 직장인을 위한 시간 관리 팁 3가지 알려줘")

if st.button("AI에게 물어보기"):
    if user_input:
        with st.spinner("AI 비서가 답변을 생각하고 있습니다..."):
            try:
                # 구버전 시스템 환경에서 가장 안정적으로 동작하는 모델 명칭 지정
                model = genai.GenerativeModel('gemini-pro')
                
                response = model.generate_content(user_input)
                
                st.success("💡 AI 비서의 답변이 완료되었습니다!")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("질문을 먼저 입력해주세요!")
