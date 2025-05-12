
from flask import Flask, request, Response, jsonify
import random

weather_app = Flask(__name__)

@weather_app.route('/w/<location>', methods=['GET'])
def w(location):
    fmt = request.args.get('format', 'json').lower()
    degree = f"{random.randint(35, 45)}°C"
    
    if fmt == 'xml':
        xml_data = f'''
        <forecast>
            <location>{location}</location>
            <temp>{degree}</temp>
            <scale>celsius</scale>
        </forecast>
        '''
        return Response(xml_data.strip(), content_type='application/xml')
   
    return jsonify({
        "location": location,
        "temp": degree,
        "scale": "celsius"
    })

if __name__ == '__main__':
    weather_app.run(debug=True)
