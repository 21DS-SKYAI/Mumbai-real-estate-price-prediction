# 🏙️ Real Estate Price Prediction Engine (Mumbai Micro-Markets)

An end-to-end ML system to predict property prices across Mumbai using structured data such as location, carpet area, floor, age, view, amenities, and proximity metrics.

---

## 🎯 Objective
Provide accurate and explainable price predictions to help:
- Brokers justify pricing  
- Buyers make informed decisions  
- Internal teams reduce over/underpricing  
- Support negotiation strategies  

---

## 🏗️ Tech Stack
- **Models:** Linear Regression, Random Forest, XGBoost  
- **Processing:** PySpark  
- **Data Storage:** SQL, CSV  
- **Visualization:** Power BI / Tableau  
- **Deployment:** Flask/FastAPI, Docker, AWS EC2  

---

## 📁 Dataset Details
- 100,000+ Mumbai property listings  
- Features include:
  - Locality score
  - Carpet area
  - Floor height
  - Age of building
  - Vastu compliance
  - View quality  
  - Nearby amenities
  - Parking availability

---

## ⚙️ Architecture Overview
1. Data ingestion (SQL, CSV)
2. PySpark-based feature engineering
3. Model training (RF, XGB)
4. Model validation
5. API deployment
6. Dashboard visualization

---

## 📊 Model Performance
| Model | R² Score |
|-------|---------|
| Linear Regression | 0.78 |
| Random Forest | 0.89 |
| XGBoost | **0.91** |

---

## 🚀 Key Features
- Automated outlier detection  
- Location encoder + clustering-based locality scores  
- Feature importance dashboard  
- Price band visualization for micro-markets  
- REST API for on-demand predictions  

---

## 🛠️ Setup

```bash
git clone https://github.com/yourusername/price-prediction-engine
cd price-prediction-engine
pip install -r requirements.txt
python src/train_model.py
python app/main.py

## 🗺️ Example Prediction

Input:

3 BHK, Worli, 1800 sq ft, Sea view, 10-year-old building

Output:

Predicted Price: ₹9.8 Cr  
Confidence Range: ± ₹0.4 Cr

📌 Future Enhancements

LSTM / Time-series based price trend forecasting

GeoAI features (distance to coastline, noise levels, AQI)

Real estate market sentiment integration
