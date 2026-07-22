import os
import pickle

from flask import Flask, render_template, request

application = Flask(__name__)
app = application

ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
scaler_model = pickle.load(open("models/scaler.pkl", "rb"))

FEATURES = ["Temperature", "RH", "Ws", "Rain", "FFMC", "DMC", "ISI", "Classes", "Region"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method != "POST":
        return render_template("home.html")

    try:
        values = [float(request.form.get(name)) for name in FEATURES]
    except (TypeError, ValueError):
        error = "Please enter a valid number in every field."
        return render_template("home.html", error=error)

    scaled_data = scaler_model.transform([values])
    result = ridge_model.predict(scaled_data)

    return render_template("home.html", results=round(float(result[0]), 2))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
