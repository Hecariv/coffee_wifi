from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

coffee_list = ["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
wifi_list = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
power_list = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[URL(message="wrong URL"), DataRequired()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=coffee_list, validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=wifi_list, validators=[DataRequired()])
    power = SelectField('Power', choices=power_list, validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('C:\\Users\\Hector Castaneda\\OneDrive\\Documentos\\Projekte\\udemy\\python\\flask\\coffee-and-wifi\\cafe-data.csv', mode="a", encoding="utf8") as csv_file:
            csv_file.write("\n")
            csv_file.write(form.cafe.data + ",")
            csv_file.write(form.location.data + ",")
            csv_file.write(form.open.data + ",")
            csv_file.write(form.close.data + ",")
            csv_file.write(form.coffee.data + ",")
            csv_file.write(form.wifi.data + ",")
            csv_file.write(form.power.data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('C:\\Users\\Hector Castaneda\\OneDrive\\Documentos\\Projekte\\udemy\\python\\flask\\coffee-and-wifi\\cafe-data.csv', encoding="utf8", newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
