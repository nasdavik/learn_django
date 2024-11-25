from django.shortcuts import render


def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)


def products(request):
    products_static = '/static/vendor/img/products/'
    context = {
        'title': 'Store - Каталог',
        'products': [
            {
                'image': f'{products_static}Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6 090,00 руб.',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'image': f'{products_static}Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': '23 725,00 руб.',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'image': f'{products_static}Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3 390,00 руб.',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            },
            {
                'image': f'{products_static}Black-Nike-Heritage-backpack.png',
                'name': 'Черный рюкзак Nike Heritage',
                'price': '2 340,00 руб.',
                'description': 'Плотная ткань. Легкий материал.'
            },
            {
                'image': f'{products_static}Black-Dr-Martens-shoes.png',
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': '13 590,00 руб.',
                'description': 'Гладкий кожаный верх. Натуральный материал.'
            },
            {
                'image': f'{products_static}Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': '2 890,00 руб.',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
            },
        ]
    }
    return render(request, 'products/products.html', context)
