import streamlit as st
import streamlit.components.v1 as components

# إضافة كود التتبع الخاص بالمنصة الربحية
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
    height=0, # نجعله مخفياً لأنه كود تتبع وليس واجهة
)
import requests

# إعدادات الصفحة الاحترافية
st.set_page_config(
    page_title="صائد صفقات السفر | Travel Sniper AI",
    page_icon="✈️",
    layout="wide"
)

# بيانات الربط مع API (تأكد من تفعيل Skyscanner في RapidAPI)
RAPID_API_KEY = "0a189d02cemsh7cf29bb265f5c0ep1917c5jsn8dcc2b79af10"
RAPID_API_HOST = "skyscanner44.p.rapidapi.com"

# تصميم الواجهة (UI)
st.title("✈️ صائد صفقات السفر الذكي")
st.markdown("### نظام رصد الرحلات وحل مشكلات السفر آلياً")
st.info("هذا التطبيق يساعدك في العثور على أرخص الرحلات العالمية باستخدام الذكاء الاصطناعي.")

st.divider()

# منطقة إدخال البيانات
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        origin = st.text_input("من (رمز المطار - مثال: RUH):", "RUH")
    with col2:
        dest = st.text_input("إلى (رمز المطار - مثال: DXB):", "DXB")
    with col3:
        date = st.text_input("التاريخ (YYYY-MM-DD):", "2026-06-15")

st.divider()

# زر البحث وتحقيق الربح
if st.button("اقتناص أفضل سعر الآن 💰"):
    with st.spinner('جاري فحص قواعد البيانات العالمية...'):
        url = f"https://{RAPID_API_HOST}/search-extended"
        
        # تصحيح الـ Querystring الذي كان به مشكلة
        querystring = {
            "origin": origin, 
            "destination": dest, 
            "departureDate": date, 
            "currency": "SAR"
        }
        
        headers = {
            "x-rapidapi-key": RAPID_API_KEY,
            "x-rapidapi-host": RAPID_API_HOST
        }
        
        try:
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
            
            if response.status_code == 200:
                st.success("تم العثور على عروض مذهلة!")
                
                # هنا نعرض النتائج بشكل مبسط (يمكن تطويرها لاحقاً لعرض الصور والأسعار)
                st.write("نتائج البحث الخام (سيتم تحويلها لواجهة احترافية عند الحجز):")
                st.json(data)
                
                st.divider()
                # زر الحجز (الذي ستضع فيه رابط العمولة الخاص بك لاحقاً للربح)
                st.markdown("### [اضغط هنا للحجز بأرخص سعر مضمون 🎫](#)")
                st.caption("سيتم توجيهك لموقع الحجز الرسمي لإتمام العملية.")
            else:
                st.error("فشل الاتصال بـ API. تأكد من مفتاح الربط أو اشتراكك في الخطة المجانية.")
                
        except Exception as e:
            st.error(f"حدث خطأ غير متوقع: {e}")

st.divider()
st.caption("تطوير وتصميم: Travel Sniper AI Team")
