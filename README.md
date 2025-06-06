<p align=center>
<img src="./lib/logo.png" width="200">
</p>

<h1 align="center">Formula One Radar - F1R</h1>

<p align=center>
<b>Powered by Turn One -</b>
<a href="www.t1f1.com">t1f1.com</a>
</p>

> [!NOTE]
> This application is still in **active development** with no official release date.
> It is going to be functional with a **basic user interface** on our website soon.

---

## Table of Contents

- [About F1 Radar](#about-fota)
- [How to install](#how-to-install)
- [How to Use](#how-to-use)
- [Future Plans](#about-fota)
- [Contact & Support](#powered-by-turnoneofficial)
- [Examples](#examples-of-plots-generated-with-fota)

---

## About FOTA

The **Formula One Radar** application is designed to process and visualize in realtime telemetry data from Formula One cars.
This tool allows users to watch Formula One live with a dashboard that is providing a deep understanding of performance metrics such as
speed, throttle, braking, and sector times. F1 Radar is built with simplicity in mind but aims to become a comprehensive telemetry analysis
suite in the future. 

Planned future updates include:
- [ ] **Enhanced Graphing Options**: More customizable data visualizations.
- [ ] **Advanced Features**: Additional functionalities like comparative analysis between drivers or races, lap-by-lap breakdowns, and real-time data tracking (subject to availability).

Whether you're a Formula One enthusiast, a data analyst, or a racing engineer, F1 Radar offers a powerful way to dive into the rich data of the sport.

## How to install:

### Update package lists and install Git
```bash
sudo apt update
sudo apt install git
```

### Clone the repository
```bash
git clone https://github.com/MihaiM21/FormulaOneRadar
cd FormulaOneTelemetryAnalysis
```

### Install Python and Pip (if not already installed)
```bash
sudo apt install python3 python3-pip
```

### (Optional) Set up a Python virtual environment
```bash
sudo apt install python3-venv
python3 -m venv fota-env
source fota-env/bin/activate
```

### Install required Python libraries from the requirements.txt file
```bash
pip install -r requirements.txt
```

### Run the program
```bash
python3 program.py
```

## How to use:

1. **Run the Application**:  
   Start the program by executing `program.py` through a Python environment or command line.
2. **Select the Parameters**:  
   Choose from the following options:
   - **Year**: Select the specific season you want data from.
   - **Plot Type**: Depending on the type of analysis you want to perform, select a plot type. Some options will require specifying the **drivers** or **teams** involved.
   - **Event Type**: Choose from various Formula One event types:
     - `"R"` → **Race**
     - `"S"` → **Sprint Race**
     - `"Q"` → **Qualifying**
     - `"SQ"` → **Sprint Qualifying**
     - `"FP1"`, `"FP2"`, `"FP3"` → **Free Practice Sessions** 1, 2, or 3

3. **Execute**:  
   Once you’ve made your selections, click on **Execute** to run the analysis. The program will process the telemetry data and generate the appropriate visualizations.

4. **Access Results**:  
   The generated plot will be saved in the `plots` folder, where you can review and analyze it at your convenience. Each file will be named according to the selected event, making it easy to organize and compare multiple data sets.

## Examples of plots generated with FOTA:
<p align=center>  
    <img src="plots/2025/Japanese Grand Prix/Driver Analysis 2025 Japanese Grand Prix SAI.png" width="800">
    <img src="plots/2025/Japanese Grand Prix/2025 Japanese Grand Prix LEC vs PIA Fastest Lap Comparison.png" width="800">
    <img src="plots/2025/Japanese Grand Prix/2025 Japanese Grand Prix Laptimes distribution.png" width="800">
    <img src="plots/2025/Japanese Grand Prix/2025 Japanese Grand Prix Tyre strategy.png" width="800">
    <img src="plots/2024/Spanish Grand Prix/2024 Spanish Grand Prix VER Laptimes.png" width="800">
    <img src="plots/2025/Japanese Grand Prix/Japanese Grand Prix Qualifying 2025 HAM vs NOR.png" width="800">
    <img src="plots/2025/Japanese Grand Prix/Top speed comparison 2025 Japanese Grand Prix Qualifying .png" width="800">
    <img src="plots/2025/Japanese Grand Prix/2025 Japanese Grand Prix Position changes.png" width="800">
    <img src="plots/2025/Japanese Grand Prix/2025 Japanese Grand Prix Team pace.png" width="800">
    <img src="plots/2025/Japanese Grand Prix/2025 Japanese Grand PrixHAM vs LEC Throttle graph.png" width="800">
</p>

---

<p align=center>
<b>Powered by TurnOneOfficial</b>
</p>
