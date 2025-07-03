

from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

API_KEY = "3012f9dd2026a4fa68b7707d491bf03d"  

def fetch_flight_data():
    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&limit=100"
    response = requests.get(url)
    data = response.json()
    flights = data.get("data", [])
    
    records = []
    for flight in flights:
        record = {
            "Airline": flight.get("airline", {}).get("name"),
            "Flight Number": flight.get("flight", {}).get("number"),
            "Departure": flight.get("departure", {}).get("airport"),
            "Arrival": flight.get("arrival", {}).get("airport"),
            "Status": flight.get("flight_status")
        }
        records.append(record)

    return pd.DataFrame(records)

@app.route("/")
def home():
    df = fetch_flight_data()

    # Route counts
    popular_routes = df.groupby(["Departure", "Arrival"]).size().reset_index(name="Count")
    popular_routes = popular_routes.sort_values(by="Count", ascending=False).head(5).to_dict(orient="records")

    # Status counts
    status_counts = df["Status"].value_counts().to_dict()

    # Airline counts
    airline_counts = df["Airline"].value_counts().head(5).to_dict()

    return render_template("index.html",
                           flights=df.head(10).to_dict(orient="records"),
                           routes=popular_routes,
                           status=status_counts,
                           airlines=airline_counts)

if __name__ == "__main__":
    app.run(debug=True)
