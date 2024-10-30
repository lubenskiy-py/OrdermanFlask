from flask import Flask, render_template

pizzas = [
        {'name':'Пепероні', 'price':3.60, 'ingredients':'Тісто, томатний соус, сир моцарела, ковбаса пепероні, орегано'},
        {'name':'Моцарела', 'price':3.10, 'ingredients':'Тісто, томатний соус, сир моцарела, базилік'},
        {'name':'Чотири сира', 'price':3.80, 'ingredients':'Тісто, томатний соус, сир моцарела, сир пармезан, сир горгонзола, сир емменталь'}
]

app = Flask('__name__')

@app.route("/homepage.html")
def homepage():
    return render_template("homepage.html", title='Orderman')

@app.route("/menu.html")
def menu():
    context = {
        'title':'Меню',
        'pizzas':pizzas,
    }
    return render_template("menu.html", **context)

if __name__ == '__main__':
    app.run(debug=True) 