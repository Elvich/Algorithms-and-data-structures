# Отчет по лабораторной работе: Интерактивное приложение для рисования

## Задание

Реализовать GUI-приложение для рисования с использованием паттерна Strategy. Требования:
- Холст для рисования фигур
- Инструменты рисования: линия, прямоугольник, овал
- Выбор цвета для рисования
- Предварительный просмотр фигур при перетаскивании мыши
- Кнопка очистки холста
- Использование паттерна Strategy для инструментов рисования

## Описание реализации

1. **Создание окна**: Используется класс `DrawingApp`, который инкапсулирует всю логику приложения. Окно создается с фиксированными размерами и запретом на изменение размеров.

2. **Холст для рисования**: Виджет `Canvas` размером 500×400 пикселей с белым фоном и рамкой. Холст привязан к обработчикам событий мыши.

3. **Паттерн Strategy**: Создан абстрактный класс `DrawingToolStrategy` с методом `draw()`. Каждый инструмент (`LineTool`, `RectangleTool`, `OvalTool`) реализует этот интерфейс.

4. **Панель инструментов**: Кнопки для выбора инструментов создаются динамически из списка. При нажатии устанавливается соответствующая стратегия.

5. **Выбор цвета**: Используется стандартный диалог `colorchooser` с индикатором текущего цвета.

6. **Обработка событий мыши**:
   - При нажатии кнопки мыши сохраняются начальные координаты
   - При перетаскивании создается временный объект для предпросмотра  
   - При отпускании создается финальный объект

7. **Предварительный просмотр**: Временные объекты создаются и удаляются во время перетаскивания мыши для показа результата до завершения рисования.

## Скриншот интерфейса

