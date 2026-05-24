import streamlit as st
import os

# 1. إعدادات الصفحة والعنوان
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

st.title("🎵 مركز تحميل الأغاني المباشر للجميع")
st.markdown("---")

# ⚠️ روابط الملفات (رابط الأغنية التجريبي حالياً)
file_direct_url = "https://soundhelix.com" 

# 2. بيانات الأغنية والمطرب
st.markdown("## 🎙️ الأغنية الحالية")
st.info("🎵 **اسم الأغنية:** حته حشيشة")
st.info("🎤 **اسم المطرب:** Ahmed Al-Asmar")

# 3. عرض صورتك الشخصية المتاحة على سطح المكتب (تم تسميتها 1.jpg بالكود)
image_name = "1.jpg"
if os.path.exists(image_name):
    st.image(image_name, caption="الفنان Ahmed Al-Asmar 📸", use_column_width=True)
else:
    # رابط احتياطي في حال لم يتم رفع الصورة بعد
    st.image("https://unsplash.com", caption="بوستر الأغنية التجريبي 📸", use_column_width=True)

st.markdown("---")
st.success("✅ الملف جاهز للتحميل الفوري لجميع الزوار!")

# 4. مشغل الصوت للاستماع داخل الموقع
st.markdown("#### 🎧 استمع إلى الأغنية قبل التحميل:")
st.audio(file_direct_url)

# 5. زر التحميل المباشر للزوار
st.markdown("#### 📥 اضغط على الزر أدناه لبدء التنزيل:")
st.link_button("📥 اضغط هنا لتنزيل الأغنية فوراً على جهازك", file_direct_url)

st.markdown("---")

# 6. بيانات التواصل المباشر برقم فونك وأزرار الدردشة الفورية
st.markdown("### 📞 لطلب الأغاني والتواصل المباشر:")
st.warning("👤 **الفنان:** Ahmed Al-Asmar\n\n📱 **رقم الهاتف:** 01098219874")

phone_number = "201098219874" # صيغة الرقم الدولية للواتساب

col_chat1, col_chat2 = st.columns(2)
with col_chat1:
    st.link_button("🟢 تواصل معي مباشرة عبر واتساب", f"https://wa.me{phone_number}?text=أهلاً%20أستاذ%20أحمد،%20أريد%20طلب%20أغنية")
with col_chat2:
    st.link_button("🔵 تواصل معي مباشرة عبر تليجرام", f"https://t.me")

st.markdown("---")

# 7. رابط موقعك العالمي وأزرار مشاركة الرابط للناس
app_url = "https://streamlit.app"

st.markdown("#### 🔗 شارك هذه الأغنية مع أصدقائك عبر وسائل التواصل:")
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("🟢 مشاركة الرابط واتساب", f"https://whatsapp.com{app_url}")
with col2:
    st.link_button("🔵 مشاركة الرابط تليجرام", f"https://t.me{app_url}&text=تحميل%20أغنية%20Ahmed%20Al-Asmar%20المباشر")
with col3:
    if st.button("📋 نسخ رابط الموقع"):
        st.toast("📋 تم نسخ الرابط المباشر!")
        st.code(app_url, language="text")
