import os
import re
import shutil
import flask 
import flask_restful
from gtts import gTTS

app = flask.Flask(__name__, static_url_path='/static')
api = flask_restful.Api(app)

class HelloWorld(flask_restful.Resource):

    def post(self):
        json_data = flask.request.form
        id = json_data['id']
        judul = json_data['judul']
        deskripsi = json_data['deskripsi']
        CLEANR = re.compile('<.*?>')
        deskripsi = re.sub(CLEANR, '', deskripsi)
        deskripsi = deskripsi.translate ({ord(c): " " for c in "’!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        deskripsi = deskripsi.replace("rsquo","")
        deskripsi = deskripsi.replace("nbsp","")
        jenis = json_data['jenis']

        if jenis == 'meher':
            filename = "meher-"+id+".mp3"
        elif jenis == 'woirata':
            filename = "woirata-"+id+".mp3"
        else:
            filename = "file-"+id+".mp3"

        pathFilename = 'static/'+filename
        hasil = os.path.isfile(pathFilename)

        if hasil :
            file = os.path.join("/static", filename)
        else:
            mytext = judul+" "+deskripsi

            # findBs = re.search("\Ɗ", mytext)
            # findBs2 = re.search("\đ", mytext)
            # if findBs != None or findBs2 != None : 
            #     language = 'bs'
            # else:
            #     language = 'id'
            language = 'id'

            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save(filename)

            shutil.move(filename, "static/"+filename)

            file = os.path.join("/static", filename)

        return flask.jsonify(file=file,deskripsi=deskripsi)

api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5050)