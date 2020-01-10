-- Profit margin per day by product category/subcategory
SELECT productCategory, productSubcategory, SUM(profit)/SUM(sales) AS profit_margin
FROM orders
GROUP BY productCategory, productSubcategory
ORDER BY profit_margin DESC
;

-- Profit margin per customer per day by product category/subcategory
SELECT productCategory, productSubcategory, AVG(profit_margin) AS avg_profit_margin
FROM
(
    SELECT productCategory, productSubcategory, orderId, SUM(profit)/SUM(sales) AS profit_margin
    FROM orders
    GROUP BY productCategory, productSubcategory, orderId
) a
GROUP BY productCategory, productSubcategory
ORDER BY avg_profit_margin DESC
;

-- shipping cost vs sales

-- shipping cost vs profit

-- products that profit poorly
SELECT productCategory, productSubcategory, AVG(profit) AS avg_prof
FROM orders
GROUP BY productCategory, productSubcategory
ORDER BY avg_prof
;

-- average ship cost / profit by city
SELECT productCategory, productSubCategory, AVG(shippingCost)/AVG(profit) AS ship_prof_ratio
FROM orders
GROUP BY productCategory, productSubCategory
    HAVING AVG(shippingCost)/AVG(profit) < 0
ORDER BY ship_prof_ratio
;

-- Customer Traffic

-- Average sales

-- Average sales order value

-- Items per purchase

-- Gross margin

-- Profit margin
SELECT productSubCategory, SUM(profit)/SUM(sales) profit_margin
FROM orders
GROUP BY productSubCategory
ORDER BY profit_margin DESC
;

-- Profit / Shipping Cost by city
SELECT CONCAT(productCategory, ': ', productSubcategory), AVG(profit)/AVG(shippingCost) AS profit_per_ship
FROM orders
GROUP BY productSubcategory
ORDER BY profit_per_ship DESC
;

-- return count per city
SELECT a.productSubcategory, COALESCE(b.Status, "Fulfilled"), COUNT(b.orderId) AS return_count
FROM orders a
LEFT JOIN returns b
ON a.orderId = b.orderId
GROUP BY a.productSubcategory, COALESCE(b.Status, "Fulfilled")
ORDER BY return_count DESC
;

SELECT COUNT(a.rowId) AS orders, COUNT(b.orderId) AS returns
FROM orders a
LEFT JOIN returns b
ON a.rowId = b.orderId
;
