import queue
import time
import random

# Створення черги
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request(request_id):
    print(f"Генерується заявка №{request_id}...")
    request_queue.put(f"Заявка №{request_id}")
    print(f"Заявка №{request_id} додана до черги.")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється {request}...")
        time.sleep(random.uniform(0.5, 1.5))  # Імітація часу обробки заявки
        print(f"{request} оброблено.")
    else:
        print("Черга порожня, немає заявок для обробки.")

# Головний цикл програми
def main():
    request_id = 1
    while True:
        print("\nМеню:")
        print("1. Згенерувати заявку")
        print("2. Обробити заявку")
        print("3. Вийти")
        choice = input("Оберіть дію: ")
        
        if choice == "1":
            generate_request(request_id)
            request_id += 1
        elif choice == "2":
            process_request()
        elif choice == "3":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
