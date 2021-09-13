import pickle

def storeData():
    #init data to be stored in db
    mapped_pixel = {[104,59],
[310,60],
[307,72],
[102,70],
[99,82],
[304,86],
[302,97],
[95,94],
[92,107],
[302,110],
[224,114],
[181,319],
[171,319],
[209,115],
[197,116],
[158,319],
[144,319],
[185,113],
[170,113],
[127,319]}

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
