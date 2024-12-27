from flask import render_template, request, session
from flask import Flask, render_template, request, redirect, url_for
from app.routes import app
from sqlalchemy import select
from datetime import datetime
from .pizza import get_all_pizzas


app.secret_key = 'q'


# Сторінка входу 
@app.get("/login/")
def login_page():
    session.pop('is_admin', None)
    return render_template("login.html")


# Перевірка входу та встановлення сесії
@app.post("/login/")
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == "@dm1n":
        session['is_admin'] = True
        return redirect(url_for("admin_page"))
    return redirect(url_for("menu_page"))


# Сторінка адмінки
@app.get("/admin/")
def admin_page():
    if not session.get('is_admin'):
        return redirect(url_for("login_page"))
    pizzas = get_all_pizzas()
    context = {
        "pizzas": pizzas
    }
    return render_template("admin.html", **context)


# Вихід з адмінки
@app.get("/logout/")
def logout():
    session.pop('is_admin', None)
    return redirect(url_for("login_page"))
