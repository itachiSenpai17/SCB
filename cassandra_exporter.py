from cassandra.cluster import cluster

cluster = Cluster()

session = cluster.connect('main_keyspace')
rows = session.execute("SELECT * FROM ohlc_table")

return rows
