from config import get_db_connection

class UserController:
    @staticmethod
    def get_users():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users

    @staticmethod
    def add_user(first_name, last_name, email, phone):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO users (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)',
            (first_name, last_name, email, phone)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM users WHERE id = %s', (user_id,))
        conn.commit()
        cur.close()
        conn.close()