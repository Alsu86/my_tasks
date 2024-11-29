import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    data = response.json()
    for post in data[:5]:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")
else:
    print(f"Ошибка: {response.status_code}")



import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values)

plt.title('Пример столбчатой диаграммы')
plt.xlabel('Категории')
plt.ylabel('Значения')

plt.show()
