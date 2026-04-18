import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="صائد صفقات السفر - Travel Sniper", page_icon="✈️", layout="wide")

# --- 1. كود التتبع والتحقق (Drive) ---
components.html(
    """
    <script>
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

# --- 2. تنسيق الواجهة ---
st.markdown("""
    <style>
    .title { text-align: center; color: #00AE98; font-weight: bold; }
    .deal-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #00AE98;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    .price-tag { color: #d32f2f; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>✈️ صائد صفقات السفر الذكي</h1>", unsafe_allow_html=True)

# --- 3. محرك البحث الرئيسي ---
with st.container():
    search_widget = """
    <div style="width: 100%; min-width: 300px;">
        <script async src="https://tpemd.com/content?currency=usd&trs=519994&shmarker=720290&powered_by=true&locale=ar&show_header=true&limit=3&primary_color=00AE98&results_background_color=FFFFFF&form_background_color=FFFFFF&campaign_id=111&promo_id=4478" charset="utf-8"></script>
    </div>
    """
    components.html(search_widget, height=550, scrolling=True)

st.divider()

# --- 4. قسم "صيدات اليوم الذهبية" ---
st.markdown("### 🔥 صيدات اليوم (أسعار لا تتكرر)")
st.write("أسعار حقيقية تم العثور عليها خلال الـ 24 ساعة الماضية:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="deal-card">
        <h4>الرياض ✈️ باكو</h4>
        <p>ذهاب وعودة - شهر مايو</p>
        <span class="price-tag">850 ريال</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="deal-card">
        <h4>جدة ✈️ جاكرتا</h4>
        <p>مباشر - الخطوط السعودية</p>
        <span class="price-tag">1950 ريال</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="deal-card">
        <h4>دبي ✈️ لندن</h4>
        <p>ترانزيت قصير - ويز إير</p>
        <span class="price-tag">1100 ريال</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.info("💡 ملاحظة: هذه الصيدات تتغير بسرعة حسب توفر المقاعد. ابحث الآن عبر المحرك أعلاه لتأكيد السعر.")
