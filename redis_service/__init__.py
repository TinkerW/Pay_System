import redis
# Создать подключения к redis
redis_db = redis.from_url('redis://localhost')
# Создать запись в базе данных
# redis_db.set("spam", 27)
# Получить значения то есть данные из базы
data = redis_db.get("spam")
print(data)

# Задать время существования переменной в базе
# redis_db.set("name", "Axad", 5)
data2 = redis_db.get("name")
print(data2)

