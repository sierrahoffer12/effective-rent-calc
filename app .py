import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Effective Rent Calculator",
    layout="centered"
)

# Sidebar branding
with st.sidebar:
    st.image("CBRE_green.png", use_container_width=True)
    st.title("LeaseLens AI")
    st.markdown("**Effective Rent Calculator**")
    st.markdown("Calculate the effective monthly rent for a commercial lease, factoring in base rent, free rent, and annual escalations.")
    st.markdown("---")
    st.markdown("Contact: sierra.hoffer@cbre.com")
    st.markdown("[CBRE Research](https://www.cbre.com/insights)")

# Main title
st.markdown(
    "<h1 style='color:#00573D;'>Effective Rent Calculator</h1>",
    unsafe_allow_html=True
)

st.markdown("""
This tool helps you compute the **effective monthly rent** for a commercial lease, taking into account:
- Base rent
- Lease term (in months)
- Free rent months
- Annual escalation rate
""")

# Input fields
base_rent = st.number_input("Base Rent ($/month)", min_value=0.0, value=30.0, step=0.5)
lease_term_months = st.number_input("Lease Term (months)", min_value=1, value=60, step=1)
free_rent_months = st.number_input("Free Rent Months", min_value=0, value=3, step=1)
annual_escalation_rate = st.number_input("Annual Escalation Rate (%)", min_value=0.0, value=3.0, step=0.1)

# Calculation function
def calculate_effective_rent(base_rent, lease_term_months, free_rent_months, annual_escalation_rate):
    total_rent = 0.0
    current_rent = base_rent

    for month in range(1, lease_term_months + 1):
        if month <= free_rent_months:
            rent_this_month = 0.0
        else:
            rent_this_month = current_rent
        total_rent += rent_this_month

        if month % 12 == 0:
            current_rent *= (1 + annual_escalation_rate / 100)

    effective_rent = total_rent / lease_term_months
    return effective_rent

# Calculate and display result
if st.button("Calculate Effective Rent"):
    effective_rent = calculate_effective_rent(base_rent, lease_term_months, free_rent_months, annual_escalation_rate)
    st.success(f"Effective Monthly Rent: **${effective_rent:.2f}**")


