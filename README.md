# CodeUp-DS-Telco-Churn-Project

## Telco Churn ###

### Project Description

#### Telco is a for profit company that provides tv, internet, services to the public. 

### Project Goal
* Discover drivers of customer churn in Telco DataSet.

* Use drivers to develop a machine learning model to classify customers as ending in churn or not ending in churn.

* Churn is defined as a customer that has cancelled (any or all) of their services.

* This information could be used to further our understanding of what makes a customer churn and how to avoid that outcome.

### Initial Thoughts

#### My initial hypothesis is that drivers of churn will be elements that either cause an outright cancellation of product/services or increase the likelihood of a customer churning.

### The Plan
* Aquire data from the CodeUp database
* Prepare data and create tailored columns from existing data
#### Explore data in search of drivers of customer churn
* Answer the following initial questions
* How often does customer churn occur?
* Does any specific feature directly affect customer churn?
* Does any combination of features directly affect customer churn?
#### Develop a Model to predict if a customer will churn
* Use drivers identified to build predictive models of different types
* Evaluate models on train and validate data
* Select the best model based on highest accuracy
* Evaluate the best model on test data

#### Draw conclusions

### Data Dictionary


### Steps to Reproduce
* Clone this repo.
* Confirm variables from user env.py file as
        user = 'your user name', 
        pwd = 'your password', 
        host = 'data.codeup.com'password pwd, etc.)
* Confirm function that returns:
        return f'mysql+pymysql://{user}:{pwd}@{host}/{database}'
* Acquire the data from CodeUp database
* Put the data in the file containing the cloned repo.
* Run notebook

