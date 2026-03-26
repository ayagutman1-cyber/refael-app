import streamlit as st

# הגדרות דף
st.set_page_config(page_title="Rafael Directors Hub", page_icon="🛡️", layout="wide")

# עיצוב RTL ושיפור ויזואלי
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .stApp {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
    }
    .stExpander { background-color: white; border-radius: 8px; border: 1px solid #e1e4e8; }
    h1 { color: #003366; border-bottom: 2px solid #003366; padding-bottom: 10px; }
    h2 { color: #004080; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("מרכז למידה דיגיטלי לדירקטורים | רפאל")

# נושאי הליבה המרכזיים
main_tabs = st.tabs(["⚖️ רגולציה וחוקיות", "📊 נהלי בקרה ודיווח", "🧠 קבלת החלטות"])

# --- פונקציה ליצירת מבנה פנימי לכל נושא ---
def create_module(topic_name, concepts, question, options, correct_answer, audio_url):
    inner_tabs = st.tabs(["📖 קריאה", "🧠 תרגול", "🎧 האזנה"])
    
    with inner_tabs[0]:
        st.subheader(f"מושגי יסוד: {topic_name}")
        for title, detail in concepts.items():
            with st.expander(f"📌 {title}"):
                st.write(detail)
        st.write("---")
        with st.expander("➕ הוספת מושג חדש (עבור מנהל המערכת)"):
            st.write("כאן ניתן להוסיף מושגים ועדכוני חקיקה בזמן אמת.")

    with inner_tabs[1]:
        st.subheader(f"בוחן ידע: {topic_name}")
        st.write(f"**הדילמה:** {question}")
        choice = st.radio("מהי הפעולה הנדרשת?", options, key=topic_name)
        if st.button("בדיקת תשובה", key=f"btn_{topic_name}"):
            if choice == correct_answer:
                st.success("תשובה נכונה! הפעולה תואמת את נהלי הארגון.")
            else:
                st.error("תשובה שגויה. מומלץ לחזור על כרטיסיות המידע.")

    with inner_tabs[2]:
        st.subheader(f"פודקאסט ממוקד: {topic_name}")
        st.info(f"הסבר קולי קצר על {topic_name} (נוצר באמצעות NotebookLM)")
        st.audio(audio_url)

# --- תוכן לכל טאב מרכזי ---

with main_tabs[0]:
    create_module(
        "רגולציה וחוקיות",
        {
            "חובת הזהירות": "על הדירקטור לפעול במיומנות וסבירות, לקבל החלטות על בסיס מידע מלא ולבחון חלופות.",
            "חובת האמונים": "איסור על ניצול הזדמנות עסקית של החברה לטובת רווח אישי ומניעת ניגוד עניינים."
        },
        "דירקטור מגלה שחברה בבעלות אחיו ניגשת למכרז של רפאל. מה עליו לעשות?",
        ["להשתתף בדיון אך לא להצביע", "לדווח מיד ולצאת מהחדר בזמן הדיון", "לא לעשות כלום"],
        "לדווח מיד ולצאת מהחדר בזמן הדיון",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    )

with main_tabs[1]:
    create_module(
        "נהלי בקרה ודיווח",
        {
            "דוחות כספיים": "בחינת המצב הכספי של החברה ואישור שהנתונים משקפים נאמנה את המציאות הכלכלית.",
            "ועדת ביקורת": "פיקוח על הבקרה הפנימית וזיהוי ליקויים בניהול העסקי."
        },
        "התגלה ליקוי משמעותי בבקרה הפנימית של אחת המחלקות. מי הגוף שאחראי לדון בכך?",
        ["ועדת הביקורת", "מחלקת השיווק", "ועדת כוח אדם"],
        "ועדת הביקורת",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    )

with main_tabs[2]:
    create_module(
        "קבלת החלטות",
        {
            "שיקול דעת עסקי": "הגנה משפטית על החלטות שהתקבלו בתום לב, ללא ניגוד עניינים ולאחר הליך סביר.",
            "ניהול סיכונים": "מיפוי סיכונים אסטרטגיים וקביעת רמת התיאבון לסיכון של הארגון."
        },
        "מתי תעמוד לדירקטור 'הגנת שיקול הדעת העסקי'?",
        ["תמיד, ללא קשר לאופן קבלת ההחלטה", "כאשר ההחלטה התקבלה בתום לב ועל בסיס מידע סביר", "רק אם ההחלטה הובילה לרווח"],
        "כאשר ההחלטה התקבלה בתום לב ועל בסיס מידע סביר",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    )


