import tkinter as tk
from tkinter import ttk
import pandas as pd

def search_data():
    search_query = search_entry.get()
    if search_query:
        # Filter the DataFrame based on the search query
        result_df = df[df['Name of movie'].str.contains(search_query, case=False, na=False)]
        result_text.delete(1.0, tk.END)  # Clear the previous results
        if not result_df.empty:
            result_text.insert(tk.END, result_df.to_string(index=False))
        else:
            result_text.insert(tk.END, "No matching data found.")
    else:
        result_text.delete(1.0, tk.END)  # Clear the previous results

# Load the CSV file
df = pd.read_csv('movie_cleaned.csv')

# Create the main window
window = tk.Tk()
window.title("CSV Search Application")

# Styling
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))

# Create a header label
header_label = ttk.Label(window, text="Movie Search", font=('Helvetica', 16, 'bold'))
header_label.pack(pady=20)

# Create a search label and entry
search_label = ttk.Label(window, text="Enter a movie name to search:")
search_label.pack()
search_entry = ttk.Entry(window, width=40)
search_entry.pack(pady=10)

# Create a search button
search_button = ttk.Button(window, text="Search", command=search_data)
search_button.pack()

# Create a text box to display search results
result_text = tk.Text(window, height=10, width=120)
result_text.pack(pady=20)

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.mainloop()
