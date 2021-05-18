#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from flask import Flask
#, render_template, request

app = Flask(__name__)


@app.route("/")
def publish():
    metier="toto"
    sujet="sujet"
    return render_template("home.html", sujet=sujet, metier=metier)


def main():
    conn = create_conn()
    init_db(get_cursor(conn))
    conn.commit()
    conn.close()
    app.run(host='0.0.0.0', port=80)
    sys.exit()


if __name__ == '__main__':
    main()
