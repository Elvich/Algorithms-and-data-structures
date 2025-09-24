import tkinter as tk

def on_click(symbol):
	current = entry.get()
	if current == 'Ошибка':
		entry.delete(0, tk.END)
		current = ''
	entry.delete(0, tk.END)
	entry.insert(0, current + str(symbol))

def on_clear():
	entry.delete(0, tk.END)

def on_equal():
	try:
		result = eval(entry.get())
		entry.delete(0, tk.END)
		entry.insert(0, str(result))
	except Exception:
		entry.delete(0, tk.END)
		entry.insert(0, 'Ошибка')

root = tk.Tk()
root.title('Калькулятор')
root.geometry('300x400')

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

buttons = [
	('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
	('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
	('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
	('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
	('=', 5, 0, 4)
]

for btn in buttons:
	if btn[0] == '=':
		b = tk.Button(root, text=btn[0], font=('Arial', 18), command=on_equal)
		b.grid(row=btn[1], column=btn[2], columnspan=btn[3], sticky='nsew', padx=2, pady=2)
	elif btn[0] == 'C':
		b = tk.Button(root, text=btn[0], font=('Arial', 18), command=on_clear)
		b.grid(row=btn[1], column=btn[2], sticky='nsew', padx=2, pady=2)
	else:
		b = tk.Button(root, text=btn[0], font=('Arial', 18), command=lambda x=btn[0]: on_click(x))
		b.grid(row=btn[1], column=btn[2], sticky='nsew', padx=2, pady=2)

for i in range(6):
	root.grid_rowconfigure(i, weight=1)
for j in range(4):
	root.grid_columnconfigure(j, weight=1)

root.mainloop()