![Изображение интерфейса](https://github.com/Elvich/Algorithms-and-data-structures/blob/main/Term%203/LR%204/Paint.png)

## Код программы

#### `draw(self, canvas: tk.Canvas, start_x: int, start_y: int, end_x: int, end_y: int, **kwargs: Any) -> int`
Создает прямоугольник на холсте, используя (start_x, start_y) и (end_x, end_y) как противоположные углы. Извлекает цвет из kwargs (по умолчанию 'red'), рисует контур прямоугольника толщиной 2 пикселя и возвращает ID созданного объекта.

### Класс `OvalTool`

```python
class OvalTool(DrawingToolStrategy):
    
    def draw(self, canvas: tk.Canvas, start_x: int, start_y: int, 
             end_x: int, end_y: int, **kwargs: Any) -> int:
        color = kwargs.get('color', 'orange')
        return canvas.create_oval(start_x, start_y, end_x, end_y, 
                                outline=color, width=2)
```

#### `draw(self, canvas: tk.Canvas, start_x: int, start_y: int, end_x: int, end_y: int, **kwargs: Any) -> int`
Рисует овал (эллипс) в прямоугольной области, ограниченной координатами (start_x, start_y) и (end_x, end_y). Извлекает цвет из kwargs (по умолчанию 'orange'), создает контур овала толщиной 2 пикселя и возвращает ID созданного объекта.

### Класс `DrawingApp`

#### `__init__(self, master: tk.Tk) -> None`
```python
def __init__(self, master: tk.Tk) -> None:
    self.master = master
    self._setup_window()
    self._setup_canvas()
    self._initialize_drawing_state()
    self._bind_canvas_events()
    self._create_ui_elements()
```
Конструктор класса. Принимает корневое окно tkinter, сохраняет ссылку на него и последовательно вызывает методы для настройки окна, создания холста, инициализации состояния рисования, привязки событий и создания элементов интерфейса.

#### `_setup_window(self) -> None`
Настраивает основные параметры окна приложения: устанавливает заголовок "Интерактивное приложение для рисования" и запрещает изменение размеров окна пользователем.

#### `_setup_canvas(self) -> None`
```python
def _setup_canvas(self) -> None:
    self.canvas = tk.Canvas(
        self.master, 
        width=self.CANVAS_WIDTH, 
        height=self.CANVAS_HEIGHT, 
        bg=self.CANVAS_BG, 
        bd=self.CANVAS_BORDER_WIDTH, 
        relief="groove"
    )
    self.canvas.pack(pady=10)
```
Создает и настраивает холст для рисования. Устанавливает размеры 500×400 пикселей, белый фон, рамку толщиной 2 пикселя с эффектом "groove" и размещает холст в окне с отступом 10 пикселей сверху.

#### `_initialize_drawing_state(self) -> None`
Инициализирует переменные состояния для рисования: обнуляет начальные координаты (start_x, start_y), устанавливает LineTool как стратегию по умолчанию, черный цвет как цвет по умолчанию и обнуляет текущий элемент.

#### `_bind_canvas_events(self) -> None`
```python
def _bind_canvas_events(self) -> None:
    self.canvas.bind("<ButtonPress-1>", self._on_button_press)
    self.canvas.bind("<B1-Motion>", self._on_mouse_drag)
    self.canvas.bind("<ButtonRelease-1>", self._on_button_release)
```
Привязывает обработчики событий мыши к холсту: нажатие левой кнопки мыши к методу `_on_button_press`, перемещение с зажатой кнопкой к `_on_mouse_drag`, отпускание кнопки к `_on_button_release`.

#### `_create_ui_elements(self) -> None`
Создает основной фрейм для элементов управления и вызывает методы для создания кнопок инструментов, кнопки очистки и элементов управления цветом.

#### `_create_tool_buttons(self, parent: tk.Frame) -> None`
```python
def _create_tool_buttons(self, parent: tk.Frame) -> None:
    tools = [
        ("Линия", LineTool),
        ("Прямоугольник", RectangleTool),
        ("Овал", OvalTool)
    ]
    
    for tool_name, tool_class in tools:
        btn = tk.Button(
            parent, 
            text=tool_name, 
            command=lambda tc=tool_class: self.set_strategy(tc())
        )
        btn.pack(side=tk.LEFT, padx=10)
```
Создает кнопки для выбора инструментов рисования. Определяет список инструментов (Линия, Прямоугольник, Овал) с соответствующими классами, создает для каждого кнопку с лямбда-функцией, которая устанавливает соответствующую стратегию при нажатии.

#### `_create_color_controls(self, parent: tk.Frame) -> None`
Создает элементы управления цветом: кнопку "Выбрать цвет", которая вызывает диалог выбора цвета, и небольшой холст размером 30×20 пикселей для отображения текущего выбранного цвета.

#### `choose_color(self) -> None`
```python
def choose_color(self) -> None:
    color_result = colorchooser.askcolor(
        title="Выберите цвет рисования", 
        initialcolor=self.current_color
    )
    if color_result and color_result[1]:  # Проверяем, что цвет выбран
        self.current_color = color_result[1]
        self.color_preview.config(bg=self.current_color)
```
Открывает стандартный диалог выбора цвета tkinter. Если пользователь выбрал цвет (проверяет наличие результата), обновляет переменную current_color и изменяет цвет фона у индикатора цвета.

#### `clear_canvas(self) -> None`
Очищает весь холст от нарисованных объектов, вызывая метод delete("all") у объекта canvas.

#### `set_strategy(self, strategy: DrawingToolStrategy) -> None`
Устанавливает новую стратегию рисования. Принимает экземпляр класса, наследующего от DrawingToolStrategy, и сохраняет его в переменной strategy для использования при рисовании.

#### `_on_button_press(self, event: tk.Event) -> None`
Обработчик нажатия левой кнопки мыши на холсте. Сохраняет координаты точки нажатия в переменные start_x и start_y из объекта события, обнуляет current_item для подготовки к новому рисованию.

#### `_on_mouse_drag(self, event: tk.Event) -> None`
```python
def _on_mouse_drag(self, event: tk.Event) -> None:
    # Проверяем, что начальные координаты установлены
    if self.start_x is None or self.start_y is None:
        return
    
    # Удаляем предыдущий временный элемент
    if self.current_item:
        self.canvas.delete(self.current_item)
    
    # Рисуем временный элемент для предварительного просмотра
    self.current_item = self.strategy.draw(
        self.canvas, 
        self.start_x, 
        self.start_y, 
        event.x, 
        event.y, 
        color=self.current_color
    )
```
Обработчик перемещения мыши с зажатой кнопкой. Проверяет наличие начальных координат, удаляет предыдущий временный элемент (если есть), создает новый временный элемент с помощью текущей стратегии для предварительного просмотра от начальной точки до текущего положения мыши.

#### `_on_button_release(self, event: tk.Event) -> None`
Обработчик отпускания левой кнопки мыши. Удаляет временный элемент предпросмотра, создает финальный элемент с помощью текущей стратегии от начальной точки до точки отпускания, обнуляет все переменные состояния для завершения операции рисования.

### Функция `main() -> None`
```python
def main() -> None: 
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```
Главная функция программы. Создает корневое окно tkinter, экземпляр приложения DrawingApp, передавая ему корневое окно, и запускает главный цикл обработки событий tkinter.
