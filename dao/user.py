class UserDAO:
    def __init__(self):
        super().__init__()

    # user = id, firstname, lastname, email, phone, date_birth, address, city, zipcode, country

    def getAllUsers(self):
        result = [
            [1, "Alex", "Smith", "asmith@gm.or", "7877778888", "02/04/1985", "Barrio El Campo", "Arecibo", "00630", "PR"],
            [1, "Minerva", "Martinez", "mmartinez@gm.or", "7877779999", "02/19/1990", "Barrio Girasoles", "Barceloneta", "00617", "PR"]
        ]
        return result 
    
    def getUserById(self, user_id):
        result = [1, "Alex", "Smith", "asmith@gm.or", "7877778888", "02/04/1985", "Barrio El Campo", "Arecibo", "00630", "PR"]
        return result

    def insert(self, ufirstname, ulastname, uemail, uphone, udate_birth, uaddress, ucity, uzipcode, ucountry):
        uid = 1
        return uid

    def update(self, uid, ufirstname, ulastname, uemail, uphone, udate_birth, uaddress, ucity, uzipcode, ucountry):
        return uid

    def delete(self, uid):
        return uid