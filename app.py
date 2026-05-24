import streamlit as st
import os

# إعدادات الصفحة والعنوان
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

st.title("🎵 مركز تحميل الأغاني المباشر للجميع")
st.markdown("---")

# روابط الملفات التجريبية للأغنية
file_direct_url = "https://soundhelix.com" 

# تقسيم الصفحة إلى جزأين لترتيب الصورة بجانب البيانات بشكل احترافي
col_profile1, col_profile2 = st.columns([1, 2])

with col_profile1:
    image_name = "1.jpg"
    if os.path.exists(image_name):
        # عرض صورتك الشخصية المرفوعة بحجم متناسق ومناسب
        st.image(image_name, caption="الفنان Ahmed Al-Asmar", width=180)
    else:
        # عرض صورة مؤقتة مرتبة لحين رفع صورتك
        st.image("https://unsplash.com", caption="يرجى رفع صورة 1.jpg", width=180)

with col_profile2:
    st.markdown("### 🎙️ البيانات الرسمية للأغنية")
    st.info("🎵 **اسم الأغنية:** حته حشيشة")
    st.info("🎤 **المطرب:** Ahmed Al-Asmar")

st.markdown("---")
st.success("✅ الملف جاهز للتحميل الفوري لجميع الزوار!")

# مشغل الصوت للاستماع
st.markdown("#### 🎧 استمع إلى الأغنية قبل التحميل:")
st.audio(file_direct_url)

# زر التحميل المباشر للزوار
st.markdown("#### 📥 اضغط على الزر أدناه لبدء التنزيل:")
st.link_button("📥 اضغط هنا لتنزيل الأغنية فوراً على جهازك", file_direct_url)

st.markdown("---")

# بيانات التواصل المباشر وأزرار الدردشة
st.markdown("### 📞 لطلب الأغاني والتواصل المباشر:")
st.warning("📱 **رقم الهاتف:** 01098219874")

phone_number = "201098219874"

col_chat1, col_chat2 = st.columns(2)
with col_chat1:
    st.link_button("🟢 تواصل معي عبر واتساب", f"https://wa.me{phone_number}?text=أهلاً%20أستاذ%20أحمد،%20أريد%20طلب%20أغنية")
with col_chat2:
    st.link_button("🔵 تواصل معي عبر تليجرام", f"https://t.me")

st.markdown("---")

# رابط موقعك المباشر وأزرار مشاركة الرابط للناس
app_url = "https://streamlit.app"

st.markdown("#### 🔗 شارك هذه الأغنية مع أصدقائك:")
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("🟢 مشاركة الرابط واتساب", f"https://whatsapp.com{app_url}")
with col2:
    st.link_button("🔵 مشاركة الرابط تليجرام", f"https://t.me{app_url}&text=تحميل%20أغنية%20Ahmed%20Al-Asmar%20المباشر")
with col3:
    if st.button("📋 نسخ رابط الموقع"):
        st.toast("📋 تم نسخ الرابط المباشر!")
        st.code(app_url, language="text")
