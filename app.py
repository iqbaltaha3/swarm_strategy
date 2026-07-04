import streamlit as st
from graph import graph
from core.state import StrategyState

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Legal Strategy Advisor",
    page_icon="⚖",
    layout="wide",
)

# ============================================================
# CUSTOM CSS - PROFESSIONAL LEGAL STYLE
# ============================================================

st.markdown("""
<style>
    /* Remove Streamlit padding */
    .main { padding: 0; }
    
    /* Professional fonts */
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    
    /* Header styling */
    h1 { 
        font-size: 2.5rem; 
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 0.5rem;
        border-bottom: 3px solid #1e3a8a;
        padding-bottom: 1rem;
    }
    
    h2 { 
        font-size: 1.75rem;
        color: #1e3a8a;
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    h3 {
        color: #2d3748;
        margin-top: 1rem;
        font-weight: 500;
    }
    
    /* Section dividers */
    hr { border-color: #cbd5e0; margin: 2rem 0; }
    
    /* Text styling */
    p { color: #2d3748; line-height: 1.6; }
    
    /* Metric cards */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #f0f4f8 0%, #ffffff 100%);
        border: 1px solid #cbd5e0;
        border-radius: 8px;
        padding: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("# Legal Strategy Advisor")
with col2:
    st.caption("Strategic Analysis Platform")

st.markdown("""
Comprehensive litigation analysis powered by multi-agent AI reasoning.
""")

# ============================================================
# INPUT SECTION
# ============================================================

st.markdown("---")
st.markdown("## Case Information")

complaint = st.text_area(
    "Describe your case or legal matter:",
    height=150,
    placeholder="Provide details about the dispute, parties involved, key facts, and timeline.",
)

col_analyze, col_info = st.columns([3, 1])

with col_analyze:
    analyze_btn = st.button("ANALYZE CASE", use_container_width=True, type="primary")

with col_info:
    st.caption("Processing: 30-60 seconds")

# ============================================================
# ANALYSIS EXECUTION
# ============================================================

if analyze_btn:
    if not complaint.strip():
        st.warning("Please enter case details to proceed.")
        st.stop()

    with st.spinner("Analyzing case..."):
        try:
            state: StrategyState = {"complaint": complaint}
            result = graph.invoke(state)
        except Exception as e:
            st.error(f"Analysis error: {str(e)}")
            st.stop()

    st.success("✓ Analysis complete")
    st.markdown("---")

    # Extract results
    judgment = result.get("strategy_judgment")
    path = result.get("recommended_path")
    plaintiff = result.get("plaintiff_strategy")
    defendant = result.get("defendant_strategy")
    evidence = result.get("evidence_attack")
    risk = result.get("risk_analysis")
    settlement = result.get("settlement")
    battlefield = result.get("battlefield_analysis")

    # ========================================================
    # KEY METRICS
    # ========================================================

    st.markdown("## Strategic Assessment")
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

    with metrics_col1:
        st.metric(
            "Plaintiff Success",
            f"{judgment.plaintiff_win_chance}%" if judgment else "—"
        )

    with metrics_col2:
        st.metric(
            "Defendant Success",
            f"{judgment.defendant_win_chance}%" if judgment else "—"
        )

    with metrics_col3:
        st.metric(
            "Settlement Likely",
            f"{judgment.settlement_probability}%" if judgment else "—"
        )

    with metrics_col4:
        st.metric(
            "Confidence Level",
            f"{judgment.confidence_level}%" if judgment else "—"
        )

    # ========================================================
    # STRATEGIC RECOMMENDATION
    # ========================================================

    st.markdown("## Recommended Strategy")
    
    if judgment:
        strategy_text = judgment.recommended_strategy.upper().replace("_", " ")
        st.markdown(f"**Primary Strategy:** {strategy_text}")
        st.markdown(judgment.rationale)

    # ========================================================
    # ACTION PLAN
    # ========================================================

    st.markdown("## Action Plan")

    if path:
        col_immediate, col_st, col_lt = st.columns(3)

        with col_immediate:
            st.markdown("### Immediate")
            st.markdown(path.immediate_action)

        with col_st:
            st.markdown("### Next 30 Days")
            st.markdown(path.short_term_strategy)

        with col_lt:
            st.markdown("### Next 6 Months")
            st.markdown(path.long_term_strategy)

        st.markdown("**Success Metrics**")
        for i, metric in enumerate(path.success_metrics, 1):
            st.markdown(f"{i}. {metric}")

    # ========================================================
    # DETAILED ANALYSIS TABS
    # ========================================================

    st.markdown("---")
    st.markdown("## Detailed Analysis")

    tab_strategy, tab_evidence, tab_risk, tab_settlement, tab_battlefield = st.tabs([
        "Strategies",
        "Evidence",
        "Risk Factors",
        "Settlement",
        "Case Overview"
    ])

    # STRATEGY TAB
    with tab_strategy:
        col_p, col_d = st.columns(2)

        with col_p:
            st.markdown("### Plaintiff Perspective")
            if plaintiff:
                st.markdown("**Strong Arguments**")
                for arg in plaintiff.strong_arguments:
                    st.write(f"• {arg}")
                st.markdown("**Evidence Priorities**")
                for ev in plaintiff.evidence_priorities:
                    st.write(f"• {ev}")

        with col_d:
            st.markdown("### Defendant Perspective")
            if defendant:
                st.markdown("**Defense Lines**")
                for defense in defendant.defense_lines:
                    st.write(f"• {defense}")
                st.markdown("**Counter Strategies**")
                for counter in defendant.counter_strategies:
                    st.write(f"• {counter}")

    # EVIDENCE TAB
    with tab_evidence:
        if evidence:
            st.markdown("**Vulnerable Evidence**")
            for item in evidence.vulnerable_evidence:
                st.write(f"• {item}")

            st.markdown("**Attack Methods**")
            for item in evidence.attack_methods:
                st.write(f"• {item}")

            st.markdown("**Counter Arguments**")
            for item in evidence.counterarguments:
                st.write(f"• {item}")

    # RISK TAB
    with tab_risk:
        if risk:
            col_pr, col_dr = st.columns(2)

            with col_pr:
                st.markdown("**Plaintiff Risks**")
                for item in risk.plaintiff_risks:
                    st.write(f"• {item}")

            with col_dr:
                st.markdown("**Defendant Risks**")
                for item in risk.defendant_risks:
                    st.write(f"• {item}")

            st.markdown("**Critical Issues**")
            for item in risk.critical_issues:
                st.write(f"• {item}")

    # SETTLEMENT TAB
    with tab_settlement:
        if settlement:
            st.markdown(f"**Proposed Range:** {settlement.settlement_range}")

            col_c, col_d = st.columns(2)

            with col_c:
                st.markdown("**Key Concessions**")
                for item in settlement.key_concessions:
                    st.write(f"• {item}")

            with col_d:
                st.markdown("**Deal Breakers**")
                for item in settlement.deal_breakers:
                    st.write(f"• {item}")

    # CASE OVERVIEW TAB
    with tab_battlefield:
        if battlefield:
            st.markdown("**Case Summary**")
            st.write(battlefield.case_summary)

            col_facts, col_issues = st.columns(2)

            with col_facts:
                st.markdown("**Key Facts**")
                for item in battlefield.key_facts:
                    st.write(f"• {item}")

            with col_issues:
                st.markdown("**Legal Issues**")
                for item in battlefield.legal_issues:
                    st.write(f"• {item}")

            st.markdown(f"**Case Strength Assessment:** {battlefield.strength_level.upper()}")

    # ========================================================
    # FOOTER
    # ========================================================

    st.markdown("---")
    st.caption("Legal Strategy Advisor | AI-powered litigation analysis | For strategic planning purposes only")


st.markdown("---")

st.caption(
    "Strategy Swarm • Litigation Intelligence Platform"
)