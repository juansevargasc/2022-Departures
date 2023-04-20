# US Flight Departures - 2022
<figure>
    <img src="img/nicolas-jehly-6WImwokn8dA-unsplash.jpg"
         alt="Newark Airport">
    <figcaption>Newark, New Jersey @nicolasjehly</figcaption>
</figure>

## Description
This project aims to explore the US flight departures features in 2022. This will be made through the analysis of weather conditions, cancellations, dates, locations and carriers among others. Nevertheless, it will feature first a ETL pipeline to preprocess different data sources and then load into a OLAP database, for BI consumption.

## Table of contents
### 1. Data Engineering Stage
- ETL Pipeline.
- Star architecture.

### 2. Data Analysis Stage
- Questions.
- Data exploration.
- Statistics.
---

### Data Engineering Stage
#### Prework and Introduction
The project aims to analyze the files that are given in this dataset:
[2022 U.S. Domestic Flights Departures](https://www.kaggle.com/datasets/jl8771/2022-us-airlines-domestic-departure-data)
<figure>
    <img src="img/Screenshot 2023-04-20 at 12.39.04 PM.png"
         alt="Kaggle Dataset Flight Dep.">
    <figcaption>Author: Jacky Luo</figcaption>
</figure>

The prework is made to take some original files and export them to SQL database and a JSON file
to simulate we have different data sources in the project.

Although all the files come as CSV files, we want to simulate that some of them come from
those sources to have a similar experience that you would have in a client project
 or in a product company project.
