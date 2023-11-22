from .models import *


def load_data(text, model):
    objs = text.split("\n")
    columns = objs[0].split(":")
    objs.pop(0)
    if model == Category:
        i = 0
        new_objs = []
        new_objs_ids = []
        for obj in objs:
            new_obj = obj.strip().split(":")
            parent_id = new_obj[2]
            if parent_id == "None":
                new_objs_ids.append(new_obj[0])
                new_objs.append(obj)

        while len(new_objs) < len(objs):
            new_obj = objs[i].strip().split(":")
            if new_obj[2] in new_objs_ids:
                new_objs_ids.append(new_obj[0])
                new_objs.append(objs[i])
            i = i + 1 if i < len(objs) - 1 else 0
        objs = new_objs

    for obj in objs:
        obj = obj.strip().split(":")
        if model == Category:
            obj[2] = None if obj[2] == "None" else Category.objects.get(
                id=obj[2])
        data = {col: val for col, val in zip(columns, obj)}
        model.objects.create(**data)


def test_db():
    """Вызвав через python manage.py shell, можно наполнить бд тестовыми данными"""

    category = """id:title:parent
    1:Велосипеды:None
    2:Кастрюли:4
    3:Тарелки:4
    4:Посуда для кухни:5
    5:Товары для дома:None"""
    load_data(category, Category)

    products = """id:title:category_id:amount:price
    1:Велосипед:1:100:100.50
    2:Кастрюля 1,5л:2:50:1200
    3:Тарелка 25см:3:1000:25
    4:Кастрюля 3л:5:5:300.78"""
    load_data(products, Product)
