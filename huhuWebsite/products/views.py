from django.shortcuts import render
from .models import Product,Category


# Create your views here.
def products(request, catalog):
    column_max = 4
    prod_column = 0
    prod_row = 0

    product_set = Product.objects.all().filter(status=1)
    product_list = list(product_set)
    prod_len = len(product_set)

    if prod_len != 0:
        prod_row = prod_len // column_max
        if prod_row == 0:
            prod_column = prod_len % column_max
        if prod_len % column_max > 0:
            prod_row += 1
        print('the value of prod_column')
        print(prod_column)

    catalog_dict = getCatalog()
    catalog_len = len(catalog_dict)

    attr_list = {
        'column_range': range(0, prod_column),
        'row_range': range(0, prod_row),
        'product_list':product_list,
        'catalog_range':range(0,catalog_len),
        'catalog_dict':catalog_dict
    }
    test_list ={
        'column_range': range(0,3),
        'row_range': range(0, 3),
        'product_list':product_list,
        'catalog_range': range(0, 4)
    }
    return render(request, 'products/productslist.html', test_list)


def getCatalog():
    #在只有两级菜单的情况下，一级菜单的父菜单为0，二级菜单的父菜单为1
    catalog_dict = {}
    catalog_set = Category.objects.all().filter(parent_id=0)
    catalog_len = len(catalog_set)
    catalog_list = list(catalog_set)
    for i in catalog_list:
        child_set = Category.objects.all().filter(parent_id=i.cat_id)
        child_list = list(child_set)
        sub_dict = {i: child_list}
        catalog_dict.update(sub_dict)
    return catalog_dict


def test(request):
    test_list = {
        'column_range': range(0, 3),
        'row_range': range(0, 2),
        'catalog_range': range(0, 4)
    }
    return render(request, 'products/productslist.html', test_list)
