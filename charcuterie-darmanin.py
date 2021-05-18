#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import random
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def publish():
    metier = random.choice(open("metiers.txt").readlines())
    sujet = random.choice(open("sujets_societe.txt").readlines())
    return render_template("home.html", sujet=sujet, metier=metier)


def main():
    app.run(host='0.0.0.0', port=8080)
    sys.exit()


if __name__ == '__main__':
    main()
