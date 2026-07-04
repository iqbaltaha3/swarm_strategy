import streamlit as st
from graph import graph
from core.state import StrategyState

st.set_page_config(page_title="Swarm Strategy", page_icon="⚖️", layout="centered")

st.title("Swarm Strategy")
st.markdown("**Think Like a Legal Team.**")
st.write("Describe the matter below and get a concise strategic analysis from the swarm.")

complaint = st.text_area(
    "Case details",
    placeholder="Paste the facts, timeline, and dispute summary here...",
    height=180,
)

if st.button("Analyze", type="primary"):
    if not complaint.strip():
        st.warning("Please enter some case details first.")
    else:
        with st.spinner("Analyzing your case..."):
            try:
                state: StrategyState = {"complaint": complaint}
                result = graph.invoke(state)
            except Exception as exc:
                st.error(f"Analysis failed: {exc}")
                st.stop()

        st.success("Analysis complete")
        st.divider()

        judgment = result.get("strategy_judgment")
        path = result.get("recommended_path")
        battlefield = result.get("battlefield_analysis")

        if battlefield:
            st.subheader("Case Overview")
            st.write(battlefield.case_summary)
            st.write(f"**Strength:** {battlefield.strength_level}")

        if judgment:
            st.subheader("Result")
            st.write(f"**Recommended strategy:** {judgment.recommended_strategy}")
            st.write(f"**Confidence:** {judgment.confidence_level}%")
            st.write(f"**Plaintiff win chance:** {judgment.plaintiff_win_chance}%")
            st.write(f"**Defendant win chance:** {judgment.defendant_win_chance}%")
            st.write(f"**Settlement probability:** {judgment.settlement_probability}%")
            st.write(judgment.rationale)

        if path:
            st.subheader("Recommended Path")
            st.write(f"**Immediate action:** {path.immediate_action}")
            st.write(f"**Short term:** {path.short_term_strategy}")
            st.write(f"**Long term:** {path.long_term_strategy}")
            if path.success_metrics:
                st.write("**Success metrics:**")
                for metric in path.success_metrics:
                    st.write(f"- {metric}")
