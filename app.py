import streamlit as st
from detector import analyze_text

st.set_page_config(
    page_title="TrustLens AI",
    page_icon="🛡️"
)

st.title("🛡️ TrustLens AI")
st.subheader("Your Digital Safety Mentor")

user_text = st.text_area(
    "Describe the situation or paste a message:",
    height=200
)

if st.button("Analyze"):

    result = analyze_text(user_text)

    risks = result["risks"]
    score = result["score"]

    st.metric("Risk Score", f"{score}/10")

    if score <= 2:
        st.success("Threat Level: LOW")
    elif score <= 5:
        st.warning("Threat Level: MEDIUM")
    else:
        st.error("Threat Level: HIGH")

    st.markdown("---")

    if risks:
        st.write("### Risks Detected")
        for risk in risks:
            st.write(f"⚠️ {risk}")
    else:
        st.write("No major warning signs detected.")