import streamlit as st
import os

# 1. إعدادات الصفحة والعنوان الرئيسي للموقع
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

# الملفات الثابتة التي يتم حفظها في السيرفر
SAVED_AUDIO_PATH = "current_song.mp3"
SAVED_INFO_PATH = "song_name.txt"  # ملف نصي صغير لحفظ اسم الأغنية الحقيقي تلقائياً

# --- لوحة تحكم الإدارة (مخفية في الشريط الجانبي) ---
with st.sidebar:
    st.markdown("### 🔐 لوحة تحكم الإدارة")
    password = st.text_input("أدخل كلمة المرور لرفع أغنية جديدة:", type="password")
    
    if password == "1234": # يمكنك تغيير الرقم السري من هنا
        st.success("تم تسجيل الدخول بنجاح!")
        uploaded_file = st.file_uploader("قم برفع الأغنية الجديدة هنا:", type=["mp3"])
        
        if uploaded_file is not None:
            # 1. حفظ ملف الصوت في السيرفر
            with open(SAVED_AUDIO_PATH, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # 2. حفظ اسم الملف الأصلي تلقائياً ليعرض للزوار
            clean_name = uploaded_file.name.replace(".mp3", "").replace("_", " ").strip()
            with open(SAVED_INFO_PATH, "w", encoding="utf-8") as f:
                f.write(clean_name)
                
            st.success("✅ تم تحديث الأغنية واسمها بنجاح لجميع الزوار!")
            st.rerun() # إعادة إنعاش الصفحة فوراً لتطبيق التعديل
            
    elif password != "":
        st.error("كلمة المرور غير صحيحة!")

# --- صفحة العرض التلقائية للزوار ---

st.title("🎵🎬 مركز التحميل المباشر للجميع")
st.markdown("### مرحباً بك! يمكنك تحميل الملف المرفوع مباشرة إلى جهازك بنقرة واحدة.")
st.markdown("---")

# جلب البيانات تلقائياً بناءً على الملف المرفوع
if os.path.exists(SAVED_AUDIO_PATH):
    # قراءة الصوت
    with open(SAVED_AUDIO_PATH, "rb") as audio_file:
        audio_bytes = audio_file.read()
    
    # قراءة اسم الأغنية التلقائي الذي تم حفظه
    if os.path.exists(SAVED_INFO_PATH):
        with open(SAVED_INFO_PATH, "r", encoding="utf-8") as f:
            display_song_name = f.read()
    else:
        display_song_name = "أغنية جديدة"
else:
    # في حال لم يتم رفع أي ملف بعد (حالة افتراضية أولى)
    display_song_name = "جاري تجهيز العمل الفني الجديد..."
    audio_bytes = "https://soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# 2. ترتيب وعرض الصورة الشخصية والبيانات بجانب بعضها بشكل تلقائي
col_profile1, col_profile2 = st.columns([1, 2])

with col_profile1:
    image_name = "Ahmed Al-Asmar1.jpg"
    # تظهر صورة الفنان تلقائياً إذا كانت مرفوعة بجانب الكود، وإلا تظهر صورة ميكروفون افتراضية احترافية
    if os.path.exists(image_name):
        st.image(image_name, caption="Ahmed Al-Asmar", width=160)
    else:
        st.image("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=400", caption="المطرب أحمد الأسمر", width=160)

with col_profile2:
    st.markdown("### 🎙️ تفاصيل العمل الحالي")
    st.info(f"🎵 **اسم الأغنية:** {display_song_name}")
    st.info("🎤 **المطرب:** Ahmed Al-Asmar")

st.markdown("---")
st.success("✅ الملف جاهز للاستماع والتحميل الفوري لجميع الزوار!")

# 3. مشغل الصوت التلقائي
st.markdown("#### 🎧 استمع قبل التحميل:")
st.audio(audio_bytes)

# 4. زر التحميل المباشر التلقائي
st.markdown("#### 📥 اضغط على الزر أدناه لبدء التنزيل:")

if os.path.exists(SAVED_AUDIO_PATH):
    st.download_button(
        label=f"📥 اضغط هنا لتنزيل ({display_song_name}) فوراً",
        data=audio_bytes,
        file_name=f"{display_song_name}.mp3",
        mime="audio/mp3",
        use_container_width=True
    )
else:
    st.link_button("📥 اضغط هنا لتنزيل الملف التجريبي", audio_bytes, use_container_width=True)

st.markdown("---")

# 5. بيانات التواصل المباشر
st.markdown("### 📞 لطلب الأغاني والتواصل المباشر:")
st.warning("📱 **رقم الهاتف:** 01098219874")