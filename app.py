from flask import Flask, request, jsonify,render_template
import util

app = Flask(__name__) 


@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
   
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath,balcony)
    })
   

    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)
