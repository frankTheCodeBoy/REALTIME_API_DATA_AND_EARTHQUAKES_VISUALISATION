## 🌍 Real-Time API Data & Earthquakes Visualization

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  
[![Made by Frank](https://img.shields.io/badge/Made%20by-FrankTheCodeBoy-blueviolet)](https://github.com/frankTheCodeBoy)

This repository contains Python scripts and HTML outputs for visualizing:

- 🔥 Real-time API data (e.g. GitHub repos, Hacker News discussions, top headlines)  
- 🌋 GeoJSON-based global earthquake and wildfire data

All visualizations are rendered as interactive HTML documents.

---

### 📁 Project Structure

```plaintext
REALTIME_API_DATA_AND_EARTHQUAKES_VISUALISATION/
├── active_discussions.py
├── global_earthquakes_visual.py
├── js_repos_visual.py
├── python_repos_visual.py
├── top_headlines_visual.py
├── world_fires_visual.py
├── *.html (output visualizations)
└── README.md
```

---

### 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/frankTheCodeBoy/REALTIME_API_DATA_AND_EARTHQUAKES_VISUALISATION.git
   cd REALTIME_API_DATA_AND_EARTHQUAKES_VISUALISATION
   ```

2. Install required modules:
   ```bash
   pip install requests plotly
   ```

3. Run any script:
   ```bash
   python global_earthquakes_visual.py
   ```

4. Open the generated `.html` file in your browser to view the visualization.

---

### 🌐 Visualizations Included

| Script                        | Output HTML               | Description                                      |
|------------------------------|---------------------------|--------------------------------------------------|
| `global_earthquakes_visual.py` | `largescale_earthquakes.html` | Maps recent global earthquakes using GeoJSON     |
| `world_fires_visual.py`        | `global_fires.html`          | Displays active wildfires around the world       |
| `top_headlines_visual.py`      | `top_usa_news.html`          | Visualizes top U.S. news headlines               |
| `js_repos_visual.py`           | `js_repos.html`              | Shows trending JavaScript GitHub repos           |
| `python_repos_visual.py`       | `python_repos.html`          | Highlights trending Python GitHub repos          |
| `active_discussions.py`        | `hn_discussions.html`        | Tracks active Hacker News threads                |

---

### 🎯 Purpose

This project was built to:

- Practice real-time API integration  
- Explore data visualization with Plotly  
- Experiment with GeoJSON and interactive maps  
- Generate reusable HTML dashboards

---

### 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.

---
