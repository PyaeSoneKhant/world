from flask import Flask, render_template, request
import json

w = json.load(open("worldl.json"))
for c in w:
	c['tld'] = c['tld'][1:]
page_size = 20
app = Flask(__name__)

@app.route('/')
def mainPage():
	return render_template('index.html',
		page_number = 0,
		page_size = page_size,
		w = w[0:page_size])

@app.route('/begin/<b>')
def beginPage(b):
	try:
		if int(b)>=0 and int(b)<=180:
			bn = int(b)
		return render_template('index.html',
		w = w[bn:bn+page_size],
		page_number = bn,
		page_size = page_size
		)
	except:
		return "error"

@app.route('/continent/<a>')
def continentPage(a):
	cl = [c for c in w if c['continent']==a]
	return render_template(
		'continent.html',
		length_of_cl = len(cl),
		cl = cl,
		a = a
		)

@app.route('/startingWith/<a>')
def firstLetterPage(a):
	cl = [c for c in w if c['name'][0]==a]
	return render_template(
		'continent.html',
		length_of_cl = len(cl),
		cl = cl,
		a = a
		)

@app.route('/country/<i>')
def countryPage(i):
	return render_template(
		'country.html',
		c = w[int(i)])

@app.route('/countryByName/<n>')
def countryByNamePage(n):
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	return render_template(
		'country.html',
		c = c)

@app.route('/delete/<n>')
def deleteCountry(n):
	i = 0
	for c in w:
	   if c['name'] == n:
	      break
	   i = i+1
	del w[i]
	return render_template('index.html',
		page_number = 0,
		page_size = page_size,
		w = w[0:page_size])

@app.route('/editCountryByName/<n>')
def editCountryByNamePage(n):
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	return render_template(
		'country_edit.html',
		c = c)

@app.route('/addCountryByName/')
def AddCountryByNamePage():
	c=None
	return render_template(
   	'country_add.html',
    c=c
    )

@app.route('/AddCountry/')
def addCountryByNamePage():
  c=None
  for x in w:	
  		c=x 
  		c['name']=request.args.get('name')
  		c['capital']=request.args.get('capital')
  		c['continent']=request.args.get('continent')
  		c['tld']=request.args.get('tld')
  		c['population']=request.args.get('population')
  		c['area']=request.args.get('area')
  		c['gdp']=request.args.get('gdp')
  		c['flag']=request.args.get('flag')
  		break
  		w.append(c)
  		return render_template(
  		'country_added.html',
  		c=c,
  		)
@app.route('/updateCountryByName')
def updateCountryByNamePage():
	n = request.args.get('name')
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	c['capital'] = request.args.get('capital')
	c['continent'] = request.args.get('continent')
	return render_template(
		'country.html',
		c = c)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=1999, debug=True)






