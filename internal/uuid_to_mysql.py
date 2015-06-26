import uuid
import MySQLdb

def creat_code(number=20):
	result = []
	while True is True:
		tem=str(uuid.uuid1()).replace('-','')
		if not tem in result:
			result.append(tem)
		if len(result) is number:
			break
	return result

def connect_db(result):
	num = len(result)
	db= MySQLdb.connect('localhost','root','','python',charset='utf8')
	cur = db.cursor()

	try:
		db= MySQLdb.connect('localhost','root','','python',charset='utf8')
		cur = db.cursor()
		print "OK"
		for i in xrange(num):
			cur.execute('insert into code (code_num) values("%s")' % (result[i]))
		db.commit()
	except:
		print "DB Connection error"
		db.rollback()
	db.close()

if __name__ == '__main__':
	connect_db(creat_code())