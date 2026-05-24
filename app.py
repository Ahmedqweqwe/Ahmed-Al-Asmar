import streamlit as st
import os

# 1. إعدادات الصفحة والعنوان الرئيسي للموقع
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

# اسم الملف الثابت الذي سيتم حفظ الأغنية المرفوعة به في السيرفر
SAVED_AUDIO_PATH = "current_song.mp3"

# --- لوحة تحكم خاصة بك لرفع الأغنية (مخفية في شريط جانبي بمشغل كلمة مرور) ---
with st.sidebar:
    st.markdown("### 🔐 لوحة تحكم الإدارة")
    password = st.text_input("أدخل كلمة المرور لرفع أغنية جديدة:", type="password")
    
    # يمكنك تغيير كلمة المرور "1234" لأي شيء تريده
    if password == "1234":
        st.success("تم تسجيل الدخول بنجاح!")
        uploaded_file = st.file_uploader("قم برفع الأغنية الجديدة هنا:", type=["mp3"])
        
        if uploaded_file is not None:
            # حفظ الملف المرفوع داخل مجلد الموقع لكي يراه كل الزوار
            with open(SAVED_AUDIO_PATH, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✅ تم تحديث الأغنية بنجاح لجميع الزوار! قم بتحديث الصفحة.")
    elif password != "":
        st.error("كلمة المرور غير صحيحة!")

# --- صفحة العرض للزوار ---

st.title("🎵🎬 مركز التحميل المباشر للجميع")
st.markdown("### مرحباً بك! يمكنك تحميل الملف المرفوع مباشرة إلى جهازك بنقرة واحدة.")
st.markdown("---")

# التحقق من وجود الأغنية المرفوعة، وإلا يتم تشغيل الرابط الافتراضي القديم
if os.path.exists(SAVED_AUDIO_PATH):
    file_name = "الأغنية المطلوبة.mp3"
    
    # قراءة الملف المحفوظ لإرساله للمشغل وزر التحميل
    with open(SAVED_AUDIO_PATH, "rb") as audio_file:
        audio_bytes = audio_file.read()
else:
    # في حال لم ترفع أي أغنية بعد، يعمل الرابط التجريبي تلقائياً
    file_name = "لم يتم رفع أغنية بعد.mp3"
    audio_bytes = "https://soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

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
    st.info(f"🎵 **اسم الأغنية:** {file_name.replace('.mp3', '')}")
    st.info("🎤 **المطرب:** Ahmed Al-Asmar")

st.markdown("---")
st.success("✅ الملف جاهز للتحميل الفوري لجميع الزوار!")

# 3. مشغل الصوت للاستماع قبل التحميل
st.markdown("#### 🎧 استمع قبل التحميل:")
st.audio(audio_bytes)

# 4. زر التحميل المباشر الثابت لجميع الناس فوراً بدون حساب
st.markdown("#### 📥 اضغط على الزر أدناه لبدء التنزيل:")

if os.path.exists(SAVED_AUDIO_PATH):
    st.download_button(
        label="📥 اضغط هنا لتنزيل الملف فوراً",
        data=audio_bytes,
        file_name="Ahmed_Al_Asmar.mp3",
        mime="audio/mp3",
        use_container_width=True
    )
else:
    st.link_button("📥 اضغط هنا لتنزيل الملف الافتراضي", audio_bytes, use_container_width=True)

st.markdown("---")

# 5. بيانات التواصل المباشر وأزرار الدردشة الفورية عبر واتساب وتليجرام برقمك
st.markdown("### 📞 لطلب الأغاني والتواصل المباشر:")
st.warning("📱 **رقم الهاتف:** 01098219874")