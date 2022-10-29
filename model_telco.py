import sklearn.preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd

########################## Modeling Prep Functions ##############################
def model_sets(train,validate,test):
    '''
    Function drops redundant columns and the target of churn column then splits data into 
    predicting variables (x) and target variable (y)
    ''' 

    x_train = train.drop(columns=['gender', 'contract_type','partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'internet_service_type', 'payment_type', 'churn_encoded', 'multiple_lines_No', 'online_security_No', 'online_backup_No', 'device_protection_No', 'tech_support_No', 'streaming_tv_No', 'streaming_movies_No'])
    y_train = train.churn_encoded


    x_validate = validate.drop(columns=['gender', 'contract_type', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'internet_service_type', 'payment_type', 'churn_encoded', 'multiple_lines_No', 'online_security_No', 'online_backup_No', 'device_protection_No', 'tech_support_No', 'streaming_tv_No', 'streaming_movies_No'])
    y_validate = validate.churn_encoded

    x_test = test.drop(columns=['gender', 'contract_type', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'internet_service_type', 'payment_type', 'churn_encoded', 'multiple_lines_No', 'online_security_No', 'online_backup_No', 'device_protection_No', 'tech_support_No', 'streaming_tv_No', 'streaming_movies_No'])
    y_test = test.churn_encoded

    return x_train, y_train, x_validate, y_validate, x_test, y_test

########################## Model Evaluation Functions ##############################

def get_tree(x_train, y_train, x_validate, y_validate, x_test, y_test):
    '''
    Function gets Decision Tree model accuracy on train and validate data set 
    ''' 
    # create decision tree model using defaults and random state to replicate results
    tree1 = DecisionTreeClassifier(max_depth=3, random_state=123)

    # fit model on training data
    tree1 = tree1.fit(x_train, y_train)

    # print result
    print('Accuracy of Decision Tree classifier on training set: {:.2f}'
      .format(tree1.score(x_train, y_train)))
    print('Accuracy of Decision Tree classifier on validate set: {:.2f}'
      .format(tree1.score(x_validate, y_validate)))
    
def get_forest(x_train, y_train, x_validate, y_validate, x_test, y_test):
    '''
    Function gets Random Forest model accuracy on train and validate data set 
    ''' 
    # create random forest model using random state to replicate results
    rf = RandomForestClassifier(max_depth =5, 
                            min_samples_leaf = 1, 
                            random_state=123)
    # fit model on training data
    rf.fit(x_train, y_train)

    # print result
    print('Accuracy of Random Forest classifier on training set: {:.2f}'
      .format(rf.score(x_train, y_train)))
    print('Accuracy of Random Forest classifier on validate set: {:.2f}'
      .format(rf.score(x_validate, y_validate)))

def get_reg(x_train, y_train, x_validate, y_validate, x_test, y_test):
    '''
    Function gets Logistic Regression model accuracy on train and validate data set 
    '''
    # create logistic regression model
    logit = LogisticRegression(C=1,random_state=123)
    # specify the features used
    features_model1 = ['contract_type_Month-to-month', 'contract_type_One year', 'contract_type_Two year']

    # fit model on training data
    logit.fit(x_train[features_model1], y_train)

    # print result
    print('Accuracy of Logistic Regression classifier on training set: {:.2f}'
      .format(logit.score(x_train[features_model1], y_train)))
    print('Accuracy of Logistic Regression classifier on validate set: {:.2f}'
      .format(logit.score(x_validate[features_model1], y_validate)))

def get_knn(x_train, y_train, x_validate, y_validate, x_test, y_test):
    '''
    Function gets KNN model accuracy on train and validate data set 
    '''
    # create KNN model
    knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
    # fit model on training data
    knn.fit(x_train, y_train)

    # print results
    print('Accuracy of KNN classifier on training set: {:.2f}'
      .format(knn.score(x_train, y_train)))
    print('Accuracy of KNN classifier on validate set: {:.2f}'
      .format(knn.score(x_validate, y_validate)))

########################## Model Test Functions ##############################

def get_rf_test(x_train, y_train, x_validate, y_validate, x_test, y_test):
    '''
    Function gets Random Forest model accuracy on test data set 
    ''' 
    # create random forest model using random state to replicate results
    rf = RandomForestClassifier(max_depth =5, 
                            min_samples_leaf = 1, 
                            random_state=123)
    # fit model on training data
    rf.fit(x_train, y_train)

    # print result
    print('Accuracy of Random Forest classifier on test set: {:.2f}'
      .format(rf.score(x_test, y_test)))