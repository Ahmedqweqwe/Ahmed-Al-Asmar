import streamlit as st
import os
import urllib.parse
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TCOP, WXXX, COMM

# 1. إعدادات الصفحة والعنوان الرئيسي للموقع
st.set_page_config(page_title="مركز تحميل الأغاني الرسمي", page_icon="🎵", layout="centered")

# الملفات الثابتة التي يتم حفظها في السيرفر
SAVED_AUDIO_PATH = "current_song.mp3"
SAVED_INFO_PATH = "song_name.txt"
SAVED_SHORT_URL_PATH = "short_url.txt"

# دالة برمجية سريعة لتوليد رابط TinyURL مختصر
def get_tinyurl(long_url):
    try:
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
    st.markdown("### 🔐 لوحة تحكم الإدارة والحقوق")
    password = st.text_input("أدخل كلمة المرور لرفع أغنية جديدة:", type="password")
    
    if password == "1234": # يمكنك تغيير الرقم السري من هنا
        st.success("تم تسجيل الدخول بنجاح!")
        
        my_website_url = st.text_input("ضع رابط موقعك الحالي هنا (لاختصاره):", placeholder="https://xxxx.streamlit.app")
        uploaded_file = st.file_uploader("قم برفع الأغنية الجديدة هنا:", type=["mp3"])
        
        if uploaded_file is not None:
            # 1. حفظ ملف الصوت المؤقت في السيرفر
            with open(SAVED_AUDIO_PATH, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # 2. تنظيف اسم الملف تلقائياً وعرضه بشكل منسق
            clean_name = uploaded_file.name.replace(".mp3", "").replace("_", " ").strip()
            with open(SAVED_INFO_PATH, "w", encoding="utf-8") as f:
                f.write(clean_name)
            
            # 3. 🛡️ إضافة حقوق الطبع والنشر الرقمية بداخل كود ملف الـ MP3 تلقائياً (تأمين دون حظر)
            try:
                audio = MP3(SAVED_AUDIO_PATH, ID3=ID3)
                try:
                    audio.add_tags()
                except:
                    pass
                
                # إضافة الميتا داتا (Metadata) لحماية ملكية الفنان
                audio.tags.add(TIT2(encoding=3, text=clean_name))                             # اسم الأغنية
                audio.tags.add(TPE1(encoding=3, text="Ahmed Al-Asmar"))                       # اسم الفنان
                audio.tags.add(TCOP(encoding=3, text="© 2026 Ahmed Al-Asmar. All Rights Reserved.")) # نص حق الطبع والنشر
                audio.tags.add(WXXX(encoding=3, desc="Official Website", url=my_website_url if my_website_url else "https://streamlit.io")) 
                audio.tags.add(COMM(encoding=3, lang="ara", desc="حقوق الملكية", text="تم الرفع عبر المركز الرسمي للمطرب أحمد الأسمر.")) 
                
                audio.save()
                st.sidebar.success("🛡️ تم دمج حقوق الملكية الرقمية داخل ملف الـ MP3!")
            except Exception as e:
                st.sidebar.error(f"تنبيه: تم حفظ الملف ولكن لم يتم تشفير الحقوق الداخلية بسبب: {e}")
            
            # 4. عمل الرابط المختصر تلقائياً
            if my_website_url:
                shortened = get_tinyurl(my_website_url)
                if shortened:
                    with open(SAVED_SHORT_URL_PATH, "w", encoding="utf-8") as f:
                        f.write(shortened)
                    st.info(f"🔗 الرابط المختصر الجديد: {shortened}")
                
            st.success("✅ تم تحديث الأغنية وتأمين الحقوق بنجاح!")
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

# عرض زر نسخ الرابط المختصر في صفحة الإدارة عند تسجيل الدخول
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

# --- ⚖️ قسم الترحيب بالنشر وصناعة التريند (الآمن 100% للجمهور) ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #888888; font-size: 13px; border: 1px dashed #4A4A4A; padding: 10px; border-radius: 5px;">
        <p>⚖️ <b>حقوق الملكية والنشر:</b></p>
        <p>جميع الحقوق الفكرية محفوظة للمطرب <b>أحمد الأسمر © 2026</b>.</p>
        <p>🎬 <b>صناع المحتوى والمبدعين:</b> مسموح ومرحب جداً باستخدام هذه الأغنية في فيديوهاتكم على (تيك توك، يوتيوب، إنستغرام) لدعم العمل الفني، الأغنية آمنة 100% ولا تسبب أي مخالفات لحساباتكم! انطلقوا 🚀🎵</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown("---")

# 5. بيانات التواصل المباشر
st.markdown("### 📞 لطلب الأغاني والتواصل المباشر:")
st.warning("📱 **رقم الهاتف:** 01098219874")