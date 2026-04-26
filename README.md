# skillsense-ai
SkillSense AI is a Streamlit-based system that evaluates real skill proficiency by comparing resumes with job descriptions. It uses conversational assessment, skill scoring, gap analysis, and adjacent skill intelligence to generate personalized, time-bound learning plans with visual insights.
# 🎯 SkillSense AI — Skill Assessment & Personalized Learning Agent

## 📌 Problem Statement
A resume tells you what someone *claims* to know — not how well they actually know it. SkillSense AI bridges this gap by conversationally assessing real proficiency on each required skill, identifying gaps, and generating a personalized learning roadmap.

## 🚀 SkillSense-AI Link
https://skillsense-ai-6urfevr9akha5qyelbfbgd.streamlit.app/

## 🎥 Demo Video
https://youtu.be/rXCwyjrDpWw

**##Drive Link** (Zip Project Folder)

https://drive.google.com/file/d/1EWLlsxrBnr1UWFBwXaEN6S5KoP40lUcr/view?usp=drive_link

**🧠 Approach**

**🔍 User-First Thinking:**
The foundation of SkillSense AI was built by thinking like an end user, not just a developer.
Most existing systems rely on keyword matching, where resumes are scanned for surface-level terms rather than actual capability. As a user, this creates a major gap — your skills are claimed but never truly assessed, validated, or understood.
SkillSense AI was designed to solve exactly this problem.

Instead of asking “What keywords exist?”, the system asks:
“How well does the candidate actually understand and apply these skills?”
This shift led to an approach focused on:
Deep skill assessment rather than shallow filtering
Contextual understanding instead of static matching
Adaptive questioning to evaluate real proficiency

**💬 Conversational Intelligence over Static Evaluation:**

Rather than building a rigid evaluation system, the platform uses a dynamic, conversational assessment model.
The AI interacts with the user like a technical interviewer, asking:
Implementation-focused questions
Scenario-based challenges
Follow-up questions to test depth and clarity
This ensures evaluation across:
Conceptual understanding
Practical application
Problem-solving ability

**🎯 Accessibility & Simplicity:**

A key design decision was to make the system accessible to everyone, not just technical experts.
AI tools are often perceived as complex or requiring prior learning. SkillSense AI removes this barrier by providing:
A clean, intuitive interface
Support for both plain text and PDF inputs
A guided, conversational flow that requires no prior training
Whether the user is a beginner or an experienced professional, the platform enables them to:
Easily input their data
Undergo assessment
Receive a structured performance report

**📊 Insight-Driven Output:**

The final approach emphasizes clarity and actionability.
Instead of long, unstructured text outputs, the system delivers:
Skill-wise scores
Strength and gap analysis
Visual dashboards
A structured “report card” of performance
This transforms raw evaluation into actionable insights, helping users clearly understand:
Where they stand
What they lack
What they should do next

**🚀 Summary:**
SkillSense AI moves beyond traditional ATS systems by combining:
User-centric design
Conversational AI-based evaluation
Structured, insight-driven outputs

The result is a system that doesn’t just process resumes — it understands, evaluates, and guides.

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

SkillSense AI evaluates candidates using a structured, multi-dimensional scoring model:

Each skill is assessed across 3 dimensions:
- **Implementation (40%)** – Ability to build and apply the skill in real projects  
- **Problem-Solving (35%)** – Handling edge cases, debugging, and logical reasoning  
- **Scalability (25%)** – Ability to optimize, extend, and improve solutions  

##SCORING CALIBRATION:
- 0-30: No knowledge or completely vague answers
- 31-50: Basic knowledge, struggled with follow-ups
- 51-70: Good understanding, answered most questions well
- 71-85: Strong knowledge, clear implementation understanding
- 86-100: Expert level, discussed optimizations and scalability


### Final Score:
The overall Job Readiness Score is calculated as the weighted average of all skill scores.

