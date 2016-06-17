#Comment

from sparkpost import SparkPost

sp = SparkPost("663c9d0ec49f661a63e8becf9fa62b35d8303e50")

response = sp.transmissions.send(
    recipients=['yuq@surveymonkey.com'],
    html='<p>Hello world</p>',
    from_email='test@sparkpostbox.com',
    subject='Hello from python-sparkpost'
)

print response
# outputs {u'total_accepted_recipients': 1, u'id': u'47960765679942446', u'total_rejected_recipients': 0}
