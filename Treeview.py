import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Show Master Table Info')
root.geometry('600x400')

# List of columns
columns = ('No.', 'Nama Tipe', 'Tahun', 'Reorder Point', 'ACTION')

tree = ttk.Treeview(root, columns=columns, show='headings')

# headings
tree.heading('No.', text='No.')
tree.heading('Nama Tipe', text='Nama Tipe')
tree.heading('Tahun', text='Tahun')
tree.heading('Reorder Point', text='Reorder Point')
tree.heading('ACTION', text='ACTION')

