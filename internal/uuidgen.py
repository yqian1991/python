import uuid

def create_code(number = 10):
    result = []
    
    while True is True:
        uuid_id = uuid.uuid1()
        tem = str(uuid_id).replace('-', '')
        tmmmm = str(tem[4:])
        if not tmmmm in result:
            result.append(tmmmm)
        if len(result) is number:
            break
    print result
    
create_code()