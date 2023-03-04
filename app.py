# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

model = pickle.load(open('songs_hit_predictor.pkl', 'rb'))

@app.route('/', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':

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
        
        prediction = model.predict([[Dancibilty,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature,chorus_hit,sections,decade]])

        model_result = prediction
        if model_result == 1:
            hit = "Hit"
        else:
            hit = "Not Hit"

        return render_template("index.html", prediction_text = "Music will {}".format(hit))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)