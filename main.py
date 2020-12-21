from flask import Flask, render_template      
from flask import Flask
from flask import render_template
import tkinter
from mttkinter import mtTkinter as tk
from tkinter import filedialog
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
    
@app.route('/upload/')
def uploaduj():
    root = tk.Tk() #esto se hace solo para eliminar la ventanita de Tkinter 
    root.withdraw() #ahora se cierra 
    file_path = filedialog.askopenfilename() #abre el explorador de archivos y guarda la seleccion en la variable!
    
    #Ahora para guardar el directorio donde se encontraba el archivo seleccionado:
    match = re.search(r'/.*\..+', file_path)#matches name of file
    file_position = file_path.find(match.group()) #defines position of filename in file path

    save_path = file_path[0: file_position+1] #extracts the saving path.
    return file_path
 
if __name__ == "__main__":
    app.run(debug=True)
    url_for('static', filename='style.css')
