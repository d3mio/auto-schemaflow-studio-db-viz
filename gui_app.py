import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

class SchemaFlowStudio(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('SchemaFlow Studio')
        self.geometry('1200x800')
        ctk.set_appearance_mode('dark')

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.schema_tab = ttk.Frame(self.notebook)
        self.migration_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.schema_tab, text='Schema Viewer')
        self.notebook.add(self.migration_tab, text='Migration Planner')
        self.notebook.add(self.settings_tab, text='Settings')

        self.setup_schema_tab()
        self.setup_migration_tab()
        self.setup_settings_tab()

    def setup_schema_tab(self):
        schema_label = ctk.CTkLabel(self.schema_tab, text='Schema Viewer', font=('Arial', 16))
        schema_label.pack(pady=10)

    def setup_migration_tab(self):
        migration_label = ctk.CTkLabel(self.migration_tab, text='Migration Planner', font=('Arial', 16))
        migration_label.pack(pady=10)

    def setup_settings_tab(self):
        settings_label = ctk.CTkLabel(self.settings_tab, text='Settings', font=('Arial', 16))
        settings_label.pack(pady=10)

if __name__ == '__main__':
    app = SchemaFlowStudio()
    app.mainloop()