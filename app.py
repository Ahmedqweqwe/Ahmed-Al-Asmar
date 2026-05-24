import streamlit as st
import os

# 1. إعدادات الصفحة والعنوان الرئيسي للموقع
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

st.title("🎵🎬 مركز التحميل المباشر للجميع")
st.markdown("### مرحباً بك! يمكنك تحميل الملف المرفوع مباشرة إلى جهازك بنقرة واحدة.")
st.markdown("---")

# --- الجزء الجديد: زر رفع الأغاني ---
st.markdown("### 📤 قسم رفع الأغاني الجديد")
uploaded_file = st.file_uploader("اختر ملف الأغنية من جهازك (MP3, WAV, OGG):", type=["mp3", "wav", "ogg"])
st.markdown("---")

# روابط وأسماء الملفات الافتراضية
default_file_url = "https://soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # رابط تجريبي يعمل مباشرة
file_name = "الأغنية المطلوبة.mp3"
audio_data = default_file_url

# التحقق مما إذا قام المستخدم برفع ملف جديد
if uploaded_file is not None:
    file_name = uploaded_file.name
    audio_data = uploaded_file.read() # قراءة بيانات الملف المرفوع

# 2. ترتيب وعرض الصورة الشخصية والبيانات بجانب بعضها بشكل منسق واحترافي
col_profile1, col_profile2 = st.columns([1, 2])

with col_profile1:
    image_name = "Ahmed Al-Asmar1.jpg"
    if os.path.exists(image_name):
        st.image(image_name, caption="Ahmed Al-Asmar", width=160)
    else:
        st.image("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=400", caption="صورة افتراضية", width=160)

with col_profile2:
    st.markdown("### 🎙️ تفاصيل العمل الحالي")
    st.info(f"🎵 **اسم الأغنية:** {file_name.replace('.mp3', '').replace('.wav', '').replace('.ogg', '')}")
    st.info("🎤 **المطرب:** Ahmed Al-Asmar")

st.markdown("---")
st.success("✅ الملف جاهز للاستماع والتحميل الفوري لجميع الزوار!")

# 3. مشغل الصوت للاستماع قبل التحميل (يتغير حسب الملف المرفوع)
st.markdown("#### 🎧 استمع قبل التحميل:")
st.audio(audio_data)

# 4. زر التحميل المباشر
st.markdown("#### 📥 اضغط على الزر أدناه لبدء التنزيل:")

# إذا كان الملف مرفوعاً من الجهاز نستخدم download_button، وإذا كان رابطاً نستخدم link_button
if uploaded_file is not None:
    st.download_button(
        label="📥 اضغط هنا لتنزيل الملف المرفوع فوراً",
        data=audio_data,
        file_name=file_name,
        mime=f"audio/{file_name.split('.')[-1]}"
    )
else:
    st.link_button("📥 اضغط هنا لتنزيل الملف الافتراضي", default_file_url)

st.markdown("---")

# 5. بيانات التواصل المباشر وأزرار الدردشة الفورية عبر واتساب وتليجرام برقمك
st.markdown("### 📞 لطلب الأغاني والتواصل المباشر:")
st.warning("📱 **رقم الهاتف:** 01098219874")