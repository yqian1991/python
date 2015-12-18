from sparkpost import SparkPost

sp = SparkPost("663c9d0ec49f661a63e8becf9fa62b35d8303e50")

print sp.recipient_lists.list()
# outputs {u'total_accepted_recipients': 1, u'id': u'47960765679942446', u'total_rejected_recipients': 0}
