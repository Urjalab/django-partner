from django.shortcuts import render
from faker import Faker

fake = Faker()


def index(request):

    context = {}
    number = request.GET.get("num")
    if number is not None:

        Faker.seed(int(number))
        name = fake.first_name_female()
        context['name'] = name

    return render(
        request,
        'demo/index.html',
        context
    )
