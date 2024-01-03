# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = pickle.load(open('songs_hit_predictor.pkl', 'rb'))
scaler = StandardScaler()


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        """
        Dancibilty = float(request.form['Dancibilty'])
        energy = float(request.form['energy'])
        key = float(request.form['key'])
        loudness = float(request.form['loudness'])
        mode = float(request.form['mode'])
        speechiness = float(request.form['speechiness'])
        acousticness = float(request.form['acousticness'])
        instrumentalness = float(request.form['instrumentalness'])
        liveness = float(request.form['liveness'])
        valence = float(request.form['valence'])
        tempo = float(request.form['tempo'])
        duration_ms = float(request.form['duration_ms'])
        time_signature = float(request.form['time_signature'])
        chorus_hit = float(request.form['chorus_hit'])
        sections = float(request.form['sections'])
        decade = float(request.form['decade'])

        user_inputs = [Dancibilty, energy, key, loudness, mode, speechiness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature, chorus_hit, sections, decade]
        """

        # Extract user inputs
        features = ['Dancibilty', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                    'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',
                    'chorus_hit', 'sections', 'decade']

        user_inputs = [float(request.form[feature]) for feature in features]

        # Scale the user inputs using the pre-fitted scaler
        scaled_inputs = scaler.fit_transform([user_inputs])

        prediction = model.predict(scaled_inputs)

        model_result = prediction
        print("Model Prediction: ", model_result)
        if model_result == 1:
            hit = "Hit"
        else:
            hit = "Not Hit"

        return render_template("index.html", prediction_text="Music will {}".format(hit))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    # If you want to run your application on just on local host uncomment the line below and run
    # app.run(debug=True)

    # If you want to run your application in your machine ip address
    app.run(debug=True, port=5000, host='0.0.0.0')
