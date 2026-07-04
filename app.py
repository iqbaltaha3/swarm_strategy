import streamlit as st

from graph import graph
from core.state import StrategyState


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Strategy Swarm",
    page_icon="⚖️",
    layout="wide",
)

# ============================================================
# HEADER
# ============================================================

st.title("⚖️ Strategy Swarm")
st.caption("AI Litigation Intelligence Platform")

with st.sidebar:
    st.header("Strategy Swarm")

    st.markdown(
        """
        Analyze litigation strategy through:

        • Plaintiff Analysis

        • Defendant Analysis

        • Evidence Review

        • Risk Assessment

        • Settlement Planning

        • Strategic Judgment
        """
    )

# ============================================================
# INPUT
# ============================================================

st.markdown("## Case Intake")

complaint = st.text_area(
    "Case Description",
    height=220,
    placeholder="""
Describe the dispute, complaint, FIR, contract issue,
criminal allegation, commercial disagreement, etc.
""",
)

analyze = st.button(
    "Analyze Strategy",
    use_container_width=True,
    type="primary",
)

# ============================================================
# RUN
# ============================================================

if analyze:

    if not complaint.strip():
        st.warning("Please enter a case description.")
        st.stop()

    with st.spinner("Running Strategy Swarm..."):

        try:

            state: StrategyState = {
                "complaint": complaint
            }

            result = graph.invoke(state)

        except Exception as e:
            st.error(str(e))
            st.stop()

    st.success("Analysis Complete")

    judgment = result.get("strategy_judgment")
    path = result.get("recommended_path")

    plaintiff = result.get("plaintiff_strategy")
    defendant = result.get("defendant_strategy")

    evidence = result.get("evidence_attack")
    risk = result.get("risk_analysis")
    settlement = result.get("settlement")

    battlefield = result.get("battlefield_analysis")

    # ========================================================
    # EXECUTIVE SUMMARY
    # ========================================================

    st.markdown("---")
    st.markdown("## Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Plaintiff Win %",
            f"{judgment.plaintiff_win_chance}%"
            if judgment else "-"
        )

    with col2:
        st.metric(
            "Defendant Win %",
            f"{judgment.defendant_win_chance}%"
            if judgment else "-"
        )

    with col3:
        st.metric(
            "Settlement %",
            f"{judgment.settlement_probability}%"
            if judgment else "-"
        )

    with col4:
        st.metric(
            "Confidence",
            f"{judgment.confidence_level}%"
            if judgment else "-"
        )

    # ========================================================
    # RECOMMENDATION
    # ========================================================

    if judgment:

        st.markdown("## Strategic Recommendation")

        st.info(judgment.recommended_strategy)

        st.markdown("### Rationale")
        st.write(judgment.rationale)

    # ========================================================
    # ACTION PLAN
    # ========================================================

    if path:

        st.markdown("## Recommended Action Plan")

        st.success(
            f"**Immediate Action**\n\n{path.immediate_action}"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Next 30 Days")
            st.write(path.short_term_strategy)

        with col2:
            st.markdown("### Long-Term Strategy")
            st.write(path.long_term_strategy)

        st.markdown("### Success Metrics")

        for metric in path.success_metrics:
            st.write(f"• {metric}")

    # ========================================================
    # TABS
    # ========================================================

    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Strategy",
            "Evidence",
            "Risks",
            "Settlement",
            "Case Map",
        ]
    )

    # ========================================================
    # STRATEGY TAB
    # ========================================================

    with tab1:

        left, right = st.columns(2)

        with left:

            st.subheader("Plaintiff Strategy")

            if plaintiff:

                for item in plaintiff.strong_arguments:
                    st.write(f"• {item}")

                st.markdown("#### Evidence Priorities")

                for item in plaintiff.evidence_priorities:
                    st.write(f"• {item}")

        with right:

            st.subheader("Defendant Strategy")

            if defendant:

                for item in defendant.defense_lines:
                    st.write(f"• {item}")

                st.markdown("#### Counter Strategies")

                for item in defendant.counter_strategies:
                    st.write(f"• {item}")

    # ========================================================
    # EVIDENCE TAB
    # ========================================================

    with tab2:

        if evidence:

            st.subheader("Vulnerable Evidence")

            for item in evidence.vulnerable_evidence:
                st.write(f"• {item}")

            st.subheader("Attack Methods")

            for item in evidence.attack_methods:
                st.write(f"• {item}")

            st.subheader("Counter Arguments")

            for item in evidence.counterarguments:
                st.write(f"• {item}")

    # ========================================================
    # RISKS TAB
    # ========================================================

    with tab3:

        if risk:

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Plaintiff Risks")

                for item in risk.plaintiff_risks:
                    st.write(f"• {item}")

            with col2:

                st.subheader("Defendant Risks")

                for item in risk.defendant_risks:
                    st.write(f"• {item}")

            st.subheader("Critical Issues")

            for item in risk.critical_issues:
                st.write(f"• {item}")

    # ========================================================
    # SETTLEMENT TAB
    # ========================================================

    with tab4:

        if settlement:

            st.metric(
                "Settlement Range",
                settlement.settlement_range
            )

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Key Concessions")

                for item in settlement.key_concessions:
                    st.write(f"• {item}")

            with col2:

                st.subheader("Deal Breakers")

                for item in settlement.deal_breakers:
                    st.write(f"• {item}")

    # ========================================================
    # CASE MAP TAB
    # ========================================================

    with tab5:

        if battlefield:

            st.subheader("Case Summary")

            st.write(battlefield.case_summary)

            st.subheader("Key Facts")

            for item in battlefield.key_facts:
                st.write(f"• {item}")

            st.subheader("Legal Issues")

            for item in battlefield.legal_issues:
                st.write(f"• {item}")

            st.subheader("Case Strength")

            st.info(battlefield.strength_level)

    # ========================================================
    # ADVANCED
    # ========================================================

    with st.expander("Advanced Analysis"):

        st.json(result)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Strategy Swarm • Litigation Intelligence Platform"
)