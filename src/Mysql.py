import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='qianyu', db='mysql', port=3306)
    cur = conn.cursor()
    cur.execute('select * from event')
    cur.close()
    conn.close()
except MySQLdb.Error:
    print ("Mysql Error %d: %s" %(e.args[0], e.args[1]))
