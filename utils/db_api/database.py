import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        # check_same_thread=False allows using the connection across different threads
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_users_table()
        self.create_orders_table()
        self.create_order_replies_table()

    def create_users_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER,
                line TEXT,
                phone_number TEXT,
                time TEXT,
                members TEXT
            )
        """)
        self.conn.commit()

    def create_pochta_table(self):
        self.cursor.execute("""
        CREATE TABLE IF  NOT EXISTS pochta(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            line TEXT,
            phone_number TEXT,
            information TEXT
        )
        """)
        self.conn.commit()

    def create_orders_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id TEXT UNIQUE,
                telegram_id INTEGER,
                line TEXT,
                phone_number TEXT,
                members TEXT,
                group_message_id INTEGER,
                replied_user_id INTEGER
            )
        """)
        self.conn.commit()

    def create_order_replies_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_replies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id TEXT,
                reply_message_id INTEGER,
                reply_type TEXT,
                reply_content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def save_reply(self, order_id, reply_message_id, reply_type, reply_content):
        self.cursor.execute("""
            INSERT INTO order_replies (order_id, reply_message_id, reply_type, reply_content)
            VALUES (?, ?, ?, ?)
        """, (order_id, reply_message_id, reply_type, reply_content))
        self.conn.commit()

    def append_user(self, data):
        user_id = data.get("user_id")
        line = data.get("line")
        phone_number = data.get("phone_number")
        time = data.get("time")
        members = data.get("members")

        try:
            self.cursor.execute("""
                INSERT INTO users (telegram_id, line, time, phone_number, members)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, line, time, phone_number, members))
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def append_pochta(self, data):
        user_id = data.get("user_id")
        line = data.get("line")
        phone_number = data.get("phone_number")
        info = data.get("information")

        try:
            self.cursor.execute("""
               INSERT INTO pochta (telegram_id, line, phone_number, information)
               VALUES (?, ?, ?, ?)
               """, (user_id, line, phone_number, info))
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def append_order(self, order_id, data, group_message_id):
        try:
            self.cursor.execute("""
                INSERT INTO orders (order_id, telegram_id, line, phone_number, members, group_message_id, replied_user_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (order_id, data.get("user_id"), data.get("line"), data.get("phone_number"), data.get("members"),
                  group_message_id, None))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_order(self, order_id):
        self.cursor.execute("""
            SELECT line, phone_number, members, replied_user_id FROM orders WHERE order_id = ?
        """, (order_id,))
        row = self.cursor.fetchone()
        if row:
            return {
                "line": row[0],
                "phone_number": row[1],
                "members": row[2],
                "replied_user_id": row[3]
            }
        return None

    def set_replied_user(self, order_id, user_id):
        self.cursor.execute("""
            UPDATE orders SET replied_user_id = ? WHERE order_id = ?
        """, (user_id, order_id))
        self.conn.commit()

    def get_user(self, telegram_id):
        self.cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return self.cursor.fetchone()

    def delete_all_users(self):
        self.cursor.execute("DELETE FROM users")
        self.conn.commit()

    def delete_table(self):
        self.cursor.execute("DROP TABLE users")
        self.conn.commit()
