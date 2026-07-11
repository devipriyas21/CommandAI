import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_report(
    disaster,
    confidence,
    state,
    district,
    weather,
    notes
):

    prompt = f"""
    You are an Emergency Response AI assisting disaster management authorities.

    Generate a professional Incident Intelligence Report in Markdown.

    Incident Details:

    Disaster: {disaster}

    Confidence: {confidence:.2f}%

    State: {state}

    District: {district}

    Weather:
    - Temperature: {weather['temperature']} °C
    - Humidity: {weather['humidity']} %
    - Wind Speed: {weather['wind']} m/s
    - Condition: {weather['condition']}

    Additional Notes:
    {notes}

    Return ONLY the following format:

    # 🚨 Executive Summary
    (2-3 lines summarizing the situation)

    # 📍 Incident Details
    - Disaster:
    - Location:
    - Confidence:
    - Priority:

    # 🌦 Weather Impact
    - Bullet point
    - Bullet point

    # 🚑 Immediate Actions
    - Bullet point
    - Bullet point
    - Bullet point
    - Bullet point
    - Bullet point

    # 🏛 Government Response
    - Bullet point
    - Bullet point
    - Bullet point

    # 🤝 NGO Recommendations
    - Bullet point
    - Bullet point
    - Bullet point

    # 🙋 Volunteer Guidelines
    - Bullet point
    - Bullet point
    - Bullet point

    Keep the report under 250 words.
    Use short bullet points instead of long paragraphs.
    Do not add any introduction or conclusion.
    """
    response = model.generate_content(prompt)

    return response.text