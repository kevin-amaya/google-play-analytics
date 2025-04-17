# 📱 Google Play Store Data Analysis

## 📌 Project Overview

This project analyzes the [Google Play Store dataset](https://www.kaggle.com/lava18/google-play-store-apps) to extract meaningful insights about mobile apps, categories, pricing models, and user engagement. The objective is to apply data cleaning, SQL querying, and Python data visualization using tools like PostgreSQL, Pandas, Matplotlib, and Seaborn.

---

## 🛠 Tools & Technologies

- PostgreSQL
- Pandas
- Seaborn & Matplotlib
- DBeaver
- Visual Studio Code
- SQL
- Python

---

## 🔄 Process

1. **Data Import**  
   - Imported the raw CSV dataset into PostgreSQL using DBeaver.

2. **Data Cleaning**  
   - Removed duplicates and nulls.
   - Cleaned columns like `Price`, `Installs`, and `Reviews`.
   - Removed `$` and `+` characters for numeric casting.

3. **Database Connection**  
   - Connected Python to PostgreSQL using `psycopg2` and `SQLAlchemy`.

4. **Data Analysis**  
   - Executed SQL queries to extract insights and trends.

5. **Visualization**  
   - Created bar charts, scatter plots, and pie charts using Seaborn and Matplotlib.

---

## 📊 Visualizations

1. **Top 10 Most Popular Categories**
2. **Distribution of App Ratings**
3. **Price vs Rating Relationship**
4. **Free vs Paid Apps**
5. **Average Rating by Category**
6. **Most Installed App Categories**

*Each visualization was generated using SQL + Python, and saved as part of the final report.*

---

## 📈 Key Insights

1. **App Category Distribution**: 
Insight:
Most of the apps in the Google Play Store belong to the Family and Games categories, which together make up a significant portion of the total offerings. This indicates that entertainment and children-oriented apps dominate the platform.

Explanation:
These categories likely cater to a wide audience, including casual users and families, explaining their popularity. Developers targeting these categories might find high competition but also a large user base.

2. **Average Rating by App Category**: 
Insight:
Categories like Books & Reference, Education, and Productivity tend to have higher average ratings, often above 4.4. In contrast, categories such as Social and Dating have more mixed reviews, with lower average ratings.

Explanation:
Higher-rated categories often provide practical, educational, or informational value, which users appreciate and reward with better ratings. Lower-rated categories may struggle due to subjective experiences, frequent updates, or privacy concerns.

3. **Most Popular App Categories**: 
Insight:
The "Family", "Game", and "Tools" categories dominate the Google Play Store in terms of the number of apps, with Family being the largest.

Explanation:
This indicates a strong market presence for apps targeted at families and children, as well as a constant demand for entertainment and utility-based solutions. For developers, these categories present high competition but also high engagement potential.

4. **Free vs Paid Apps**: Free vs Paid Apps: Which Have Better Ratings?
Insight:
On average, paid apps have slightly higher ratings than free apps, with paid apps averaging around 4.3 and free apps around 4.1.

Explanation:
This suggests that users who pay for apps may be more selective and have higher expectations, often leading to better development quality. Paid apps may also have fewer ads and better support, resulting in more positive experiences.

5. **Relationship Between Rating and Number of Reviews** 
Insight:
Apps with higher ratings generally receive more reviews, but a few apps with average ratings (3.5–4.0) have surprisingly high review counts.

Explanation:
This suggests that while high ratings often reflect user satisfaction and encourage downloads, some apps manage to become popular (high review count) despite not being top-rated. These might be essential tools or widely needed services where function matters more than polish. It also highlights the importance of user engagement and marketing strategies.

6. **Most Installed App Categories**
Insight:
Communication, Social, and Tools categories dominate in total installs, with Communication apps (like WhatsApp, Messenger) being the top.

Explanation:
This shows how basic human needs like connection and productivity drive app usage at scale. Apps that enable people to communicate or simplify daily tasks tend to have the highest penetration. This insight could be crucial for developers or marketers deciding which categories have the broadest reach.


---

## 📁 Folder Structure

```
portfolio/
│
├── import_products.py          # Connects to PostgreSQL and runs queries
├── googleplaystore_cleaned.csv # Cleaned dataset
├── visualizations/             # Folder containing chart images
│   ├── top_categories.png
│   ├── rating_distribution.png
│   ├── price_vs_rating.png
│   ├── free_vs_paid.png
│   ├── avg_rating_by_category.png
│   └── most_installed_categories.png
└── README.md                   # Project documentation
```

---

## ✅ Conclusion

This project demonstrates real-world data analysis skills, including SQL, data cleaning, and insightful visualization. It’s ideal for showcasing analytical thinking and Python/SQL proficiency in a data analyst portfolio.

---

## 📬 Contact

**Kevin Amaya**  
Data Analyst | Python & SQL Developer  
📧 kevin.amayav@outlook.com  
📍 Calgary, Canada  
🔗 [LinkedIn](https://www.linkedin.com/in/kevin-santiago-amaya-vargas/)
