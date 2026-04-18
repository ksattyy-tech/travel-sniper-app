import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة لتكون عريضة واحترافية
st.set_page_config(page_title="صائد صفقات السفر - Travel Sniper", page_icon="✈️", layout="wide")

# تصميم الواجهة وتنسيق العرض
st.markdown("""
    <style>
    /* جعل الحاوية تأخذ العرض الكامل */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .title {
        text-align: center;
        color: #00AE98;
        font-family: 'Arial';
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>✈️ صائد صفقات السفر الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>محرك بحث متطور لإيجاد أرخص تذاكر الطيران والفنادق</p>", unsafe_allow_html=True)

st.divider()

# إضافة صندوق البحث مع تعديل اللغة إلى العربية (locale=ar) والعرض (width: 100%)
with st.container():
    # لاحظ تغيير locale=ar في الرابط أدناه لتعريب المحرك
    search_widget = """
    <div style="width: 100%; min-width: 300px;">
        <script async src="https://tpemd.com/content?currency=usd&trs=519994&shmarker=720290&powered_by=true&locale=ar&show_header=true&limit=5&primary_color=00AE98&results_background_color=FFFFFF&form_background_color=FFFFFF&campaign_id=111&promo_id=4478" charset="utf-8"></script>
    </div>
    """
    
    # زيادة الارتفاع لضمان ظهور النتائج كاملة
    components.html(search_widget, height=700, scrolling=True)

st.divider()

st.info("💡 نصيحة: للحصول على أفضل النتائج، ابحث قبل موعد سفرك بفترة كافية.")
