# Global Electric Vehicle Market & Performance Insights
Electric Vehicle (EV) adoption is accelerating worldwide but how do different models compare in range, battery technology, efficiency, pricing, and segment performance?

This project scrapes a comprehensive dataset of EV models, preprocesses and analyzes the data, and visualizes key performance & market insights using an interactive Tableau dashboard.

## Problem Statement
This project collects data for 1,000+ EV models from this [website](https://ev-database.org) globally, enabling deeper analytical insights into EV technological competitiveness and market positioning.

## Goals and Objective
**Goal:**
Understand EV performance trends and market competitiveness across brands & segments.

**Objectives:**
- Scrape EV specifications using Selenium
- Preprocess, Transform and Manipulate the data using Python
- Visualize insights in Tableau Dashboard for clear interpretation

**Key Questions**
- Do larger batteries always translate to better driving range?
- Which segments deliver the best efficiency and range?
- Which brands offer the strongest overall performance?
- What are the Top 10 EVs in battery, range, efficiency & value?
- How do price and performance correlate across the market?

## Tableau Dashboard
Explore the interactive dashboard here: [Tableau Dashboard](https://public.tableau.com/app/profile/mohtasim.fahim/viz/GlobalEVMarketPerformanceInsights/Dashboard1)


## Key Findings & Insights  

Top 20 Longest-Range EVs
- Lucid Air Grand Touring variants dominate with 700+ km range — highest in the dataset
- High-end Mercedes EQS models are also strong in long-distance capability (~600–650 km)
- Longest-range EVs are mostly from the Executive & Luxury segments
- Few mainstream or budget brands appear in the Top 20, high range is still a premium feature

Most Models by Brand
- Mercedes-Benz, Volkswagen, and Audi lead EV production volume
- Ford, Volvo, Peugeot, Tesla also demonstrate significant model diversification
- This shows legacy automakers are rapidly expanding EV portfolios, not just EV-only brands

Average Range by Segment
- Luxury (F) and Executive (E) segments provide the highest average range
- Medium (C) and Large (D) segments offer a good balance of range and affordability → likely best value for most consumers
- Mini (A) segment performs poorly in range, remaining city-focused
- Passenger vans (N) have lower efficiency and shorter range due to their weight & purpose

Average Price by Brand
- Lightyear, Porsche, Lucid, and Lotus are the most premium-priced EV manufacturers
- Luxury-focused brands correlate with higher range and performance
- However, high price does not always ensure superior efficiency (seen in next insight)

Price vs Range (Market Value Distribution)
- Positive correlation: higher price → higher range
- But, Several expensive EVs sit below trendline , overpriced for the range offered
- Some mid-budget EVs perform above trendline, excellent value per km

Battery vs Range (Tech Efficiency)
- Strong linear correlation, larger batteries = better range
- But diminishing returns after ~90–100 kWh → efficiency, not size, becomes the bottleneck
- Outliers above the line (e.g., Lucid) indicate superior battery & aerodynamic tech

## Build From Sources and Run the Selenium Scraper
1. Clone the repo
```bash
git clone https://github.com/mohtasim22/Global-EV-Market-Performance-Insights.git
```
2. Intialize and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the scraper
```bash
python src/scraper.py
```
5. Run the preprocessing file
```bash
python src/preprocessing.py
```
6. You will get ev_cars_details.csv inside data folder. To check our scraped data you can visit [ev_cars_details.csv](https://github.com/mohtasim22/Global-EV-Market-Performance-Insights/blob/main/data/ev_cars_details.csv)

## Contact
If you have any queries you can contact me here: fahimatbd@gmail.com
