from flask import jsonify, request, make_response
import re
import json


class Helper:

    def __init__(self, provider):
        self.mysql = provider
        
    def helper_list_drones(self):
        try:
            response=[]
            with self.mysql.cursor() as cursor:
                sql = "SELECT serial_number,model,weight_limit,battery_capacity,state FROM drone"
                cursor.execute(sql)
                response=cursor.fetchall()            
                self.mysql.close()
            drones=[]
            for row in response:
                drone = {"serial_number":row[0], "model":row[1],"weight_limit":row[2],"battery_capacity":row[3],"state":row[4]}
                drones.append(drone)  
            message = "Drone listings."         
            return drones,message
        except Exception as e:
            message="An exception occurred: {}".format(str(e))
            return {},message
        
    def helper_get_battery_capacity(self, request_json):
        try:
            if "serial_number" not in request_json or type(request_json["serial_number"]) is not str or len(request_json["serial_number"])>100:
                message = "The serial_number field is required, it must be of type str and have a maximum of 100 characters."
                return {},message     
            else:
                with self.mysql.cursor() as cursor:
                    sql = """SELECT battery_capacity FROM drone
                    WHERE serial_number = '{}'""".format(request_json["serial_number"])
                    cursor.execute(sql)
                    response=cursor.fetchone()
                    if response is None or response == 0:                   
                        self.mysql.close()   
                        message = "Drone not found."
                        return {},message
                    else:   
                        self.mysql.close()
                        drone = {"battery_capacity":response[0]}
                        message = "Drone battery capacity."
                        return drone,message
        except Exception as e:
            message = "An exception occurred: {}".format(str(e))
            return {},message  
        
    def helper_get_drone(self, serial_number):
        try:
            response=[]
            with self.mysql.cursor() as cursor:
                sql = """SELECT serial_number,model,weight_limit,battery_capacity,state 
                FROM drone where serial_number = '{}'""".format(serial_number)
                cursor.execute(sql)
                response=cursor.fetchone() 
                if response != None:
                    drone = {"serial_number":response[0], "model":response[1],"weight_limit":response[2],"battery_capacity":response[3],"state":response[4]}
                    self.mysql.close()
                    message="Drone found."
                    return drone,message
                else:  
                    self.mysql.close()
                    message="Drone not found."
                    return {},message
        except Exception as e:
            message = "An exception occurred: {}".format(str(e))
            return {},message  