import tkinter as tk
window = tk.Tk()

window.title("Dota 2 Terrain Manager")
window.geometry("600x400")
window.iconphoto(False, tk.PhotoImage(file="assets/icon/icon.png"))
window.resizable(False, False)
window.configure(bg="#3c3c3c")

button = tk.Button(window, text="Apply Terrain")
button.configure(bg="#4b4b4b", fg="#ffffff", font=("Ubuntu", 12))
button.pack()

window.mainloop()