from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate(objects_list, request):
    page = request.GET.get('page')

    paginator = Paginator(objects_list, 20)
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        objects_page = paginator.page(paginator.num_pages)

    low = objects_page.number - 2
    high = objects_page.number + 2
    if low < 1:
        low = 1
    if high > paginator.num_pages:
        high = paginator.num_pages

    return objects_page, paginator, range(low, high + 1)