from  flask  import Flask,request,jsonify,render_template
# the app func
app = Flask(__name__)
# importing function for the calculation and operations
from  operations import add,sub,mult,div


@app.route('/')
def home():
  return   render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
  a = request.form['a']
  b = request.form['b']
  operation =  str(request.form['operation'])
  if operation == "add":
    result = add(a,b)
  elif operation == "subtract":
    result  =  sub(a,b)
  elif operation == "multiply":
    result  =  mult(a,b)
  elif operation ==  "divide":
    result  = div(a,b)

  return render_template ('index.html',prediction_text = str(result)  )

if  __name__ == "__main__":
  app.run(debug=True)