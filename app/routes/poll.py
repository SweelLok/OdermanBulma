from flask import Flask, render_template, request
from app.routes import app
from connection import get_db_connection


filename = "data.txt"


# Сторінка голосування
@app.get("/poll/")
def poll_page():

    connection = get_db_connection()
    pizzas = connection.execute("SELECT * FROM pizza").fetchall()
    connection.close()

    return render_template("poll.html", data=pizzas)


# Голосування
@app.post("/poll/")
def poll():

    connection = get_db_connection()
    pizzas = connection.execute("SELECT * FROM pizza").fetchall()
    connection.close()

    vote = request.form.get("field")
    if vote:
        with open(filename, "a", encoding='utf-8') as out:
            out.write(vote + "\n")
    return render_template("poll.html", data=pizzas)


# Сторінка результатів
@app.get("/results/")
def get_results():
    with open(filename, "r", encoding='utf-8') as file:
        total_votes = {}
        data = file.readlines()

    for vote in data:
        vote = vote.strip()
        total_votes[vote] = total_votes.get(vote, 0) + 1
    
    formatted_votes = {}
    for vote, count in total_votes.items():
        formatted_name = vote.replace("_", " ")
        formatted_votes[formatted_name] = count

    return render_template("results.html", total_count=formatted_votes)
