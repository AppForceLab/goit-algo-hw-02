from collections import deque

def is_palindrome(input_string):
    """
    Перевіряє, чи є рядок паліндромом, з використанням двосторонньої черги.
    
    :param input_string: Рядок для перевірки
    :return: True, якщо рядок паліндром, і False, якщо ні
    """
    # Попередня обробка: видаляємо пробіли та приводимо до нижнього регістру
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Додаємо символи до двосторонньої черги
    char_deque = deque(cleaned_string)
    
    # Порівнюємо символи з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не збігаються, це не паліндром
    
    return True  # Якщо всі символи збіглися, це паліндром

# Тестування
if __name__ == "__main__":
    test_strings = [
        "A man a plan a canal Panama",
        "Racecar",
        "hello",
        "Madam, in Eden, I'm Adam",
        "Not a palindrome"
    ]
    
    for s in test_strings:
        result = is_palindrome(s)
        print(f"Рядок: '{s}' - {'Паліндром' if result else 'Не паліндром'}")
