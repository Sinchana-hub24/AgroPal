# Synaptrixhackathon

AgroPal _
Submission for the Synaptrix Hackathon.

Domain : AgriSense

Problem Statement: 
Build an AI-powered farm companion that acts like an agronomist, a market analyst, and a weather advisor all in one - diagnosing crop health from a photo, explaining the diagnosis in plain conversational language, and
helping the farmer decide not just what's wrong with the crop, but when and where to sell it for the best
possible return.

Team Name : Team Ascend

Our Solution :
AgroPal is an AI-powered farm companion designed to support smallholder farmers throughout the farming lifecycle. It analyzes crop images to identify diseases and health issues, provides personalized recommendations through a conversational AI assistant, and integrates weather insights to support informed farming decisions. AgroPal also delivers market intelligence, helping farmers determine the best time and place to sell their produce. By combining agronomy, weather forecasting, and market analysis into a single platform, AgroPal empowers farmers to grow smarter and earn better.


AI Component :

1) CLIP (Contrastive Language–Image Pretraining) for crop image understanding and disease identification.
2) Google Gemini API for conversational responses, explanations, and personalized farming recommendations.

 What it does in the app:

- Analyzes uploaded crop images to identify potential diseases, pests, or nutrient deficiencies.
- Converts technical diagnosis results into simple, farmer-friendly explanations.
- Provides contextual recommendations by combining crop health information with weather and market insights.
- Powers the AgroPal chatbot, enabling farmers to ask questions and receive natural language guidance.

Why we chose this approach:

- CLIP is effective for understanding visual agricultural data and associating images with disease-related descriptions.
- Gemini enables natural, multilingual, conversational interactions, making the system accessible to farmers with varying levels of technical knowledge.
- Together, they create an end-to-end AI companion that not only detects problems but also helps farmers make informed decisions about treatment, harvesting, and selling.



Tech Stack -
● Frontend : Streamlit
● Backend : FastAPI
● AI/ML : CLIP and Google Gemini
● Other tools : VS Code

Features Implemented :
- Crop Disease Detection – Upload a crop image to identify diseases, pests, or nutrient deficiencies.
- AI-Powered Chatbot – Conversational assistant that provides farming guidance in simple language.
- Weather Intelligence – Weather-based recommendations to support farming decisions.
- Market Analysis – Provides insights on crop prices and optimal selling opportunities.

How to run the project - 

