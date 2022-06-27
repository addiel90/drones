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