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
        
    def helper_register_drone(self,request_json):
        try:
            if "serial_number" not in request_json or type(request_json["serial_number"]) is not str or len(request_json["serial_number"])>100:
                message = "The serial_number field is required, it must be of type str and have a maximum of 100 characters."
                return False,message      
            elif "weight_limit" not in request_json or type(request_json["weight_limit"]) is not int or request_json["weight_limit"]>500:
                message = "The weight_limit field is required, it must be of type int and should be a maximum of 500 gr."
                return False,message      
            elif "model" not in request_json or type(request_json["model"]) is not str or len(request_json["model"])>50:
                message = "The model field is required, it must be of type str and have a maximum of 50 characters."
                return False,message      
            elif "battery_capacity" not in request_json or type(request_json["battery_capacity"]) is not int or request_json["battery_capacity"]>100:
                message = "The battery_capacity field is required, it must be of type int and have a maximum of 100 %."
                return False,message      
            elif "state" not in request_json or type(request_json["state"]) is not str:
                message = "The state field is required and it must be of type str."
                return False,message      
            else:
                with self.mysql.cursor() as cursor:
                    sql = "SELECT * FROM drone WHERE serial_number = '{}'".format(request_json["serial_number"])
                    cursor.execute(sql)
                    response=cursor.fetchone()
                    if response == 0 or response is None:
                        sql = """INSERT INTO drone (serial_number,model,weight_limit,battery_capacity,state) 
                        VALUES ('{0}','{1}',{2},{3},'{4}')""".format(request_json["serial_number"],request_json["model"],
                                                                request_json["weight_limit"],request_json["battery_capacity"],
                                                                request_json["state"].upper())
                        cursor.execute(sql)
                        self.mysql.commit()
                        self.mysql.close()
                        message="Registered drone."
                        return True,message
                    else:
                        message = "The drone with serial_number '{}' exists in DB.".format(request_json["serial_number"])
                        return False,message
        except Exception as e:
            message = "An exception occurred: {}".format(str(e))
            return False,message
        
    def helper_delete_drone(self,request_json):
        try:
            if "serial_number" not in request_json or type(request_json["serial_number"]) is not str or len(request_json["serial_number"])>100:
                message = "The serial_number field is required, it must be of type str and have a maximum of 100 characters."
                return False,message                   
            else:
                with self.mysql.cursor() as cursor:
                    sql = "DELETE FROM drone WHERE serial_number = '{}'".format(request_json["serial_number"])
                    cursor.execute(sql)
                    response=cursor.rowcount
                    if response == 0:                    
                        self.mysql.close()
                        message = "The drone with serial_number '{}' does not exist.".format(request_json["serial_number"])
                        return False,message
                    else:                    
                        self.mysql.commit()
                        self.mysql.close()
                        message = "The drone has been removed."
                        return True,message
        except Exception as e:
            message = "An exception occurred: {}".format(str(e))
            return False,message  
    
    def helper_update_drone(self,request_json,serial_number):
        try:
            if "model" not in request_json or "weight_limit" not in request_json or "battery_capacity" not in request_json or "state" not in request_json:
                message = "All fields are required to update."
                return False,message     
            elif "model" in request_json and type(request_json["model"]) is not str:
                message = "The model field must be of type str."
                return False,message      
            elif "weight_limit" in request_json and type(request_json["weight_limit"]) is not int:
                message = "The weight_limit field must be of type int."
                return False,message      
            elif "battery_capacity" in request_json and type(request_json["battery_capacity"]) is not int:
                message = "The battery_capacity field must be of type int."
                return False,message      
            elif "state" in request_json and type(request_json["state"]) is not str:
                message = "The battery_capacity field must be of type str."
                return False,message      
            else:
                with self.mysql.cursor() as cursor:
                    sql = """UPDATE drone SET model = '{0}',weight_limit = {1},battery_capacity = {2},state = '{3}' 
                    WHERE serial_number = '{4}'""".format(request_json["model"],request_json["weight_limit"],
                                                        request_json["battery_capacity"],request_json["state"],serial_number)
                    cursor.execute(sql)
                    response=cursor.rowcount
                    if response is None or response == 0:                   
                        self.mysql.close()   
                        message = "Drone not found or has already been updated."
                        return False,message 
                    else:   
                        self.mysql.commit()
                        self.mysql.close()
                        message = "The drone has been upgraded."
                        return True,message
        except Exception as e:
            message = "An exception occurred: {}".format(str(e))
            return False,message
        