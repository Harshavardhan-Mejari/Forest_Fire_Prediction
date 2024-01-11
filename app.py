from flask import *
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def hello():
        return render_template("forest.html")

@app.route("/predict",methods=["POST"])
def predict():
        param1=request.form["temp"]
        param2=request.form["oxy"]
        param3=request.form["humi"]
        # arr=np.array([[param1,param2,param3]])
        prediction=model.predict([[param1,param2,param3]])
        #return prediction
        return render_template("after.html",data=prediction)
if __name__=="__main__":
          app.run(debug=True) 