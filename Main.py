from NDB import Neo4jDB

uri = "bolt://localhost:7687"
user = "neo4j"
password = "myneo4jpassword"

db = Neo4jDB(uri, user, password)
db.create_player(1, "João")
db.update_player(1, "José")
players = db.get_players()
print(players)