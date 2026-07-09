# Smart Pantry & Food Waste Tracker

A production-grade, Streamlit-based pantry management and sustainability application designed to track grocery inventories, automate expiry monitoring, analyze financial waste metrics, and optimize household grocery utilization.

---

## Live Application

Access the deployed system here: **[Smart Pantry Dashboard](https://smart-pantry-food-waste-tracker.streamlit.app/)**

---

## Application Demonstration

Here is a live walkthrough showcasing item management, real-time analytics, and expirations tracking:

<video src="https://github.com/user-attachments/assets/6548310a-6523-4d34-994f-a0fb3b831723" width="100%" controls autoplay loop muted playsinline></video>

---

##  Key Features

* **Full CRUD Operations:** Add, update, query, and eliminate grocery inventory items seamlessly.
* **Automated Expiry Tracking:** Visual alerts and chronological warnings for items approaching critical dates.
* **Pantry Health Scoring:** Algorithmic sustainability metrics reflecting inventory efficiency and minimized waste trends.
* **Advanced Category Analytics:** Visual distribution charts segmenting pantry cost concentration and quantity balances.
* **Interactive Data Visualization:** Custom Plotly dashboards tracking waste projections and financial data.
* **Robust Persistence & Export:** Flat-file JSON structural storage with single-click custom CSV schema reports exporting.
* **Dynamic Search Architecture:** Instant multi-parameter querying and granular structural inventory filtering.

---

## Tech Stack & Dependencies

* **Interface & Framework:** Streamlit (Dynamic layout compilation)
* **Data Processing Engines:** Python 3.9+, Pandas (Structured data frame manipulation), NumPy
* **Data Visualization Layer:** Plotly Express (Interactive charts & engine rendering)
* **Storage Schema:** Native JSON Engine (Lightweight local state persistence)

---

##  Project Architecture

```text
food-waste-project/
│
├── app/
│   └── app.py               # Main UI rendering engine and routing controls
│
├── data/
│   └── grocery_data.json    # Local state persistence data schema
│
├── utils/
│   └── pantry.py            # Business logic and abstract data handling functions
│
├── requirements.txt         # Package pinning and dependencies list
│
└── README.md                # Structural documentation
```

---

##  Local Installation & Setup

Follow these steps to deploy a localized instance of the project environment:

### 1. Replicate Project Files
```bash
git clone https://github.com
cd food-waste-project
```

### 2. Configure Virtual Environment & Packages
```bash
pip install -r requirements.txt
```

### 3. Initialize Runtime Engine
```bash
streamlit run app/app.py
```

---

##  Engineering Roadmap & Future Scale

* **Storage Evolution:** Migrate flat JSON schemas over to fully relational SQLite database clustering.
* **Access Control Infrastructure:** Implement robust multi-tenant encryption and secure User Authentication.
* **Hardware Integration APIs:** Deploy mobile device Barcode Camera Scanning functionalities.
* **Computer Vision Processing:** Integrate OCR receipt capture pipelines to instantly parse retail checkouts.
* **Predictive AI Modelling:** Build machine learning forecast engines to proactively alert consumption velocities.
* **Cloud Architecture:** Transition baseline hosting dependencies out to managed distributed systems.

---

##  License

Distributed under the MIT License. See `LICENSE` for more details.
