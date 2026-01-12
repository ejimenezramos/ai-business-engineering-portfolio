import streamlit as st
import sys
from pathlib import Path
from ai_service import analyze_requirements, split_analysis_sections



# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Requirements Analyzer",
    layout="wide"
)

# ---------------- Header ----------------
st.title("🧠 AI Requirements Analyzer")

st.markdown(
    """
    Translate **business requirements** into clear **technical tasks**,  
    **effort estimations** and **risk analysis** using **Generative AI (Gemini)**.

    Designed for **consultants, engineers and business-oriented technical roles**.
    """
)

st.divider()

# ---------------- Layout ----------------
left_col, right_col = st.columns([1, 1.2])

# ---------------- LEFT: Input ----------------
with left_col:
    st.subheader("📋 Business Requirements")

    requirements = st.text_area(
        label="Business requirements input",
        label_visibility="collapsed",
        placeholder=(
            "Example:\n\n"
            "The business needs an internal web application to submit incidents.\n"
            "Users must be able to track the status of their submissions.\n"
            "Managers need dashboards showing open incidents and resolution time."
        ),
        height=260
    )

    analyze_btn = st.button(
        "🔍 Analyze requirements",
        type="primary",
        use_container_width=True
    )

# ---------------- RIGHT: Output ----------------
with right_col:
    st.subheader("📊 Analysis Output")

    if analyze_btn:
        if not requirements.strip():
            st.warning("Please enter business requirements to start the analysis.")
        else:
            with st.spinner("Analyzing requirements..."):
                try:
                    result = analyze_requirements(requirements)
                    sections = split_analysis_sections(result)

                    tab_tasks, tab_estimation, tab_risks = st.tabs(
                        ["🛠 Technical Tasks", "⏱ Estimation", "⚠️ Risks & Ambiguities"]
                    )

                    with tab_tasks:
                        st.markdown("### 🛠 Technical Tasks")
                        st.markdown(sections["tasks"] or "_No tasks identified._")

                    with tab_estimation:
                        st.markdown("### ⏱ Effort Estimation")
                        st.markdown(sections["estimation"] or "_No estimation provided._")

                    with tab_risks:
                        st.markdown("### ⚠️ Risks & Ambiguities")
                        st.markdown(sections["risks"] or "_No risks identified._")

                except Exception as e:
                    st.error("An error occurred during analysis.")
                    st.exception(e)