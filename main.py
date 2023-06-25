#Импорт
from flask import Flask, render_template,request, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#class Card(db.Model):
    #Создание поле
    #id = db.Column(db.Integer, primary_key=True)
    #email = db.Column(db.Text, nullable=False)
    #text = db.Column(db.Text, nullable=False)

    #def __repr__(self):
        #return f'<Card {self.id}>'
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False, autoincrement=True)
    text = db.Column(db.String(50), nullable=False, autoincrement=True)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')



#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    
    return render_template('index.html', button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db
                           )


#@app.route('/')
#def card(id):
    c#ard = Card.query.get(id)

    #return render_template('card.html', card=card)

@app.route('/', methods=['GET','POST'])
def feedback():
    
    if request.method == 'POST':
        email= request.form['email']
        text= request.form['text']
        users_db = User.query.all()
        for user in users_db:
            if email == user.email and text == user.text:
                return redirect('/')
        
        #with open ("feedback.txt", 'a') as f:
            #f.write("email:" + email + "\n" + "text:" + text + "\n\n")

        #card = Card(email=email, text=text)

        #db.session.add(card)
        #db.session.commit()
        
        user = User(email=email, text=text)
        db.session.add(user)
        db.session.commit()
        return redirect('/index')
        
        


        

if __name__ == "__main__":
    app.run(debug=True)