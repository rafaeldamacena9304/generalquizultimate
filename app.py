from flask import Flask, render_template, url_for, request, redirect, current_app, session, jsonify
from pymongo import MongoClient
import uuid
import random
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = 'sae5f4a56we5r4f$$#@!!!g5s4ae5r42/xz12*@!(#)13505435t5e4698+4f5w95+-d4154r5tgs54er524435t45596e4gf5'
client = MongoClient(os.getenv("MONGODB_URI"))
app.db = client.generaldb
resultados = []
def question_id():
    return random_number


def is_logged_in():
    return 'user_email' in session

@app.route('/login', methods=["POST", "GET"])
def login():
    email = request.form.get("email")
    session['user_email'] = email
    current_app.db.generaldb.insert_one({"email": email})
    if is_logged_in():
        return render_template('homepage.html', title="General Quiz | Homepage")
    else:
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")

    if request.form.get("email"):
        is_logged_in()
        return render_template('homepage.html')
    else:
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")


@app.route('/logout', methods=["POST"])
def logout():
    session.pop('user_email', None)
    return render_template('homepage.html')


def is_logged_in():
    return 'user_email' in session



@app.route('/')
def homepage():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if is_logged_in():
        return render_template('homepage.html', title="General Quiz | Homepage")
    else:
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")


@app.route('/contact')
def contact():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if is_logged_in():
        return render_template('contact.html', title="General Quiz | Contact")
    else:
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")




@app.route('/questions', methods=["POST", "GET"])
def questions():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    global random_number
    random_number = random.randint(1,1000)
    if is_logged_in():
        return render_template('question1.html', title='General Quiz | Question 1')
    else:
        return render_template('login.html')



# QUESTÃO 1
@app.route('/answer1', methods=["POST"])
def answer1():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    question1d = request.form.get("question1d")
    if request.form.get("question1d"):
        random_number = random.randint(1, 500)
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question1": request.form.get("question1d")})
        resultados.append(random_number)
    else:
        print('incorreto')
    return render_template('question2.html', title="General Quiz | Question 2")


#QUESTÃO 2
@app.route('/answer2', methods=["POST"])
def answer2():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    question2c = request.form.get("question2c")
    if  request.form.get("question2c"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question2": request.form.get("question2c")})
        resultados.append(random_number)
    else:
            pass
    return render_template('question3.html', title="Question 3")


# QUESTÃO 3
@app.route('/answer3', methods=["POST"])
def answer3():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    question3 = []
    question3a = request.form.get("question3a")
    if request.form.get("question3a"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question3": request.form.get("question3a")})
        resultados.append(random_number)
    else:
            pass
    return render_template('question4.html', title='General Quiz | Question 4')


# QUESTÃO 4
@app.route('/answer4', methods=["POST"])
def answer4():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    if  request.form.get("question4b"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question4": request.form.get("question4b")})
        resultados.append(random_number)
    else:
            pass
    return render_template('question5.html', title='General Quiz | Question 5')


# QUESTÃO 5
@app.route('/answer5', methods=["POST"])
def answer5():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    if  request.form.get("question5b"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question5": request.form.get("question5b")})
        resultados.append(random_number)
    else:
            pass
    return render_template('question6.html', title='General Quiz | Question 6')


# QUESTÃO 6
@app.route('/answer6', methods=["POST"])
def answer6():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    if  request.form.get("question6a"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question6": request.form.get("question6a")})
        resultados.append(random_number)
    else:
            pass
    return render_template('question7.html', title='General Quiz | Question 7')


# QUESTÃO 7
@app.route('/answer7', methods=["POST"])
def answer7():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    if  request.form.get("question7a"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question7": request.form.get("question7a")})
        resultados.append(random_number)
    else:
        pass
    return render_template('question8.html', title='General Quiz | Question 8')


# QUESTÃO 8
@app.route('/answer8', methods=["POST"])
def answer8():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    if  request.form.get("question8c"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question8": request.form.get("question8c")})
        resultados.append(random_number)
    else:
            pass
    return render_template('question9.html', title='General Quiz | Question 9')


# QUESTÃO 9
@app.route('/answer9', methods=["POST"])
def answer9():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    if  request.form.get("question9d"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question9": request.form.get("question9d")})
        resultados.append(random_number)
    else:
            pass
    return render_template('question10.html', title='General Quiz | Question 10')


# QUESTÃO 10
@app.route('/answer10', methods=["POST"])
def answer10():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    email = session['user_email']
    if  request.form.get("question10c"):
        current_app.db.generaldb.insert_one({"id": question_id(),"user_email": email, "question10": request.form.get("question10c")})
        resultados.append(random_number)
    else:
            pass
    if len(resultados) == 10:
        qtd = len(resultados)
    else:
        qtd = len(resultados)
    return render_template('results.html', title='General Quiz | Results', qtd=qtd )

@app.route('/results', methods=["POST"])
def results():
    if current_app.db.generaldb.find_one({"email": {"$exists": False}}):
        return render_template('login.html', h="You're not logged-in", p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if not is_logged_in():
        return render_template('login.html', h="You're not logged-in",
                               p="Please input your pay-pal e-mail. That'll be the way you receive rewards.")
    if request.form.get("return_button1", "return_button"):
        global random_number
        random_number = None
        return render_template('homepage.html')
        if request.form.get("logout_button"):
            logout()
    else:
        return render_template('results.html')
        random_number = None
        logout()
    return url_for('logout')


if __name__ == "__main__":
    app.run(debug=True)
