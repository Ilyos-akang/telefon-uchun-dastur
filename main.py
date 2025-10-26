from flask import Flask,render_template,request
from  flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
db=SQLAlchemy(app)




class Telefon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    tel_nom=db.Column(db.String(100),nullable=True)
    yil=db.Column(db.Integer,nullable=True)
    xotira=db.Column(db.Integer,nullable=True)
    rang=db.Column(db.String(100),nullable=True)
    malumot=db.Column(db.String(100),nullable=True)
    narxi=db.Column(db.Integer,nullable=True)

    def __repr__(self):
        return f"telefon malumotlari nomi:{self.tel_nom} narxi: {self.narxi} , rangi {self.rang}, ishlab chiqarilgan yili {self.yil} holati {self.malumot} xotirasi {self.xotira} "


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/index_telefon",methods=["GET","POST"])
def index():
    if request.method=="POST":
        tel_nom=request.form.get("tel_nom")
        yil=request.form.get("yil")
        xotira=request.form.get("xotira")
        rang=request.form.get("rang")
        malumot=request.form.get("malumot")
        narxi=request.form.get("narxi")

        tel=Telefon(tel_nom=tel_nom,
                    yil=yil,
                    xotira=xotira,
                    rang=rang,
                    malumot=malumot,
                    narxi=narxi)

        db.session.add(tel)
        db.session.commit()
    return render_template ("index_telefon.html")




@app.route("/kom")
def  kom():
    return render_template ("index_kom.html")



if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(debug=True)


"""from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"

db=SQLAlchemy(app)

@app.route("/")
def index():
    return render_template ("index.html")



if __name__=="__main__":
    app.run(debug=True)
"""