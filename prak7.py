import pandas as pd
#memanggil dan menampilkan dataset
data_nama = pd.read_csv('C:/Users/HP/Downloads/titanic.csv')
print(data_nama)

#mengambil data pada kolom tertentu
data1 = data_nama.loc[:,['Age','Pclass','Survived']]
print(data1)

#memvisualisasikan data titanic
data2 = data_nama[['Age', 'Pclass', 'Survived']]
data2.plot(title='Persebaran Data', x='Age', y='Pclass', kind='scatter', c='Survived',
colormap='Paired')

#memanipulasi data jumlah penumpang berdasarkan group Pclass
data3 = data_nama[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
penumpang=data3.groupby('Pclass')['Name'].nunique()
print('Jumlah Penumpang:\n', penumpang)

#memfilter data penumpang yang selamat berdasarkan pclass
data4 = data_nama[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger=data4['Pclass'].loc[data_nama['Survived']==0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())
survivedpassanger=data4['Pclass'].loc[data_nama['Survived']==1]
print('\nPenumpang yang survived:\n', survivedpassanger.value_counts())

# Latihan
data5 = data_nama[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
malepassanger=data5['Pclass'].loc[data_nama['Sex']=='male']
print('Penumpang laki-laki di setiap Kelas:\n', malepassanger.value_counts())
femalepassanger=data5['Pclass'].loc[data_nama['Sex']=='female']
print('Penumpang Perempuan di setiap Kelas:\n', femalepassanger.value_counts())

data6 = data_nama[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
survivedpassanger=data6['Sex'].loc[data_nama['Survived']==1]
print('Penumpang yang Selamat berdasar Kelamin:\n', survivedpassanger.value_counts())
unsurvivedpassanger=data6['Sex'].loc[data_nama['Survived']==0]
print('Penumpang yang Tidak Selamat berdasar Kelamin:\n', unsurvivedpassanger.value_counts())