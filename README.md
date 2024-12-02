 # California Wildfire Prediction

A machine learning project to predict wildfire occurrences in California using historical fire data and temperature data.

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Conda package manager (>= 4.6)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/alhridoy/California_wildfire_prediction.git
cd California_wildfire_prediction
```

2. Create and activate the virtual environment:
```bash
conda env create -f environment.yml
conda activate wildfire
```

### Running the Application

Launch the web interface:
```bash
streamlit run server.py
```
The application will open in your default web browser automatically.

> **Note:** If prompted for an email by Streamlit, you can skip this by pressing 'Enter'.

## 📊 Features

- Interactive wildfire prediction interface
- Historical data analysis and visualization
- Model performance evaluation
- Custom data generation capabilities

## 🔧 Advanced Usage

### Custom Data Generation and Model Training

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to the `notebook` folder and run notebooks in numerical order:
   - `01. WildfireData.ipynb`: Process raw fire data
   - `02. TemperatureData.ipynb`: Process temperature data
   - `03. DataAnalysis.ipynb`: Analyze processed data
   - `04. DatasetCreation.ipynb`: Create training datasets
   - `05. ModelTuning.ipynb`: Tune model parameters
   - `06. ModelTraining.ipynb`: Train the final model

### Raw Data Sources

- **Fire Data**: [H2O Global Fire Data](https://s3.us-west-1.amazonaws.com/ai.h2o.challenge.datasets/wildfire-challenge/firms_fires_2013_2021.zip)
- **Temperature Data**:
  - [Average Temperature (2010-2019)](http://berkeleyearth.lbl.gov/auto/Global/Gridded/Complete_TAVG_Daily_LatLong1_2010.nc)
  - [Average Temperature (2020-)](http://berkeleyearth.lbl.gov/auto/Global/Gridded/Complete_TAVG_Daily_LatLong1_2020.nc)
  - [Maximum Temperature (2010-2019)](http://berkeleyearth.lbl.gov/auto/Global/Gridded/Complete_TMAX_Daily_LatLong1_2010.nc)
  - [Maximum Temperature (2020-)](http://berkeleyearth.lbl.gov/auto/Global/Gridded/Complete_TMAX_Daily_LatLong1_2020.nc)
  - [Minimum Temperature (2010-2019)](http://berkeleyearth.lbl.gov/auto/Global/Gridded/Complete_TMIN_Daily_LatLong1_2010.nc)
  - [Minimum Temperature (2020-)](http://berkeleyearth.lbl.gov/auto/Global/Gridded/Complete_TMIN_Daily_LatLong1_2020.nc)

### Managing Dependencies

Add new dependencies to `req.in` and regenerate `req.txt`:
```bash
pip-compile req.in
pip install -r req.txt
```

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
