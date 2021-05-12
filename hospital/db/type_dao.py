from db.mysql_db import pool

class TypeDao:
    #查询分类列表
    def search_list(self):
        def search_count_page(self):
            try:
                con = pool.get_connection()
                cursor = con.cursor()
                sql = "SELECT id,type FROM t_type"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(e)
            finally:
                if "con" in dir():
                    con.close()