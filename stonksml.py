from flask import Flask, render_template_string
import os
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the API key from environment variables
    API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

    if not API_KEY:
        return "API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable."

    # Initialize TimeSeries object
    ts = TimeSeries(key=API_KEY, output_format='pandas')

    # Fetch intraday stock data for Microsoft (MSFT)
    data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='compact')

    # Plot the data
    plt.figure()
    data['4. close'].plot()
    plt.title('Intraday Stock Data for MSFT')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Render the plot in an HTML template
    return render_template_string('''
        <h1>Intraday Stock Data for MSFT</h1>
        <img src="data:image/png;base64,{{ plot_url }}" />
    ''', plot_url=plot_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0')