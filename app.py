import streamlit as st
import os
import urllib.parse

# 1. إعدادات الصفحة والعنوان الرئيسي للموقع
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

# الملفات الثابتة التي يتم حفظها في السيرفر
SAVED_AUDIO_PATH = "current_song.mp3"
SAVED_INFO_PATH = "song_name.txt"
SAVED_SHORT_URL_PATH = "short_url.txt" # ملف لحفظ الرابط المختصر

# دالة برمجية سريعة لتوليد رابط TinyURL مختصر بدون مكتبات معقدة
def get_tinyurl(long_url):
    try:
        # نستخدم خدمة tinyurl المجانية عبر طلب بسيط
        api_url = f"http://tinyurl.com/api-create.php?url={urllib.parse.quote(long_url)}"
        import requests
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None

# --- لوحة تحكم الإدارة (مخفية في الشريط الجانبي) ---
with st.sidebar:
    st.markdown("### 🔐 لوحة تحكم الإدارة")
    password = st.text_input("أدخل كلمة المرور لرفع أغنية جديدة:", type="password")
    
    if password == "1234": # يمكنك تغيير الرقم السري من هنا
        st.success("تم تسجيل الدخول بنجاح!")
        
        # خانة لوضع رابط الموقع الحالي ليتم اختصاره
        my_website_url = st.text_input("ضع رابط موقعك الحالي هنا (لاختصاره):", placeholder="https://xxxx.streamlit.app")
        
        uploaded_file = st.file_uploader("قم برفع الأغنية الجديدة هنا:", type=["mp3"])
        
        if uploaded_file is not None:
            # 1. حفظ ملف الصوت في السيرفر
            with open(SAVED_AUDIO_PATH, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # 2. حفظ اسم الملف الأصلي تلقائياً
            clean_name = uploaded_file.name.replace(".mp3", "").replace("_", " ").strip()
            with open(SAVED_INFO_PATH, "w", encoding="utf-8") as f:
                f.write(clean_name)
            
            # 3. عمل الرابط المختصر تلقائياً لو تم إدخال رابط الموقع
            if my_website_url:
                shortened = get_tinyurl(my_website_url)
                if shortened:
                    with open(SAVED_SHORT_URL_PATH, "w", encoding="utf-8") as f:
                        f.write(shortened)
                    st.info(f"🔗 الرابط المختصر الجديد الخاص بك: {shortened}")
                
            st.success("✅ تم تحديث الأغنية وتهيئة الرابط بنجاح!")
            st.rerun()
            
    elif password != "":
        st.error("كلمة المرور غير صحيحة!")

# --- صفحة العرض التلقائية للزوار ---

st.title("🎵🎬 مركز التحميل المباشر للجميع")
st.markdown("### مرحباً بك! يمكنك تحميل الملف المرفوع مباشرة إلى جهازك بنقرة واحدة.")
st.markdown("---")

# جلب البيانات تلقائياً
if os.path.exists(SAVED_AUDIO_PATH):
    with open(SAVED_AUDIO_PATH, "rb") as audio_file:
        audio_bytes = audio_file.read()
    
    if os.path.exists(SAVED_INFO_PATH):
        with open(SAVED_INFO_PATH, "r", encoding="utf-8") as f:
            display_song_name = f.read()
    else:
        display_song_name = "أغنية جديدة"
else:
    display_song_name = "جاري تجهيز العمل الفني الجديد..."
    audio_bytes = "https://soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# عرض زر نسخ الرابط المختصر في صفحة الإدارة أو للزوار لو أحببت (هنا يظهر في الأعلى لو تم إنشاؤه)
if os.path.exists(SAVED_SHORT_URL_PATH) and password == "1234":
    with open(SAVED_SHORT_URL_PATH, "r", encoding="utf-8") as f:
        saved_short_url = f.read()
    st.code(f"الرابط المختصر لنشره: {saved_short_url}", language="text")

# 2. الصورة الشخصية والبيانات بجانب بعضها
col_profile1, col_profile2 = st.columns([1, 2])

with col_profile1:
    image_name = "Ahmed Al-Asmar1.jpg"
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

# 3. مشغل الصوت
st.markdown("#### 🎧 استمع قبل التحميل:")
st.audio(audio_bytes)

# 4. زر التحميل المباشر
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