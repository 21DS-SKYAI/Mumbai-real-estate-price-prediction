import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Mumbai House Price Estimator",
    layout="centered"
)

# -------------------------------
# Price Prediction Function
# -------------------------------
def predict_house_price(
    carpet_area_sqft,
    rate_per_sqft,
    location_multiplier,
    floor_multiplier,
    amenities_multiplier,
    age_multiplier
):
    base_price = carpet_area_sqft * rate_per_sqft
    final_price = (
        base_price
        * location_multiplier
        * floor_multiplier
        * amenities_multiplier
        * age_multiplier
    )
    return round(final_price / 1e7, 2)  # Crores


# -------------------------------
# SaaS Controls (Branding)
# -------------------------------
with st.sidebar:
    st.subheader("⚙️ SaaS Controls")
    client_name = st.selectbox(
        "Client",
        ["Internal Demo", "ABC Realty", "XYZ Developers", "Private Client"]
    )
    is_paid_user = st.toggle("Paid Client (Remove Branding)")

# -------------------------------
# Title & Description
# -------------------------------
st.title("🏙️ Mumbai House Price Estimator")
st.markdown(
    "Estimate apartment prices using **Mumbai-specific real estate logic** "
    "(used by brokers, banks, and prop-tech platforms)."
)

st.divider()

# -------------------------------
# User Inputs
# -------------------------------
carpet_area = st.slider("Carpet Area (sqft)", 300, 2000, 600, step=50)

location = st.selectbox(
    "Location Zone",
    ["South Mumbai", "Western Suburbs", "Central Suburbs"]
)

floor = st.selectbox(
    "Floor Level",
    ["Low Floor (1–3)", "Mid Floor (4–10)", "High Floor (10+)"]
)

building_age = st.slider("Building Age (Years)", 0, 40, 10)

amenities = st.multiselect(
    "Amenities Available",
    ["Lift", "Parking", "Security", "Gym", "Garden", "Swimming Pool"]
)

# -------------------------------
# Mumbai Pricing Logic
# -------------------------------
rate_mapping = {
    "South Mumbai": 60000,
    "Western Suburbs": 40000,
    "Central Suburbs": 22000
}

location_multiplier_mapping = {
    "South Mumbai": 1.75,
    "Western Suburbs": 1.20,
    "Central Suburbs": 1.10
}

floor_multiplier_mapping = {
    "Low Floor (1–3)": 0.98,
    "Mid Floor (4–10)": 1.08,
    "High Floor (10+)": 1.14
}

# Age depreciation
if building_age <= 5:
    age_multiplier = 1.00
elif building_age <= 15:
    age_multiplier = 0.85
elif building_age <= 30:
    age_multiplier = 0.75
else:
    age_multiplier = 0.65

# Amenities uplift
amenities_multiplier = 1 + (0.02 * len(amenities))

# -------------------------------
# Price Calculation
# -------------------------------
estimated_price = predict_house_price(
    carpet_area_sqft=carpet_area,
    rate_per_sqft=rate_mapping[location],
    location_multiplier=location_multiplier_mapping[location],
    floor_multiplier=floor_multiplier_mapping[floor],
    amenities_multiplier=amenities_multiplier,
    age_multiplier=age_multiplier
)

# -------------------------------
# Output
# -------------------------------
st.divider()

st.subheader("INR Estimated Property Price")
st.metric(
    label="Approx Market Value",
    value=f"₹ {estimated_price} Cr"
)

st.caption(
    "⚠️ Indicative valuation based on market heuristics. "
    "Actual price varies by society, view, demand, and negotiation."
)

# -------------------------------
# Footer
# -------------------------------
st.divider()
st.markdown(
    "<hr><center><small>© 21DS_SkYAI · Built with Python & Streamlit</small></center>",
    unsafe_allow_html=True
)

