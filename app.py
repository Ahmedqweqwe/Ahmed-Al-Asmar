import streamlit as st

st.set_page_config(page_title="مركز تحميل الملفات المباشر", page_icon="📥", layout="centered")

st.title("🎵🎬 مركز التحميل المباشر للجميع")
st.markdown("### مرحباً بك! يمكنك تحميل الملف المرفوع مباشرة إلى جهازك بنقرة واحدة.")

# ⚠️ ضع هنا الرابط المباشر الذي نسخته من موقع Archive أو أي سيرفر رفع
file_direct_url = "https://soundhelix.com" 

# اسم الملف الذي سيظهر للناس عند التحميل
file_name = "الأغنية المطلوبة.mp3" 

st.markdown("---")

st.success("✅ الملف جاهز للتحميل الفوري لجميع الزوار!")

# مشغل للملف ليسمعه أي شخص يفتح الرابط
st.markdown("#### 🎧 استمع أو شاهد قبل التحميل:")
st.audio(file_direct_url)

# زر التحميل المباشر الذي سيعمل عند كل الناس فوراً
st.markdown("#### 📥 اضغط على الزر أدناه لبدء التنزيل:")
st.link_button("📥 اضغط هنا لتنزيل الملف فوراً", file_direct_url)
