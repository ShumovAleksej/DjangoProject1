from django.http import HttpResponse
from django.shortcuts import render
import my_import
import time
from categories.models import Categories, Offers


def qwery_app(request, cat_id):
    co_list = []
    get_all_offers(cat_id, co_list)
    print(co_list)
    return HttpResponse('THIS IS CATEGORY_ID:' + cat_id)


def get_all_offers(cat_id, clist):
    if cat_id == '':
        return []

    childs = Categories.objects.filter(parent_id=cat_id)
    # print(childs[0])
    if len(childs) > 0:
        for ch in childs:
            get_all_offers(ch.category_id, clist)
    else:
        for offer in Offers.objects.filter(category_id=cat_id):
            clist.append(offer)


def menu_app(request, cat_id=''):
    main_list = []
    main_cats = Categories.objects.filter(parent_id='')
    for main_parent in main_cats:
        child_list = []
        for child in Categories.objects.filter(parent_id=main_parent.category_id):
            child_list.append(child)

        main_list.append({'main_parent': main_parent, 'child_list': child_list})

    tovars = []
    get_all_offers(cat_id, tovars)

    return render(request, 'ul.html', {'main_list': main_list, 'tovars': tovars})


def render_app(request):
    elements = [
        '<p>' + str(11) + '</p>',
        '<p>22</p>',
        '<p>33</p>'
    ]
    # parents = Categories.objects.filter(parent_id='')
    # child = []
    # for ob in Categories.objects.all():
    #     for p in parents:
    #         if ob.parent_id == p.category_id:
    #             child.append(ob)
    return render(request, 'try_one.html', {'elements': elements, 'name': 'putin'})


def update_categories_upp(request):
    # tm_one = time.time()
    #
    # Offers.objects.filter(self_id='199726').update(picture='Everything is the same')
    # tm_two = time.time()
    # print(tm_two-tm_one)
    #
    # ttt = Offers.objects.filter(self_id='199726')
    # for offer in ttt:
    #      print(offer)
    #     # offer.update(picture='7777')
    # return HttpResponse("OK update db")
    print('_-_-_-_')
    all_prod = my_import.load_prod()
    print('_-_-_-_')
    tm_one = time.time()
    for prod in all_prod:
        print('000')
        for offer in Offers.objects.filter(self_id=prod['id']):
            print('111')
            offer.picture = prod['picture']
            offer.save()
            # Offers.objects.filter(self_id=offer.self_id).update(picture=prod['picture'])
            print('222')
        print('333')




        # q = Offers.objects.get(self_id=prod['id'])
        # of = Offers.objects.filter(self_id=prod['id'])
        # of[0].update(picture='Everything is the same')
        # q.picture = 'ddgdfg'
        # q.save()
        # print(time.time())
        # ttt = Offers.objects.filter(self_id=prod['id'])
        # if len(ttt) > 1:
        #     print(len(ttt))
        # for offer in ttt:
        #     print(offer)
        #     print(prod['picture'])
        #
        #     offer.update(picture=prod['picture'])
    # for prod in all_prod:
    #         offer.update(picture=prod['picture'])
    tm_two = time.time()
    print(tm_two - tm_one)
    return HttpResponse("OK update db")


def load_categories_app(request):
    # Загружаем json
    all_cat = my_import.load_cats()
    for cat in all_cat:
        Categories.objects.create(category_id=cat['category_id'], parent_id=cat['parent_id'], name=cat['name'])
    return HttpResponse("Pass text")


def read_json(request):
    x = my_import.load_prod()
    for obj, val in x[0].items():
        print(obj, ": ", val, end='\n')
    return HttpResponse("Pass text")


def load_offers_app(request):
    # Загружаем json
    all_prod = my_import.load_prod()
    for pr in all_prod:
        Offers.objects.create(category_id=pr['category']['category_id'], self_id=pr['id'], name=pr['name'])
    return HttpResponse("Pass text")
