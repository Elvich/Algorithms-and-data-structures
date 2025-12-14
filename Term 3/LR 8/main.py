import sqlite3
from datetime import datetime
import os


class PurchaseLog:
    def __init__(self, db_name='LR 8/purchases.db'):
        """Инициализация подключения к базе данных и создание таблицы"""
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()
    
    def _create_table(self):
        """Создание таблицы transactions, если она не существует"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                price_per_unit REAL NOT NULL CHECK(price_per_unit > 0),
                purchase_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def record_purchase(self):
        """Функция 1: Запись покупки"""
        print("\n=== Запись покупки ===")
        try:
            item_name = input("Введите название товара: ").strip()
            if not item_name:
                print("Ошибка: Название товара не может быть пустым!")
                return
            
            quantity = int(input("Введите количество: "))
            if quantity <= 0:
                print("Ошибка: Количество должно быть больше 0!")
                return
            
            price_per_unit = float(input("Введите цену за единицу: "))
            if price_per_unit <= 0:
                print("Ошибка: Цена за единицу должна быть больше 0!")
                return
            
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            self.cursor.execute('''
                INSERT INTO transactions (item_name, quantity, price_per_unit, purchase_date)
                VALUES (?, ?, ?, ?)
            ''', (item_name, quantity, price_per_unit, current_date))
            
            self.conn.commit()
            print(f"✓ Покупка успешно записана! ID транзакции: {self.cursor.lastrowid}")
        
        except ValueError:
            print("Ошибка: Некорректный формат данных! Используйте числа для количества и цены.")
        except Exception as e:
            print(f"Ошибка при записи покупки: {e}")
    
    def show_all_purchases(self):
        """Функция 2: Показать все покупки"""
        print("\n=== Все покупки ===")
        try:
            self.cursor.execute('''
                SELECT transaction_id, item_name, quantity, price_per_unit, purchase_date
                FROM transactions
                ORDER BY purchase_date DESC
            ''')
            
            purchases = self.cursor.fetchall()
            
            if not purchases:
                print("Журнал покупок пуст.")
                return
            
            print(f"{'ID':<6} {'Товар':<20} {'Кол-во':<8} {'Цена/ед.':<12} {'Дата покупки':<20} {'Сумма':<12}")
            print("-" * 90)
            
            for purchase in purchases:
                transaction_id, item_name, quantity, price_per_unit, purchase_date = purchase
                total = quantity * price_per_unit
                print(f"{transaction_id:<6} {item_name:<20} {quantity:<8} {price_per_unit:<12.2f} {purchase_date:<20} {total:<12.2f}")
        
        except Exception as e:
            print(f"Ошибка при получении покупок: {e}")
    
    def calculate_total_cost(self):
        """Функция 3: Вычислить общую стоимость покупок"""
        print("\n=== Общая стоимость покупок ===")
        try:
            self.cursor.execute('''
                SELECT SUM(quantity * price_per_unit) as total
                FROM transactions
            ''')
            
            result = self.cursor.fetchone()
            total = result[0] if result[0] is not None else 0.0
            
            print(f"Общая стоимость всех покупок: {total:.2f}")
        
        except Exception as e:
            print(f"Ошибка при вычислении общей стоимости: {e}")
    
    def find_purchases_by_date(self):
        """Функция 4: Найти покупки по конкретной дате"""
        print("\n=== Поиск покупок по дате ===")
        try:
            date_input = input("Введите дату (формат: YYYY-MM-DD): ").strip()
            
            # Проверка формата даты
            try:
                datetime.strptime(date_input, '%Y-%m-%d')
            except ValueError:
                print("Ошибка: Неверный формат даты! Используйте формат YYYY-MM-DD")
                return
            
            self.cursor.execute('''
                SELECT transaction_id, item_name, quantity, price_per_unit, purchase_date
                FROM transactions
                WHERE DATE(purchase_date) = ?
                ORDER BY purchase_date DESC
            ''', (date_input,))
            
            purchases = self.cursor.fetchall()
            
            if not purchases:
                print(f"Покупки за {date_input} не найдены.")
                return
            
            print(f"\nПокупки за {date_input}:")
            print(f"{'ID':<6} {'Товар':<20} {'Кол-во':<8} {'Цена/ед.':<12} {'Время':<20} {'Сумма':<12}")
            print("-" * 90)
            
            total_day = 0
            for purchase in purchases:
                transaction_id, item_name, quantity, price_per_unit, purchase_date = purchase
                total = quantity * price_per_unit
                total_day += total
                print(f"{transaction_id:<6} {item_name:<20} {quantity:<8} {price_per_unit:<12.2f} {purchase_date:<20} {total:<12.2f}")
            
            print(f"\nИтого за день: {total_day:.2f}")
        
        except Exception as e:
            print(f"Ошибка при поиске покупок: {e}")
    
    def delete_purchase_by_id(self):
        """Функция 5: Удалить покупку по ID"""
        print("\n=== Удаление покупки ===")
        try:
            transaction_id = int(input("Введите ID транзакции для удаления: "))
            
            self.cursor.execute('''
                SELECT transaction_id, item_name, quantity, price_per_unit, purchase_date
                FROM transactions
                WHERE transaction_id = ?
            ''', (transaction_id,))
            
            purchase = self.cursor.fetchone()
            
            if not purchase:
                print(f"Транзакция с ID {transaction_id} не найдена.")
                return
            
            _, item_name, quantity, price_per_unit, purchase_date = purchase
            print(f"\nНайдена покупка:")
            print(f"  ID: {transaction_id}")
            print(f"  Товар: {item_name}")
            print(f"  Количество: {quantity}")
            print(f"  Цена за единицу: {price_per_unit:.2f}")
            print(f"  Дата: {purchase_date}")
            
            confirm = input("\nВы уверены, что хотите удалить эту покупку? (да/нет): ").strip().lower()
            
            if confirm in ['да', 'yes', 'y', 'д']:
                self.cursor.execute('''
                    DELETE FROM transactions
                    WHERE transaction_id = ?
                ''', (transaction_id,))
                
                self.conn.commit()
                print(f"✓ Покупка с ID {transaction_id} успешно удалена!")
            else:
                print("Удаление отменено.")
        
        except ValueError:
            print("Ошибка: ID транзакции должен быть числом!")
        except Exception as e:
            print(f"Ошибка при удалении покупки: {e}")
    
    def close(self):
        """Закрытие подключения к базе данных"""
        self.conn.close()
    
    def __enter__(self):
        """Поддержка контекстного менеджера"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрытие подключения при выходе из контекста"""
        self.close()


def main():
    """Главная функция с меню"""
    print("=" * 50)
    print("     ЖУРНАЛ ПОКУПОК")
    print("=" * 50)
    
    with PurchaseLog() as log:
        while True:
            print("\nВыберите действие:")
            print("1. Записать покупку")
            print("2. Показать все покупки")
            print("3. Вычислить общую стоимость покупок")
            print("4. Найти покупки по дате")
            print("5. Удалить покупку по ID")
            print("0. Выход")
            
            choice = input("\nВаш выбор: ").strip()
            
            if choice == '1':
                log.record_purchase()
            elif choice == '2':
                log.show_all_purchases()
            elif choice == '3':
                log.calculate_total_cost()
            elif choice == '4':
                log.find_purchases_by_date()
            elif choice == '5':
                log.delete_purchase_by_id()
            elif choice == '0':
                break
            else:
                print("Неверный выбор! Пожалуйста, выберите число от 0 до 5.")


if __name__ == '__main__':
    main()

