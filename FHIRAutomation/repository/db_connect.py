import os
import psycopg2
from dotenv import load_dotenv

class DBConnect:
    def __init__(self):
        load_dotenv()

    async def get_required_fields(self):
        try:
            connection = psycopg2.connect(
            host=os.environ["DB_HOST"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            port=int(os.environ["DB_PORT"]),
            database=os.environ["DB_NAME"]
            )

            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM CAREPLANFIELDS WHERE STATUS='ACTIVE'")
            rows = cursor.fetchall()

            required_fields = [name for id,name,status in rows]
            return required_fields

        except Exception as error:
            print(f"Error - {error}")
        finally:
            connection.close()