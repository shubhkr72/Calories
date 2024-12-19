from flask import Flask,request,jsonify,render_template
import pickle

import pandas as pd
#load trained model
model_path='calories.pkl'
with open(model_path,'rb') as file:
    model=pickle.load(file)
    
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', output=None,display='none')

@app.route('/predict',methods=['POST'])
def predict():
    # extract data from
    features=[float(feature) for feature in request.form.values()]
    # final_features=[np.array(int_features)]
    feature_names = ['Gender', 'Age', 'Height','Weight','Duration','Heart_Rate','Body_Temp']
    # Convert input to DataFrame with correct feature names
    final_features = pd.DataFrame([features], columns=feature_names)
    
    #make predictions
    predicted_burn=model.predict(final_features)
    output = float(predicted_burn[0])
    return render_template('index.html',output=output,display='flex')

if __name__=="__main__":
    app.run(debug=True)