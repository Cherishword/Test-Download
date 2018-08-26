from flask import Flask,render_template,Response
#import re
#os.environ['NLS_LANG'] = ".AL32UTF8"

app = Flask(__name__)

@app.route("/demo", methods=['POST','GET'])
def demo():
    return render_template('demo.html')

@app.route("/getcsv")
def getcsv():
    table='a,b,c,\n1,2,3,\n4,5,6'
#    data=pd.DataFrame(table)
#    csv = re.sub(' +',',',data.to_string().strip())
    return Response("\ufeff"+table,mimetype="text/csv",headers={"Content-disposition":"attachment; filename=getcsv.csv"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9875)
