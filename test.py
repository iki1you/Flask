from requests import get, post, delete, put


# Корректный запрос
print(put('http://localhost:5000/api/jobs/1',
           json={'job': 'Заголовок',
                 'team_leader': 'Текст новости',
                 'user_id': 4,
                 'is_finished': False,
                 'work_size': 123,
                 'collaborators': '1, 4, 5',
                 'id': 3}).json())

# Получаем все работы
print(get('http://localhost:5000/api/jobs').json())