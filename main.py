    import pandas as pd
df = pd.read_csv('data.csv')
#печать заголовков  о датасете (первые 5 строк)
print(df.head())
#печать информации  о датасете
print(df.info())
#печать описания  о датасете
print(df.describe(ign))
df1 = pd.read_csv('dz.csv')
#печать средней зарплаты в городах
group =  df1.groupby('City')['Salary'].mean()
print(group)