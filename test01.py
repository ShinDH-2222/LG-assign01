import streamlit as st
import pandas as pd
# from dotenv import load_dotenv
# load_dotenv()

# 페이지 설정
st.set_page_config(page_title="엑셀 파일 업로드", page_icon="📊")

# 제목
st.title("📊 엑셀 파일 업로드")
st.write("엑셀 파일(.xlsx, .xls)을 업로드하세요.")

# 파일 업로드 위젯
uploaded_file = st.file_uploader(
    "파일 선택", 
    type=['xlsx', 'xls'],
    help="엑셀 파일만 업로드 가능합니다."
)

# 파일이 업로드되었을 때
if uploaded_file is not None:
    try:
        # 엑셀 파일 읽기
        df = pd.read_excel(uploaded_file)
        
        # 성공 메시지
        st.success(f"✅ 파일 '{uploaded_file.name}'이 성공적으로 업로드되었습니다!")
        
        # 파일 정보 표시
        st.subheader("📋 데이터 정보")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("행 수", df.shape[0])
        with col2:
            st.metric("열 수", df.shape[1])
        with col3:
            st.metric("파일 크기", f"{uploaded_file.size / 1024:.2f} KB")
        
        # 데이터 미리보기
        st.subheader("👀 데이터 미리보기")
        st.dataframe(df.head(10), use_container_width=True)
        
        # 전체 데이터 보기 옵션
        if st.checkbox("전체 데이터 보기"):
            st.dataframe(df, use_container_width=True)
        
        
    except Exception as e:
        st.error(f"❌ 파일을 읽는 중 오류가 발생했습니다: {str(e)}")
else:
    st.info("👆 위에서 엑셀 파일을 업로드하세요.")

# 실행할 때 터미널에서 입력
# streamlit run "조코딩\AI 에이전트\LG과제01\test01.py"