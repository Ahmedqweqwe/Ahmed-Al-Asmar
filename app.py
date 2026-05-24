import streamlit as st
import os

# 1. إعدادات الصفحة والعنوان
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

st.title("🎵🎬 مركز التحميل المباشر للجميع")
st.markdown("### مرحباً بك! يمكنك تحميل الملف المرفوع مباشرة إلى جهازك بنقرة واحدة.")
st.markdown("---")

# ⚠️ ضع هنا الرابط المباشر لملفك (الملف الحالي تجريبي)
file_direct_url = "https://soundhelix.com" 

# اسم الملف الذي سيظهر للناس عند التحميل
file_name = "حته حشيشة.mp3" 

# 2. ترتيب وعرض الصورة الشخصية والبيانات بجانب بعضها بشكل متناسق
col_profile1, col_profile2 = st.columns([1, 2])

with col_profile1:
    image_name = "1.jpg"
    if os.path.exists(image_name):
        # عرض صورتك الشخصية المرفوعة بحجم متناسق ومناسب
        st.image(image_name, caption="Ahmed Al-Asmar", width=160)
    else:
        # عرض بوستر مؤقت في حال لم ترفع الصورة بعد
        st.image("https://unsplash.com", caption="يرجى رفع صورة 1.jpg", width=160)

with col_profile2:
    st.markdown("### 🎙️ تفاصيل العمل الحالي")
    st.info(f"🎵 **اسم الأغنية:** {file_name.replace('.mp3', '')}")
    st.info("🎤 **المطرب:** Ahmed Al-Asmar")

st.markdown("---")
st.success("✅ الملف جاهز للتحميل الفوري لجميع الزوار!")

# 3. مشغل الصوت للاستماع قبل التحميل
st.markdown("#### 🎧 استمع أو شاهد قبل التحميل:")
st.audio(file_direct_url)

# 4. زر التحميل المباشر الذي سيعمل عند كل الناس فوراً
st.markdown("#### 📥 اضغط على الزر أدناه لبدء التنزيل:")
st.link_button("📥 اضغط هنا لتنزيل الملف فوراً", file_direct_url)

st.markdown("---")

# 5. بيانات التواصل المباشر وأزرار الدردشة عبر واتساب وتليجرام
st.markdown("### 📞 لطلب الأغاني والتواصل المباشر:")
st.warning("📱 **رقم الهاتف:** 01098219874")

phone_number = "201098219874"

col_chat1, col_chat2 = st.columns(2)
with col_chat1:
    st.link_button("🟢 تواصل معي عبر واتساب", f"https://wa.me{phone_number}?text=أهلاً%20أستاذ%20أحمد،%20أريد%20طلب%20أغنية")
with col_chat2:
    st.link_button("🔵 تواصل معي عبر تليجرام", f"https://t.me")

st.markdown("---")

# 6. رابط موقعك العالمي وأزرار مشاركة الرابط للناس
app_url = "https://streamlit.app"

st.markdown("#### 🔗 شارك هذا المركز مع أصدقائك:")
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("🟢 مشاركة الرابط واتساب", f"https://whatsapp.com{app_url}")
with col2:
    st.link_button("🔵 مشاركة الرابط تليجرام", f"https://t.me{app_url}&text=تحميل%20أغنية%20Ahmed%20Al-Asmar%20المباشر")
with col3:
    if st.button("📋 نسخ رابط الموقع"):
        st.toast("📋 تم نسخ الرابط المباشر للموقع!")
        st.code(app_url, language="text")
