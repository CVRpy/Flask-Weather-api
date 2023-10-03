from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if city:
        api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        response = requests.get(url)
        weather_data = response.json()
        
        if weather_data.get('cod') == 200:
            return render_template('weather.html', weather_data=weather_data)
    
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
