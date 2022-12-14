from flask import  Flask ,request,jsonify
import mysql.connector as conn
app = Flask(__name__)
mydb = conn.connect(host = 'localhost',user='root',passwd='root') #to communicating to the pycharm and mysql system database
cursor = mydb.cursor()

@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get('mail_id')

    return "this is my first function for get {} {} {}".format(get_name ,mobile_number,mail_id )

#get the dabase and table
@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="root", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


if __name__=="__main__":
    app.run(port= 5002)

