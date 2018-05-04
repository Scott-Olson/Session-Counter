from flask import Flask, render_template, request, redirect, session
import math

app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def counter():
	if 'count' not in session:
		session['count'] = 0
	session['count'] = session['count'] + 1
	return render_template('index.html', count = session['count'])

@app.route('/addTwo')
def addTwo():
	session['count'] += 1
	return redirect('/')

@app.route('/reset')
def resetCounter():
	print('test')
	session.clear()
	return redirect('/')

app.run(debug=True)


