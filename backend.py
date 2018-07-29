from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import json



app = Flask(__name__)
app.debug = True

def getflavor():
        userid = "admin"
        password = "qwerty"
        namaproject = "demo"
        url = 'http://192.168.8.110/identity/v3/auth/tokens'
        headers = {'content-type': 'application/json'}
        payload = { "auth": {"identity": {"methods": ["password"],"password": {"user": {"name": userid,"domain": { "id": "default" },"password":password}}},"scope": {"project": {"name": namaproject,"domain": { "id": "default" }}}}}    
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print r.headers.get('X-Subject-Token')
        #print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
        json_data = r.json()
        r.close()
        tokens = r.headers.get('X-Subject-Token')
        url = 'http://192.168.8.110/compute/v2.1/flavors/detail'
        headers = {'X-Auth-Token':str(tokens)}
        r = requests.get(url, headers=headers)
        json_data = r.json()
        print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
        r.close()
        return render_template(json_data = json_data)

@app.route('/')
def create():

        userid = "admin"
        password = "qwerty"
        namaproject = "demo"
        url = 'http://192.168.8.110/identity/v3/auth/tokens'
        headers = {'content-type': 'application/json'}
        payload = { "auth": {"identity": {"methods": ["password"],"password": {"user": {"name": userid,"domain": { "id": "default" },"password":password}}},"scope": {"project": {"name": namaproject,"domain": { "id": "default" }}}}}    
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print r.headers.get('X-Subject-Token')
        #print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
        json_data = r.json()
        r.close()
        tokens = r.headers.get('X-Subject-Token')
        url = 'http://192.168.8.110/compute/v2.1/servers'
        #print tokens
        #tokenid = token['audit_ids']['token']['id']
        #print tokenid
        name = 'surya wibawa'
        flavor = '2'
        image = '6537791c-4cd5-44ba-90c0-d96f4e63d1a6'
        adminPass = 'qwerty'
        keyname = 'secret'
        url = 'http://192.168.8.110/compute/v2.1/servers'
        headers = {'content-type': 'application/json','X-Auth-Token':str(tokens)}
        payloads = {'server':{'name': name, 'flavorRef':flavor, 'imageRef':image, 'adminPass':adminPass, 'key_name':keyname}}
        create = requests.post(url, data=json.dumps(payloads), headers=headers)
        json_data = create.json()
        print json.dumps(create.json(), sort_keys=True, indent=4, separators=(',', ': '))
        json_data = create.json()
        create.close()
        json_data = create.json()
        create.close()
        # headers = {'X-Auth-Token':str(tokens)}
        # r = requests.get(url, headers=headers)
        # json_data = r.json()
        # print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
        # json_data = r.json()
        # r.close()
        return render_template('coba.html', json_data = json_data)




if __name__ == "__main__":
    app.run()
