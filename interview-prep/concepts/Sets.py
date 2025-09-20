novel= {"TBATE", "LOTM"}
novel2= {"ORV", "TGED", "LOTM"}
intersect = novel & novel2
print(intersect) # Output: {'LOTM'}
union = novel | novel2
print(union) # Output: {'TBATE', 'LOTM', 'ORV', 'TGED'}
diff = novel - novel2
print(diff) # Output: {'TBATE'}
symbol = novel2 > novel
print(symbol) # Output: False
print(list(novel))