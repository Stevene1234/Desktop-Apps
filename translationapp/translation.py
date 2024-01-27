from googletrans import Translator
import tkinter as tk
#Note I had to use the pip install --upgrade googletrans==4.0.0-rc1 to get the translator to work right.

class TranslationApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Set Title
        self.title("Translation App")

        # Initialize Translator instance for language translation
        self.translator = Translator()

        # Language codes and corresponding language names
        self.language_codes = ['fr', 'es', 'de', 'it', 'pt']
        self.languages = ['French', 'Spanish', 'German', 'Italian', 'Portuguese']

        # Create the UI elements
        self.create_widgets()

    def create_widgets(self):
        # Text box for entering English text
        self.text_box = tk.Text(self, height=7, width=40, wrap=tk.WORD)
        self.text_box.pack(pady=10)
        self.text_box.insert("1.0", 'Write English here...')


        # Dropdown menu for selecting the target language
        self.selected_language = tk.StringVar() # Create a StringVar for the selected language
        self.selected_language.set("Select Language")

        self.language_dropdown = tk.OptionMenu(self, self.selected_language, *self.languages)
        self.language_dropdown.pack(pady=5)

        # Button to trigger the translation process
        self.translate_button = tk.Button(self, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=5)

        # Text box for displaying the translated text
        self.translated_text_box = tk.Text(self, height=7, width=40, wrap=tk.WORD, state=tk.DISABLED)
        self.translated_text_box.pack(pady=10)

    def translate_text(self):
        # Retrieve English text from the input text box
        english_text = self.text_box.get(1.0, tk.END)

        # Retrieve the selected target language
        chosen_language = self.selected_language.get()
        chosen_language_code = self.language_codes[self.languages.index(chosen_language)]

        # Perform translation and get the translated text
        translated_text = self.translator.translate(english_text, dest=chosen_language_code).text

        # Update the translated text box
        self.translated_text_box.config(state=tk.NORMAL)
        self.translated_text_box.delete(1.0, tk.END)
        self.translated_text_box.insert(1.0, translated_text)
        self.translated_text_box.config(state=tk.DISABLED)


app = TranslationApp()
app.mainloop()