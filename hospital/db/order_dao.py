from db.mysql_db import pool
class OrderDao:
    #需就诊人
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM t_order n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.patient_id=u.id " \
                  "WHERE n.state=%s " \
                  "ORDER BY n.create_time ASC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ("预约成功", (page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #预约成功
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_order WHERE state=%s"
            cursor.execute(sql, ["预约成功"])
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #就诊完成
    def update_unreview_order(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_order SET state=%s WHERE id=%s"
            cursor.execute(sql,("就诊完成",id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #查询预约过名单
    def search_list(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM t_order n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.patient_id=u.id " \
                  "ORDER BY n.create_time ASC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #查询全部名单页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_order"
            cursor.execute(sql)
            count_page=cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #删除预约记录
    def delete_by_id(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_order WHERE id=%s"
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #申请预约
    def insert(self,title,user_id,type_id,state):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_order(title,user_id,type_id,state) " \
                  "VALUES(%s,%s,%s,%s)"
            cursor.execute(sql,(title,user_id,type_id,state))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
'''service=OrderDao()
result=service.search_unreview_list(1)
print(result)'''
