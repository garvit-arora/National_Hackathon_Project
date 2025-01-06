# Retrieval-Augmented Generation (RAG) Pipeline
def get_personalized_recommendations(data):
    recommendations = []
    if data["heart_rate"].iloc[0] > 120:
        recommendations.append("⚠️ High heart rate detected. Rest and hydrate immediately.")
    if data["steps"].iloc[0] < 5000:
        recommendations.append("🚶‍♀️ Low activity detected. A 15-minute walk is recommended.")
    if data["SpO2"].iloc[0] < 95:
        recommendations.append("🫁 SpO₂ is low. Practice deep breathing or consult a doctor if persistent.")
    if data["weather"].iloc[0] == "High Humidity":
        recommendations.append("🌦️ Avoid outdoor activities due to high humidity.")
    return recommendations
