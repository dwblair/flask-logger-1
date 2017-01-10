from flask import Flask
from flask import request

app = Flask(__name__)

publickey='222'
privatekey='333'

@app.route('/')
def index():
    return "Flask logger!"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/log')
def data():
   
    argdict = request.args.to_dict()
   
    pub=argdict['publickey']
    priv=argdict['privatekey']

    if priv==privatekey and pub==publickey:

	    alpha_dict = sorted(argdict.items())

	    line = ""
	    for key,value in alpha_dict:
		if key!='publickey' and key!='privatekey':
		    print key,value
		    line=line+str(value)+","

	    #drop the last comma and add a return char
	    line = line[:-1]+"\n"

	    print line

	    filename=pub+"_log.csv"
            with open(filename,"a") as fo:
	        fo.write(line)

	    return "Success"
    else:
	return "Fail"

if __name__ == "__main__":
    app.run()
