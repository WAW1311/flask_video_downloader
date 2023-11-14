from flask import Flask, render_template, request, redirect,url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/youtube',methods=['GET','POST'])
def youtube():
	if request.method == "POST":
		link = request.form['url']
		api = f"https://api.ibeng.tech/api/downloader/youtube-video?apikey=vpUslpPCwv&url={link}"
		get_data = requests.get(api)

		get_data_json = get_data.text
		data = json.loads(get_data_json)
		judul = data['data']['title']
		thumb = data['data']['thumb']
		download = data['data']['url']
		return render_template('youtube.html',judul=judul,thumb=thumb,download=download)
	else:
		return render_template('youtube.html')

@app.route('/facebook',methods=['GET','POST'])
def facebook():
	if request.method == "POST":
		link = request.form['url']
		api = f"https://api.ibeng.tech/api/downloader/facebook?apikey=vpUslpPCwv&url={link}"
		get_data = requests.get(api)

		get_data_json = get_data.text
		data = json.loads(get_data_json)
		judul = data['data']['title']
		hd = data['data']['isHdAvailable']
		if hd == True:
			download = data['data']['urls'][0]['hd']
			return render_template('facebook.html',judul=judul,download=download)
		else:
			download = data['data']['urls'][1]['sd']
			return render_template('facebook.html',judul=judul,download=download)
	else:
		return render_template('facebook.html')

@app.route('/instagram',methods=['GET','POST'])
def instagram():
	if request.method == "POST":
		link = request.form['url']
		api = f"https://api.ibeng.tech/api/downloader/instagram?apikey=vpUslpPCwv&url={link}"
		get_data = requests.get(api)
		get_data_json = get_data.text
		data = json.loads(get_data_json)
		thumb = data['data'][0]['thumbnail']
		download = data['data'][0]['url']
		return render_template('instagram.html',thumb=thumb,download=download)
	else:
		return render_template('instagram.html')

@app.route('/tiktok',methods=['GET','POST'])
def tiktok():
	if request.method == "POST":
		link = request.form['url']
		api = f"https://api.ibeng.tech/api/downloader/tiktok?apikey=vpUslpPCwv&url={link}"
		get_data = requests.get(api)
		get_data_json = get_data.text
		data = json.loads(get_data_json)
		judul = data['data']['unique_id']
		deskripsi = data['data']['description']
		durasi = data['data']['duration']
		download = data['data']['play']
		return render_template('tiktok.html',judul=judul,deskripsi=deskripsi,durasi=durasi,download=download)
	else:
		return render_template('tiktok.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)