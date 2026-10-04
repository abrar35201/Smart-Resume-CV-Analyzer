import streamlit as st

# Skill Matching
found_skills = []
missing_skills = []

for skill in skills_database:

    # Found Skills
    if skill in cleaned_resume:
        found_skills.append(skill)

    # Missing Skills
    if skill in cleaned_jd and skill not in cleaned_resume:
        missing_skills.append(skill)

# Suggestions
suggestions = []

for skill in missing_skills:
    suggestions.append(f"Add {skill} skill or certification")

# Results
st.success("Analysis Completed Successfully")

# Match Score
st.subheader("Resume Match Score")

st.metric(
    label="Match Percentage",
    value=f"{match_score}%"
)

# Resume Skills
st.subheader("Detected Skills")

if found_skills:
    for skill in found_skills:
        st.write(f"✔ {skill.title()}")
else:
    st.write("No skills detected")

# Missing Skills
st.subheader("Missing Skills")

if missing_skills:
    for skill in missing_skills:
        st.write(f"❌ {skill.title()}")
else:
    st.write("No missing skills")

# Suggestions
st.subheader("Suggestions")

if suggestions:
    for suggestion in suggestions:
        st.write(f"👉 {suggestion}")
else:
    st.write("Excellent Resume")

# Resume Preview
st.subheader("Resume Text Preview")

st.text(resume_text[:1500])