# 🚀 Алгоритмы, построение и анализ

<p align="center">
  <img align="center" width="280" src="https://cdn-icons-png.flaticon.com/512/2172/2172943.png" alt="Алгоритмы"/>
</p>

## 📚 Описание

Этот проект содержит реализацию лабораторных работ по курсу **Алгоритмы, построение и анализ**. Проект включает фронтенд и бэкенд части, которые взаимодействуют через API. Все сервисы можно легко развернуть с помощью Docker Compose.

## 🛠️ Состав проекта:

-   **Frontend**: 🖥️ Написан на React с использованием TypeScript, включает интерфейс для каждой лабораторной работы.
-   **Backend**: ⚙️ Написан на Python с использованием FastAPI, содержит логику для выполнения вычислений.
-   **Docker Compose**: 📦 Автоматизированное развертывание фронтенда и бэкенда.

## 🔬 Лабораторные работы:

1. **Лабораторная работа №1: Сортировка массивов** 🧮

    - Сравнение времени сортировки массивов с различной степенью упорядоченности.
    - Пользователь задает размер массива и процент упорядоченности.

2. **Лабораторная работа №2: Умножение матриц** ➗

    - Оптимизация порядка умножения цепочки матриц с использованием динамического программирования.

3. **Лабораторная работа №3: Задача о рюкзаке** 🎒

    - Классическая задача динамического программирования для максимизации ценности предметов в рюкзаке.

4. **Лабораторная работа №4: Наибольшая общая подпоследовательность (LCS)** 🔡

    - Определение наибольшей общей подпоследовательности для двух строк.

5. **Лабораторная работа №5: B-дерево** 🌳
    - Операции с B-деревом: вставка, поиск и отображение структуры дерева.
    - 
5. **Лабораторная работа №6: AVL-дерево** 🌴
    - Операции с AVL-деревом: вставка, поиск и отображение структуры дерева.
## 🚀 Запуск проекта

1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Выполните следующую команду для развертывания всех сервисов:
    ```bash
    make all
    ```
3. После успешного запуска:

-   **Фронтенд** будет доступен по адресу: http://localhost:5171 🌐
-   **Бэкенд** API будет доступен по адресу: http://localhost:8000 ⚙️

## 🧩 Требования

- Docker
- Docker Compose
- Make (для автоматизации команд)

## 🛠️ Команды Makefile

- `make all` — Запуск всех сервисов (фронтенд и бэкенд).
- `make front` — Запуск только фронтенда.
- `make back` — Запуск только бэкенда.
- `make drop-front` — Остановка только фронтенда.
- `make drop-back` — Остановка только бэкенда.
- `make drop-all` — Остановка и удаление всех сервисов.
- `make logs` — Просмотр логов всех сервисов (фронтенд и бэкенд).
