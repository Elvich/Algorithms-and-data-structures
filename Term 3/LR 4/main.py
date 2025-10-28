import tkinter as tk
from tkinter import colorchooser
from abc import ABC, abstractmethod
from typing import Optional, Any


class DrawingToolStrategy(ABC):
    
    @abstractmethod
    def draw(self, canvas: tk.Canvas, start_x: int, start_y: int, 
             end_x: int, end_y: int, **kwargs: Any) -> int:
        pass

class LineTool(DrawingToolStrategy):
    
    def draw(self, canvas: tk.Canvas, start_x: int, start_y: int, 
             end_x: int, end_y: int, **kwargs: Any) -> int:
        color = kwargs.get('color', 'blue')
        return canvas.create_line(start_x, start_y, end_x, end_y, 
                                fill=color, width=2)


class RectangleTool(DrawingToolStrategy):
    
    def draw(self, canvas: tk.Canvas, start_x: int, start_y: int, 
             end_x: int, end_y: int, **kwargs: Any) -> int:
        color = kwargs.get('color', 'red')
        return canvas.create_rectangle(start_x, start_y, end_x, end_y, 
                                     outline=color, width=2)


class OvalTool(DrawingToolStrategy):
    
    def draw(self, canvas: tk.Canvas, start_x: int, start_y: int, 
             end_x: int, end_y: int, **kwargs: Any) -> int:
        color = kwargs.get('color', 'orange')
        return canvas.create_oval(start_x, start_y, end_x, end_y, 
                                outline=color, width=2)

class DrawingApp:

    # Константы приложения
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 400
    CANVAS_BG = "white"
    CANVAS_BORDER_WIDTH = 2
    DEFAULT_COLOR = 'black'
    
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self._setup_window()
        self._setup_canvas()
        self._initialize_drawing_state()
        self._bind_canvas_events()
        self._create_ui_elements()
    
    def _setup_window(self) -> None:
        self.master.title("Интерактивное приложение для рисования")
        self.master.resizable(False, False)
    
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
    
    def _initialize_drawing_state(self) -> None:
        self.start_x: Optional[int] = None
        self.start_y: Optional[int] = None
        self.strategy: DrawingToolStrategy = LineTool()  # Стратегия по умолчанию
        self.current_color: str = self.DEFAULT_COLOR
        self.current_item: Optional[int] = None
    
    def _bind_canvas_events(self) -> None:
        self.canvas.bind("<ButtonPress-1>", self._on_button_press)
        self.canvas.bind("<B1-Motion>", self._on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_button_release)
    
    def _create_ui_elements(self) -> None:
        frame = tk.Frame(self.master)
        frame.pack(pady=10)

        # Кнопки выбора инструментов
        self._create_tool_buttons(frame)
        
        # Кнопка очистки
        clear_btn = tk.Button(frame, text="Очистить", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT, padx=10)

        # Элементы управления цветом
        self._create_color_controls(frame)
    
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
    
    def _create_color_controls(self, parent: tk.Frame) -> None:
        color_btn = tk.Button(parent, text="Выбрать цвет", command=self.choose_color)
        color_btn.pack(side=tk.LEFT, padx=5)

        # Показ текущего цвета
        self.color_preview = tk.Canvas(parent, width=30, height=20, bg=self.current_color)
        self.color_preview.pack(side=tk.LEFT, padx=5)

    def choose_color(self) -> None:
        color_result = colorchooser.askcolor(
            title="Выберите цвет рисования", 
            initialcolor=self.current_color
        )
        if color_result and color_result[1]:  # Проверяем, что цвет выбран
            self.current_color = color_result[1]
            self.color_preview.config(bg=self.current_color)

    def clear_canvas(self) -> None:
        self.canvas.delete("all")

    def set_strategy(self, strategy: DrawingToolStrategy) -> None:
        self.strategy = strategy

    def _on_button_press(self, event: tk.Event) -> None:
        self.start_x = event.x
        self.start_y = event.y
        self.current_item = None

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

    def _on_button_release(self, event: tk.Event) -> None:
        # Удаляем временный элемент
        if self.current_item:
            self.canvas.delete(self.current_item)
        
        # Рисуем окончательный элемент
        if self.start_x is not None and self.start_y is not None:
            self.strategy.draw(
                self.canvas, 
                self.start_x, 
                self.start_y, 
                event.x, 
                event.y, 
                color=self.current_color
            )
        
        # Сбрасываем состояние
        self.start_x = None
        self.start_y = None
        self.current_item = None


def main() -> None: 
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()