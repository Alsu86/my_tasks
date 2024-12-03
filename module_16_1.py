from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return 'Главная страница'

@app.get('/user/admin')
def admin():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
def user(user_id : int):
    return f'Вы вошли под пользователем {user_id}'

@app.get('/user')
def get_user_data(name : str, age : int):
    return f'Информация о пользователе. Имя: {name}, Возраст: {age}'