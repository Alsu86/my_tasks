from fastapi import FastAPI, Path
from pydantic import  BaseModel, Field
from typing import Annotated


app = FastAPI()

@app.get('/')
def main():
    return 'Главная страница'

@app.get('/user/admin')
def admin():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
def user(user_id : Annotated[int, Path(title = 'Enter User ID', ge = 1, le = 100)] ):
    return f'Вы вошли под пользователем {user_id}'

@app.get('user/{username}/{age}')
def get_user_data(username : Annotated[str, Path(title = 'Enter username', min_length=5, max_length=20)], \
                  age : Annotated[int, Path(title = 'Enter age', ge = 18, le = 120)]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'