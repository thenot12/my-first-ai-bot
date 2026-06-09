import streamlit as st
import google.generativeai as genai

# 1. 렌더 환경변수에서 제미나이 API 키 가져오기
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
except Exception:
    st.error("Render 설정에서 GEMINI_API_KEY를 등록해주세요!")

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
                # 최신 제미나이 모델 호출
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # 제미나이에게 군더더기 없는 일반 답변 요청
                response = model.generate_content(user_input)
                
                st.success("💡 AI 비서의 답변이 완료되었습니다!")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("질문을 먼저 입력해주세요!")
