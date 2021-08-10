from django.shortcuts import render, redirect
from mould.forms.repairparts import RepairpartsModelForm
from utils.pagination import Pagination
from django.http import HttpResponse, JsonResponse, request
from mould.models import Mould, RepairParts, SpecialParts
from manuf import settings
from PIL import Image
import os
import uuid


def index(request):
    return render(request, 'web/index.html')


# 在库备件查询
def r_parts(request, tool_id):
    if request.method == 'GET':
        # 分页获取数据
        queryset = RepairParts.objects.filter(tool_id=tool_id, quantity__gt=0)
        mould_object = Mould.objects.filter(
            id=tool_id).first()  # .values('name')
        '''print(tool_id)'''
        form = RepairpartsModelForm(request)

        if queryset:
            page_object = Pagination(
                current_page=request.GET.get('page'),
                all_count=queryset.count(),
                base_url=request.path_info,
                query_params=request.GET,
                per_page=9
            )

            rparts_object_list = queryset[page_object.start:page_object.end]
            print(mould_object)

            context = {
                'tool_id': tool_id,
                'mould': mould_object,
                'search_result': rparts_object_list,
                'page_html': page_object.page_html(),
                'form': form,
            }
            return render(request, 'mould/repair.html', context)

        error_msg = "出错了！没有备件在库信息！"

        return render(request, 'mould/repair.html', locals())
     # 备件出库
    print('Post')
    tool_id = request.POST.get('tool_id')
    rpartid = request.POST.get('rpartid')
    used = request.POST.get('use')
    print(used)
    oldquantity = RepairParts.objects.get(id=rpartid).quantity

    newquantity = int(oldquantity) - int(used)
    print(newquantity)
    RepairParts.objects.filter(id=rpartid).update(quantity=newquantity)
    context = {
        'tool_id': tool_id,
    }

    return redirect('r_parts', tool_id=tool_id,)

# 上传图片


def upload_handle(request):

    # 1.获取上传文件的处理对象
    pic = request.FILES['pic']
# <class 'django.core.files.yploadedfile.InMemoryuploadedFile'>
# <class 'django.core.files.yploadedfile.TemporaryuploadedFile'>
# print(pic.name)
# pic.chunks()
# 2.创建一个文件
    save_path = '%s/baoktest/%s' % (settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 3.获取上传文件的内容并写到创建的文件中
        for content in pic.chunks():
            f.write(content)
# 4.在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/‰s' % pic.name)

# 压缩图片


def crop_image(to_file, file):

    # 随机生成新的图片名，自定义路径。
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)

    # 相对根目录路径

    file_path = os.path.join(
        "static", "Mould",  str(to_file), "repair", file_name)
    print(file_path)

    img = Image.open(file)
    # 获取图像 width
    w = img.size[0]
    # 获取图像 height
    h = img.size[1]
    # 比例缩放
    scale = 800/w
    crop_im = img.resize(
        (int(w*scale), int(h*scale)), Image.ANTIALIAS)

    directory = os.path.dirname(file_path)
    if os.path.exists(directory):
        crop_im.save(file_path)
    else:
        os.makedirs(directory)
        crop_im.save(file_path)

    return file_path


# 添加备件
def add_rpart(request, tool_id):
    if request.method == 'GET':
        print(request.GET)

        context = {
            'tool_id': tool_id,
            'form': RepairpartsModelForm(request),
        }

        return render(request, 'mould/a_rparts.html', context)

        form = RepairpartsModelForm()
        return render(request, 'mould/a_rparts.html', {'form': form})
    print('post')

    form = RepairpartsModelForm(request, data=request.POST)
    if form.is_valid():
        # 获得上传的文件
        file = request.FILES.get('imgs')
        print(file)
    # 获得模具编号
        tool_no_object = Mould.objects.filter(
            id=tool_id).values('tool_no')
        for t in tool_no_object:
            tool_no = t['tool_no']

        print(request.FILES)
        print(tool_no)

        file_path = crop_image(tool_no, file)

        #save_path = '%s/repair/%s' % (settings.MEDIA_ROOT, file.name)

    #  2.创建一个文件
        # with open(file_path, 'wb') as f:
        # 3.获取上传文件的内容并写到创建的文件中
        #    for content in file.chunks():
        #        f.write(content)

        file_path = '/' + file_path
        form.instance.tool_id = tool_id
        form.instance.modify = request.web.user
        form.instance.imgs = file_path
        form.save()
        print('post成功')
        return JsonResponse({'status': True, })
    return JsonResponse({'status': False, 'error': form.errors})


def none_rparts(request):
    pass
    context = "查询失败"
    return HttpResponse(context)

# 在库标准件查询


def search3(request):
    if request.method == 'GET':
        A1 = ''
        if request.GET['D']:
            D = str(request.GET['D'])
            A1 = (D)
        print('D没有值')
        if request.GET['L']:
            L = str(request.GET['L'])
            A1 = (A1+'-'+L)
        print('L没有值')
        if request.GET['P']:
            P = str(request.GET['P'])
            A1 = (A1+'-P'+P)
        print('L没有值')
        if request.GET['W']:
            W = str(request.GET['W'])
            A1 = (A1+'-W'+W)
        print('L没有值')
        print(A1)
        if len(A1) == 0:
            error_msg = "输入信息有误！没有备件在库信息！"
            return render(request, 'mould/search_result3.html', locals())

        # 分页获取数据
        queryset = SpecialParts.objects.filter(
            model__icontains=A1, quantity__gt=0)

        count = queryset.count()
 # .values('name')
        if queryset:
            page_object = Pagination(
                current_page=request.GET.get('page'),
                all_count=queryset.count(),
                base_url=request.path_info,
                query_params=request.GET,
                per_page=9
            )

            rparts_object_list = queryset[page_object.start:page_object.end]

            context = {

                'search_result': rparts_object_list,
                'page_html': page_object.page_html(),
                'count': count

            }
            return render(request, 'mould/search_result3.html', context)

        error_msg = "出错了！没有备件在库信息！"

        return render(request, 'mould/search_result3.html', locals())
    else:
        return render(request, 'web/index.html')
