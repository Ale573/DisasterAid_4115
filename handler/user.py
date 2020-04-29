from flask import jsonify
from dao.user import UserDAO

class UserHandler: 

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ufirstname'] = row[1]
        result['ulastname'] = row[2]
        result['uemail'] = row[3]
        result['uphone'] = row[4]
        result['udate_birth'] = row[5]
        result['uaddress'] = row[6]
        result['ucity'] = row[7]
        result['uzipcode'] = row[8]
        result['ucountry'] = row[9]
        return result

    def build_user_attributes(self, uid, ufirstname, ulastname, uemail, uphone, udate_birth, uaddress, ucity, uzipcode, ucountry):
        result = {}
        result['uid'] = uid
        result['ufirstname'] = ufirstname
        result['ulastname'] = ulastname
        result['uemail'] = uemail
        result['uphone'] = uphone
        result['udate_birth'] = udate_birth
        result['uaddress'] = uaddress
        result['ucity'] = ucity
        result['uzipcode'] = uzipcode
        result['ucountry'] = ucountry
        return result 

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        result_list = []
        for row in result:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)

    def getUserById(self, uid):
        dao = UserDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)

    def insertUser(self, json):
        ufirstname = json['ufirstname']
        ulastname = json['ulastname']
        uemail = json['uemail']
        uphone = json['uphone']
        udate_birth = json['udate_birth']
        uaddress = json['uaddress']
        ucity = json['ucity']
        uzipcode = json['uzipcode']
        ucountry = json['ucountry']

        if ufirstname and ulastname and uemail and uphone and udate_birth and uaddress and ucity and uzipcode and ucountry:
            dao = UserDAO()
            uid = dao.insert(ufirstname, ulastname, uemail, uphone, udate_birth, uaddress, ucity, uzipcode, ucountry)
            result = self.build_user_attributes(uid, ufirstname, ulastname, uemail, uphone, udate_birth, uaddress, ucity, uzipcode, ucountry)
            return jsonify(User = result), 201

    def updateUser(self, uid, json):
        dao = UserDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User not found."), 404
        else:
            ufirstname = json['ufirstname']
            ulastname = json['ulastname']
            uemail = json['uemail']
            uphone = json['uphone']
            udate_birth = json['udate_birth']
            uaddress = json['uaddress']
            ucity = json['ucity']
            uzipcode = json['uzipcode']
            ucountry = json['ucountry']

            if ufirstname and ulastname and uemail and uphone and udate_birth and uaddress and ucity and uzipcode and ucountry:
                dao = UserDAO()
                dao.update(uid, ufirstname, ulastname, uemail, uphone, udate_birth, uaddress, ucity, uzipcode, ucountry)
                result = self.build_user_attributes(uid, ufirstname, ulastname, uemail, uphone, udate_birth, uaddress, ucity, uzipcode, ucountry)
                return jsonify(User = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteUser(self, uid):
        dao = UserDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User not found."), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus = "OK"), 200