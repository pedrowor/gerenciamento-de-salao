"""Tela de login e cadastro local."""

import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller

        self.window = tk.Toplevel(self.master)
        self.window.title("Login - Salão de Beleza Neide Leila")
        self.window.geometry("350x230")
        self.window.resizable(False, False)

        frame = ttk.Frame(self.window, padding=20)
        frame.pack(expand=True, fill=tk.BOTH)

        ttk.Label(frame, text="Usuário:").pack(anchor=tk.W)
        self.username_entry = ttk.Entry(frame, width=36)
        self.username_entry.pack(pady=(3, 9), fill=tk.X)

        ttk.Label(frame, text="Senha:").pack(anchor=tk.W)
        self.password_entry = ttk.Entry(frame, width=36, show="*")
        self.password_entry.pack(pady=(3, 12), fill=tk.X)

        self.login_button = ttk.Button(frame, text="Entrar")
        self.login_button.pack(fill=tk.X)
        self.register_button = ttk.Button(
            frame, text="Criar conta", command=self._show_registration_dialog
        )
        self.register_button.pack(pady=(7, 0), fill=tk.X)

        self.username_entry.focus_set()
        if controller:
            self.username_entry.bind("<Return>", controller.handle_login_event)
            self.password_entry.bind("<Return>", controller.handle_login_event)
            self.login_button.config(command=controller.handle_login_event)
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        else:
            self.window.protocol("WM_DELETE_WINDOW", self.destroy)

    def _show_registration_dialog(self):
        dialog = tk.Toplevel(self.window)
        dialog.title("Criar conta")
        dialog.geometry("360x285")
        dialog.resizable(False, False)
        dialog.transient(self.window)
        dialog.grab_set()

        frame = ttk.Frame(dialog, padding=20)
        frame.pack(expand=True, fill=tk.BOTH)

        ttk.Label(frame, text="Novo usuário:").pack(anchor=tk.W)
        username = ttk.Entry(frame, width=36)
        username.pack(fill=tk.X, pady=(3, 9))

        ttk.Label(frame, text="Senha (mínimo 8 caracteres):").pack(anchor=tk.W)
        password = ttk.Entry(frame, width=36, show="*")
        password.pack(fill=tk.X, pady=(3, 9))

        ttk.Label(frame, text="Confirme a senha:").pack(anchor=tk.W)
        confirmation = ttk.Entry(frame, width=36, show="*")
        confirmation.pack(fill=tk.X, pady=(3, 12))

        def submit(event=None):
            if not self.controller:
                return
            success, message = self.controller.handle_register_event(
                username.get(), password.get(), confirmation.get()
            )
            if success:
                self.username_entry.delete(0, tk.END)
                self.username_entry.insert(0, username.get().strip())
                self.password_entry.delete(0, tk.END)
                dialog.destroy()
                messagebox.showinfo("Conta criada", message, parent=self.window)
                self.password_entry.focus_set()
            else:
                messagebox.showerror("Cadastro", message, parent=dialog)

        ttk.Button(frame, text="Cadastrar", command=submit).pack(fill=tk.X)
        dialog.bind("<Return>", submit)
        username.focus_set()

    def get_username(self):
        return self.username_entry.get()

    def get_password(self):
        return self.password_entry.get()

    def show(self):
        self.window.deiconify()
        self.window.grab_set()

    def hide(self):
        self.window.withdraw()

    def destroy(self):
        self.window.destroy()

    def show_error(self, title, message):
        messagebox.showerror(title, message, parent=self.window)

    def on_closing(self):
        if messagebox.askokcancel(
            "Sair", "Deseja sair da aplicação?", parent=self.window
        ):
            self.master.destroy()
