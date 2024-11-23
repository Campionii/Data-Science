import seaborn as sns
import matplotlib.pyplot as plt

gorjeta = sns.load_dataset('tips')

print(gorjeta.head())
'''
#plotagem Univariada
sns.histplot(gorjeta['Total_bill'], kde = True, bins = 30)
plt.show()

#Plotagem
sns.jointplot(X='total_bill', Y='tip', data=gorjeta, Kind='hex', color='red')
plt.title('Correlação entre e Gorjeta')
plt.show()

sns.jointplot(X='total_bill', Y='tip', data=gorjeta, Kind='reg', color='red')
plt.title('Correlação entre e Gorjeta')
plt.show()
'''

sns.pairplot(gorjeta)
plt.show()

sns.kdeplot(gorjeta['total_bill'])
plt.show()