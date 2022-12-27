import webbrowser
import asyncio
def home(request):
    query = request.GET.get('query', '').strip()
    print('Query: {!r}'.format(query))
    if query:
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(**vars(descr))
                        for descr in descriptions)
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'

    html = template.format(query=query, result=res,
                            message=msg)
    print('Sending {} results'.format(len(descriptions)))
    return web.Response(content_type=CONTENT_TYPE, text=html)