import tkinter as tk
import requests
from bs4 import BeautifulSoup

def get_elements(url, tag):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_doc = response.text
        else:
            print("Error: {}".format(response.status_code))
            return

        soup = BeautifulSoup(html_doc, 'html.parser')
        elements = soup.find_all(tag)
        return elements
    except Exception as e:
        print("Error: {}".format(e))
        return []

def run_script():
    url = url_entry.get()
    tag = tag_entry.get()
    elements = get_elements(url, tag)

    if len(elements) > 0:
        result_label.config(text="Extracted elements:")
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        for i in range(min(len(elements), 5)):
            result_text.insert(tk.END, str(elements[i]) + '\n')
        result_text.config(state=tk.DISABLED)
    else:
        result_label.config(text="No elements found.")

# Create the GUI
root = tk.Tk()
root.title("Web Scraping App")

# URL entry
url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)
url_entry = tk.Entry(root)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Tag entry
tag_label = tk.Label(root, text="Tag:")
tag_label.grid(row=1, column=0, padx=5, pady=5)
tag_entry = tk.Entry(root)
tag_entry.grid(row=1, column=1, padx=5, pady=5)

# Button
enter_button = tk.Button(root, text="Enter", command=run_script)
enter_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Result area
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
result_text = tk.Text(root, height=10, width=30, state=tk.DISABLED)
result_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()