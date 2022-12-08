import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

ave_file = "/Users/kuran/project1/Mall_Customers.csv"
df = pd.read_csv(ave_file, sep=',')
print(df.head())

gender = df.groupby(['Genre'])['Genre'].count()
# print(gender)

# plt.title("Количество женщин и мужчин")
# plt.pie(gender, labels=gender.index)
# plt.show()


# #Бар горизонтальный количества людей определенного возраста
# age = df.groupby(['Age'])['Age'].count()
# print(age)
# plt.title ('Age Plot')
# plt.xlabel('Number')
# plt.ylabel('Age')
# plt.barh(age.index, age)
# plt.show()



# Пай количества женщин и мужчин с рейтингом трат выше 50
# score = df[(df['Spending Score (1-100)'] > 50)]
# female = score.groupby(['Genre'])['Genre'].count()
# print(female)
# plt.pie(female, labels=female.index)
# plt.title('Рейтинг трат женщин и мужчин')
# plt.show()



# Бар возраст против рейтинга дохода
# age = df["Age"]
# income = df["Annual Income (k$)"]
# plt.bar(age, income)
# plt.title('Бар возраст/доход')
# plt.xlabel('Age')
# plt.ylabel('Annual Income (k$)')
# plt.show()
