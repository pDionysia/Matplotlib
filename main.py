import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

"""
plt.plot([0,10],[0,300])
plt.title("Title")
plt.xlabel("X - Axis")
plt.ylabel("y - Axis")
plt.grid()
plt.show()

plt.plot([0, 10], [0, 300], 'o')

plt.show()

plt.plot([0, 2, 4, 6, 8, 10], [3, 8, 1, 10, 5, 12])

plt.show()
plt.plot([0, 2, 4], [3, 8, 1], marker='o')

plt.show()
plt.plot([0, 2, 4], [3, 8, 1], ls='dotted')

plt.show()
plt.subplot(2, 1, 1)
plt.plot([0, 2, 4, 6, 8, 10], [3, 8, 1, 10, 5, 12])

plt.subplot(2, 1, 2)
plt.plot([0, 10], [0, 300])

plt.show()
x = np.array([99, 86, 87, 88, 111, 86,
              103, 87, 94, 78, 77, 85, 86])

y = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])

plt.scatter(x, y)

plt.show()

x = np.array([99, 86, 87, 88, 111, 86,
              103, 87, 94, 78, 77, 85, 86])
y = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
plt.scatter(x, y)

x = np.array([100, 105, 84, 105, 90, 99,
              90, 95, 94, 100, 79, 112, 91, 80, 85])
y = np.array([2, 2, 8, 1, 15, 8, 12, 9,
              7, 3, 11, 4, 7, 14, 12])
plt.scatter(x, y)

plt.show()
x = np.array(["A", "B", "C", "D"])

y = np.array([4, 5, 1, 10])

plt.bar(x, y)

plt.show()

mylabels = np.array(["Potatoes",
                     "Bacon", "Tomatoes", "Sausages"])

x = np.array([25, 35, 15, 25])

plt.pie(x, labels=mylabels)
plt.legend()

plt.show()

age = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
cardiac_cases = [5, 15, 20, 40, 55, 55, 70, 80, 90, 95]
survival_chances = [99, 99, 90, 90, 80, 75, 60, 50, 30, 25]

plt.xlabel("Age")
plt.ylabel("Percentage")

plt.plot(age, cardiac_cases, color='black', linewidth=2,
label="Cardiac Cases",
marker='o',markerfacecolor='red',markersize=12)

plt.plot(age, survival_chances, color='yellow', linewidth=3,
label="Survival chances",
marker='o',markerfacecolor='green',markersize=12)

plt.legend(loc='lower right', ncol=1)

plt.show()



products = np.array([["Apple", "Orange"],
                    ["Beef", "Chicken"],
                    ["Candy", "Chocolate"],
                    ["Fish", "Bread"],
                    ["Eggs", "Bacon"]])
random = np.random.randint(2, size=5)

choices = []

counter = 0
for product in products:
    choices.append(product[random[counter]])
    counter += 1

print(choices)
percentages = []

for i in range(4):
    percentages.append(np.random.randint(25))

percentages.append(100 - np.sum(percentages))

print(percentages)
plt.pie(percentages, labels=choices)
plt.legend(loc='lower right', ncol=1)

plt.show()

data = pd.read_csv("1.supermarket.csv")
q = data.groupby("item_name").quantity.sum()
plt.bar(q.index,q,color=[ "orange", "purple","yellow", "red","green","blue","cyan"])
plt.xlabel("Items")
plt.xticks(rotation=6)
plt.ylabel("Number of times ordered")
plt.title("Most ordered supermarket\'s items")
plt.show()

url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_text = requests.get(url).text
#print(url_text)
s = BeautifulSoup(url_text, "html.parser")
#print(s.prettify())
#print(s.title)
#print(s.title.string)

tag = s.find_all('a')
print(tag)
my_table = s.find('table', class_='wikitable sortable plainrowheaders')
table_links = my_table.find
print(table_links)
"""

print("hello world!")