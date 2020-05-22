from flask import Flask,render_template,request
import label_it
import os
import PIL
app=Flask(__name__)

##m=joblib.load('model.pkl')

@app.route('/')
def Hello():
    return render_template('index.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")



@app.route('/',methods=['POST'])
def classification():
    if request.method=='POST':
        f=request.files['userfile']
        path="./static/{}".format(f.filename)
        f.save(path)
        image=path
        target1=label_it.ans(path)
        ##target1=str(target[0][0])
    return render_template('index.html',my_target=target1,my_image=image)

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,port=port)
