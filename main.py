from flask import Flask, render_template, request, redirect, url_for #Частичный вызов компенентов из библиотеки

app = Flask (__name__) #Объявление экземпляра класса

@app.route('/') #Указание маршрута
def home(): #Объявление названия функции
    return redirect(url_for('form1')) #

@app.route ('/form1', methods = ['GET', 'POST']) #Указание маршрута для формы 1 с ограничением методов с этой формой
def form1(): # Объявление названия функции 
    if request.method == 'POST': 
        name = request.form('name')
        return redirect(url_for('form2', name=name))
    return render_template('form1.html') #Сборка и возвращение шаблона

@app.route ('/form1', methods = ['GET', 'POST']) #Указание маршрута
def form2():
    if request.method == 'POST':
        age = request.form('age')
        name = request.args.get('name')
        return f'Привет, {name}. Твой возраст {age} год.'
    return render_template('form2.html')
    
    if __name__ == '__main__':
        app.run (debug = True)