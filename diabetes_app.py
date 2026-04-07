import tkinter as tk
from tkinter import messagebox
import numpy as np
import pickle
import streamlit as st

# Load the trained model
try:
    with open('Diabetesmodel.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file 'Diabetesmodel.pkl' not found. Please ensure it's in the same directory.")
    raise SystemExit

# Function to predict
def predict():
    try:
        glucose = float(entry_glucose.get())
        bp = float(entry_bp.get())
        bmi = float(entry_bmi.get())
        age = int(entry_age.get())

        if glucose <= 0 or bp <= 0 or bmi <= 0 or age <= 0:
            raise ValueError("All values must be positive.")
        
        # Add a check for reasonable ranges (optional, but good practice for real-world apps)
        if not (20 <= glucose <= 200 and 30 <= bp <= 150 and 10 <= bmi <= 60 and 1 <= age <= 120):
            messagebox.showwarning("Input Warning", "Please enter realistic values for glucose (20-200), blood pressure (30-150), BMI (10-60), and age (1-120).")
            return

        input_data = np.array([[glucose, bp, bmi, age]])
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            result_label.config(text="⚠️ You are likely to have diabetes.", fg="#e74c3c") # Red for risk
        else:
            result_label.config(text="✅ You are not likely to have diabetes.", fg="#2ecc71") # Green for no risk

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers:\n- Glucose, Blood Pressure, BMI: decimals (e.g., 12.5)\n- Age: whole number (e.g., 30)")
    except Exception as e:
        messagebox.showerror("Prediction Error", f"An unexpected error occurred during prediction: {e}")

# GUI setup
root = tk.Tk()
root.title("AI Diabetes Risk Assessment")
root.geometry("480x550") # Slightly larger for better spacing
root.config(bg="#E0F2F7") # Light blue background
root.resizable(False, False)

# Modern Fonts
TITLE_FONT = ("Segoe UI", 22, "bold")
LABEL_FONT = ("Segoe UI", 13)
ENTRY_FONT = ("Segoe UI", 13)
BUTTON_FONT = ("Segoe UI", 14, "bold")
RESULT_FONT = ("Segoe UI", 16, "bold")
FOOTER_FONT = ("Segoe UI", 10)

# Header Frame with a subtle gradient effect (simulated with different shades)
header_frame = tk.Frame(root, bg="#2196F3", height=80) # Deeper blue
header_frame.pack(fill="x", pady=(0, 20)) # Padding below header

tk.Label(header_frame, text="AI Diabetes Risk Assessment", font=TITLE_FONT, bg="#2196F3", fg="white").pack(pady=20)


# Input frame
input_frame = tk.Frame(root, bg="#E0F2F7", padx=20, pady=10)
input_frame.pack(pady=10)

# Style for input fields
entry_style = {
    "font": ENTRY_FONT,
    "bg": "#FFFFFF", # White background
    "fg": "#333333", # Dark grey text
    "width": 20,
    "relief": "flat", # Flat border
    "bd": 1,
    "highlightbackground": "#BBDEFB", # Light blue border when not focused
    "highlightcolor": "#2196F3", # Deeper blue border when focused
    "highlightthickness": 2,
    "insertbackground": "#2196F3" # Blue cursor
}

def create_input_row(label_text, row):
    label = tk.Label(input_frame, text=label_text, font=LABEL_FONT, bg="#E0F2F7", fg="#333333")
    label.grid(row=row, column=0, sticky="w", pady=12, padx=15) # Aligned left
    entry = tk.Entry(input_frame, **entry_style)
    entry.grid(row=row, column=1, pady=12, padx=15)
    return entry

entry_glucose = create_input_row("Glucose (mg/dL):", 0)
entry_bp = create_input_row("Blood Pressure (mmHg):", 1)
entry_bmi = create_input_row("BMI (kg/m²):", 2)
entry_age = create_input_row("Age (years):", 3)

# Predict button
def on_hover(e):
    predict_btn['background'] = '#1976D2' # Darker blue on hover

def on_leave(e):
    predict_btn['background'] = '#2196F3' # Original blue

predict_btn = tk.Button(root, text="Predict", command=predict, font=BUTTON_FONT, 
                        bg="#2196F3", fg="white", width=25, height=2, 
                        bd=0, relief="raised", cursor="hand2", 
                        activebackground="#1976D2", # Active (clicked) background
                        activeforeground="white", # Active (clicked) foreground
                        highlightbackground="#64B5F6", # Outline color
                        highlightthickness=2,
                        padx=10, pady=5) # Internal padding
predict_btn.pack(pady=30)
predict_btn.bind("<Enter>", on_hover)
predict_btn.bind("<Leave>", on_leave)

# Result Label
result_label = tk.Label(root, text="", font=RESULT_FONT, bg="#E0F2F7", wraplength=400) # Wrap long text
result_label.pack(pady=15)

# Footer
footer_frame = tk.Frame(root, bg="#E0F2F7")
footer_frame.pack(side="bottom", fill="x", pady=(10, 5))
tk.Label(footer_frame, text="Developed with ❤️ using AI", font=FOOTER_FONT, bg="#E0F2F7", fg="#757575").pack()

# Run the application
root.mainloop()