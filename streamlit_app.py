import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="صائد صفقات السفر - Travel Sniper", page_icon="✈️", layout="wide")

# --- 1. وضع كود التحقق (Drive Code) في خلفية الموقع ---
components.html(
    """
    <script nowprocket data-noptimize="1" data-cfasync="false" data-wpfc-render="false" seraph-accel-crit="1" data-no-defer="1">
      (function () {
          var script = document.createElement("script");
          script.async = 1;
          script.src = 'https://emrldtp.com/NTE5OTk0.js?t=519994';
          document.head.appendChild(script);
      })();
    </script>
    """,
    height=0,
)

# --- 2. تصميم الواجهة ---
st.markdown("""
    <style>
    .title { text-align: center; color: #00AE98; font-family: 'Arial'; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>✈️ صائد صفقات السفر الذكي</h1>", unsafe_allow_html=True)

st.divider()

# --- 3. محرك البحث العربي ---
with st.container():
    search_widget = """
    <div style="width: 100%; min-width: 300px;">
        <script async src="https://tpemd.com/content?currency=usd&trs=519994&shmarker=720290&powered_by=true&locale=ar&show_header=true&limit=5&primary_color=00AE98&results_background_color=FFFFFF&form_background_color=FFFFFF&campaign_id=111&promo_id=4478" charset="utf-8"></script>
    </div>
    """
    components.html(search_widget, height=600, scrolling=True)

st.divider()
st.info("💡 الموقع جاهز الآن للبحث والحجز المباشر.")
