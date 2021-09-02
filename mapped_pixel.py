import pickle

def storeData():
    #init data to be stored in db
    mapped_pixel = {(0,1), (0,2), (0,3), (0,4)}

    #database
    db = {}
    db['mapped_pixel'] = mapped_pixel

    #Use binary
    dbfile = open('mapped_pixel', 'ab')

    # source, destination
    pickle.dump(db, dbfile)
    dbfile.close()

def loadData():
    # for reading also binary mode is important
    dbfile = open('mapped_pixel', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

if __name__ == '__main__':
    storeData()
    loadData()
