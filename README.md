# 🚨 CommandAI - AI-Powered Disaster Decision Support System

CommandAI is an AI-powered web application that assists in disaster assessment by combining **Deep Learning**, **Real-Time Weather Data**, and **Generative AI**. The system classifies disaster images, retrieves live weather information, and generates an intelligent incident report to support emergency decision-making.

---

## 🌟 Features

- 🖼️ Disaster Image Classification using CNN (MobileNetV2)
- 📊 Prediction Confidence Score & Top-3 Predictions
- 🚦 Automatic Priority Level Assessment
- 🌦️ Live Weather Information using OpenWeather API
- 🤖 AI-Generated Incident Intelligence Report using Google Gemini AI
- 📄 Downloadable Incident Report
- 💻 Interactive Streamlit Web Interface

---

## 🛠️ Tech Stack

- **Python**
- **TensorFlow & Keras**
- **MobileNetV2 (Transfer Learning)**
- **Streamlit**
- **NumPy**
- **Pillow (PIL)**
- **Google Gemini AI**
- **OpenWeather API**
- **Git & GitHub**

---

## 📂 Project Structure

```
CommandAI/
│
├── app.py                  # Main Streamlit application
├── weather.py              # Weather API integration
├── recommendation.py       # Gemini AI report generation
├── requirements.txt        # Project dependencies
│
├── models/
│   └── commandai_model.keras
│
├── sample_images/
│
├── assets/
│
└── .streamlit/
    └── config.toml
```

---

## 🚀 How It Works

1. Upload a disaster image.
2. Enter the state and district/city.
3. (Optional) Add incident notes.
4. The CNN model classifies the disaster.
5. Live weather data is retrieved using the OpenWeather API.
6. Google Gemini AI generates an Incident Intelligence Report.
7. Download the generated report.

---

## 🧠 Supported Disaster Classes

- 🌍 Earthquake
- 🔥 Fire
- 🌊 Flood
- ⛰️ Landslide
- 💨 Smoke
- ✅ Normal

---

## 📸 Sample Workflow

```
Upload Image
      ↓
Image Preprocessing
      ↓
CNN (MobileNetV2)
      ↓
Disaster Prediction
      ↓
Live Weather API
      ↓
Google Gemini AI
      ↓
Incident Intelligence Report
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/devipriyas21/CommandAI.git
cd CommandAI
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## 📌 Future Enhancements

- Satellite and drone image integration
- GIS-based disaster visualization
- Live CCTV/video analysis
- Mobile application support
- Multilingual interface
- Real-time emergency notifications

---

## 👩‍💻 Developed By

**Devipriya S**

B.Tech Computer Science Engineering (Data Science)  
Presidency University, Bengaluru

---

## 📜 License

This project is developed for academic and educational purposes.
