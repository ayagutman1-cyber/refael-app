import streamlit as st

# הגדרות דף
st.set_page_config(page_title="Rafael Directors Hub", page_icon="🛡️", layout="centered")

# עיצוב RTL נקי
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .stApp {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
    }
    .concept-card {
        background-color: #ffffff;
        padding: 15px;
        border-right: 5px solid #003366;
        border-radius: 5px;
        margin-bottom: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("מרכז למידה דיגיטלי לדירקטורים | רפאל")
st.write("---")

# יצירת שלוש הקוביות המרכזיות כטאבים
tabs = st.tabs(["⚖️ רגולציה וחוקיות", "📊 נהלי בקרה ודיווח", "🧠 קבלת החלטות"])

# --- נושא 1: רגולציה וחוקיות ---
with tabs[0]:
    st.markdown("### מאגר מושגים: רגולציה וחוקיות")
    st.info("לחצי על המושג כדי להרחיב את ההסבר המפורט")
    
    with st.expander("📌 חובת הזהירות (Duty of Care)"):
        st.write("**המושג:** דרישה מהדירקטור לפעול במיומנות וסבירות.")
        st.write("**הסבר מפורט:** על הדירקטור לקבל החלטות על בסיס מידע מלא, לבחון חלופות ולהתייעץ עם מומחים במידת הצורך כדי למנוע רשלנות בניהול נכסי החברה.")

    with st.expander("📌 חובת האמונים (Duty of Loyalty)"):
        st.write("**המושג:** עשיית פעולות לטובת החברה בלבד.")
        st.write("**הסבר מפורט:** איסור על ניצול הזדמנות עסקית של החברה לטובת רווח אישי וקביעת מנגנונים למניעת ניגוד עניינים.")

    with st.expander("📌 [מושג נוסף - להשלמה לעתיד]"):
        st.write("כאן יתווספו תכנים רגולטוריים נוספים בהתאם לעדכוני החקיקה האחרונים.")

# --- נושא 2: נהלי בקרה ודיווח ---
with tabs[1]:
    st.markdown("### מאגר מושגים: נהלי בקרה ודיווח")
    
    with st.expander("📊 דוחות כספיים רבעוניים"):
        st.write("**המושג:** אחריות הדירקטוריון על נאותות הדיווח.")
        st.write("**הסבר מפורט:** בחינת הרווח וההפסד, תזרים המזומנים ווידוא שהנתונים משקפים את המציאות הכלכלית של הארגון ללא הצגות מטעות.")

    with st.expander("📊 ועדת ביקורת (Audit Committee)"):
        st.write("**המושג:** הגוף המפקח על הבקרה הפנימית.")
        st.write("**הסבר מפורט:** תפקיד הוועדה לבחון ליקויים בניהול העסקי של החברה ולהציע דרכים לתיקונם בשיתוף המבקר הפנימי.")

    with st.expander("📊 [קוביה ריקה להרחבה]"):
        st.write("בשלב הייצור, כאן יוטמעו נהלי הדיווח הספציפיים של רפאל.")

# --- נושא 3: תהליכי קבלת החלטות ---
with tabs[2]:
    st.markdown("### מאגר מושגים: קבלת החלטות ארגונית")
    
    with st.expander("🧠 שיקול דעת עסקי (Business Judgment Rule)"):
        st.write("**המושג:** הגנה משפטית על החלטות שהתקבלו בתום לב.")
        st.write("**הסבר מפורט:** בתי המשפט לא יתערבו בהחלטה עסקית של דירקטור אם הוכח שהיא התקבלה באופן מיודע, ללא ניגוד עניינים ובתום לב לטובת התאגיד.")

    with st.expander("🧠 ניהול סיכונים אסטרטגי"):
        st.write("**המושג:** שקלול סיכונים מול הזדמנויות.")
        st.write("**הסבר מפורט:** תהליך קבלת החלטות הכולל מיפוי סיכונים (פיננסיים, תפעוליים, תדמיתיים) וקביעת רמת התיאבון לסיכון של הארגון.")

    with st.expander("🧠 [קוביה ריקה להרחבה]"):
        st.write("כאן יפותחו סימולציות לקבלת החלטות במצבי משבר.")

st.sidebar.title("עזרים לדירקטור")
st.sidebar.markdown("### 🎙️ פודקאסט AI (NotebookLM)")
st.sidebar.info("פרק שבועי: 'ניתוח רגולציה 2026' - נוצר אוטומטית ממסמכי המדיניות.")
st.sidebar.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.divider()
st.caption("מערכת ליווי דירקטורים | גרסת אב-טיפוס פדגוגית")
