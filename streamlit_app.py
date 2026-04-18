import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="صائد صفقات السفر - Travel Sniper", page_icon="✈️", layout="wide")

# تصميم الواجهة العلوية (تم تصحيح الخطأ هنا)
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        text-align: center;
        color: #00AE98;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>✈️ صائد صفقات السفر الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ابحث عن أرخص رحلات الطيران والفنادق حول العالم واحجز بأفضل سعر</p>", unsafe_allow_html=True)

st.divider()

# إضافة صندوق البحث (الـ Widget الخاص بك)
with st.container():
    search_widget = """
    <div style="display: flex; justify-content: center;">
        <script async src="https://tpemd.com/content?currency=usd&trs=519994&shmarker=720290&powered_by=true&locale=en&show_header=true&limit=3&primary_color=00AE98&results_background_color=FFFFFF&form_background_color=FFFFFF&campaign_id=111&promo_id=4478" charset="utf-8"></script>
    </div>
    """
    
    # عرض الـ Widget
    components.html(search_widget, height=600, scrolling=True)

st.divider()

st.info("💡 ملاحظة: جميع عمليات الحجز تتم عبر شركاء عالميين موثوقين لضمان أفضل سعر وأمان لبياناتك.")
