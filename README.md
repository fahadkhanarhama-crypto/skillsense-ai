# skillsense-ai
SkillSense AI is a Streamlit-based system that evaluates real skill proficiency by comparing resumes with job descriptions. It uses conversational assessment, skill scoring, gap analysis, and adjacent skill intelligence to generate personalized, time-bound learning plans with visual insights.
# 🎯 SkillSense AI — Skill Assessment & Personalized Learning Agen

## 📌 Problem Statement
A resume tells you what someone *claims* to know — not how well they actually know it. SkillSense AI bridges this gap by conversationally assessing real proficiency on each required skill, identifying gaps, and generating a personalized learning roadmap.

## 🚀 Live Demo
https://skillsense-ai-6urfevr9akha5qyelbfbgd.streamlit.app/

## 🎥 Demo Video
[Add your video link here]

## ✨ Features
- 📄 Upload Resume + Job Description (PDF or text)
- 🤖 AI-powered conversational skill assessment
- 📊 Visual skill proficiency charts (Bar, Radar, Pie)
- 🎯 Job Readiness Score (0–100)
- 🚀 Adjacent skill suggestions
- 📚 Personalized 3-phase learning roadmap with clickable resources
- 💡 New project suggestions tailored to your skill level

## 🧠 Scoring Logic
Each skill is assessed across 3 dimensions:
| Dimension | Description |
|-----------|-------------|
| Implementation | How the candidate built or used the skill |
| Problem-solving | How they handled edge cases and errors |
| Scalability | How they would improve or extend their work |

Score Breakdown:
- 0–40: Vague or no understanding
- 41–65: Basic working knowledge
- 66–85: Strong implementation knowledge

**#Architecture:**

User Input (JD + Resume) -> Text Extraction (PyPDF2) -> System Prompt Builder -> OpenRouter API (GPT-4o-mini) -> Conversational Assessment Engine -> JSON Report Generator -> Dashboard (Plotly Charts + Learning Plan)

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Model:** GPT-4o-mini via OpenRouter API
- **Charts:** Plotly
- **PDF Parsing:** PyPDF2
- **Language:** Python 3.12

## ⚙️ Local Setup
1. Clone the repo:
git clone https://github.com/fahadkhanarhama-crypto/skill-assess-agent.git
cd skill-assess-agent

2. Install dependencies:
pip install streamlit openai plotly PyPDF2

3. Add your OpenRouter API key in `app.py`

4. Run the app:
streamlit run app.py

## 📁 Sample Inputs
**Sample JD:** We are looking for a motivated and enthusiastic **Web Development Intern** who is eager to learn, build, and grow in a fast-paced environment. The ideal candidate should have a passion for web technologies and a strong willingness to turn ideas into functional, user-friendly websites.

### **Key Responsibilities**
* Assist in the design and development of responsive websites and web applications
* Write clean, efficient, and well-documented code
* Collaborate with designers and backend developers
* Test and debug websites to ensure smooth performance
* Optimize websites for speed and scalability
* Stay updated with the latest web development trends and technologies

### **Required Skills**
* Basic knowledge of **HTML, CSS, and JavaScript**
* Familiarity with frontend frameworks like **React.js / Angular / Vue.js** (preferred but not mandatory)
* Understanding of responsive design and cross-browser compatibility
* Basic knowledge of version control systems like **Git**
* Problem-solving mindset and attention to detail
* Good communication and teamwork skills

### **Preferred Skills (Bonus)**
* Knowledge of backend technologies like **Node.js, Python, or PHP**
* Experience with databases like **MySQL or MongoDB**
* Familiarity with APIs and RESTful services
* Basic UI/UX design understanding

**Sample Resume:** Enthusiastic BCA scholar with a strong foundation in Frontend Web Development and AI. Experienced in building responsive user interfaces and integrating hardware-software systems. A fast learner with a proven track record of academic excellence and leadership, eager to contribute to innovative web projects.
Technical Skills
Web Development: HTML5, CSS, JavaScript, Responsive Web Design
Programming & Tools: Python, C++
Core Competencies: Hardware-Software Integration, Debugging, Problem Solving.
Soft Skills: Fluent Communication (C2 English), Team Leadership, Adaptability.
Web Development Projects
Travel Destination Platform: Developed a multi-page responsive website featuring destination galleries and navigation using HTML and CSS.
Interactive FAQ Accordion: Built a dynamic Frequently Asked Questions component using JavaScript to improve user engagement and information accessibility.
Education
Bachelor of Computer Applications (BCA): Career College, Bhopal | Expected 07/2028

## 👩‍💻 Built By
Arhama Khan — Solo participant, Catalyst Hackathon by Deccan AI
