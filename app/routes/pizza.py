from flask import render_template, request, session
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from app import app
from sqlalchemy import select
from datetime import datetime
from connection import get_db_connection


# Отримання всіх піц
def get_all_pizzas():
    try:
        connection = get_db_connection()
        pizza = connection.execute("SELECT * FROM pizza").fetchall()
        connection.close()
        return pizza
        

    except sqlite3.Error as error:
        print("Помилка при отримані кода:", error)
        return []

    finally:
        if connection:
            connection.close()
            print("Піца отримана")
            

# Сторінка меню
@app.get("/menu/")
def menu_page():
    pizzas = get_all_pizzas()
    # Проверяем, является ли пользователь админом
    if session.get('is_admin'):
        return redirect(url_for("admin_page"))
    
    context = {
        "back_button": "Повернутися на головну сторінку",
        "pizzas": pizzas
    }
    return render_template("menu.html", **context)


# Сторінка додавання піци
@app.get("/add_pizza/")
def add_pizza_get():
    return render_template("add_pizza.html")


# Додавання піци
@app.post("/add_pizza/")
def add_pizza_post():
    if request.method == "POST":
        name = request.form.get("name")
        ingredients = request.form.get("ingredients")
        price = request.form.get("price")
        photo = request.form.get("photo")

        try:
            connection = get_db_connection()
            insert_query = """INSERT INTO pizza 
            (name, ingredients, price, photo) 
            VALUES (?, ?, ?, ?);"""
            connection.execute(insert_query, (name, ingredients, int(price), photo))
            connection.commit()
            print("Нова піца успішно додана")

        except sqlite3.IntegrityError:
            print("Помилка: піца з такою назвою або інгредієнтами вже існує.")
        except sqlite3.Error as error:
            print("Помилка при роботі з SQLite:", error)
        finally:
            if connection:
                connection.close()

    return render_template("add_pizza.html")
