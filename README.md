# Smart Pantry & Food Waste Tracker

A Streamlit-based pantry management application that helps users track groceries, monitor expiry dates, analyze pantry value, and reduce food waste.

## Features

* Add, update, search, and delete pantry items
* Track expiry dates automatically
* Pantry health score system
* Category-based analytics
* Interactive charts and visualizations
* CSV export support
* Persistent storage using JSON
* Smart filtering and search

## Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* JSON

## Project Structure

food-waste-project/
│
├── app/
│   └── app.py
│
├── data/
│   └── grocery_data.json
│
├── utils/
│   └── pantry.py
│
├── requirements.txt
│
└── README.md

## How to Run

1. Clone the repository

```bash
git clone <repo-link>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
streamlit run app/app.py
```

## Future Improvements

* SQLite database integration
* User authentication
* Barcode scanning
* OCR receipt scanning
* AI-based food waste prediction
* Cloud deployment
