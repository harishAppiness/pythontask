import math


def paginate(result, serializer, page=1, context=None, order='desc', PAGE_SIZE=3):
    if page and order == 'desc':
        query_filter = {'id__lt': page}
    elif page and order == 'asc':
        query_filter = {'id__gt': page}
    else:
        query_filter = {}
    # query_pages = list(result.values_list('id', flat=True))
    # query_pages = [None] + query_pages
    if page == '' or page is None or page < 1:
        page = 1
    else:
        page = int(page)
    if isinstance(result, list):
        query = result[(page - 1) * PAGE_SIZE:page * PAGE_SIZE]
        total_results = len(result)
    else:
        query = result.filter()[(page-1) * PAGE_SIZE:page * PAGE_SIZE]
        total_results = result.count()
    total_pages = math.ceil(total_results / PAGE_SIZE) if total_results != 0 else 1
    # page_ids = query_pages[::PAGE_SIZE][:total_pages]
    page_ids = list(range(1, total_pages + 1))
    results = serializer(query, many=True, context=context).data
    # current_page = page_ids.index(page_ids[-1]) + 1 if len(page_ids) != 0 else 1
    current_page = page
    # for each_id in reversed(page_ids):
    #     if each_id is not None:
    #         if results[-1]['id'] < each_id:
    #             current_page = page_ids.index(each_id) + 1
    #             break
    #     else:
    #         current_page = 1
    result = {
        'page_ids': page_ids,
        'current_page': current_page,
        'next_page_id': current_page + 1 if current_page < total_pages else None,
        'total_pages': total_pages,
        'total_results': total_results,
        'results': results
    }
    return result