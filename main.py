from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from model.utils2 import insurance_data_prediction1
import config

app=Flask(__name__)
@app.route('/')
def home():
    print('we are in now home API')
    return render_template('index.html')

@app.route("/predict_fraud1",methods =["GET","POST"])
def predicted_diabetes():
    if request.method=="GET" :
        print("we are using GET method")

        File_Name=request.args.get("File_Name")
        download_file_name=request.args.get('download_file_name')
        

        insurance_data_subscibe =  insurance_data_prediction1(File_Name)
        output = insurance_data_subscibe .get_predicted_Fraud_or_geniune()
        if output ==0:
            return render_template("index.html", prediction ='Genuine')
        else:
            return render_template("index.html", prediction ='Fraud ')

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= config.Port_Number, debug=True) 