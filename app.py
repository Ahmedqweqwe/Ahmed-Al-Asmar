import streamlit as st
import os

# 1. إعدادات الصفحة والعنوان الرئيسي للموقع
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

st.title("🎵🎬 مركز التحميل المباشر للجميع")
st.markdown("### مرحباً بك! يمكنك تحميل الملف المرفوع مباشرة إلى جهازك بنقرة واحدة.")
st.markdown("---")

# روابط وأسماء الملفات (يمكنك تعديلها لاحقاً لربط أغنيتك الخاصة)
file_direct_url = "https://soundhelix.com" 
file_name = "الأغنية المطلوبة.mp3" 

# 2. ترتيب وعرض الصورة الشخصية والبيانات بجانب بعضها بشكل منسق واحترافي
col_profile1, col_profile2 = st.columns([1, 2])

with col_profile1:
    image_name = "Ahmed Al-Asmar1.jpg"
    if os.path.exists(image_name):
        st.image(image_name, caption="Ahmed Al-Asmar", width=160)
    else:
        st.image("https://unsplash.com", caption="يرجى رفع الصورة", width=160)

with col_profile2:
    st.markdown("### 🎙️ تفاصيل العمل الحالي")
    st.info(f"🎵 **اسم الأغنية:** {file_name.replace('.mp3', '')}")
    st.info("🎤 **المطرب:** Ahmed Al-Asmar")

st.markdown("---")
st.success("✅ الملف جاهز للتحميل الفوري لجميع الزوار!")

# 3. مشغل الصوت للاستماع قبل التحميل
st.markdown("#### 🎧 استمع أو شاهد قبل التحميل:")
st.audio(file_direct_url)

# 4. زر التحميل المباشر الذي سيعمل عند كل الناس فوراً بدون حساب
st.markdown("#### 📥 اضغط على الزر أدناه لبدء التنزيل:")
st.link_button("📥 اضغط هنا لتنزيل الملف فوراً", file_direct_url)

st.markdown("---")

# 5. بيانات التواصل المباشر وأزرار الدردشة الفورية عبر واتساب وتليجرام برقمك
st.markdown("### 📞 لطلب الأغاني والتواصل المباشر:")
st.warning("📱 **رقم الهاتف:** 01098219874")

phone_number = "201098219874"

col_chat1, col_chat2 = st.columns(2)
with col_chat1:
    st.link_button("🟢 تواصل معي عبر واتساب", f"https://wa.me{phone_number}?text=أهلاً%20أستاذ%20أحمد،%20أريد%20طلب%20أغنية")
with col_chat2:
    st.link_button("🔵 تواصل معي عبر تليجرام", f"https://t.me")

st.markdown("---")

# 6. رابط موقعك العالمي وأزرار مشاركة الرابط السريعة للناس
app_url = "https://streamlit.app"


with col2:
        st.code(app_url, language="text")
