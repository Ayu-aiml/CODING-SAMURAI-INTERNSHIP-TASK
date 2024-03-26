import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # PIL library for handling images
from modeling import get_movie_recommendations, movies_df

# Function to handle movie selection from the combo box
def on_movie_selection(event):
    selected_movie = combo.get().strip('"')
    recommendations = get_movie_recommendations(selected_movie)
    recommendation_listbox.delete(0, tk.END)  # Clear previous recommendations

    if recommendations:
        for i, movie in enumerate(recommendations):
            recommendation_listbox.insert(tk.END, f"{i + 1}. {movie}")
    else:
        recommendation_listbox.insert(tk.END, "No recommendations found.")

# Create a Tkinter window
window = tk.Tk()
window.title("Movie Recommendation System")
window.geometry("600x500")
window.configure(background="#000000")  # Set background color

# Load and display background image
bg_image = Image.open("C:/Users/AYUSH/OneDrive/Desktop/wallpaper2.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create a custom style for the combo box and listbox
style = ttk.Style()
style.theme_use("clam")  

# Configure the combo box style
style.configure("TCombobox", padding=5,
                background="white", font=("Arial", 12))
style.map("TCombobox", fieldbackground=[("readonly", "#000000")])

# Create a combo box (dropdown menu) for movie selection
movie_titles = [title for title in movies_df['title']]
combo = ttk.Combobox(
    window, values=movie_titles, state="readonly")
combo.set("Select a movie")
combo.bind("<<ComboboxSelected>>", on_movie_selection)
combo.pack(pady=10)
combo.focus()

# Configure the listbox style
style.configure("TListbox", padding=5, background="#000000",
                font=("Arial", 12), foreground="#000000")
style.map("TListbox", background=[("active", "#000000")])

# Create a listbox to display movie recommendations
recommendation_listbox = tk.Listbox(window, width=50, height=10)
recommendation_listbox.pack(pady=20)

# Run the Tkinter main loop
window.mainloop()
