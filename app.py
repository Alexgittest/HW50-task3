#!/app/venv/bin/python

from flask import Flask,request
import json
from datetime import date

today = date.today()
app=Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    with open("./birthdays.txt",'r') as filename:
        birthday_list=filename.read()
        data=json.loads(birthday_list)
    if request.method == 'POST':
        user=request.form['username']
        dr=request.form['dr']
        with open("./birthdays.txt",'w') as filename:
            data[user]=dr
            filename.write(json.dumps(data))
        return "Add new user \n"
    else:       
        return "Hello it is flask app \n"

@app.route("/<username>")
def show_user_birthday(username):
    with open("./birthdays.txt",'r') as filename:
        birthday_list=filename.read()
        data=json.loads(birthday_list)
        birthday="Совпадений не найдено \n"   
        for i in data.keys():
            if i == username:
                birthday=data[i].split(".")
                dr=date(today.year,int(birthday[1]),int(birthday[0]))
                delta=(today-dr).days
                if 0<delta<3:
                    birthday="ДР было меньше чем 3 дня назад \n"
                elif -3<delta<0:
                    birthday="ДР будет через меньше чем через 3 дня \n"
                elif delta==0:
                    birthday="ДР Сегодня! \n"
                else:
                    birthday="ДР еще не скоро \n"
    return birthday


if __name__=="__main__":
    app.run(port=5000, host='0.0.0.0')
