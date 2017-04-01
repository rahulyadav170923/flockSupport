from flask import Flask, json,jsonify,render_template
app = Flask(__name__)
from flask import request
import pprint

@app.route("/",methods=['GET','POST'])
def install():
    return render_template('home.html')

@app.route('/freshdesk_webhook',methods=['POST','GET'])
def freshdesk_webhook():
    content = request.get_json(silent=True)

    # my_json =  json.dumps(content, indent=4, sort_keys=True)
    data = content['data']
    data = data['item']
    data = data['conversation_parts']
    data = data['conversation_parts']
    data = data[0]
    
    body = data['body']
    attachment_link = None
    attachment_name = None
    try:
    	attachment = data['attachments']
    	attachment = attachment[0]
    	attachment_name = attachment['name']
    	attachment_link = attachment['url']
    except:
    	pass

    print body
    print attachment_name
    print attachment_link

    return "done"

if __name__ == "__main__":
    app.run(debug=True)
