import streamlit as st

st.set_page_config(page_title="موقع رفع الأغاني", page_icon="🎵")

st.title("🎵 مركز رفع وتحميل الأغاني")
st.write("قم برفع ملف الأغنية للحصول على رابط تحميل مباشر فوراً.")

uploaded_file = st.file_uploader("اختر ملف الأغنية (MP3)", type=["mp3", "wav"])

if uploaded_file is not None:
    st.success(f"✅ تم رفع الملف بنجاح: {uploaded_file.name}")
    st.audio(uploaded_file, format="audio/mp3")
    
    st.download_button(
        label="📥 اضغط هنا لتنزيل الأغنية مباشرة",
        data=uploaded_file,
        file_name=uploaded_file.name,
        mime="audio/mp3"
    )
