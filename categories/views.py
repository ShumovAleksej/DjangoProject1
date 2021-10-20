from django.http import HttpResponse
from django.shortcuts import render
import unifunc
from unifunc import list_to_matrix
from categories.models import Categories, Offers


def qwery_app(request, cat_id):
    co_list = []
    get_all_offers(cat_id, co_list)
    print(co_list)
    return HttpResponse('THIS IS CATEGORY_ID:' + cat_id)


# Рекурсивная функция, принимающая id необходмой категории и возвращающая список товаров
def get_all_offers(cat_id, clist):
    if cat_id == '':
        return []

    childs = Categories.objects.filter(parent_id=cat_id)
    if len(childs) > 0:
        for ch in childs:
            get_all_offers(ch.category_id, clist)
    else:
        for offer in Offers.objects.filter(category_id=cat_id):
            clist.append(offer)


def boot_app(request):
    return render(request, 'index.html')


# Основная функция
def menu_app(request, cat_id=''):
    main_list = []
    # Поиск главных категорий и их первых подкатегорий
    main_cats = Categories.objects.filter(parent_id='')
    for main_parent in main_cats:
        child_list = []
        for child in Categories.objects.filter(parent_id=main_parent.category_id):
            child_list.append(child)
        main_list.append({'main_parent': main_parent, 'child_list': child_list})

    tovars = []
    # Получение списка товаров категории
    get_all_offers(cat_id, tovars)
    x = list_to_matrix(tovars, 3)
    return render(request, 'test.html', {'main_list': main_list, 'tovars': x[:10]})


def update_categories_upp(request):
    all_prod = my_import.load_prod()
    for prod in all_prod:
        for offer in Offers.objects.filter(self_id=prod['id']):
            offer.update(picture=prod['picture'])
    return HttpResponse("OK update db")


def load_categories_app(request):
    # Загружаем в БД из json файла категории товаров
    all_cat = unifunc.load_cats()
    for cat in all_cat:
        Categories.objects.create(category_id=cat['category_id'], parent_id=cat['parent_id'], name=cat['name'])
    return HttpResponse("Pass text")


def load_offers_app(request):
    # Загружаем в БД из json файла товары
    all_prod = unifunc.load_prod()
    for pr in all_prod:
        Offers.objects.create(category_id=pr['category']['category_id'], self_id=pr['id'], name=pr['name'])
    return HttpResponse("Pass text")
