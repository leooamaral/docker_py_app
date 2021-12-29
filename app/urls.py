#!/usr/bin/python

import json
from flask import Flask
from services import Services
app = Flask(__name__)


class Urls(Services):

    @app.route("/")
    def hello():
        return "<h1>Hello world!</h1>"

    @app.route("/pwd")
    def pwd():
        return "<h1>Where I am: </h1>" + Services.pwd()

    @app.route("/healthchecker")
    def healthchecker():
        return "<h1>OK</h1>"

    @app.route("/conf/env")
    def env():
        env = Services.env()
        return "<h1>env_vars using env</h1>" + json.dumps(env)

    @app.route("/conf/printenv")
    def printenv():
        printenv = Services.printenv()
        return "<h1>env_vars using printenv</h1>" + printenv

    @app.route("/env/<env_name>/<env_v>")
    def create_env(env_name, env_v):
        new_env_var = Services.create_env(env_name, env_v)
        return new_env_var

    @app.route("/running-software")
    def pid():
        pid = Services.running_software()
        return "<h1>listing all running software</h1>" + pid

    @app.route("/running-software/<serv_name>")
    def specific_running_software(serv_name):
        specific_software = Services.specific_running_software(serv_name)
        return "<h1>listing specific running software</h1>" + specific_software


if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
    
