from shop.models import Category, Order, OrderItem, Product

Category.objects.all().delete()
Order.objects.all().delete()
Product.objects.all().delete()

category_names = [
    'Арабика', 'Робуста', 'Бленды', 'Десертные', 'Без кофеина',
    'Растворимый', 'Зелёный кофе', 'Кофе в капсулах', 'Молотый кофе',
    'Кофе в зёрнах', 'Спешелти', 'Органический кофе',
]
cats = {}
for name in category_names:
    cats[name] = Category.objects.create(name=name)

products_data = [
    ('Арабика', 'Ethiopia Yirgacheffe', 890.00),
    ('Арабика', 'Colombia Supremo', 750.00),
    ('Арабика', 'Brazil Santos', 620.00),
    ('Арабика', 'Kenya AA', 980.00),
    ('Арабика', 'Guatemala Antigua', 810.00),
    ('Робуста', 'Vietnam Robusta', 450.00),
    ('Робуста', 'India Cherry', 480.00),
    ('Робуста', 'Uganda Robusta', 430.00),
    ('Бленды', 'Espresso Blend', 560.00),
    ('Бленды', 'Italian Roast', 590.00),
    ('Бленды', 'House Blend', 520.00),
    ('Десертные', 'Caramel Macchiato Beans', 640.00),
    ('Десертные', 'Chocolate Hazelnut', 670.00),
    ('Без кофеина', 'Swiss Water Decaf', 720.00),
    ('Без кофеина', 'Decaf Colombia', 690.00),
    ('Растворимый', 'Instant Gold Arabica', 390.00),
    ('Растворимый', 'Freeze-Dried Premium', 420.00),
    ('Зелёный кофе', 'Green Ethiopia Sidamo', 540.00),
    ('Зелёный кофе', 'Green Brazil Cerrado', 460.00),
    ('Кофе в капсулах', 'Nespresso Compatible Classic', 350.00),
    ('Кофе в капсулах', 'Lungo Capsules 20 pcs', 380.00),
    ('Молотый кофе', 'Turkish Grind Fine', 310.00),
    ('Молотый кофе', 'French Press Grind', 290.00),
    ('Кофе в зёрнах', 'House Whole Beans 1kg', 820.00),
    ('Кофе в зёрнах', 'Espresso Whole Beans 1kg', 870.00),
    ('Спешелти', 'Geisha Panama Lot 4', 2450.00),
    ('Спешелти', 'Blue Mountain Jamaica', 3200.00),
    ('Органический кофе', 'Organic Peru Arabica', 760.00),
    ('Органический кофе', 'Organic Mexican Chiapas', 730.00),
    ('Органический кофе', 'Organic Sumatra Mandheling', 790.00),
]
prods = {}
for cat, name, price in products_data:
    prods[name] = Product.objects.create(category=cats[cat], name=name, price=price)

orders_data = [
    [('Ethiopia Yirgacheffe', 2), ('Colombia Supremo', 1)],
    [('Vietnam Robusta', 3), ('House Blend', 1)],
    [('Kenya AA', 1), ('Decaf Colombia', 2), ('Espresso Blend', 1)],
    [('Brazil Santos', 5)],
    [('Caramel Macchiato Beans', 1), ('Chocolate Hazelnut', 2)],
    [('Italian Roast', 2), ('India Cherry', 1), ('Uganda Robusta', 2)],
    [('Guatemala Antigua', 1)],
    [('Swiss Water Decaf', 2), ('House Blend', 2)],
    [('Geisha Panama Lot 4', 1)],
    [('Blue Mountain Jamaica', 1), ('House Whole Beans 1kg', 2)],
    [('Nespresso Compatible Classic', 4), ('Lungo Capsules 20 pcs', 2)],
    [('Organic Peru Arabica', 1), ('Organic Sumatra Mandheling', 1)],
]
for items in orders_data:
    o = Order.objects.create()
    for pname, qty in items:
        OrderItem.objects.create(order=o, product=prods[pname], quantity=qty)

print('Categories:', Category.objects.count())
print('Products:', Product.objects.count())
print('Orders:', Order.objects.count())
print('OrderItems:', OrderItem.objects.count())
