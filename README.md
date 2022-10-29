# CodeUp-DS-Telco-Churn-Project

### Project Description

#### Telco is a for profit company that provides tv, internet, and phone services to the public. 

### Project Goals
* Discover drivers of customer churn in Telco DataSet.

* Use drivers to develop a machine learning model to classify customers as ending in churn or not ending in churn.

* This information could be used to further our understanding of what makes a customer churn and how to avoid that outcome.

#### My initial hypothesis is that drivers of churn will be elements that either cause an outright cancellation of product/services or increase the likelihood of a customer churning.

### The Plan
* Aquire data from the CodeUp database
* Prepare data for exploration by creating tailored columns from existing data
#### Explore data in search of drivers of customer churn by asking the following:
* How often does customer churn occur?
* Does any specific feature directly affect customer churn?
#### Develop a Model to predict customer churn
* Use drivers identified to build predictive models of different types
* Evaluate models on train and validate data samples
* Select the best model based on highest accuracy
* Evaluate the best model on test data samples
#### Draw conclusions

### Data Dictionary

* Churn is defined as a customer that has cancelled (any or all) of their services.

### Steps to Reproduce
* Clone this repo.
* Confirm variables from user env.py file as
        user = 'your user name', 
        pwd = 'your password', 
        host = 'data.codeup.com'password pwd, etc.)
* Acquire the data from CodeUp database
* Put the data in the file containing the cloned repo.
* Run notebook
### Conclusions

* Random Forest classifier model showed accuracy of :

        * 81% on training data samples
        * 79% on validate data samples
        * 81% on test data samples

### Key Takeaway
* Random Forest model was able to predict with 81% Accuracy of Telco customer churn based soley on the customers contract type.

### Recommendations

   * Consider customer contract type when making projections of customer churn rate.
   * Isolate month to month customer data for more in depth analysis to prevent churn.  
   * Consider monthly service fees for customers that opt out of 1 or 2 year contracts.
   * Consider marketing strategies that target month to month customers.  
