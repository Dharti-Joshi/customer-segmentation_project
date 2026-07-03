-- ===========================================
-- Customer Segmentation SQL Queries
-- ===========================================

-- 1. Display all customers
SELECT * FROM customers;

-- 2. Total number of customers
SELECT COUNT(*) AS Total_Customers
FROM customers;

-- 3. Average Annual Income
SELECT AVG(AnnualIncome) AS Average_Income
FROM customers;

-- 4. Average Spending Score
SELECT AVG(SpendingScore) AS Average_Spending_Score
FROM customers;

-- 5. Total Revenue
SELECT SUM(TotalSpent) AS Total_Revenue
FROM customers;

-- 6. Male vs Female Customers
SELECT Gender, COUNT(*) AS Total_Customers
FROM customers
GROUP BY Gender;

-- 7. Top 10 Highest Spending Customers
SELECT CustomerID,
       TotalSpent
FROM customers
ORDER BY TotalSpent DESC
LIMIT 10;

-- 8. Top 10 Highest Spending Score
SELECT CustomerID,
       SpendingScore
FROM customers
ORDER BY SpendingScore DESC
LIMIT 10;

-- 9. Customers with Annual Income above 60000
SELECT *
FROM customers
WHERE AnnualIncome > 60000;

-- 10. High Spending Customers
SELECT *
FROM customers
WHERE SpendingScore >= 80;

-- 11. Average Purchase Frequency
SELECT AVG(PurchaseFrequency) AS Average_Purchase_Frequency
FROM customers;

-- 12. Customers by Age
SELECT Age,
       COUNT(*) AS Total
FROM customers
GROUP BY Age
ORDER BY Age;

-- 13. Highest Annual Income
SELECT *
FROM customers
ORDER BY AnnualIncome DESC
LIMIT 1;

-- 14. Lowest Annual Income
SELECT *
FROM customers
ORDER BY AnnualIncome ASC
LIMIT 1;

-- 15. Customers Spending More Than ₹40,000
SELECT *
FROM customers
WHERE TotalSpent > 40000;

-- 16. Average Total Spent by Gender
SELECT Gender,
       AVG(TotalSpent) AS Average_Spent
FROM customers
GROUP BY Gender;

-- 17. Customers by Spending Score Category
SELECT
CASE
    WHEN SpendingScore >= 80 THEN 'High'
    WHEN SpendingScore >= 50 THEN 'Medium'
    ELSE 'Low'
END AS Spending_Category,
COUNT(*) AS Total_Customers
FROM customers
GROUP BY Spending_Category;

-- 18. Highest Purchase Frequency
SELECT *
FROM customers
ORDER BY PurchaseFrequency DESC
LIMIT 5;

-- 19. Total Revenue by Gender
SELECT Gender,
       SUM(TotalSpent) AS Revenue
FROM customers
GROUP BY Gender;

-- 20. Customer Segments (if CustomerSegment column exists)
SELECT CustomerSegment,
       COUNT(*) AS Customers
FROM customers
GROUP BY CustomerSegment;