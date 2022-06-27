from flask import Flask, jsonify, request, make_response
from conf import conf
from MySQLConnection import get_conexion
from Helper import Helper

app = Flask(__name__)

@app.route("/drones", methods=['GET'])
def list_drones():
    try:
        conexion=get_conexion()
        _helper=Helper(conexion)
        drones,message=_helper.helper_list_drones()
        return make_response(jsonify({"drones":drones,"message":message}), 200)
    except Exception as e:
        return make_response(jsonify({"message":"An exception occurred: {}".format(str(e))}), 400)
    
@app.route("/drones/battery", methods=['GET'])
def get_battery_capacity():
    try:
        request_json=request.json
        conexion=get_conexion()
        _helper=Helper(conexion)
        drone,message=_helper.helper_get_battery_capacity(request_json)
        if len(drone)>0:
            return make_response(jsonify({"drone":drone,"message":message}), 200)
        else:
            return make_response(jsonify({"message":message}), 400) 
    except Exception as e:
        return make_response(jsonify({"message":"An exception occurred: {}".format(str(e))}), 400)
    
@app.route("/drones/<serial_number>", methods=['GET'])
def get_drone(serial_number):
    try:
        conexion=get_conexion()
        _helper=Helper(conexion)
        drone,message=_helper.helper_get_drone(serial_number) 
        if len(drone)>0:
            return make_response(jsonify({"drone":drone,"message":message}), 200)
        else:
            return make_response(jsonify({"message":message}), 400)   
    except Exception as e:
        return make_response(jsonify({"message":"An exception occurred: {}".format(str(e))}), 400)
    
@app.route("/drones", methods=['POST'])
def register_drone():
    try:
        request_json=request.json
        conexion=get_conexion()        
        _helper=Helper(conexion)  
        drone,message=_helper.helper_register_drone(request_json)      
        if drone:
            return make_response(jsonify({"message":message}), 200)
        else:
            return make_response(jsonify({"message":message}), 400) 
    except Exception as e:
        return make_response(jsonify({"message":"An exception occurred: {}".format(str(e))}), 400)
  
@app.route("/drones", methods=['DELETE'])
def delete_drone():
    try:
        request_json=request.json
        conexion=get_conexion()              
        _helper=Helper(conexion)  
        drone,message=_helper.helper_delete_drone(request_json)
        if drone:
            return make_response(jsonify({"message":message}), 200)
        else:
            return make_response(jsonify({"message":message}), 400)
    except Exception as e:
        return make_response(jsonify({"message":"An exception occurred: {}".format(str(e))}), 400)

@app.route("/drones/<serial_number>", methods=['PUT'])
def update_drone(serial_number):
    try:
        request_json=request.json
        conexion=get_conexion()             
        _helper=Helper(conexion) 
        drone,message=_helper.helper_update_drone(request_json,serial_number)
        if drone:
            return make_response(jsonify({"message":message}), 200)
        else:
            return make_response(jsonify({"message":message}), 400)
    except Exception as e:
        return make_response(jsonify({"message":"An exception occurred: {}".format(str(e))}), 400)
    
def page_not_found(error):
    return "<h1>The page you are trying to access does not exist...</h1>", 404

if __name__ == '__main__':
    app.config.from_object(conf["development"])
    app.register_error_handler(404, page_not_found)
    app.run()