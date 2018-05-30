from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from art.models import Art, Tag


def IndexHandler(request):
    url = request.path
    page = int(request.GET.get("page", 1))
    t = int(request.GET.get("t", 0))
    if t == 0:
        art_list = Art.objects.all()
        total = art_list.count()
    else:
        art_list = Art.objects.filter(a_tag_id=t)
        total = art_list.count()
    tags = Tag.objects.all()
    context = dict(
        pagenum=1,
        total=1,
        prev=1,
        next=1,
        pagerange=range(1, 2),
        data=[],
        url=url,
        tags=tags,
        page=1,
        t=0
    )
    if total > 0:
        import math
        show_num = 2
        pagenum = math.ceil(total / show_num)
        if page < 1:
            url = url + "?page=1&t=%s" % t
            return HttpResponseRedirect(url)
        if page > pagenum:
            url = url + "?page=%s&t=%s" % (pagenum, t)

        offset = (page - 1) * show_num
        if t == 0:
            data = Art.objects.all()[offset:offset + show_num]
        else:
            data = Art.objects.filter(a_tag_id=t)[offset:offset + show_num]

        btnum = 5
        if btnum > pagenum:
            firstpage = 1
            lastpage = pagenum
        else:
            firstpage = page - 1
            lastpage = page + btnum
            if firstpage < 1:
                firstpage = 1
            if lastpage > pagenum:
                lastpage = pagenum
        prev = page - 1
        next = page + 1
        if prev < 1:
            prev = 1
        if next > pagenum:
            next = pagenum
        context = dict(
            pagenum=pagenum,
            total=total,
            prev=prev,
            next=next,
            pagerange=range(firstpage, lastpage),
            data=data,
            url=url,
            tags=tags,
            page=page,
            t=t
        )
    return render(request, 'home/index.html', context=context)
