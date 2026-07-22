# Algerian Forest Fire — FWI Prediction

A web app that predicts the **Fire Weather Index (FWI)** from weather and fuel-moisture readings using a Ridge Regression model. Built with Flask and scikit-learn, with a custom front end.

The model is trained on the [Algerian Forest Fires dataset](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset) from the UCI Machine Learning Repository, which covers the Bejaia and Sidi-Bel Abbes regions of Algeria between June and September 2012.

## How it works

The user enters nine values (temperature, humidity, wind, rain, and four fire-behaviour indices). The app scales them with the same `StandardScaler` used during training and feeds them to the trained Ridge model, which returns the predicted FWI along with a danger band (Low / Moderate / High / Extreme).

## Project structure

```
.
├── application.py          Flask app: routes and prediction logic
├── requirements.txt        Python dependencies
├── models/
│   ├── ridge.pkl           Trained Ridge Regression model
│   └── scaler.pkl          StandardScaler fitted on the training data
├── static/css/style.css    Front-end styling
├── templates/
│   ├── index.html          Landing page
│   └── home.html           Prediction form and result
└── notebooks/
    ├── project.ipynb       Full workflow: cleaning, EDA, training, export
    └── *.csv               Raw and cleaned datasets
```

## Getting started

Clone the repository:

```bash
git clone https://github.com/Hanzala-Nadeem/algerian-forest-fire-fwi-prediction-using-ridge_regression.git
cd algerian-forest-fire-fwi-prediction-using-ridge_regression
```

Create a virtual environment and install the dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Run the app:

```bash
python application.py
```

Then open http://localhost:5000 in your browser. For a production server, use `gunicorn application:app`.

## Model inputs

| Feature | Description | Example |
|---|---|---|
| Temperature | Temperature at noon (°C) | 29 |
| RH | Relative humidity (%) | 57 |
| Ws | Wind speed (km/h) | 18 |
| Rain | Total rain (mm) | 0.0 |
| FFMC | Fine Fuel Moisture Code | 65.7 |
| DMC | Duff Moisture Code | 3.4 |
| ISI | Initial Spread Index | 1.3 |
| Classes | Fire class (0 = not fire, 1 = fire) | 0 |
| Region | 0 = Bejaia, 1 = Sidi-Bel Abbes | 0 |

## Notebook

`notebooks/project.ipynb` contains the full pipeline: cleaning the raw data, exploratory analysis, dropping highly correlated features, comparing Linear, Lasso, Ridge and ElasticNet regressors, and exporting the chosen Ridge model and scaler used by the app.

## Tech stack

Python · Flask · scikit-learn · pandas · numpy · matplotlib · seaborn

The bundled model files were produced with scikit-learn 1.7.2. To regenerate them with your own version, re-run `notebooks/project.ipynb`.

## Author

hanzalanadeem
