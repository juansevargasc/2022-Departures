# US Flight Departures - 2022
<figure>
    <img src="img/nicolas-jehly-6WImwokn8dA-unsplash.jpg"
         alt="Newark Airport">
    <figcaption>Newark, New Jersey @nicolasjehly</figcaption>
</figure>

## Description
This project aims to explore the US flight departures features in 2022. This will be made through the analysis of weather conditions, cancellations, dates, locations and carriers among others. Nevertheless, it will feature first a ETL pipeline to preprocess different data sources and then load into a OLAP database, for BI consumption.

## Table of contents
### Data Engineering Stage
**Objectives**
- Extract data from different sources. In this case it comes from 5 CSV Files but two of them are worked out to be in a Relational Database and the other to be a JSON file so simulate different types of sources. See prework.
- Design a data schema that allows to query data for BI purposes
- Create an ETL Pipeline.
- Clean data by choosing which `NaN` (empty) values should be dropped.
- Standardizing names, making conventions.
- Testing and enforcing data types and schemas.
- Build a Star architecture.

### Data Analysis Stage
**Objectives**
- Make questions interesting questions such as: 
    - Is there a correlation between delays and wheather?
    - How many flights did a certain airline make during the year?
    - What's the most common route? Is there an impact from wheather in a route?
- Make a Data exploration and characterize some columns.
- Make some Statistics:
    - What's the average of flights per day?
    - How many flights are delayed per day?
    - Does the wheather events follow a normal distribution? Another type of distribuition?
---

### 1. Data Engineering Stage

**Introduction**

The project aims to analyze the files that are given in this dataset:
[2022 U.S. Domestic Flights Departures](https://www.kaggle.com/datasets/jl8771/2022-us-airlines-domestic-departure-data)
<figure>
    <img src="img/Screenshot 2023-04-20 at 12.39.04 PM.png"
         alt="Kaggle Dataset Flight Dep.">
    <figcaption>Author: Jacky Luo</figcaption>
</figure>

---

**Prework**

The prework is made to take some original files and export them to SQL database and a JSON file
to simulate we have different data sources in the project.  See more in [Prework](./prework)

**Documentation of Stages**

- [Raw Tables](./docs/RawTables.md)
- [Staging Tables](./docs/StagingTables.md)
- [Star Schema Tables](./docs/RawTables.md)

