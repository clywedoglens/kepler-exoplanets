import flask
import os
import pickle
import pandas as pd
import skimage



app = flask.Flask(__name__, template_folder='templates')



@app.route('/', methods=['GET', 'POST'])
def new_home_bootstrap():
    if flask.request.method == 'GET':
        return(flask.render_template('new_home_bootstrap.html'))

@app.route('/data_exp_and_eng/', methods=['GET', 'POST'])
def data_exp_and_eng():
    if flask.request.method == 'GET':
        return(flask.render_template('data_exp_and_eng.html'))

@app.route('/features_and_models/', methods=['GET', 'POST'])
def features_and_models():
    if flask.request.method == 'GET':
        return(flask.render_template('features_and_models.html'))

@app.route('/model_evaluation/', methods=['GET', 'POST'])
def model_evaluation():
    if flask.request.method == 'GET':
        return(flask.render_template('model_evaluation.html'))

if __name__ == '__main__':
    app.run(debug=True)
