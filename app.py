import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

from weather import get_weather
from recommendation import generate_report

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="CommandAI",
    page_icon="🚨",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "models/commandai_model.keras"
    )

model = load_model()

classes = [
    "Earthquake",
    "Fire",
    "Flood",
    "Landslide",
    "Normal",
    "Smoke"
]

# ---------------- HEADER ----------------

st.markdown("""
# 🚨 CommandAI

### AI-Powered Disaster Decision Support System

*From Detection to Action.*
""")

# ---------------- USER INPUT ----------------

uploaded_file = st.file_uploader(
    "📷 Upload Disaster Image",
    type=["jpg", "jpeg", "png"]
)

col1, col2 = st.columns(2)

with col1:
    state = st.text_input(
        "🏛️ State",
        placeholder="Example: Kerala"
    )

with col2:
    district = st.text_input(
        "📍 District / City",
        placeholder="Example: Wayanad"
    )

additional_notes = st.text_area(
    "📝 Additional Notes (Optional)",
    placeholder="Example: Heavy rainfall since morning. Roads blocked. Around 20 people trapped."
)

generate = st.button(
    "🚨 Generate Incident Report",
    use_container_width=True
)

# ---------------- MAIN ----------------

if uploaded_file is not None and generate:

    image = Image.open(uploaded_file).convert("RGB")

    left, right = st.columns([1,1])

    with left:
        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

    # ---------- PREPROCESS ----------

    img = image.resize((160,160))
    img = np.array(img)/255.0
    img = np.expand_dims(img,axis=0)

    with st.spinner("🧠 AI is analyzing the image..."):
        prediction = model.predict(img, verbose=0)[0]

    top3 = np.argsort(prediction)[-3:][::-1]

    predicted_class = classes[top3[0]]

    confidence = prediction[top3[0]]*100

    # ---------- PRIORITY ----------

    if predicted_class == "Normal":
        priority = "🟢 NORMAL"

    elif confidence >= 90:
        priority = "🔴 CRITICAL"

    elif confidence >= 75:
        priority = "🟠 HIGH"

    elif confidence >= 50:
        priority = "🟡 MODERATE"

    else:
        priority = "🟢 LOW"

    # ---------- AI CARD ----------

    with right:

        st.subheader("🧠 AI Situation Report")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "🚨 Disaster",
                predicted_class
            )

        with c2:
            st.metric(
                "📈 Confidence",
                f"{confidence:.2f}%"
            )

        with c3:
            if "CRITICAL" in priority:
                st.error(priority)

            elif "HIGH" in priority:
                st.warning(priority)

            elif "MODERATE" in priority:
                st.info(priority)

            else:
                 st.success(priority)

        st.markdown("---")

        st.markdown("### 📊 Prediction Confidence")

        for i in top3:

            st.write(f"**{classes[i]}**")

            st.progress(float(prediction[i]))

            st.caption(
                f"{prediction[i]*100:.2f}%"
            )

    st.markdown("---")
        # ---------------- WEATHER ----------------

    weather = get_weather(
        state,
        district
    )

    if weather:

        st.subheader("🌦 Live Weather")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🌡 Temperature",
                f"{weather['temperature']} °C"
            )

        with c2:
            st.metric(
                "💧 Humidity",
                f"{weather['humidity']} %"
            )

        with c3:
            st.metric(
                "💨 Wind Speed",
                f"{weather['wind']} m/s"
            )

        with c4:
            st.metric(
                "☁ Condition",
                weather["condition"]
            )

    else:

        st.warning(
            "Unable to retrieve weather information."
        )

    st.markdown("---")

    # ---------------- INCIDENT INFORMATION ----------------

    st.subheader("📋 Incident Information")

    info1, info2 = st.columns(2)

    with info1:
        st.write(f"**🏛 State:** {state}")

    with info2:
        st.write(f"**📍 District / City:** {district}")

    if additional_notes.strip():

        st.info(additional_notes)

    else:

        st.info("No additional notes were provided.")

    st.markdown("---")

    # ---------------- GEMINI REPORT ----------------

    if weather:

        with st.spinner("🤖 Generating Incident Intelligence Report..."):

            report = generate_report(
                disaster=predicted_class,
                confidence=confidence,
                state=state,
                district=district,
                weather=weather,
                notes=additional_notes
            )

        st.subheader("🤖 Incident Intelligence Report")

        st.markdown(report)

        st.markdown("---")
                # ---------------- DOWNLOAD REPORT ----------------

        st.download_button(
            label="📄 Download Incident Report",
            data=report,
            file_name="CommandAI_Incident_Report.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_incident_report"
        )

    else:

        st.info(
            "⚠ Weather information is unavailable. AI report could not be generated."
        )

# ---------------- WELCOME SCREEN ----------------

elif uploaded_file is not None:

    st.warning("👆 Click **Generate Incident Report** to start the analysis.")

else:

    st.info(
        """
# 👋 Welcome to CommandAI

### AI-Powered Disaster Decision Support System

Upload a disaster image, enter the location details, and click **Generate Incident Report**.

### 🚀 Features

- 🧠 CNN-based Disaster Classification
- 📊 Confidence Score & Top-3 Predictions
- 🚦 Priority Assessment
- 🌦 Live Weather Information
- 🤖 AI Decision Support Report (Gemini)
- 📄 Downloadable Incident Report

**Tagline:** *From Detection to Action.*
"""
    )

st.markdown("---")

st.caption(
    "🚨 CommandAI • AI-Powered Disaster Decision Support System • "
    "Built with TensorFlow, Gemini AI, OpenWeather API & Streamlit"
)