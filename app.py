import streamlit as st
import google.generativeai as genai
import os

# 1. Render 시스템 환경 변수에서 안전하게 키 가져오기
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    # [치트키 1] 구글 라이브러리가 낡았더라도 최신 정식 v1 통로를 바라보도록 강제 환경변수 주입
    os.environ["STREAMLIT_GOOGLE_ENTRYPOINT_VERSION"] = "v1"
    
    # [치트키 2] 구글 클라이언트 환경을 'v1' 정식 버전으로 고정하여 초기화
    client_options = {"api_version": "v1"}
    genai.configure(api_key=GEMINI_API_KEY, client_options=client_options)
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
                # v1 통로에서 가장 완벽하게 지원하는 최신 무료 모델 지정
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # 답변 생성 요청
                response = model.generate_content(user_input)
                
                st.success("💡 AI 비서의 답변이 완료되었습니다!")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("질문을 먼저 입력해주세요!")
