import string
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np


colnames = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
df =pd.read_csv("adult.data.txt",names = colnames, header=None)

sumOver = df.loc[df['income']== " >50K"].fnlwgt.sum()
sumUnder = df.loc[df['income']== " <=50K"].fnlwgt.sum()

countOver = df.loc[df['income']== " >50K"].shape[0]
countUnder = df.loc[df['income']== " <=50K"].shape[0]

#Age
fig = plt.figure(figsize=(20,5))
ax = sns.countplot(data= df, x='age', hue='income')
ax.set_title("Income distribution by Age (per income group)", loc='center', fontweight='bold', fontsize=18)
ax.set_xlabel("Age")
ax.set_ylabel(" ")
ax.legend(loc="upper right") 

countPrivate  = df[df['workclass']== " Private"].shape[0]
countAll = df.shape[0]

#Workclass
fig = plt.figure(figsize=(14,5))
df.loc[df.workclass == ' ?', 'workclass'] = 'Unknown'
ax2 = sns.countplot(data= df, x='workclass', hue='income')
ax2.set_title("Income count by work class (by income group)", loc='center', fontweight='bold', fontsize=18)
ax2.set_ylabel("Work class")
ax2.legend(loc="upper right") 

df.groupby(['education','education_num']).size().reset_index().rename(columns={0:'count'})

#Education
fig = plt.figure(figsize=(14,5))
ax3 = sns.countplot(data= df, y='education', hue='income')
ax3.set_title("Income count by education", loc='center', fontweight='bold', fontsize=18)
ax3.set_ylabel("Education")
ax3.legend(loc="upper right") 


fig = plt.figure(figsize=(14,5))
ax4 = sns.countplot(data= df, y='marital_status', hue='income')
ax4.set_title("Income count by marital status", loc='center', fontweight='bold', fontsize=18)
ax4.set_ylabel("Marital Status")
ax4.legend(loc="upper right") 


fig = plt.figure(figsize=(14,5))
ax5 = sns.countplot(data= df, y='occupation', hue='income')
ax5.set_title("Income count by occupation", loc='center', fontweight='bold', fontsize=18)
ax5.set_ylabel("Occupation")
ax5.legend(loc="upper right") 

fig = plt.figure(figsize=(14,5))
ax6 = sns.countplot(data= df, y='relationship', hue='income')
ax6.set_title("Income count by relationship", loc='center', fontweight='bold', fontsize=18)
ax6.set_ylabel("Relationship")
ax6.legend(loc="upper right") 

fig = plt.figure(figsize=(14,5))
ax7 = sns.countplot(data= df, x='race', hue='income')
ax7.set_title("Income count by race", loc='center', fontweight='bold', fontsize=18)
ax7.set_xlabel("Race")
ax7.legend(loc="upper right") 



fig = plt.figure(figsize=(14,5))
ax8 = sns.countplot(data= df, x='sex', hue='income')
ax8.set_title("Income count by sex", loc='center', fontweight='bold', fontsize=18)
ax8.set_xlabel("Sex")
ax8.legend(loc="upper right") 


fig = plt.figure(figsize=(14,8))
df["hours_per_week_grouped"] = (df.hours_per_week/5.0).astype("int64") * 5
ax9 = sns.countplot(data= df, y='hours_per_week_grouped', hue='income')
ax9.set_title("Income count by weekly hours", loc='center', fontweight='bold', fontsize=18)
ax9.set_ylabel("Weekly hours")
ax9.legend(loc="upper right") 

fig = plt.figure(figsize=(14,10))
ax10 = sns.countplot(data= df [ (df.native_country != " United-States")], y='native_country', hue='income')
ax10.set_title("Income count by native country", loc='center', fontweight='bold', fontsize=18)
ax10.set_ylabel("Native Country")
ax10.legend(loc="upper right") 

df2 = pd.DataFrame(df,columns=['capital-loss','capital-gain','income'])
sns.heatmap(df2.corr('pearson'),annot=True)


#sns.catplot(col="sex",y="occupation",hue="income", data=df,kind="count")
#sns.catplot(col="sex",y="education_num",hue="income", data=df,kind="count")
#sns.catplot(col="marital_status",y="education_num",hue="income", data=df,kind="count")
#sns.catplot(col="marital_status",y="occupation",hue="income", data=df,kind="count")

plt.show()