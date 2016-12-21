import adodbapi, pypyodbc
databasename = 'c:/users/v.korolev/desktop/dev/python/ntkdata.mdb' 
constr = 'Provider=Microsoft.JET.OLEDB.4.0;Data Source=%s'  % databasename 
db = adodbapi.connect(constr)
cs = db.cursor()
cs.execute('DELETE FROM History where LogDate < now() - 30')
db.commit()
cs.close()
db.close()
pypyodbc.win_compact_mdb("c:/users/v.korolev/desktop/dev/python/ntkdata.mdb","c:/users/v.korolev/desktop/dev/python/ntkdata.mdb")
