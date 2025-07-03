


# ✈️ Airline Booking Market Demand Web App

This project is a simple Python-based web application that fetches, processes, and visualizes real-time airline booking data. It is built using Flask and Chart.js, and uses the Aviationstack API to provide valuable insights such as popular travel routes, flight statuses, and airline-wise flight frequencies.



## 📌 Objective

To help travel-related businesses track market demand in the airline booking industry using real-time data, presented in an easy-to-use dashboard with tables and charts.



## 🚀 Features

- 🔄 Real-time flight data from **Aviationstack API**
- 📊 Data analysis using **Pandas**
- 🌐 Web interface created with **Flask**
- 📈 Interactive charts using **Chart.js**
- 🧾 Summary tables for routes, statuses, and airlines



## 🧱 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Backend      | Python (Flask)     |
| Frontend     | HTML + Chart.js    |
| API          | Aviationstack      |
| Data Library | Pandas, Requests   |
| Deployment   | Localhost (for now)|



## 📂 Folder Structure



airline-demand-app/
│
├── app.py                 # Flask app logic
├── requirements.txt       # Project dependencies
├── README.md              # Project overview
│
├── templates/
│   └── index.html         # Main HTML page


## 🧪 How to Run This Project

### 1. Clone this repository
bash
git clone https://github.com/Shreyabagal/airline-demand-app.git
cd airline-demand-app


### 2. Install the required packages

bash
pip install -r requirements.txt


### 3. Add your API key

In `app.py`, replace:

python
API_KEY = "your_key_here"


with your personal Aviationstack API key
(Get a free key at: [https://aviationstack.com](https://aviationstack.com))

### 4. Run the Flask app

bash
python app.py


Open your browser and go to:


http://127.0.0.1:5000/


## 📈 Dashboard Insights

* **Top 5 Most Popular Routes**
* **Flight Status Counts** (Active, Landed, etc.)
* **Flights Per Airline**

Each section shows both a **data table** and an **interactive chart** for easy understanding.



## 🔑 API Used

**Aviationstack API**
Free flight data API that provides access to global airline schedules, statuses, and route details.
🔗 [https://aviationstack.com](https://aviationstack.com)



## 👩‍💻 Developer

**Shreya Bagal**
📧 Email: [shreyabagal@gmail.com](mailto:shreyabagal@gmail.com)
🔗 GitHub: [https://github.com/Shreyabagal](https://github.com/Shreyabagal)


