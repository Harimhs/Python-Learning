novel= ["TBATE", "ORV", "TGED", "LOTM", "SSS", "MEMP"]
readed= ["TGED", "MEMP", "SSS"]
novel_readed= [book for book in novel if book in readed]
print(novel_readed)