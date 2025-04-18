import re

# task4.py

# читаем файл text.txt
with open('text.txt', 'r') as file:
    content = file.read()

# находим email-адреса и сохраняем в emails.txt
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
with open('emails.txt', 'w') as email_file:
    for email in emails:
        email_file.write(email + '\n')

# находим номера телефонов и сохраняем в phones.txt
phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', content)
with open('phones.txt', 'w') as phone_file:
    for phone in phones:
        phone_file.write(phone + '\n')

# находим слова с заглавной буквы и сохраняем в capital_words.txt
capital_words = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]*\b', content)
with open('capital_words.txt', 'w') as capital_file:
    for word in capital_words:
        capital_file.write(word + '\n')

print("обработка завершена. Результаты сохранены в файлы.")