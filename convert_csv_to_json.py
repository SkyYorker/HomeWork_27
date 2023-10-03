import csv
import json





def convert(csv_file, json_file):
    data = []

    with open(csv_file,'r', encoding='utf-8') as file:
        csv_read = csv.DictReader(file)
        counter = 0
        for i in csv_read:
            counter += 1
            data.append({
                "model": "ads.ad",
                "pk": counter,
                "fields": {
                   'id': int(i['Id']),
                   'name': i['name'],
                   'author': int(i['author_id']),
                   'price': int(i['price']),
                   'description': i['description'],
                   'is_published': bool(i['is_published']),
                   'image': i['image'],
                   'category': int(i['category_id'])
                  
                }
            })


    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))



convert('R:\Python\HomeWork_27\datasets\\ad.csv', 'R:\Python\HomeWork_27\\ads\\fixtures\\ad.json')