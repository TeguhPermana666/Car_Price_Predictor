from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

house=pd.read_csv("Data\Cleaned_House_Data.csv")

app = Flask(__name__)
@app.route('/')
def index():
    LT = sorted(house['LT'].unique())
    LB = sorted(house['LB'].unique())
    return render_template('index.html',LT=LT,LB=LB)

if __name__ == "__main__":
    app.run(debug=True)
