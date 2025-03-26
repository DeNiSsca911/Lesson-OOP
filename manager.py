# Определяем класс Task для представления одной задачи
class Task:
    # Конструктор класса, инициализирующий атрибуты задачи
    def __init__(self, description, due_date):
        self.description = description  # Описание задачи
        self.due_date = due_date  # Срок выполнения задачи
        self.is_completed = False  # Статус выполнения (по умолчанию False - не выполнено)

    # Метод для пометки задачи как выполненной
    def mark_as_completed(self):
        self.is_completed = True  # Устанавливаем статус в True

    # Метод для строкового представления задачи (используется при печати)
    def __str__(self):
        status = "✓" if self.is_completed else "✗"  # Выбираем символ статуса
        return f"[{status}] {self.description} (до {self.due_date})"  # Форматированная строка


# Определяем класс TaskManager для управления списком задач
class TaskManager:
    # Конструктор класса, инициализирующий список задач
    def __init__(self):
        self.tasks = []  # Пустой список для хранения задач

    # Метод для добавления новой задачи
    def add_task(self, description, due_date):
        new_task = Task(description, due_date)  # Создаем объект Task
        self.tasks.append(new_task)  # Добавляем в список задач
        print(f"Добавлена задача: {new_task}")  # Выводим сообщение о добавлении

    # Метод для пометки задачи как выполненной по индексу
    def complete_task(self, task_index):
        # Проверяем, что индекс в допустимых пределах
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()  # Вызываем метод задачи
            print(f"Задача отмечена как выполненная: {self.tasks[task_index]}")
        else:
            print("Ошибка: неверный индекс задачи")  # Сообщение об ошибке

    # Метод для отображения текущих (не выполненных) задач
    def show_current_tasks(self):
        # Создаем список невыполненных задач с помощью list comprehension
        current_tasks = [task for task in self.tasks if not task.is_completed]

        # Если список пуст, выводим сообщение и выходим
        if not current_tasks:
            print("Нет текущих задач!")
            return

        # Выводим заголовок и нумерованный список задач
        print("\nТекущие задачи:")
        for i, task in enumerate(current_tasks, 1):  # Нумерация с 1
            print(f"{i}. {task}")

    # Метод для отображения всех задач (и выполненных, и нет)
    def show_all_tasks(self):
        # Если список задач пуст, выводим сообщение
        if not self.tasks:
            print("Нет задач!")
            return

        # Выводим заголовок и нумерованный список всех задач
        print("\nВсе задачи:")
        for i, task in enumerate(self.tasks, 1):  # Нумерация с 1
            print(f"{i}. {task}")


# Блок для демонстрации работы классов
if __name__ == "__main__":
    # Создаем экземпляр менеджера задач
    manager = TaskManager()

    # Добавляем несколько тестовых задач
    manager.add_task("Купить молоко", "2023-12-15")
    manager.add_task("Сделать домашку по Python", "2023-12-20")
    manager.add_task("Записаться к врачу", "2023-12-31")

    # Показываем все задачи
    manager.show_all_tasks()

    # Отмечаем первую задачу выполненной (индекс 0)
    manager.complete_task(0)

    # Показываем только текущие (не выполненные) задачи
    manager.show_current_tasks()