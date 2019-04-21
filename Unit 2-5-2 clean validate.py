# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:38:39 2019

@author: Computer
"""
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std
#%%
#check linearity, normality, homoscedasticity, multicoll
df = pd.read_excel(r'C:\Users\Computer\Desktop\School\xls\offenses_new_york_by_city_2013.xls', header = None)
#remove empty rows for data analysis
fbi_df = df.drop([0, 1, 2, 3, 4, 353, 354, 355])

fbi_df.columns = ['City', 'Population', 'Violent crime', 'Murder', 'Rape', 'Rape(revised)','Robbery', 'Aggravated assault',
              'Propertycrime', 'Burglary', 'Larceny-theft', 'Motorvehicletheft', 'Arson']

fbi_df['Murder'] = pd.to_numeric(fbi_df['Murder'])
fbi_df['Robbery'] = pd.to_numeric(fbi_df['Robbery'])
fbi_df['Population'] = pd.to_numeric(fbi_df['Population'])
fbi_df['Propertycrime'] = pd.to_numeric(fbi_df['Propertycrime'])
#make outcome categorical
murder = np.array(fbi_df['Murder'].values.tolist())
robbery = np.array(fbi_df['Robbery'].values.tolist())

fbi_df['Murder'] = np.where(murder > 0, 1, murder).tolist()
fbi_df['Robbery'] = np.where(robbery > 0, 1, robbery).tolist()
#%%
sns.regplot(fbi_df['Population'],fbi_df['Propertycrime'])
#%%
plt.hist(fbi_df['Population'])
#why is this notating to the 7th?
#%%
#20000 seems like a lot, is this an error or is this accurate?
fbi_df.loc[fbi_df['Murder'].idxmax()]
#it is New York which has a dense population, so let's leave it in the analysis for now but may need to remove
#%%
murder = np.array(fbi_df['Murder'].values.tolist())
robbery = np.array(fbi_df['Robbery'].values.tolist())

fbi_df['Murder'] = np.where(murder > 0, 1, murder).tolist()
fbi_df['Robbery'] = np.where(robbery > 0, 1, robbery).tolist()
#%%
#Make nonlinear variable
fbi_df['Population_sq'] = fbi_df['Population'] **2
#%%
regr = linear_model.LinearRegression()
Y = fbi_df['Propertycrime'].values.reshape(-1,1)
X = fbi_df[['Population', 'Population_sq', 'Murder', 'Robbery']]
regr.fit(X,Y)

print('\nCoefficients: \n', regr.coef_)
print('\nIntercept: \n', regr.intercept_)
print('\nR-squared:')
print(regr.score(X, Y))
#overfitted
#%%
#validate using test statistics
linear_formula = 'Propertycrime ~ Population+Population_sq+Murder+Robbery'
lm = smf.ols(formula=linear_formula, data=fbi_df).fit()

#%%
lm.params
#not right
#%%
Y = fbi_df['Propertycrime'].values.reshape(-1,1)
X = fbi_df[['Population', 'Murder', 'Robbery']]
regr.fit(X,Y)

print('\nCoefficients: \n', regr.coef_)
print('\nIntercept: \n', regr.intercept_)
print('\nR-squared:')
print(regr.score(X, Y))
#overfitted
#%%
linear_formula = 'Propertycrime ~ Population+Murder+Robbery'
lm = smf.ols(formula=linear_formula, data=fbi_df).fit()
#%%
lm.params
#fixed it, but the thinkful formula said to use pop squared
#%%
lm.pvalues
#??
#%%
lm.rsquared
#overfitted but we knew that
#%%
lm.conf_int()
#I can't drop population from the model because it is the only continuous variable....