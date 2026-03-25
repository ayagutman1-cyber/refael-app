app.py


     1 import streamlit as st
     2
     3 # Basic Page Config
     4 st.set_page_config(page_title="Executive Briefing 2026", page_icon="📈", layout="centered")
     5
     6 # Custom CSS for RTL, Rafael Style, and Mobile Optimization
     7 st.markdown("""
     8     <style>
     9     @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
    10
    11     html, body, [data-testid="stSidebar"] {
    12         font-family: 'Assistant', sans-serif;
    13         direction: rtl;
    14         text-align: right;
    15     }
    16     .main { background-color: #f0f2f6; }
    17     .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #003366; color: white; font-weight: bold; border: none; }
    18     .stButton>button:hover { background-color: #004080; border: 1px solid white; }
    19     .stExpander { background-color: white; border-radius: 12px; border: 1px solid #ddd; margin-bottom: 10px; }
    20     h1, h2, h3 { color: #003366; text-align: center; }
    21     p, li, div { text-align: right; }
    22
    23     /* Center sidebar elements for RTL */
    24     [data-testid="stSidebar"] { text-align: right; }
    25     [data-testid="stMarkdownContainer"] > p { text-align: right; }
    26     .stTabs [data-baseweb="tab-list"] { direction: rtl; }
    27     .stTabs [data-baseweb="tab"] { font-size: 1.1em; font-weight: bold; }
    28
    29     /* Info box styling */
    30     .stAlert { border-radius: 12px; }
    31     </style>
    32     """, unsafe_allow_config_with_script=True)
    33
    34 # App Header
    35 st.title("Executive Briefing 2026")
    36 st.subheader("מרכז כשירות ועדכון לדירקטורים")
    37
    38 # Sidebar for Topic Selection
    39 with st.sidebar:
    40
       st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Rafael_Advanced_Defense_Systems_logo.svg/512px-Rafael_Advanced_Defense_Systems_logo.svg
       .png", width=150)
    41     st.header("תחומי לימוד")
    42     topic = st.selectbox("בחר/י נושא למידה:",
    43                          ["רגולציה וחוקיות", "נהלי בקרה ודיווח", "קבלת החלטות אסטרטגיות"])
    44     st.divider()
    45     st.caption("פותח עבור תהליך המיון ברפאל | מרץ 2026")
    46
    47 # Main Interface Tabs
    48 tab_audio, tab_read, tab_case = st.tabs(["🎧 האזנה (Podcast)", "📖 קריאה מהירה", "🧠 מקרה בוחן"])
    49
    50 # Content Mapping
    51 if topic == "רגולציה וחוקיות":
    52     with tab_audio:
    53         st.header("פודקאסט: רגולציה במרחב הדיגיטלי")
    54         st.write("תמצית עדכוני החקיקה בנושא אחריות דירקטורים לאבטחת מידע וסייבר (5 דקות).")
    55         st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    56         st.info("נקודות מפתח: חובת הדיווח המיידי, אחריות אישית נושאי משרה, וקנסות מנהליים.")
    57
    58     with tab_read:
    59         st.header("קריאה מהירה: דגשי רגולציה 2026")
    60         with st.expander("📌 כרטיסייה 1: אחריות אישית בסייבר"):
    61             st.write("דירקטורים נושאים באחריות אישית אם לא הוכח כי התקיים דיון מהותי בסיכוני הסייבר של הארגון לפחות פעם ברבעון.")
    62         with st.expander("📌 כרטיסייה 2: חובת הדיווח המיידי"):
    63             st.write("אירוע 'מהותי' חייב בדיווח לרשות לניירות ערך תוך 24 שעות מרגע הגילוי הראשוני, גם אם טרם הוערך הנזק המלא.")
    64         with st.expander("📌 כרטיסייה 3: אתיקה וציות"):
    65             st.write("נהלים חדשים למניעת שוחד ושחיתות בחוזים בינלאומיים (ISO 37001).")
    66
    67     with tab_case:
    68         st.header("דילמה: הדיווח המעכב")
    69         st.markdown("""
    70         **התרחיש:** מנכ"ל החברה מעדכן אותך (כיו"ר ועדת הביקורת) בשישי בערב על פריצה למאגרי המידע.
    71         הוא מבקש להמתין עם הדיווח לבורסה עד יום שני כדי "לא ליצור פאניקה" וכדי לסיים את בדיקת המומחים.
    72         """)
    73         choice = st.radio("כיצד עליך לפעול כחבר דירקטוריון?",
    74                          ["קבלת עמדת המנכ"ל - הוא איש המקצוע וצריך זמן לבירור", 
    75                           "דרישה לדיווח מיידי לרשות לניירות ערך בהתאם לחוק",
    76                           "כינוס ישיבת דירקטוריון ביום ראשון בבוקר להחלטה משותפת"])
    77
    78         if st.button("בדיקת תשובה - רגולציה"):
    79             if "דרישה לדיווח מיידי" in choice:
    80                 st.success("תשובה נכונה! חובת הדיווח היא אבסולוטית ומידית. השתהות חושפת אותך לתביעות אישיות.")
    81             else:
    82                 st.error("טעות. השהיית דיווח מהותי היא עבירה רגולטורית חמורה.")
    83                 st.warning("מומלץ לעיין שוב ב'כרטיסייה 2: חובת הדיווח המיידי' בלשונית קריאה מהירה.")
    84
    85 elif topic == "נהלי בקרה ודיווח":
    86     with tab_audio:
    87         st.header("פודקאסט: תזרים ובקרת תקציב")
    88         st.write("שיחה עם סמנכ\"ל הכספים על ניהול סיכוני תזרים ודיווח רבעוני (6 דקות).")
    89         st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
    90
    91     with tab_read:
    92         st.header("קריאה מהירה: בקרת פנים")
    93         with st.expander("📊 כרטיסייה 1: חריגות תקציב"):
    94             st.write("כל חריגה מסעיף תקציבי מאושר שמעל ל-5% מחייבת אישור מראש של ועדת הכספים.")
    95         with st.expander("📊 כרטיסייה 2: בקרת איכות הדיווח"):
    96             st.write("יש לוודא הלימה מלאה בין הצהרת המנכ\"ל (Section 302) לבין ממצאי מבקר הפנים.")
    97         with st.expander("📊 כרטיסייה 3: ניהול סיכוני שרשרת אספקה"):
    98             st.write("חובה לבצע הערכת סיכונים שנתית לספקים אסטרטגיים במדינות עם סיכון פוליטי גבוה.")
    99
   100     with tab_case:
   101         st.header("דילמה: האיזון התקציבי")
   102         st.markdown("""
   103         **התרחיש:** חטיבת הטילים מדווחת על חריגה של 12% בתקציב הפיתוח.
   104         מנהל החטיבה מציע 'לקזז' את החריגה מול חיסכון שהושג בחטיבת התחזוקה, מבלי לדווח על כך כחריגה מהותית בדירקטוריון.
   105         """)
   106         choice = st.radio("מהי הפעולה הנכונה?",
   107                          ["אישור הקיזוז - העיקר שהשורה התחתונה של הארגון מאוזנת",
   108                           "דרישה לדיווח מפורט על החריגה המקורית לוועדת הכספים",
   109                           "התעלמות מהנושא כל עוד הפרויקט מתקדם בלוח הזמנים"])
   110
   111         if st.button("בדיקת תשובה - בקרה"):
   112             if "דרישה לדיווח מפורט" in choice:
   113                 st.success("נכון מאוד! שקיפות בסעיפי תקציב היא קריטית לממשל תאגידי תקין. קיזוזים 'מסתירים' כשלים ניהוליים.")
   114             else:
   115                 st.error("טעות. חריגה מעל 5% מחייבת דיווח פורמלי ללא קשר לחיסכון במקום אחר.")
   116                 st.warning("מומלץ לעיין שוב ב'כרטיסייה 1: חריגות תקציב' בלשונית קריאה מהירה.")
   117
   118 elif topic == "קבלת החלטות אסטרטגיות":
   119     with tab_audio:
   120         st.header("פודקאסט: מיזוגים ורכישות (M&A)")
   121         st.write("כיצד לקבל החלטה על רכישה במיליארדי שקלים? ראיון עם יו\"ר רפאל (8 דקות).")
   122         st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3")
   123
   124     with tab_read:
   125         st.header("קריאה מהירה: קבלת החלטות")
   126         with st.expander("🤝 כרטיסייה 1: ניגוד עניינים"):
   127             st.write("בכל עסקה, על הדירקטור להצהיר על כל זיקה (ישירה או עקיפה) לצד השני, כולל קשרים משפחתיים או עסקיים בעבר.")
   128         with st.expander("🤝 כרטיסייה 2: בדיקת נאותות (Due Diligence)"):
   129             st.write("אין לאשר עסקה ללא דוח 'בדיקת נאותות' חיצוני ובלתי תלוי המכסה היבטים פיננסיים, משפטיים וטכנולוגיים.")
   130         with st.expander("🤝 כרטיסייה 3: ראייה ארוכת טווח"):
   131             st.write("אישור החלטות השקעה חייב להתכתב עם התוכנית האסטרטגית לחמש השנים הבאות, ולא רק עם רווח רבעוני.")
   132
   133     with tab_case:
   134         st.header("דילמה: זיקה לא מוצהרת")
   135         st.markdown("""
   136         **התרחיש:** רגע לפני הצבעה על רכישת סטארט-אפ, מתברר לך כי אחד מחברי הדירקטוריון מחזיק במניות בחברת האם של הסטארט-אפ דרך קרן השקעות פרטית. הוא טוען
       שזה 'זניח' ולא משפיע על שיקול דעתו.
   137         """)
   138         choice = st.radio("מה עלייך לעשות?",
   139                          ["להמשיך בהצבעה כרגיל אם הדירקטור מבטיח שהוא אובייקטיבי",
   140                           "לדרוש מהדירקטור לצאת מהחדר ולא להשתתף בדיון ובהצבעה",
   141                           "לדחות את כל העסקה לצמיתות בשל החשש"])
   142
   143         if st.button("בדיקת תשובה - החלטות"):
   144             if "לצאת מהחדר" in choice:
   145                 st.success("נכון! חובת הנאמנות מחייבת נטרול מוחלט של כל חשש לניגוד עניינים. נוכחותו בחדר עלולה להשפיע על אחרים.")
   146             else:
   147                 st.error("טעות. החלטה שהתקבלה בנוכחות אדם עם ניגוד עניינים ניתנת לביטול בבית משפט.")
   148                 st.warning("מומלץ לעיין שוב ב'כרטיסייה 1: ניגוד עניינים' בלשונית קריאה מהירה.")
   149
   150 # Footer and Progress
   151 st.divider()
   152 st.progress(100)
   153 st.caption("מערכת ליווי דירקטורים - גרסה 2.1 | © 2026")

