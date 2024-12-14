from flask import jsonify , Flask , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/AppData'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class AppDetails(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    device_id = db.Column(db.String(100), nullable = False)
    device_model = db.Column(db.String(100),nullable = False)
    version = db.Column(db.String(100),nullable = False)
    manufacturer = db.Column(db.String(500),nullable = False)
with app.app_context():
    db.create_all()

@app.route('/getApp/<int:id>',methods=['GET'])
def get_app(id):
    app_details = AppDetails.query.get(id)
    if not app_details:
        return jsonify({"Error": "App is not present"}),404
    else:
        return jsonify({
            "id" : app_details.id,
            "device_id" : app_details.device_id,
            "App Name" : app_details.app_name,
            "Version" : app_details.version,
            "Description" : app_details.description
        }),201
    
@app.route("/postApp" , methods =['POST'])
def post_app():
    data = request.get_json()
    if not data:
        return jsonify({"Error" : "Missing Values"}),400
    
    myApp = AppDetails(
        device_id = data['device_id'],
        device_model = data['device_model'],
        version =data['os_version'],
        manufacturer = data.get('device_manufacturer', '')
    )
    db.session.add(myApp)
    db.session.commit()
    return jsonify({"Message" : "App created successfully", "app_id" : myApp.id}),201

@app.route("/deleteApp/<int:id>" , methods=['DELETE'])
def del_app(id):
    data = AppDetails.query.get(id)
    if not data:
        return jsonify({"Error" : "App not found"}),404
    else:
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message": "App deleted successfully!"})
    
if __name__== "__main__":
    app.run(debug=True)
