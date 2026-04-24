import tkinter as tk
from tkinter import font, messagebox

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load product dataset
product_df = pd.read_csv('product_dataset.csv')
products = product_df.to_dict(orient='records')

# Initialize global variables
user_preferences = []

# Function to calculate recommendations based on cosine similarity
def recommend_products(user_input):
    # Extract product features
    product_features = product_df['features'].tolist()

    # Add user preferences to the product features list for vectorization
    all_features = product_features + [user_input]

    # Vectorize the text data using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_features)

    # Calculate cosine similarity between user input and product features
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    similarity_scores = cosine_sim.flatten()

    # Get the top 5 recommendations based on similarity score
    top_indices = similarity_scores.argsort()[-5:][::-1]
    recommendations = [products[i] for i in top_indices]

    return recommendations

# Function to dynamically update user preferences based on input
def update_user_preferences(user_input):
    global user_preferences
    user_preferences.append(user_input)

# Function to handle the recommendation request
def get_recommendations():
    user_input = entry.get()
    update_user_preferences(user_input)  # Update user preferences

    recommendations = recommend_products(user_input)
    recommendations_text = '\n'.join([
        f"Name: {rec['name']}\nCategory: {rec['category']}\nFeatures: {rec['features']}\n"
        for rec in recommendations
    ])
    if not recommendations_text:
        recommendations_text = "No recommendations found."
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, recommendations_text)

# Function to display user preferences and influence on recommendations
def show_user_preferences():
    preferences_text = "User Preferences:\n" + "\n".join(user_preferences)
    messagebox.showinfo("User Preferences", preferences_text)

# Set up the GUI
root = tk.Tk()
root.title("SMART CART - AI-Powered Product Picker")

# Configure window size and background color
root.geometry("800x600")  # Bigger window
root.config(bg="#2c3e50")  # Dark background color

# Custom fonts
heading_font = font.Font(family="Helvetica", size=18, weight="bold")
label_font = font.Font(family="Helvetica", size=14)
button_font = font.Font(family="Helvetica", size=12)

# Label for input
label = tk.Label(root, text="Enter product preferences (keywords separated by spaces):", font=label_font, bg="#2c3e50", fg="white")
label.pack(pady=20)

# Input field for user preferences
entry = tk.Entry(root, width=50, font=label_font)
entry.pack(pady=10)

# Button to get recommendations
recommend_button = tk.Button(root, text="Get Recommendations", font=button_font, bg="#3498db", fg="white", width=20, height=2, command=get_recommendations)
recommend_button.pack(pady=10)

# Text area to display recommendations
text_output = tk.Text(root, width=80, height=15, font=("Helvetica", 12), bg="#ecf0f1", fg="#2c3e50", wrap=tk.WORD)
text_output.pack(pady=20)

# Button to view user preferences
preferences_button = tk.Button(root, text="View User Preferences", font=button_font, bg="#e74c3c", fg="white", width=20, height=2, command=show_user_preferences)
preferences_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
