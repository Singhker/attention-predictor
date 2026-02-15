🧠 AI-Based Human Attention Predictor
📌 Project Overview

This project is a rule-based AI system that predicts human attention levels for students, employees, and general users.
It does not use machine learning or datasets.
Instead, it uses simple logical rules to calculate attention scores and give recommendations.

🎯 Aim

To predict human attention levels using an explainable rule-based approach without relying on datasets.

👤 User Categories

Students – study duration, subject difficulty, exam proximity

Employees – work duration, fatigue, noise

General Users – daily activity and well-being factors

🔧 Input Factors

Continuous work / study duration

Number of breaks

Noise level

Fatigue level

Additional for Students:

Subject difficulty

Study type (Revision / New topic)

Days remaining for exam

🧠 How It Works

The attention score is calculated using the formula:

Attention Score = 100 − Decay − Penalties + Recovery


Decay depends on work duration

Penalties include noise and fatigue

Recovery is based on breaks taken

The final score ranges from 0 to 100.

💻 Technologies Used

Python

Streamlit

Rule-Based Logic

🚀 How to Run the Project
▶️ Run Locally
pip install streamlit
streamlit run app.py

🌐 Run Online

The app is deployed on Streamlit Cloud and can be accessed using the public link.

📁 Project Files

app.py – Main application file

requirements.txt – Required libraries

README.md – Project documentation

🎓 Academic Use

This project is developed as part of an academic mini / major project for learning AI concepts and explainable systems.

👨‍🎓 Developed By

Your Name
MCA Student

📄 License

This project is for educational purposes only.
