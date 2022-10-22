import boto3
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
s3 = boto3.resource('s3')
s3.meta.client.download_file('germancredit2', 'datos/model/preprocessing (1).joblib', 'preprocessing (1).joblib')
model = joblib.load("modelrf.joblib")

@app.route("/")
def infex():
    return "Hi Flask"
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

@app.route("/predict", methods=["POST"])
def predict():
    request_data = request.get_json()
    age = request_data["age"]
    credit_amount = request_data["credit_amount"]
    duration = request_data["duration"]
    sex = request_data["sex"]
    purpose = request_data["purpose"]
    housing = request_data["housing"]
    predict = model.predict([[age, credit_amount, duration, sex, purpose, housing]])
    dict = {'resultado' : predict.tolist()}
    return jsonify(dict)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
