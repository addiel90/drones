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
        
    def helper_register_medication(self,request_json):
        try:
            name_ex=r"(^[a-zA-Z0-9_-]+$)"
            code_ex=r"(^[A-Z0-9_]+$)"
            if "name" not in request_json or type(request_json["name"]) is not str or len(request_json["name"])==0:
                message = "The name field is required, it must be of type str and not be empty."
                return False,message      
            elif "weight" not in request_json or type(request_json["weight"]) is not int or request_json["weight"]==0:
                message = "The weight field is required, it must be of type int and not be empty."
                return False,message      
            elif "code" not in request_json or type(request_json["code"]) is not str or len(request_json["code"])==0:
                message = "The code field is required, it must be of type str and not be empty."
                return False,message      
            elif re.match(name_ex, request_json["name"]) is None:
                message = "In the field name allowed only letters, numbers, ‘-‘, ‘_’."
                return False,message      
            elif re.match(code_ex, request_json["code"]) is None:
                message = "In the field code allowed only upper case letters, underscore and numbers."
                return False,message       
            else:
                with self.mysql.cursor() as cursor:
                    sql = "SELECT * FROM medication WHERE code = '{}'".format(request_json["code"])
                    cursor.execute(sql)
                    response=cursor.fetchone()
                    if response == 0 or response is None:
                        sql = """INSERT INTO medication (name,weight,code) 
                        VALUES ('{0}',{1},'{2}')""".format(request_json["name"],request_json["weight"],
                                                                request_json["code"])
                        cursor.execute(sql)
                        self.mysql.commit()
                        self.mysql.close()
                        message="Registered medication."
                        return True,message
                    else:
                        message = "The medication with code '{}' exists in DB.".format(request_json["code"])
                        return False,message
        except Exception as e:
            message = "An exception occurred: {}".format(str(e))
            return False,message
        
    def helper_get_available_drones(self, request_json):
        try:         
            code_ex=r"(^[A-Z0-9_]+$)"
            if "medication_codes" not in request_json or type(request_json['medication_codes']) is not str or len(request_json['medication_codes']) in (0,2):
                message = "The medication_codes field is required, it must be of type str and not be empty."
                return {},message            
            code_list=list(json.loads(request_json['medication_codes']))
            for code in code_list:
                if type(code) is not str or len(code)==0:
                    message = "The code field is required, it must be of type str and not be empty. Value: '{}'".format(str(code))
                    return {},message
                elif re.match(code_ex, code) is None:
                    message = "The value '{}' allowed only upper case letters, underscore and numbers.".format(str(code))
                    return {},message
            code_tuple = tuple(code_list) 
            with self.mysql.cursor() as cursor:
                sql = """SELECT SUM(weight) FROM medication WHERE code in {}""".format(str(code_tuple))
                cursor.execute(sql)
                response=cursor.fetchone()
                if response is None or response == 0:                   
                    self.mysql.close()   
                    message = "The total weight of the load has not been completed."
                    return {},message
                else:
                    weight_total=int(response[0]) 
                    sql = """SELECT * FROM drone WHERE battery_capacity > 24 and weight_limit >= {} 
                    and state = 'LOADING'""".format(weight_total)
                    cursor.execute(sql)
                    response=cursor.fetchall()
                    drones=[]
                    if len(response)!=0:
                        for row in response:
                            drone = {"serial_number":row[0], "model":row[1],"weight_limit":row[2],"battery_capacity":row[3],"state":row[4]}
                            drones.append(drone) 
                        self.mysql.close()
                        drone = {"weight_load":weight_total, "available_drones":drones}
                        message = "Available drones for loading."
                        return drone,message
                    else:
                        message = "Drones not available for loading."
                        return {},message 
        except Exception as e:
            message = "An exception occurred: {}".format(str(e))
            return {},message