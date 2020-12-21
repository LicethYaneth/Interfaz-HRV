from flask import Flask, render_template      
from flask import Flask
from flask import render_template
import tkinter as tk
from tkinter import filedialog
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
    
@app.route('/upload/')
def uploaduj():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path
 
if __name__ == "__main__":
    app.run(debug=True)
    url_for('static', filename='style.css')
