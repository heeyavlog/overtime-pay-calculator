import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="야근 수당 계산기",
    page_icon="🌙",
    layout="wide"
)

# CSS 스타일
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stProgress > div > div > div > div {
        background-color: #1f77b4;
    }
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
    }
    .result-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


def format_number(number):
    """숫자에 콤마를 추가하는 함수"""
    return f"{int(number):,}원"


def calculate_overtime_pay():
    st.title('🌙 야근 수당 계산기')
    st.markdown(
        '#### 시급, 야근 시간 등을 입력하면 야근 수당을 계산해 드립니다.')

    # 입력 섹션
    col1, col2, col3 = st.columns(3)

    with col1:
        hourly_wage = st.number_input("시급을 입력하세요 (원)",
                                     min_value=0,
                                     value=10000,
                                     step=100,
                                     format="%d")

    with col2:
        overtime_hours = st.number_input("야근 시간을 입력하세요 (시간)",
                                        min_value=0.0,
                                        value=2.0,
                                        step=0.5,
                                        format="%.1f")

    with col3:
        overtime_rate = st.number_input("야근 수당 할증률을 입력하세요 (예: 1.5)",
                                        min_value=1.0,
                                        value=1.5,
                                        step=0.1,
                                        format="%.1f")

    # 주 52시간 근무제 적용 여부
    apply_52h_rule = st.checkbox("주 52시간 근무제 적용", value=True)

    if apply_52h_rule:
        weekly_overtime_hours = st.number_input(
            "주 52시간 초과 야근 시간을 입력하세요 (시간)",
            min_value=0.0,
            value=0.0,
            step=0.5,
            format="%.1f")
        overtime_rate_52h = st.number_input(
            "주 52시간 초과 야근 수당 할증률을 입력하세요 (예: 2.0)",
            min_value=1.0,
            value=2.0,
            step=0.1,
            format="%.1f")

    if st.button('계산하기', use_container_width=True):
        # 야근 수당 계산
        overtime_pay = hourly_wage * overtime_hours * overtime_rate
        if apply_52h_rule:
            overtime_pay_52h = hourly_wage * weekly_overtime_hours * overtime_rate_52h
            total_overtime_pay = overtime_pay + overtime_pay_52h
        else:
            total_overtime_pay = overtime_pay

        # 결과 표시
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('### 💵 야근 수당')
        st.markdown(
            f'<p class="big-font">{format_number(total_overtime_pay)}</p>',
            unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 상세 정보 표시
        st.markdown('### 📋 상세 정보')
        st.markdown(f'- 시급: {format_number(hourly_wage)}')
        st.markdown(f'- 야근 시간: {overtime_hours:.1f}시간')
        st.markdown(f'- 야근 수당 할증률: {overtime_rate:.1f}배')
        if apply_52h_rule:
            st.markdown(f'- 주 52시간 초과 야근 시간: {weekly_overtime_hours:.1f}시간')
            st.markdown(f'- 주 52시간 초과 야근 수당 할증률: {overtime_rate_52h:.1f}배')
        st.markdown('---')

        # 주의사항
        st.info('''
            #### ℹ️ 참고사항
            - 이 계산기는 개략적인 예상 금액을 계산합니다.
            - 실제 야근 수당은 회사 정책, 근로 계약, 관련 법규에 따라 달라질 수 있습니다.
            - 정확한 금액은 회사 급여 담당자나 노무사와 상담하시기 바랍니다.
            ''')


if __name__ == '__main__':
    calculate_overtime_pay()
