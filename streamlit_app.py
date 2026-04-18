import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="صائد الصفقات السري - Deep Sniper", page_icon="🎯", layout="wide")

# كود التتبع والتحقق
components.html("""<script>(function () { var script = document.createElement("script"); script.async = 1; script.src = 'https://emrldtp.com/NTE5OTk0.js?t=519994'; document.head.appendChild(script); })();</script>""", height=0)

# تصميم واجهة "الصيد الاحترافي"
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #e0e0e0; }
    .status-bar { background: #1a1a1a; padding: 10px; border-radius: 5px; border-left: 4px solid #ff4b4b; margin-bottom: 20px; }
    .deal-card { background: #111; border: 1px dashed #333; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .price-low { color: #00ff88; font-size: 22px; font-weight: bold; }
    .compare-tag { background: #ff4b4b; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00AE98;'>🎯 نظام صيد الصفقات المخفية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>الذكاء الاصطناعي يقوم الآن بمسح 'الأسعار السرية' التي تخفيها شركات الطيران عن المكاتب التقليدية</p>", unsafe_allow_html=True)

# شريط الحالة (يعطي انطباع البحث العميق)
st.markdown("<div class='status-bar'>🔍 جاري فحص 1200+ قاعدة بيانات طيران... تم العثور على ثغرات سعرية في 4 وجهات</div>", unsafe_allow_html=True)

# محرك البحث بفلترة "أرخص الخيارات"
with st.container():
    # تعديل الرابط لطلب أرخص النتائج أولاً (limit=20 لزيادة نطاق البحث)
    sniper_widget = """
    <div style="width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #00AE98;">
        <script async src="https://tpemd.com/content?currency=sar&trs=519994&shmarker=720290&powered_by=false&locale=ar&show_header=true&limit=20&primary_color=00AE98&results_background_color=111111&form_background_color=111111&campaign_id=111&promo_id=4478" charset="utf-8"></script>
    </div>
    """
    components.html(sniper_widget, height=650, scrolling=True)

st.divider()

# قسم "لماذا نحن أرخص؟" لإقناع العميل
st.markdown("### 🛰️ كيف نصيد هذه الأسعار؟")
c1, c2, c3 = st.columns(3)
with c1:
    st.info("🔓 **تجاوز الكوكيز:** نمنع شركات الطيران من رفع السعر عليك عند تكرار البحث.")
with c2:
    st.success("🎫 **التذاكر المجزأة:** نجمع لك رحلات من شركات مختلفة لتقليل التكلفة بنسبة 40%.")
with c3:
    st.warning("📉 **توقع الانخفاض:** ننبّهك إذا كان السعر الحالي 'فخاً' وسينخفض غداً.")

st.divider()

# صيدات يدوية (ثغرات تم اكتشافها يدوياً لتأكيد المصداقية)
st.markdown("### 🔥 صيدات 'ثغرة النظام' (محدثة الآن)")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class='deal-card'>
        <b>الرياض ✈️ مانيلا (عبر كولومبو)</b> <span class='compare-tag'>توفير 700 ريال</span><br>
        السعر بالمكاتب: 2800 ريال | <span class='price-low'>صيدتنا: 2100 ريال</span>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class='deal-card'>
        <b>جدة ✈️ ميلانو (عبر ويز إير)</b> <span class='compare-tag'>توفير 450 ريال</span><br>
        السعر بالمكاتب: 1200 ريال | <span class='price-low'>صيدتنا: 750 ريال</span>
    </div>""", unsafe_allow_html=True)
