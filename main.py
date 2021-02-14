from flask import Flask, render_template      
from mttkinter import mtTkinter as tk
from scipy.signal import find_peaks
from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix
from scipy import sparse
from tkinter import filedialog
from wfdb import processing
import easygui
import matplotlib.pyplot as plt, mpld3
import numpy as np
import pandas as pd
import re
import statistics as st
import sys
import tkinter
import wfdb

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route('/upload/')
def uploaduj():
    root = tk.Tk() #esto se hace solo para eliminar la ventanita de Tkinter 
    root.withdraw() #ahora se cierra 
    data_file_path = easygui.fileopenbox()  #abre el explorador de archivos y guarda la seleccion en la variable!
    
    #Ahora para guardar el directorio donde se encontraba el archivo seleccionado:
    match = re.search(r'/.*\..+', data_file_path)#matches name of file
    file_position = data_file_path.find(match.group()) #defines position of filename in file path

    save_path = data_file_path[0: file_position+1] #extracts the saving path.

    record = wfdb.rdrecord(data_file_path[:-4]) 

    signals, fields = wfdb.rdsamp(data_file_path[:-4], channels=[0])
    record = wfdb.rdrecord(data_file_path[:-4], channels=[0])
    signal=signals.reshape(record.sig_len)

    fig=plt.figure(figsize=(12, 6))
    plt.plot(signal[:4000])
    plot=mpld3.save_html(fig,'static/grafica.html')
    fig2=plt.figure(figsize=(25, 2))
    plt.plot(signal[:int(len(signal)/10)])
    plot2=mpld3.save_html(fig2,'static/grafica2.html')
    return render_template('home.html',data=plot,record_name=record.__dict__['record_name'], file_name=data_file_path, fs=record.__dict__['fs'],sig_len=record.__dict__['sig_len'], resumen=record.__dict__)


if __name__ == "__main__":
    app.run(debug=True)
    url_for('static/css', filename='style.css')
