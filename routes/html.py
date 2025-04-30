from flask import Blueprint, render_template, url_for, redirect, request
html_bp = Blueprint("html", __name__)

@html_bp.route("/")
def home():
    return "<h1>HEY THERE</h1>"

@html_bp.route("/qa")
def q_and_a():
    return "q and a page"

@html_bp.route("/login")
def login():
    return "login"



