CREATE TABLE ecommerce_clean (
    transaction_id TEXT,
    customer_id TEXT,
    category TEXT,
    item TEXT,
    price_per_unit FLOAT,
    quantity INT,
    total_spent FLOAT,
    payment_method TEXT,
    location TEXT,
    transaction_date DATE,
    discount_applied BOOLEAN
)

SELECT * FROM ecommerce_clean
LIMIT 10

-- Q1: Total Revenue

SELECT SUM(total_spent) AS total_revenue
FROM ecommerce_clean

-- Q2: Total Orders

SELECT COUNT(*) AS total_orders
FROM ecommerce_clean

-- Q3: Average Order Value

SELECT AVG(total_spent) AS average_order_value
FROM ecommerce_clean

-- Q4: Top Selling Category

SELECT
category,
SUM(quantity) AS total_quantity
FROM ecommerce_clean
GROUP BY category
ORDER BY total_quantity DESC
LIMIT 1

-- Q5: Revenue by Category

SELECT 
category, 
SUM(total_spent) AS revenue
FROM ecommerce_clean
GROUP BY category
ORDER BY revenue DESC

-- Q6: Top 5 Customers by Spending

SELECT
customer_id,
SUM(total_spent) AS total_spent
FROM ecommerce_clean
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5

-- Q7: Repeat Customers

SELECT
customer_id,
COUNT(*) AS orders
FROM ecommerce_clean
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY orders DESC

-- Q8: Payment Method Distribution

SELECT
payment_method,
COUNT(*) AS total_orders
FROM ecommerce_clean
GROUP BY payment_method
ORDER BY total_orders DESC

-- Q9: Revenue by Payment Method

SELECT
payment_method,
SUM(total_spent) AS revenue
FROM ecommerce_clean
GROUP BY payment_method
ORDER BY revenue DESC

-- Q10: Top Locations by Revenue

SELECT
location,
SUM(total_spent) AS revenue
FROM ecommerce_clean
GROUP BY location
ORDER BY revenue DESC
LIMIT 1

-- Q11: Monthly Sales

SELECT
	TO_CHAR(DATE_TRUNC('month',transaction_date), 'YYYY-MM') AS month,
	SUM(total_spent) AS revenue
FROM ecommerce_clean
GROUP BY month
ORDER BY month

-- Q12: Best Sales Day

SELECT
	TO_CHAR(transaction_date, 'Day') AS days,
	COUNT(*) AS total_orders
FROM ecommerce_clean
GROUP BY days
ORDER BY total_orders

-- Q13: Running Revenue

SELECT
	transaction_date,
	SUM(daily_revenue) OVER(ORDER BY transaction_date) AS running_total
FROM (
	SELECT
	transaction_date,
	SUM(total_spent) AS daily_revenue
	FROM ecommerce_clean
	GROUP BY transaction_date
) t