💡 Unlike traditional ATS systems, SkillSense AI uses LLM-based semantic evaluation to assess *depth of understanding*, not just keyword presence.

### Trade-offs & Decisions
| Decision | Why |
|----------|-----|
| OpenRouter over direct API | Flexibility to switch models, better free tier |
| Streamlit over custom frontend | Faster development, built-in components |
| LLM-based scoring over keyword matching | Semantic understanding over surface matching |
| GPT-4o-mini over larger models | Cost effective, fast, sufficient for assessment |
| JSON output parsing | Structured data enables rich visualizations |

# 🏗️ Architecture
<img width="761" height="210" alt="unnamed (1)" src="https://github.com/user-attachments/assets/efd9f827-967c-44a2-935f-b9c5494d4822" />

SkillSense AI follows a modular AI-driven architecture:

1. **Input Layer**
   - Resume (PDF/Text)
   - Job Description

2. **Processing Layer**
   - Text extraction using PyPDF2
   - Skill and keyword identification

3. **AI Engine**
   - Prompt engineering layer
   - OpenRouter API (GPT-4o-mini) for semantic analysis
   - Conversational assessment generation

4. **Scoring Engine**
   - Multi-dimensional evaluation (Implementation, Problem-solving, Scalability)
   - Job Readiness Score calculation

5. **Output Layer**
   - JSON report generation
   - Visualization via Plotly (Bar, Radar, Pie charts)
   - Personalized learning roadmap

6. **User Interface**
   - Interactive dashboard built with Streamlit

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
<img width="1794" height="740" alt="Screenshot (116)" src="https://github.com/user-attachments/assets/d8f002a2-8bba-4dfc-8769-a7b39c3df078" />

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

**📤##Sample Output**
- **Job Readiness Score:** 72/100  
- **Strong Skills:** HTML, CSS, Communication  
- **Skill Gaps:** JavaScript, Git, React
- **Skills That Need Improvement:** (This section is displayed only incase the candiadte lacks improvement in certains skills)
📍JavaScript — Score: 20/100
📍React.js — Score: 30/100

**Skill Analysis:**
- Skill Analysis is done and visuallly represented using bar Chart, Radar Chart and Pie Chart.

**Adjacent Skills To Learn Next:**
-  JavaScript, Git, React
  
- **Suggested Projects To Build:**
  - Build 2 JavaScript projects
  - Learn Git version control
  - Practice debugging exercises  

- **Personalised Learning Roadmap:**
  - Phase 1: Fundamentals (2 weeks)
  - Phase 2: Projects (3 weeks)
  - Phase 3: Advanced + Deployment (2 weeks)

  <img width="1743" height="667" alt="Screenshot (117)" src="https://github.com/user-attachments/assets/80b591e4-28f4-4324-b1d1-11a65635f78c" />
  <img width="1704" height="674" alt="Screenshot (118)" src="https://github.com/user-attachments/assets/30235c4b-6910-4dd0-88b5-5d3fbc4d45a3" />
  <img width="1165" height="599" alt="Screenshot (119)" src="https://github.com/user-attachments/assets/a3825378-d131-4a5d-ad06-0cfb7ffeb342" />
  <img width="1750" height="560" alt="Screenshot (120)" src="https://github.com/user-attachments/assets/35d47814-24c4-4213-a902-dd7f72dc50b4" />
  <img width="1239" height="453" alt="Screenshot (123)" src="https://github.com/user-attachments/assets/023ac0aa-197a-42b9-9415-81d7f3a28365" />
  <img width="1750" height="761" alt="Screenshot (121)" src="https://github.com/user-attachments/assets/898965fb-ec21-4999-b6d5-4ebe282022db" />
  <img width="1734" height="698" alt="Screenshot (122)" src="https://github.com/user-attachments/assets/574ebc89-2c5c-4947-a59b-137ee1dc115f" />







## 👩‍💻 Built By
Arhama Khan — Solo participant, Catalyst Hackathon by Deccan AI
