## Overview
An interactive Streamlit web app for analyzing helicopter aerodynamic performance and finding optimal flight velocities ($V_{opt}$).

## Key Features
- **Dynamic Parameter Configuration**: Adjust velocity ranges and calculation resolution in real-time via the sidebar.
- **Aerodynamic Analysis**: Calculates Parasite Drag, Induced Drag, and Total Drag based on helicopter specifications.
- **Performance Optimization**: Automatically identifies the Optimal Velocity ($V_{opt}$) for minimum drag.
- **High-Resolution Visualization**: Generates clear, multi-column grid layouts for fleet comparisons using Matplotlib.
- **Interactive Reports**: View summary tables of optimal flight parameters for the entire fleet.

## Tech Stack
- **Frontend**: Streamlit
- **Data Handling**: Pandas, NumPy
- **Visualization**: Matplotlib
- **Core Logic**: Object-Oriented Programming (OOP) in Python

## Project Structure
helicopter-drag-optimizer/
├── app.py               # Main Streamlit application entry point
├── src/                 # Core logic modules
│   ├── models.py        # Helicopter class and physics calculations
│   ├── DataProcessing.py # Data validation and CSV parsing
│   └── visualizer.py    # Plotting logic and grid layout management
├── data/                # Sample CSV data files
├── requirements.txt     # Project dependencies
└── README.md            # Documentation

## Getting Started

### 1. Clone the Repository
git clone https://github.com/your-username/helicopter-drag-optimizer.git
cd helicopter-drag-optimizer

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Application
streamlit run app.py


## 📊 Methodology
The optimizer uses standard aerodynamic drag equations:
1. **Parasite Drag**: $D_p = \frac{1}{2} \rho V^2 f$
2. **Induced Drag**: $D_i = \frac{k W^2}{2 \rho V^2 \pi R^2}$
3. **Total Drag**: $D_t = D_p + D_i$
