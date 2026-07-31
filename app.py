import streamlit as st
import requests

st.set_page_config(
    page_title="AI Farm Companion",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AI Farm Companion")
st.markdown("### Your Smart Farming Assistant")

uploaded_file = st.file_uploader(
    "Upload a crop image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(uploaded_file, caption="Uploaded Image", width=350)

    city = st.text_input(
        "Enter your city",
        value="Bangalore"
    )

    if st.button("Analyze Crop"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type,
            )
        }

        # ---------------- Diagnosis ---------------- #

        diagnosis_response = requests.post(
            "http://127.0.0.1:8000/diagnosis",
            files=files
        )

        if diagnosis_response.status_code != 200:
            st.error(f"Backend Error ({diagnosis_response.status_code})")
            st.code(diagnosis_response.text)
            st.stop()

        result = diagnosis_response.json()

        # Safely read values returned by backend
        crop = result.get("crop", "Tomato")
        prediction = result.get("prediction", "Unknown")
        confidence = result.get("confidence", 0)
        explanation = result.get("explanation", "No explanation available.")

        # ---------------- Weather ---------------- #

        weather_response = requests.get(
            f"http://127.0.0.1:8000/weather/{city}"
        )

        if weather_response.status_code == 200:
            weather = weather_response.json()
        else:
            weather = {"error": "Unable to fetch weather."}

        # ---------------- Market ---------------- #

        market_response = requests.get(
            f"http://127.0.0.1:8000/market/{crop}/{city}"
        )

        if market_response.status_code == 200:
            market = market_response.json()
        else:
            market = {"error": "Unable to fetch market data."}

        st.success("Analysis Complete")

        col1, col2 = st.columns(2)

        # ================= LEFT ================= #

        with col1:

            st.subheader("🌾 Crop Detection")
            st.success(crop)

            st.subheader("🦠 Disease Detection")
            st.write(prediction)

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

            if confidence < 60:
                st.warning(
                    "Low Confidence - Consider uploading another image."
                )

            st.subheader("🤖 AI Agronomist")
            st.write(explanation)

        # ================= RIGHT ================= #

        with col2:

            st.subheader("🌦 Weather")

            if "error" not in weather:

                st.metric(
                    "Temperature",
                    f"{weather.get('temperature', 'N/A')} °C"
                )

                st.metric(
                    "Humidity",
                    f"{weather.get('humidity', 'N/A')} %"
                )

                st.write(
                    f"Condition: **{weather.get('condition', 'N/A')}**"
                )

            else:
                st.error(weather["error"])

            st.divider()

            st.subheader("💰 Market Intelligence")

            if "error" not in market:

                st.write(
                    f"**Market:** {market.get('market', 'N/A')}"
                )

                st.metric(
                    "Price / Quintal",
                    f"₹ {market.get('price_per_quintal', 'N/A')}"
                )

                st.write(
                    f"**Trend:** {market.get('trend', 'N/A')}"
                )

                # Safe check for recommendation key
                recommendation = market.get("recommendation")
                if recommendation:
                    st.success(recommendation)
                else:
                    st.info("No market recommendation available.")

            else:
                st.error(market["error"])
# ---------------- AI Chatbot Section ---------------- #
st.divider()
st.subheader("💬 Ask AI Agronomist")

# Initialize chat history state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User prompt input
if prompt := st.chat_input("Ask a question about your crops, weather, or farming advice..."):
    # Display user query in UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call FastAPI backend chatbot endpoint
    try:
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": prompt}
        )
        if response.status_code == 200:
            bot_reply = response.json().get("reply", "No response from assistant.")
        else:
            bot_reply = f"Backend Error ({response.status_code})"
    except Exception as e:
        bot_reply = f"Could not connect to chat backend: {e}"

    # Display assistant response in UI
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})