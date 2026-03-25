import streamlit as st

# הגדרות דף
st.set_page_config(page_title="Executive Briefing 2026", page_icon="📈", layout="centered")

# עיצוב RTL לרפאל
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"] {
        font-family: 'Assistant', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .main { background-color: #f0f2f6; }
    div.stButton > button:first-child {
        background-color: #003366;
        color: white;
        border-radius: 12px;
        height: 3.5em;
        width: 100%;
        border: none;
    }
    .stExpander { background-color: white; border-radius: 12px; border: 1px solid #ddd; margin-bottom: 10px; }
    h1, h2, h3 { color: #003366; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("מרכז למידה לדירקטורים - רפאל")
st.subheader("ברוכה הבאה, איה | גרסת MVP 1.0")

tabs = st.tabs(["🎧 האזנה (Listen)", "📖 קריאה (Read)", "🧠 תרגול (Solve)"])

with tabs[0]:
    st.info("פודקאסטים קצרים (3-5 דקות) לעדכון בדרכים")
    st.write("---")
    st.write("🎙️ **פרק 1:** עדכוני רגולציה - מרץ 2026")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.write("🎙️ **פרק 2:** ניהול סיכונים בשרשרת האספקה")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")

with tabs[1]:
    st.write("### כרטיסיות ידע ממוקדות")
    with st.expander("📌 כרטיסיית 1: ניגוד עניינים"):
        st.write("דירקטור חייב להימנע מכל מצב של ניגוד עניינים בין טובתו האישית לבין טובת החברה.")
    with st.expander("📌 כרטיסיית 2: חובת הזהירות"):
        st.write("על הדירקטור לפעול ברמת מיומנות שדירקטור סביר היה פועל בה בנסיבות דומות.")
    with st.expander("📌 כרטיסיית 3: דוחות כספיים"):
        st.write("אחריות הדירקטוריון היא לוודא כי הדוחות משקפים באופן נאות את המצב הכספי.")

with tabs[2]:
    st.write("### סימולציית דילמה ניהולית")
    st.markdown("> **הסיטואציה:** חברה בבעלות קרוב משפחה של אחד מחברי הדירקטוריון מגישה הצעה למכרז משמעותי ברפאל.")
    
    choice = st.radio("מה על הדירקטור לעשות?", [
        "להשתתף בישיבה כרגיל אך להימנע מהצבעה",
        "לדווח מיד על הקשר האישי ולצאת מהחדר בזמן הדיון וההצבעה",
        "לא לעשות כלום, המכרז מנוהל על ידי הדרג המקצועי"
    ])
    
    if st.button("בדיקת תשובה"):
        if "לדווח מיד" in choice:
            st.success("נכון מאוד! שקיפות מלאה ויציאה מהחדר הן הדרך למנוע חשש לניגוד עניינים.")
        else:
            st.error("טעות. השתתפות בדיון, גם ללא הצבעה, עלולה להשפיע על מקבלי ההחלטות.")
            st.warning("מומלץ לעיין שוב בכרטיסיית 'ניגוד עניינים' בלשונית קריאה.")

st.divider()
st.caption("מערכת ליווי דירקטורים | רפאל מערכות לחימה מתקדמות")
