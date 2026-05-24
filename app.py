import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="مركز رفع ومشاركة الملفات", page_icon="🎬", layout="centered")

st.title("🎵🎬 مركز رفع وتحميل الأغاني والفيديوهات المباشر")
st.markdown("### مرحباً بك! يمكنك رفع أي ملف صوتي أو فيديو هنا ومشاركته فوراً بدون اشتراك.")

# رابط موقعك العالمي
app_url = "https://streamlit.app"

# أزرار المشاركة والتواصل الاجتماعي
st.markdown("#### 🔗 شارك هذا المركز مع أصدقائك:")
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("🟢 شارك عبر واتساب", f"https://whatsapp.com{app_url}")
with col2:
    st.link_button("🔵 شارك عبر تليجرام", f"https://t.me{app_url}&text=مركز%20رفع%20وتحميل%20الأغاني%20والفيديوهات")
with col3:
    if st.button("📋 نسخ رابط الموقع"):
        st.toast("📋 تم نسخ الرابط المباشر للموقع!")
        st.code(app_url, language="text")

st.markdown("---")

# منطقة رفع الملفات (يدعم الأغاني والفيديوهات معاً)
uploaded_file = st.file_uploader(
    "📂 اختر ملف الأغنية أو الفيديو من جهازك (MP3, WAV, MP4, MOV):", 
    type=["mp3", "wav", "mp4", "mov"]
)

if uploaded_file is not None:
    st.success(f"✅ تم رفع الملف بنجاح: {uploaded_file.name}")
    
    # معرفة نوع الملف المرفوع لفتح المشغل المناسب
    file_extension = uploaded_file.name.split(".")[-1].lower()
    
    st.markdown("#### 🎧🎬 استعرض الملف قبل التحميل:")
    if file_extension in ["mp3", "wav"]:
        # مشغل صوت للأغاني
        st.audio(uploaded_file, format="audio/mp3")
        mime_type = "audio/mp3"
    elif file_extension in ["mp4", "mov"]:
        # مشغل فيديو للفيديوهات
        st.video(uploaded_file)
        mime_type = "video/mp4"
        
    # زر التحميل المباشر للزائر
    st.markdown("#### 📥 رابط التحميل المباشر للزائر:")
    st.download_button(
        label="📥 اضغط هنا للتنزيل فوراً على جهازك",
        data=uploaded_file,
        file_name=uploaded_file.name,
        mime=mime_type
    )
