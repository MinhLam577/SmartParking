from models.db import Database
class User:
    def __init__(self):
        self.db = Database()

    def get_users(self):
        db, cursor = self.db.get_connection()
        cursor.execute("SELECT * FROM user")
        users = cursor.fetchall()

        # Chuyển đổi kết quả từ tuple sang dictionary
        users_list = []
        for user in users:
            user_dict = {
                'id': user[0],
                'name': user[1],
                # Thêm các trường dữ liệu khác tùy thuộc vào cấu trúc bảng user của bạn
            }
            users_list.append(user_dict)
        return users_list
    def create_user(self,gmail,password,role):
        db, cursor = self.db.get_connection()
        cursor.execute("INSERT INTO user (gmail,password,role) VALUES (%s ,%s,%s)",(gmail,password,role))
        db.commit()

    def check_user_existence(self, gmail):
        db, cursor = self.db.get_connection()
        cursor.execute("SELECT * FROM user WHERE gmail = %s ", (gmail,))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False
    def signup(self,gmail,password):
        db, cursor = self.db.get_connection()
        sql = "SELECT gmail, role  FROM user WHERE gmail = %s AND password = %s"
        val = (gmail, password)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
