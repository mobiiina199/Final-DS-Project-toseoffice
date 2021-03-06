# -*- coding: utf-8 -*-
"""DS_Project_ hause_prediction(MVI_2).ipynb

Automatically generated by Colaboratory.

 @author: mobiiina199
"""


import numpy as np



# Strategy 3
# **3. Data Munging**

## **3.1 Missing Values Imputation**


import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
    header=dict(values=['Features', 'Count', 'Features', 'Count', 'Features', 'Count', 'Features', 'Count'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[df.columns[0:20],  # 1st column
                       df.isnull().sum()[0:20],  # 2nd column
                       df.columns[20:40],  # 3nd column
                       df.isnull().sum()[20:40],  # 4nd column
                       df.columns[40:60],  # 5nd column
                       df.isnull().sum()[40:60],  # 6nd column
                       df.columns[60:80],  # 7nd column
                       df.isnull().sum()[60:80]],  # 8nd column
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))
])

fig.update_layout(width=1000, height=650)
fig.show()

"""**Group of Features that there have not Missng values but they are recognized as missing data. for example in Alley feature NA is (No alley access) and is not missing data.**"""

df = df.drop(['Alley', 'PoolQC', 'Fence', 'MiscFeature'], axis=1)

Notnull = df.loc[:, ['BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1',
                   'BsmtFinType2', 'FireplaceQu', 'GarageType', 'GarageFinish',
                   'GarageQual', 'GarageCond']]

Notnull.fillna('Unknow', inplace=True)

df.loc[:, ['BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 
           'BsmtFinType2', 'FireplaceQu', 'GarageType', 'GarageFinish',
           'GarageQual', 'GarageCond']] = Notnull

"""### **Feature: GarageYrBlt** 

"""

df[df.GarageYrBlt.isnull()]

df.GarageYrBlt.value_counts()

df.GarageType.value_counts()


df.dropna(subset=['GarageYrBlt'], inplace=True)

df.groupby(['GarageQual', 'GarageType']).GarageYrBlt.value_counts()


"""### **Feature: LotFrontage**"""

LotFrontagenull = df[df['LotFrontage'].isnull()]
LotFrontagenull

df.LotFrontage.value_counts()

mean = train.LotFrontage.mean()
std = test.LotFrontage.std()

is_null = df.LotFrontage.isnull().sum()
rand_LotFrontage = np.random.randint(mean - std, mean + std, size =is_null)

LotFrontage_slice = df.LotFrontage.copy()
LotFrontage_slice[np.isnan(LotFrontage_slice)] = rand_LotFrontage
df.LotFrontage = LotFrontage_slice

df.LotFrontage = df.LotFrontage.astype(np.int64)

"""

### **Feature: MSZoning**"""

df[df.MSZoning.isnull()]

df.MSZoning.value_counts()

df.groupby(['MSZoning']).Neighborhood.count()

df.MSZoning.fillna('RL', inplace=True)

"""### **Feature: Utilities**"""

df[df.Utilities.isnull()]

df.Utilities.value_counts()

df.Utilities.fillna('AllPub', inplace=True)

"""### **Feature: Exterior1st**"""
df[df.Exterior1st.isnull()]

df.Exterior1st.value_counts()

df.loc[691, ['RoofStyle', 'Exterior1st']]

df.groupby(['RoofStyle', 'Exterior1st']).SaleCondition.count()

df.Exterior1st.fillna('Plywood', inplace=True)

"""### **Feature: MasVnrType**"""

Masonry_veneer_typenull = df[df.MasVnrType.isnull()]
Masonry_veneer_typenull

df.MasVnrType.value_counts()

Masonry_veneer_typenull.loc[:, ['MasVnrType', 'ExterQual']]

df.groupby(['ExterQual', 'MasVnrType']).ExterCond.count()

df.MasVnrType.fillna('None', inplace=True)

"""### **Feature: MasVnrArea** 

"""

df[df.MasVnrArea.isnull()]

df.MasVnrArea.value_counts()

df.loc[(df.MasVnrType =='None'), 'MasVnrArea'] = 0

"""### **Feature: BsmtFinSF1**"""

df[df.BsmtFinSF1.isnull()]

df.BsmtFinSF1.value_counts()

df.loc[(df.BsmtFinType1 == 'Unknow'), 'BsmtFinSF1'] = 0

"""### **Feature: BsmtFinSF2**"""

df[df.BsmtFinSF2.isnull()]

df.BsmtFinSF2.value_counts()

df.loc[(df.BsmtFinType2 == 'Unknow'), 'BsmtFinSF2']
A = df.groupby('BsmtFinType2')
A.BsmtFinSF2.value_counts()

df.loc[(df.BsmtFinType2 == "Unknow") & (df.BsmtFinSF2 != 0)]

df.BsmtFinSF2.fillna(0, inplace=True)

"""**I think that we in BsmtFinType2= 'Without' and BsmtFinSF2=479 have Outlier**

### **Feature: BsmtUnfSF and TotalBsmtSF**
"""

df[df.TotalBsmtSF.isnull()]
df[df.BsmtUnfSF.isnull()]

df.BsmtUnfSF.fillna(0, inplace=True)
df.TotalBsmtSF.fillna(0, inplace=True)

"""### **Feature: Electrical**"""

df[df.Electrical.isnull()]

df.Electrical.value_counts()

df.Electrical.fillna('SBrkr', inplace=True)

"""### **Feature: BsmtFullBath and BsmtHalfBath**"""

df[df.BsmtFullBath.isnull()]

df.BsmtFullBath.value_counts()

df.BsmtHalfBath.value_counts()

A=df.groupby('OverallCond')
A['BsmtHalfBath'].value_counts()

df.BsmtFullBath.fillna(0, inplace=True)
df.BsmtHalfBath.fillna(0, inplace=True)

"""### **Feature: KitchenQual**"""

df[df.KitchenQual.isnull()]

df.KitchenQual.value_counts()

df.groupby('KitchenAbvGr').KitchenQual.value_counts()

df.KitchenQual.fillna('TA', inplace=True)

"""### **Feature: Functional**"""

df[df.Functional.isnull()]

df.Functional.value_counts()

df.Functional.fillna('Typ', inplace=True)

df[df.GarageCars.isnull()]

df.GarageArea.fillna(0, inplace=True)
df.GarageCars.fillna(0, inplace=True)

"""### **Feature: SaleType**"""

df[df.SaleType.isnull()]

df.SaleType.value_counts()

df.SaleType.fillna('WD', inplace=True)
