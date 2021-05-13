from flask import Flask,request


app=Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        print(request.method)
    else:
         print(request.method)

if __name__=='__main__':
    app.run()