from flask import Flask, render_template,request
import AlphaBot 


app=Flask(__name__)
robot=AlphaBot()
robot.stop()

@app.route("/",methods=["GET","POST"])

def index():
    if request.method=="POST":
        if "Avanti" in request.form:
            robot.forward()
        elif "Indietro" in request.form:
            robot.backward()
        elif "Destra" in request.form:
            robot.right()
        elif "Sinistra" in request.form:
            robot.left()
        elif "Stop" in request.form:
            robot.stop()
    elif request.method=="GET":
        return render_template("index.html")
    
    

app.run(debug=True, host="0.0.0.0")