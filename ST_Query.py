import json
import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Function to fetch data from the API
def fetch_data(file_name='ST_API.json'):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        messagebox.showerror("Error", "ST_API.json file not found.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Failed to decode JSON from ST_API.json.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Function to handle object selection
def select_objects(data):
    selected_data= data[selected_key.get()]
    display_data(selected_data)


# Function to display data in the fresh UI
def display_data(selected_data):
    tree.delete(*tree.get_children())

    try:
        if len(selected_data[0])!=1:
            for item in selected_data:
                tree.insert("", "end", values=(item['component'], item['capability'], item['command']))
        else:
            for item in selected_data:
                item0 = item[0]
                tree.insert("", "end", values=(item0['component'], item0['capability'], item0['command']))

    #do nothing
    except:
        None


# Create the main window
root = tk.Tk()
root.title("ST API Query")

# Create a frame for the treeview
frame = ttk.Frame(root)
frame.config(height=20)
frame.pack(padx=4, pady=4, fill=tk.BOTH, expand=True)

# Create the treeview
columns = ("component", "capability", "command")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("component", text="component")
tree.heading("capability", text="capability")
tree.heading("command", text="command")
tree.pack(fill=tk.BOTH, expand=True)

data = fetch_data()
data_keys = data.keys()

# Create a variable to store the selected key and ratio button for each key in data_keys
selected_key = tk.StringVar()
for item in data_keys:
    radio_button = ttk.Radiobutton(root, text=item, variable=selected_key, value=item)
    radio_button.pack(side=tk.LEFT, padx=5)
    
# Create a button to select objects
select_button = ttk.Button(root, textvariable=selected_key, command=lambda: select_objects(data))
select_button.pack(pady=10)

# Run the application
root.mainloop()