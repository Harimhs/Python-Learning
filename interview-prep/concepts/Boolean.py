ingredients_purchased = True
completed_cooking = False
ready_to_serve = all([ingredients_purchased, completed_cooking])
print(ready_to_serve)
            

readed_manhwa = True
readed_manhua = False
finished_reading = any([readed_manhua, readed_manhwa])
print(finished_reading)