import streamlit as st
import os

st.set_page_config(page_title="مركز تحميل الأغاني", page_icon="🎵", layout="centered")

st.title("🎵 مركز تحميل الأغاني المباشر")
st.write("اضغط على الزر أدناه لتنزيل الأغنية مباشرة إلى جهازك:")

# اسم ملف الأغنية الذي رفعته على جيت هاب
song_name = "حته حشيشة.mp3"

if os.path.exists(song_name):
    with open(song_name, "rb") as file:
        st.success(f"✅ الأغنية جاهزة للتحميل: {song_name}")
        st.audio(file, format="audio/mp3")
        
        st.download_button(
            label="📥 اضغط هنا لتنزيل الأغنية مباشرة",
            data=file,
            file_name=song_name,
            mime="audio/mp3"
        )
else:
    st.error("❌ تأكد من رفع ملف الأغنية على GitHub بنفس الاسم تماماً لتظهر هنا.")
