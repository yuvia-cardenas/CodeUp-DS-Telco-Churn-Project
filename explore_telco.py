import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

#################### Statistical and Visuals Functions ##################################
alpha = 0.05 
def get_chi_gender(train):
    '''
    Function gets results of chi-square statistical test for gender and churn
    '''

    observed = pd.crosstab(train.churn_encoded, train.gender)
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis')
    else:
        print('We fail to reject the null hypothesis')

    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')

def get_chi_phone(train):
    '''
    Function gets results of chi-square statistical test for phone service and churn
    '''

    observed = pd.crosstab(train.churn_encoded, train.phone_service_encoded)
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis')
    else:
        print('We fail to reject the null hypothesis')

    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')

def get_chi_contract_type(train):
    '''
    Function gets results of chi-square statistical test for contract type and churn
    '''

    observed = pd.crosstab(train.churn_encoded, train.contract_type)
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis')
    else:
        print('We fail to reject the null hypothesis')

    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')

def get_chi_internet_type(train):
    '''
    Function gets results of chi-square statistical test for internet type and churn
    '''

    observed = pd.crosstab(train.churn_encoded, train.internet_service_type)
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis')
    else:
        print('We fail to reject the null hypothesis')

    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}') 
    

