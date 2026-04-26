import streamlit as st
from openai import OpenAI
import PyPDF2
import plotly.graph_objects as go
import plotly.express as px
import json
import io

# ─── Client Setup ───────────────────────────────────────────────────────────
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SkillSense AI",
    page_icon="🎯",
    layout="wide"
)

# ─── Custom Styling ─────────────────────────────────────────────────────────
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background: linear-gradient(135deg, #f8f9fa 0%, #e8eef5 100%) !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f8f9fa 0%, #e8eef5 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #ffffff 0%, #f0f4ff 50%, #e8eef5 100%);
    }
    
    .title-text {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    .subtitle-text {
        text-align: center;
        color: #64748b;
        font-size: 1.15rem;
        margin-bottom: 2.5rem;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        border: 2px solid #e0e7ff;
        border-radius: 20px;
        padding: 2rem 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.08);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: #6366f1;
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.15);
        transform: translateY(-2px);
    }
    
    .phase-card {
        background: linear-gradient(135deg, #eef2ff 0%, #f3e8ff 100%);
        border-left: 5px solid #6366f1;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: #1e293b;
        font-weight: 500;
        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.1);
    }
    
    .resource-item {
        background: #ffffff;
        border-left: 4px solid #8b5cf6;
        padding: 1rem;
        margin: 0.8rem 0;
        border-radius: 8px;
        color: #334155;
    }
    
    h1, h2, h3 {
        color: #1e293b !important;
    }
    
    label {
        color: #475569 !important;
        font-weight: 600 !important;
    }
    
    .stTextArea textarea {
        background: #ffffff !important;
        color: #1e293b !important;
        border: 2px solid #e0e7ff !important;
        border-radius: 12px !important;
        font-size: 0.95rem !important;
    }
    
    .stFileUploader {
        border: 2px dashed #8b5cf6 !important;
        border-radius: 12px !important;
        background: rgba(139, 92, 246, 0.03) !important;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    }
    
    .stButton > button:hover {
        box-shadow: 0 6px 25px rgba(99, 102, 241, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    .stChatMessage {
        border-radius: 12px !important;
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        color: #64748b !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: white !important;
    }
    
    .stExpander {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%) !important;
        border: 1px solid #e0e7ff !important;
        border-radius: 12px !important;
    }
    
    .stSpinner > div {
        border-color: #6366f1 !important;
    }
    
    .stWarning, .stError {
        background: rgba(239, 68, 68, 0.1) !important;
        color: #dc2626 !important;
        border-radius: 12px !important;
        border: 1px solid #fecaca !important;
    }
    
    .stSuccess {
        background: rgba(34, 197, 94, 0.1) !important;
        color: #16a34a !important;
        border-radius: 12px !important;
        border: 1px solid #bbf7d0 !important;
    }
    
    .stInfo {
        background: rgba(59, 130, 246, 0.1) !important;
        color: #1e40af !important;
        border-radius: 12px !important;
        border: 1px solid #bfdbfe !important;
    }
</style>
""", unsafe_allow_html=True)

# ─── Session State Init ──────────────────────────────────────────────────────
for key, val in {
    "skill_gaps": [],
    "messages": [],
    "assessment_started": False,
    "assessment_complete": False,
    "skill_scores": {},
    "readiness_score": 0,
    "learning_plan": [],
    "adjacent_skills": [],
    "projects": []
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ─── PDF Extractor ───────────────────────────────────────────────────────────
def extract_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    return " ".join(page.extract_text() or "" for page in reader.pages)

# ─── AI Call ─────────────────────────────────────────────────────────────────
def call_ai(messages, json_mode=False):
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content

# ─── Charts ──────────────────────────────────────────────────────────────────
def show_skill_chart(skill_scores):
    if not skill_scores:
        return
    skills = list(skill_scores.keys())
    scores = list(skill_scores.values())

    fig = go.Figure()
    colors = ['#00d2ff' if s >= 70 else '#7b2ff7' if s >= 40 else '#ff6b6b' for s in scores]
    fig.add_trace(go.Bar(
        x=skills, y=scores,
        marker_color=colors,
        text=scores,
        textposition='outside',
        textfont=dict(size=14, color='white')
    ))
    fig.update_layout(
        title="Skill Proficiency Scores",
        yaxis=dict(range=[0, 100], title="Score", title_font=dict(color='white')),
        xaxis=dict(title_font=dict(color='white')),
        paper_bgcolor='rgba(15,17,23,1)',
        plot_bgcolor='rgba(30,30,50,1)',
        font=dict(color='white', size=12),
        height=400,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
# ─── Learning Plan Display ───────────────────────────────────────────────────
def show_learning_plan(plan):
    for phase in plan:
        with st.expander(f"📌 {phase.get('phase', 'Phase')} — ⏱ {phase.get('duration', '')}"):
            st.markdown(f"**Topics:** {', '.join(phase.get('topics', []))}")
            st.markdown("**Resources:**")
            for r in phase.get('resources', []):
                if r.startswith('http'):
                    st.markdown(f"- 🔗 [{r}]({r})")
                else:
                    st.markdown(f"- 🔗 {r}")

# ─── Generate Final Report ───────────────────────────────────────────────────
def generate_report():
    conversation = "\n".join(
        f"{m['role'].upper()}: {m['content']}"
        for m in st.session_state.messages
        if m['role'] != 'system'
    )

    prompt = f"""You are a calibrated skill assessment expert. Based on this conversation, return ONLY valid JSON with accurate scoring.

{conversation}

SCORING CALIBRATION:
- 0-30: No knowledge or completely vague answers
- 31-50: Basic knowledge, struggled with follow-ups
- 51-70: Good understanding, answered most questions well
- 71-85: Strong knowledge, clear implementation understanding
- 86-100: Expert level, discussed optimizations and scalability

Return ONLY this JSON structure with NO extra text:
{{
  "skill_scores": {{"SkillName": score_integer_0_to_100}},
  "readiness_score": number_0_to_100,
  "skill_gaps": ["skill_name_with_low_score"],
  "adjacent_skills": ["skill1", "skill2", "skill3"],
  "projects": ["NEW project 1", "NEW project 2", "NEW project 3"],
  "learning_plan": [
    {{
      "phase": "Phase 1: Foundations",
      "duration": "2 weeks",
      "topics": ["topic1", "topic2"],
      "resources": ["https://resource1.com", "https://resource2.com"]
    }},
    {{
      "phase": "Phase 2: Practice",
      "duration": "3 weeks",
      "topics": ["topic1"],
      "resources": ["https://resource.com"]
    }},
    {{
      "phase": "Phase 3: Projects",
      "duration": "2 weeks",
      "topics": ["topic1"],
      "resources": ["https://resource.com"]
    }}
  ]
}}"""

    result = call_ai([{"role": "user", "content": prompt}])
    try:
        clean = result.strip().replace("```json", "").replace("```", "").strip()
        data = json.loads(clean)
        st.session_state.skill_scores = data.get("skill_scores", {})
        st.session_state.readiness_score = data.get("readiness_score", 0)
        st.session_state.adjacent_skills = data.get("adjacent_skills", [])
        st.session_state.projects = data.get("projects", [])
        st.session_state.learning_plan = data.get("learning_plan", [])
        st.session_state.skill_gaps = data.get("skill_gaps", [])
        st.session_state.assessment_complete = True
    except:
        st.error("Could not parse assessment report. Please try again.")
# ─── Dashboard ───────────────────────────────────────────────────────────────
def show_gap_chart(skill_scores):
    if not skill_scores:
        return
    strong = sum(1 for s in skill_scores.values() if s >= 70)
    moderate = sum(1 for s in skill_scores.values() if 40 <= s < 70)
    weak = sum(1 for s in skill_scores.values() if s < 40)

    fig = px.pie(
        values=[strong, moderate, weak],
        names=["Strong ✅", "Moderate ⚡", "Gap ❌"],
        color_discrete_sequence=["#6366f1", "#8b5cf6", "#ef4444"],
        hole=0.4
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#1e293b', size=13),
        height=300
    )
    st.plotly_chart(fig, use_container_width=True)

def show_radar_chart(skill_scores):
    if not skill_scores:
        return
    skills = list(skill_scores.keys())
    scores = list(skill_scores.values())
    skills_loop = skills + [skills[0]]
    scores_loop = scores + [scores[0]]

    fig = go.Figure(go.Scatterpolar(
        r=scores_loop, theta=skills_loop,
        fill='toself',
        fillcolor='rgba(99, 102, 241, 0.2)',
        line=dict(color='#6366f1', width=2)
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color='#64748b'),
            angularaxis=dict(color='#1e293b')
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#1e293b'),
        height=350
    )
    st.plotly_chart(fig, use_container_width=True)

def show_dashboard():
    st.markdown("---")
    st.markdown("## 📊 Assessment Dashboard")

    scores = st.session_state.skill_scores
    readiness = st.session_state.readiness_score

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🎯 Job Readiness", f"{readiness}%")
        st.progress(readiness / 100)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        strong = sum(1 for s in scores.values() if s >= 70)
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("✅ Strong Skills", f"{strong}/{len(scores)}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        gaps = sum(1 for s in scores.values() if s < 40)
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("❌ Skill Gaps", gaps)
        st.markdown('</div>', unsafe_allow_html=True)
        # Show Skill Gaps Only If They Exist
    weak_skills = {skill: score for skill, score in scores.items() if score < 40}
    if weak_skills:
        st.markdown("### ⚠️ Skills That Need Improvement")
        for skill, score in weak_skills.items():
            st.warning(f"📍 {skill} — Score: {score}/100")

    st.markdown("### 📈 Skill Analysis")
    tab1, tab2, tab3 = st.tabs(["📊 Bar Chart", "🕸 Radar Chart", "🥧 Gap Analysis"])
    with tab1:
        show_skill_chart(scores)
    with tab2:
        show_radar_chart(scores)
    with tab3:
        show_gap_chart(scores)

    if st.session_state.adjacent_skills:
        st.markdown("### 🚀 Adjacent Skills to Learn Next")
        cols = st.columns(len(st.session_state.adjacent_skills))
        for i, skill in enumerate(st.session_state.adjacent_skills):
            with cols[i]:
                st.info(f"⚡ {skill}")

    if st.session_state.learning_plan:
        st.markdown("### 📚 Personalized Learning Roadmap")
        show_learning_plan(st.session_state.learning_plan)

    if st.session_state.projects:
        st.markdown("### 💡 Suggested Projects to Build")
        for p in st.session_state.projects:
            st.markdown(f'<div class="phase-card">🛠 {p}</div>', unsafe_allow_html=True)
# ─── MAIN APP ────────────────────────────────────────────────────────────────
st.markdown('<div class="title-text">🎯 SkillSense AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Your AI-Powered Skill Assessment & Career Coach</div>', unsafe_allow_html=True)

# Input Section
if not st.session_state.assessment_started:
    st.markdown("### 📋 Step 1: Provide Your Details")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📄 Job Description")
        jd_file = st.file_uploader("Upload JD (PDF)", type=["pdf"], key="jd_file")
        jd_text = st.text_area("Or paste JD here", height=150, key="jd_text")

    with col2:
        st.markdown("#### 📝 Your Resume")
        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"], key="resume_file")
        resume_text = st.text_area("Or paste Resume here", height=150, key="resume_text")

    if st.button("🚀 Start Assessment", use_container_width=True):
        with st.spinner("Analyzing your resume and job description..."):
            jd = extract_pdf_text(jd_file) if jd_file else jd_text
            resume = extract_pdf_text(resume_file) if resume_file else resume_text

            if not jd or not resume:
                st.warning("Please provide both Job Description and Resume!")
            else:
                system_prompt = system_prompt = """You are SkillSense AI — a technical skill assessment expert and career coach.

ASSESSMENT RULES:
1. Ask ONE question at a time — never multiple questions together
2. When a candidate gives a vague or simple answer, do NOT say "tell me more" or "can you elaborate"
3. Instead, ask a SPECIFIC technical follow-up question that tests deeper understanding

FOR EVERY SKILL, assess in this order:
- Implementation: How did they build it? What structure/logic did they use?
- Problem-solving: How did they handle edge cases or errors?
- Scalability: How would they improve or extend it?

EXAMPLE — If candidate says "I made a calculator in Python":
BAD: "Can you share more details about your calculator?"
GOOD: "How did you structure your calculator? Did you use functions, classes, or just conditional statements?"
Then follow up: "How did your program handle invalid inputs like letters or division by zero?"
Then: "If you had to add a GUI or scientific functions, how would you approach that?"

SCORING MINDSET:
- Vague answers = low score (0-40)
- Basic correct answers = medium score (50-65)  
- Detailed implementation knowledge = high score (70-85)
- Optimization and scalability thinking = excellent score (90-100)
Always identify at least (1-2) missing or weak skills based on the job description.

After assessing 5 skills with 2-3 follow-ups each, tell the candidate the assessment is complete and their report is being generated.

Be professional, direct, and technically sharp. Not overly friendly or generic."""

                user_prompt = f"""Job Description:
{jd}

Candidate Resume:
{resume}

Start the assessment by warmly greeting the candidate, briefly explaining what you'll do, then ask your first question about their most important skill. Be conversational and friendly."""

                st.session_state.messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]

                response = call_ai(st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.assessment_started = True
                st.rerun()

# Chat Section
if st.session_state.assessment_started and not st.session_state.assessment_complete:
    st.markdown("### 💬 Skill Assessment Chat")

    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            st.chat_message("assistant", avatar="🤖").write(msg["content"])
        elif msg["role"] == "user" and msg != st.session_state.messages[0] and msg != st.session_state.messages[1]:
            st.chat_message("user", avatar="👤").write(msg["content"])

    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.chat_input("Type your response...")
    with col2:
        if st.button("📊 Generate Report", use_container_width=True):
            with st.spinner("Generating your personalized report..."):
                generate_report()
                st.rerun()

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Assessing skill proficiency..."):
            response = call_ai(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# Dashboard Section
if st.session_state.assessment_complete:
    show_dashboard()

    st.markdown("---")
    if st.button("🔄 Start New Assessment", use_container_width=True):
        for key in ["messages", "assessment_started", "assessment_complete",
            "skill_scores", "readiness_score", "learning_plan",
            "adjacent_skills", "projects", "skill_gaps"]:
            st.session_state[key] = [] if key in ["messages", "learning_plan", "adjacent_skills", "projects"] else False if "started" in key or "complete" in key else {} if key == "skill_scores" else 0
        st.rerun()