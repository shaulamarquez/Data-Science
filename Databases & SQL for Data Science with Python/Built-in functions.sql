DROP TABLE IF EXISTS PETRESCUE;

CREATE TABLE PETRESCUE (
    ID INTEGER NOT NULL,
    ANIMAL VARCHAR(20),
    QUANTITY INTEGER,
    COST DECIMAL(6,2),
    RESCUEDATE DATE,
    PRIMARY KEY (ID)
);

INSERT INTO PETRESCUE (ID, ANIMAL, QUANTITY, COST, RESCUEDATE) VALUES 
    (1,'Cat',9,450.09,'2018-05-29'),
    (2,'Dog',3,666.66,'2018-06-01'),
    (3,'Dog',1,100.00,'2018-06-04'),
    (4,'Parrot',2,50.00,'2018-06-04'),
    (5,'Dog',1,75.75,'2018-06-10'),
    (6,'Hamster',6,60.60,'2018-06-11'),
    (7,'Cat',1,44.44,'2018-06-11'),
    (8,'Goldfish',24,48.48,'2018-06-14'),
    (9,'Dog',2,222.22,'2018-06-15');


# AGGREGATION FUNCTION
#1. For this query, we will use the function SUM(COLUMN_NAME). The output of this query will be the total value of all elements in the column. The query for this question can be written as:

SELECT SUM(COST) FROM PETRESCUE;

#2.You can further assign a label to the query SUM_OF_COST.

SELECT SUM(COST) AS SUM_OF_COST FROM PETRESCUE;

# For this query, we will use the function MAX(COLUMN_NAME). The output of this query will be the maximum value of all elements in the column. The query for this question can be written as:

SELECT MAX(QUANTITY) FROM PETRESCUE;

# The query can easily be changed to display the minimum quantity using the MIN function instead.

SELECT MIN(QUANTITY) FROM PETRESCUE;

#3.  Write a query that displays the average cost of animals rescued.

SELECT AVG(COST) FROM PETRESCUE;


# Scalar Functions and String Functions
# 1. Write a query that displays the rounded integral cost of each rescue.

SELECT ROUND(COST) FROM PETRESCUE;

# In case the question was to round the value to 2 decimal places, the query would change to:

SELECT ROUND(COST, 2) FROM PETRESCUE;

# 2. Write a query that displays the length of each animal name.
# For this query, we will use the function LENGTH(COLUMN_NAME). The output of this query will be the length of each element in the column. The query for this question can be written as:

SELECT LENGTH(ANIMAL) FROM PETRESCUE;

# 3. Write a query that displays the animal name in each rescue in uppercase.
# For this query, we will use the function UCASE(COLUMN_NAME). The output of this query will be each element in the column in upper case letters. The query for this question can be written as:

SELECT UCASE(ANIMAL) FROM PETRESCUE;

# Just as easily, the user could ask for a lower case representation, and the query would be changed to:

SELECT LCASE(ANIMAL) FROM PETRESCUE;


# Data Functions
# 1. Write a query that displays the rescue date.
# For this query, we will use the function DAY(COLUMN_NAME). The output of this query will be only the DAY part of the date in the column. The query for this question can be written as:

SELECT DAY(RESCUEDATE) FROM PETRESCUE;

# In case the query was asking for MONTH of rescue, the query would change to:

SELECT MONTH(RESCUEDATE) FROM PETRESCUE;

# In case the query was asking for YEAR of rescue, the query would change to:

SELECT YEAR(RESCUEDATE) FROM PETRESCUE;

# Animals rescued should see the vet within three days of arrival. Write a query that displays the third day of each rescue.
# For this query, we will use the function DATE_ADD(COLUMN_NAME, INTERVAL Number Date_element). Here, the quantity in Number and in Date_element will combine to form the interval to be added to the date in the column. For the given question, the query would be:

SELECT DATE_ADD(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE;

# If the question was to add 2 months to the date, the query would change to:

SELECT DATE_ADD(RESCUEDATE, INTERVAL 2 MONTH) FROM PETRESCUE;

# Similarly, we can retrieve a date before the one given in the column by a given number using the function DATE_SUB. By modifying the same example, the following query would provide the date 3 days before the rescue.

SELECT DATE_SUB(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE;

# If the question was to add 2 months to the date, the query would change to:

SELECT DATE_ADD(RESCUEDATE, INTERVAL 2 MONTH) FROM PETRESCUE;

# Similarly, we can retrieve a date before the one given in the column by a given number using the function DATE_SUB. By modifying the same example, the following query would provide the date 3 days before the rescue.

SELECT DATE_SUB(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE;

# Write a query that displays the length of time the animals have been rescued, for example, the difference between the current date and the rescue date.
# For this query, we will use the function DATEDIFF(Date_1, Date_2). This function calculates the difference between the two given dates and gives the output in number of days. For the given question, the query would be:

SELECT DATEDIFF(CURRENT_DATE, RESCUEDATE) FROM PETRESCUE;

# CURRENT_DATE is also an inbuilt function that returns the present date as known to the server.
# To present the output in a YYYY-MM-DD format, another function FROM_DAYS(number_of_days)can be used. This function takes a number of days and returns the required formatted output. The query above would thus be modified to

SELECT FROM_DAYS(DATEDIFF(CURRENT_DATE, RESCUEDATE)) FROM PETRESCUE;


# Practice Problem
# 1. Write a query that displays the average cost of rescuing a single dog. Note that the cost per dog would not be the same in different instances.

SELECT AVG(COST/QUANTITY) FROM PETRESCUE WHERE ANIMAL = 'Dog';

# 2. Write a query that displays the animal name in each rescue in uppercase without duplications.

SELECT DISTINCT UPPER(ANIMAL) FROM petrescue;

# 3. Write a query that displays all the columns from the PETRESCUE table where the animal(s) rescued are cats. Use cat in lowercase in the query.

SELECT * FROM petrescue
WHERE LOWER(ANIMAL)= 'cat';

# 4. Write a query that displays the number of rescues in the 5th month.

SELECT SUM(QUANTITY) 
FROM petrescue
WHERE MONTH(RESCUEDATE) = '05';

# 5. The rescue shelter is supposed to find good homes for all animals within 1 year of their rescue. Write a query that displays the ID and the target date.

SELECT ID, DATE_ADD(RESCUEDATE, INTERVAL 1 YEAR) FROM petrescue;
