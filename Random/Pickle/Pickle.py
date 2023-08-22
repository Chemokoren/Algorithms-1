
"""
- program illustrating how to store efficiently using pickle module
- The module translates an in-memory Python object into a serialized byte stream—a string
 - of bytes that can be written to a file-like object
"""
import pickle


def writeData():
    # initializing data to be stored in db
    Mango = {'key': 'Mango', 'name': 'Mangifera indica',
             'weight': 21, 'pay': 100}
    Apple = {'key': 'Apple', 'name': 'Malus domestica',
             'weight': 50, 'pay': 250}

    # database
    db = {}
    db['Mango'] = Mango
    db['Apple'] = Apple

    # using binary mode is votal
    db_file = open('../fruits_pickle', 'ab')

    # source, destination
    pickle.dump(db, db_file)
    db_file.close()


def readData():
    # binary mode is critical when reading
    db_file = open('../fruits_pickle', 'rb')
    db = pickle.load(db_file)
    for keys in db:
        print(keys, '=>', db[keys])
    db_file.close()

# driver code for the pickle program
if __name__ == '__main__':
    print("######  initiate storing the data ###### : ")
    writeData()
    print("\n\n\n ######  start loading the data ######  : ")
    readData()


"""
Pickling without a file
"""
print("###### pickling without a file ######")

#  data to be stored in the db is initialized
Mango = {'key' : 'Mango', 'name' : 'Mangifera indica',
'weight' : 21, 'pay' : 100}
Apple = {'key' : 'Apple', 'name' : 'Malus domestica',
'weight' : 50, 'pay' : 250}

# database
db = {}
db['Mango'] = Mango
db['Apple'] = Apple



# driver code for the pickle program
if __name__ == '__main__':
    # storing
    b = pickle.dumps(db)  # type(b) gives <class 'bytes'>

    # loading
    my_entry = pickle.loads(b)
    print(my_entry)
