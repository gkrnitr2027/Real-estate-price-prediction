import streamlit as st
import util
import time

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="Real Estate Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    color: #2E86C1;
    text-align: center;
}

h3 {
    text-align: center;
    color: gray;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 10px;
    background-color: #2E86C1;
    color: white;
    font-size: 20px;
    border: none;
}

.stButton > button:hover {
    background-color: #1B4F72;
    color: white;
}

.result-box {
    background-color: #DB62F9;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    border: 2px solid #1ABC9C;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: gray;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.markdown("""
# 🏠 Real Estate Price Prediction

### Predict Bengalore House Prices Instantly
""")

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.title("🏡 Project Information")

st.sidebar.markdown("""
### Machine Learning Model

**Linear Regression**

---

### Input Features

- 📐 Total Square Feet
- 🏢 BHK
- 🛁 Bathrooms
- 📍 Location

---

### Technologies Used

- Python
- Streamlit
- Scikit-Learn
- NumPy
- Pandas

---

Developed as a Machine Learning Deployment Project.
""")

# -------------------------------------------------------
# FORM
# -------------------------------------------------------

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        sqft = st.number_input(
            "📐 Total Square Feet",
            min_value=300,
            max_value=10000,
            value=1000,
            step=50
        )

        bhk = st.number_input(
            "🏢 BHK",
            min_value=1,
            max_value=8,
            value=2
        )

    with col2:

        bath = st.number_input(
            "🛁 Bathrooms",
            min_value=1,
            max_value=4,
            value=2
        )

        location = st.selectbox(
            "📍 Location",
            util.get_location_names()
        )

    submitted = st.form_submit_button("Predict House Price")

# -------------------------------------------------------
# PREDICTION
# -------------------------------------------------------

if submitted:

    with st.spinner("Predicting price..."):

        time.sleep(1)

        price = util.predict_price(
            location,
            sqft,
            bath,
            bhk
        )

    st.markdown(
        f"""
        <div class="result-box">
            <h2>🏡 Estimated House Price</h2>
            <h1>₹ {price*1e5:.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    c1.metric("📐 Area", f"{sqft} sqft")
    c2.metric("🏢 BHK", bhk)
    c3.metric("🛁 Bathrooms", bath)

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.divider()

st.markdown(
    """
<div class="footer">
Made using Streamlit | Real Estate Price Prediction
</div>
""",
    unsafe_allow_html=True
)