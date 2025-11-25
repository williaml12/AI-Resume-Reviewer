import streamlit as st
import google.generativeai as genai

# -----------------------
# 🔑 Configure Gemini API
# -----------------------
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------
# 🌟 Page Config
# -----------------------
st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)

# -----------------------
# 🎯 Header Section
# -----------------------
st.markdown("""
<h1 style='text-align:center; margin-bottom:0;'>📄 AI Resume Reviewer</h1>
<p style='text-align:center; font-size:18px; color:gray;'>
Upload your resume and get industry-ready feedback powered by Google Gemini.
</p>
""", unsafe_allow_html=True)

st.write("---")

# -----------------------
# 💡 About the Project
# -----------------------
with st.expander("💡 About the Project", expanded=True):
    st.markdown("""
**AI Resume Reviewer** simplifies your resume improvement process using generative AI:

- Analyzes your resume content  
- Identifies strengths & weaknesses  
- Suggests improvements for clarity, relevance, and professionalism  
- Gives tips tailored to your target job or industry  
- No downloads or coding required — upload and get instant feedback  
    """)

st.write("---")

# -----------------------
# 📤 Upload Resume
# -----------------------
st.subheader("📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or TXT)",
    type=["pdf", "txt"]
)

# -----------------------
# 🎯 Job Context Input
# -----------------------
st.subheader("🎯 Target Job / Industry")

job_title = st.text_input("Job Title (optional)")
job_description = st.text_area(
    "Job Description / Requirements (optional)",
    height=150,
    placeholder="Paste job description or describe the role you're targeting..."
)

st.write("---")

# -----------------------
# 🔍 Analyze Button
# -----------------------
if st.button("🔍 Analyze My Resume", type="primary"):
    if not uploaded_file:
        st.error("Please upload your resume first.")
    else:
        with st.spinner("Analyzing your resume with Gemini... ⏳"):

            # Read uploaded file
            resume_text = uploaded_file.read().decode("utf-8", errors="ignore")

            # Prompt to Gemini
            prompt = f"""
You are an expert resume reviewer. Analyze the following resume and give clear, structured feedback.

Resume Content:
{resume_text}

Job Target:
- Job Title: {job_title}
- Job Description / Requirements: {job_description}

Please provide analysis in the following format:

1. **Overall Summary**
2. **Strengths**
3. **Weaknesses**
4. **Suggestions for Improvement**
5. **ATS Optimization Tips**
6. **Job Target Alignment Assessment**
7. **Rewrite Suggestions (Bullet Points / Summary / Skills)**

Make the feedback detailed, actionable, and easy to follow.
"""

            response = model.generate_content(prompt)

        # Display response
        st.subheader("📊 Resume Analysis Report")
        st.markdown(response.text)

        st.success("Done! Scroll up to view your report.")

# -----------------------
# 📌 Footer
# -----------------------
st.write("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with ❤️ using Streamlit + Google Gemini</p>",
    unsafe_allow_html=True
)
