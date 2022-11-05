import numpy as np


model=pickle.load(open('model.pkl','rb'))
app=Flask(_name_)
@app.route('/')
def home():
    return "Hello world"
@app.route('/predict',methods=['POST'])
def predict():
    X=int(request.form.get('X'))
    Y=int(request.form.get('Y'))
    Z=int(request.form.get('Z'))
    g_force=int(request.form.get('g_force'))


    input_query = np.array([['X','Y','Z','g_force']])
    result=model.predict(input_query)[0]
    return jsonify(int(result))

if _name=='__main_':
    app.run(debug=True)