# Bike Sharing Data Analisys Project

## Project Description
This project aims to analyze Bike Sharing data to answer business questions in the form of:
1. Is there a difference in bicycle demand between weekday and holyday?
2. How does weather affect bicycle demand?
3. How does bicycle usage differ between registered and unregistered users?
4. Is there a seasonal trend in bicycle usage?

## Dataset

## Analysis steps
- Data Wrangling: Collecting and organizing data from various sources for further analysis.
- Data Assessment: Assessing data quality before the preprocessing stage, including the identification of missing values, duplicates, and other errors.
- Data Preprocessing: Performing data cleaning, including handling missing values and duplicates. Exploratory Data Analysis (EDA) is also performed at this stage to gain initial insights from the clean data and understand patterns.
- Visualization and Inference: Answering business questions with supporting visualizations, as well as summarizing findings and providing recommendations based on the analysis.

## Tool And Library
- Google Colab
- Numpy
- Pandas
- Matplotib
- Seaborn

## Results and Discussion
1. Conclution question 1: Is there a difference in bicycle demand between weekday and holyday?

The total demand for bicycles on weekdays/*working day* is higher than on holidays/*Holiday*, indicating that more people use bicycles for commuting to work or other routine activities on weekdays.

![download (6)](https://github.com/user-attachments/assets/959b7b49-5447-4224-8c5c-21e0c8ea7ded)

2. Conclution question 2: How does weather affect the demand for bicycles?

- The number of bicycle users is very high in *clear, cloudy* weather. this means that bicycle users will decrease if the weather starts to get bad or worse.
- There is a positive correlation between temperature (temp, atemp) and bicycle demand. This means that as temperature increases, the amount of bicycle demand also tends to increase.
- There is a negative correlation between humidity (hum) and bicycle demand, indicating that humid conditions reduce bicycle use.
- Windspeed also shows a negative correlation with the amount of bicycle demand.

![download (7)](https://github.com/user-attachments/assets/1508af82-402b-4aee-9699-d524c9dff02b)
![download (6)](https://github.com/user-attachments/assets/eed9803b-65e9-4287-9893-8b0363cd3e06)

3. Conclution Question 3: How does bicycle use differ between registered and unregistered users?

Registered users tend to use bicycles more often than unregistered users. The average amount of bicycle use by registered users is higher. This suggests that registered users may use bicycles more often for routine purposes such as commuting to work, while unregistered users are more likely to use bicycles for recreation.

![download (9)](https://github.com/user-attachments/assets/b064de8c-4ab7-4697-8b27-890bb1643e64)

4. Conclution Question 4: Are there any seasonal trends in bicycle use?

Bicycle use peaks in the fall. Fall often has more comfortable temperatures than summer which may be too hot and winter which may be too cold. Cooler temperatures make cycling more enjoyable.

![download (10)](https://github.com/user-attachments/assets/c5940b20-e741-4b15-b01d-97333211d50d)

## How Run Streamlit Dashboard
```
Clone Repository
git clone https://github.com/Smjfirna/Bike-Sharing-Data-Analisys.git
```
Setup Environment - Terminal
```
pip install -r requirements.txt
```
Run steamlit app
```
streamlit run dashboard.py
```





  
