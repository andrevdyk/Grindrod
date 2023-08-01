from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
# Route to serve the index.html page----------------------------------------------------------------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('/index.html')

# This is the route for the vessel simulations page-------------------------------------------------------------------------------------------------------------------
@app.route('/vessel_simulations')  
def vessel_simulations():
    return render_template('/vessel_sim.html')



# Route to handle the container tracking API call for status -----------------------------------------------------------------------------------------------------------

@app.route('/status', methods=['POST'])
def get_container_status():
    container_number = request.form['container_number']
    api_key = '729757e8-e969-4cbe-851e-f3e58c83116f'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'https://api.sinay.ai/container-tracking/api/v1/status/container?number={container_number}'

    headers = {
        'accept': 'application/json',
        'API_KEY': api_key,
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print('Error fetching container status data:', e)
        return jsonify({'error': 'Something went wrong while fetching data.'}), 500
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------  





# Route handler for the container tracking API call for location------------------------------------------------------------------------------------------------------------
@app.route('/location', methods=['POST'])
def get_container_location():
    container_number = request.form['container_number']
    api_key = '729757e8-e969-4cbe-851e-f3e58c83116f'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'https://api.sinay.ai/container-tracking/api/v1/location/container?number={container_number}'

    headers = {
        'accept': 'application/json',
        'API_KEY': api_key,
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        print('Error fetching container location data:', e)
        return jsonify({'error': 'Something went wrong while fetching data.'}), 500
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)