import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Attention Predictor",
    page_icon="🧠",
    layout="centered"
)

# ---------------- USER PROFILES ----------------
PROFILES = {
    "Student": {
        "decay": 0.4,
        "noise_pen": 2.5,
        "description": "Optimized for study sessions, exams, and learning quality."
    },
    "Employee": {
        "decay": 0.6,
        "noise_pen": 1.5,
        "description": "Optimized for office work and productivity."
    },
    "General": {
        "decay": 0.5,
        "noise_pen": 2.0,
        "description": "Optimized for daily activities and well-being."
    }
}

# ---------------- CORE LOGIC ----------------


def calculate_attention_student(work_mins, breaks, noise, fatigue,
                                subject_difficulty, study_type, exam_days):
    score = 100
    reasons = []

    score -= work_mins * PROFILES["Student"]["decay"]
    score -= noise * PROFILES["Student"]["noise_pen"]
    score -= fatigue * 3.0
    score += breaks * 15

    if work_mins > 90:
        reasons.append("Long continuous study")

    if subject_difficulty == "Hard":
        score -= 15
        reasons.append("Difficult subject")

    if study_type == "New Topic":
        score -= 10
        reasons.append("Studying new topic")

    if exam_days <= 7:
        score -= 20
        reasons.append("Exam very close")
    elif exam_days <= 14:
        score -= 10
        reasons.append("Exam approaching")

    return max(0, min(100, score)), reasons


def calculate_attention_generic(work_mins, breaks, noise, fatigue, user_type):
    rules = PROFILES[user_type]
    score = 100
    reasons = []

    score -= work_mins * rules["decay"]
    score -= noise * rules["noise_pen"]
    score -= fatigue * 3.0
    score += breaks * 15

    if work_mins > 90:
        reasons.append("Long continuous work")
    if noise > 6:
        reasons.append("High noise")
    if fatigue > 6:
        reasons.append("High fatigue")

    return max(0, min(100, score)), reasons


def get_recommendation(score, user_type):
    if score < 40:
        if user_type == "Student":
            return "⚠️ CRITICAL: Stop studying. Rest or sleep before continuing."
        elif user_type == "Employee":
            return "⚠️ BURNOUT RISK: Take a break or step away from the screen."
        else:
            return "⚠️ EXHAUSTED: Take proper rest."
    elif score < 70:
        return "📉 Focus is dropping. Try short sessions with breaks."
    else:
        return "✅ Flow state detected. Keep going wisely."


# ---------------- UI ----------------
st.title("🧠 AI Attention Predictor")
st.markdown("### Rule-Based Expert System (Explainable AI)")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("👤 User Profile")
    user_type = st.radio(
        "Select your role:",
        ["Student", "Employee", "General"]
    )

    st.info(PROFILES[user_type]["description"])
    st.write(f"Decay Rate: **{PROFILES[user_type]['decay']}**")
    st.write(f"Noise Sensitivity: **{PROFILES[user_type]['noise_pen']}x**")

    # ---- CREDIT SECTION ----
    st.markdown("---")
    st.markdown("""
📌 **Project By**  
**Keisham Roshkumar Singh**  
MCA Student
""")

# ---------------- INPUT FORM ----------------
with st.form("attention_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔧 Input Factors")

        work_mins = st.slider(
            "⏱️ Continuous Work / Study (minutes)", 0, 240, 45)
        breaks = st.slider("☕ Breaks Taken", 0, 5, 0)
        noise = st.slider("🔊 Noise Level (0-10)", 0, 10, 2)
        fatigue = st.slider("🔋 Fatigue Level (1-10)", 1, 10, 3)

        if user_type == "Student":
            subject_difficulty = st.selectbox(
                "📘 Subject Difficulty",
                ["Easy", "Medium", "Hard"]
            )
            study_type = st.selectbox(
                "📝 Study Type",
                ["Revision", "New Topic"]
            )
            exam_days = st.slider(
                "📅 Days Until Exam",
                0, 60, 15
            )

    submit = st.form_submit_button("🔍 Analyze Attention")

# ---------------- ANALYSIS ----------------
if submit:

    if user_type == "Student":
        score, reasons = calculate_attention_student(
            work_mins, breaks, noise, fatigue,
            subject_difficulty, study_type, exam_days
        )
    else:
        score, reasons = calculate_attention_generic(
            work_mins, breaks, noise, fatigue, user_type
        )

    recommendation = get_recommendation(score, user_type)

    # ---------------- OUTPUT ----------------
    with col2:
        st.subheader("📊 AI Prediction")

        st.metric("Focus Score", f"{int(score)}/100")
        st.progress(int(score))

        if score >= 70:
            quality = "Excellent 🌟"
        elif score >= 50:
            quality = "Good ✅"
        elif score >= 40:
            quality = "Fair ⚠️"
        else:
            quality = "Poor ❌"

        label = (
            "📘 Learning Quality" if user_type == "Student"
            else "💼 Work Performance" if user_type == "Employee"
            else "🌱 Daily Focus & Well-being"
        )

        st.write(f"**{label}:** {quality}")
        st.info(recommendation)

        if reasons:
            st.write("**Factors Affecting Attention:**")
            for r in reasons:
                st.write("•", r)

    # ---------------- LOGIC TRACE ----------------
    with st.expander("🔍 See How the AI Decided"):
        st.code(f"""
USER TYPE: {user_type}
Base Score: 100
Time Worked: {work_mins} minutes
Noise Level: {noise}
Fatigue Level: {fatigue}
Breaks Taken: {breaks}

FINAL SCORE = {score:.1f}
""")
