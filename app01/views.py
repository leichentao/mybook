from django.shortcuts import render

# Create your views here.

# 登录
from app01.models import User, Press, Book, Author
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    error_msg = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        ret = User.objects.filter(email=email, pwd=pwd)
        if ret:
            # 登录成功
            return redirect('/press_list/')
        else:
            # 登录失败
            error_msg = '邮箱或者密码错误'
    return render(request, 'login.html', {'error': error_msg})


# 出版社列表
def press_list(request):
    # 查询列表数据
    result = Press.objects.all().order_by('id')
    return render(request, 'list/press_list.html', {'ret': result})


# 书籍列表
def book_list(request):
    # 查询列表数据
    result = Book.objects.all().order_by('id')
    return render(request, 'list/book_list.html', {'ret': result})


# 作者列表
def author_list(request):
    # 查询列表数据
    result = Author.objects.all().order_by('id')
    return render(request, 'list/author_list.html', {'ret': result})


# 添加作者
def add_author(request):
    if request.method == 'POST':
        # 获取页面上的控件值
        author = request.POST.get('author_name')
        book_ids = request.POST.getlist('books')
        # 进行添加
        author_obj = Author.objects.create(author_name=author)
        author_obj.books.add(*book_ids)  # ID是一个单独的值 *打散后添加进去
        return redirect('/author_list/')
    # 返回页面，回填作者信息
    book_data = Book.objects.all().order_by('id')
    return render(request, 'add_author.html', {'book_list': book_data})


# 添加书籍
def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('book_name')
        press_id = request.POST.get('press_id')
        Book.objects.create(book_name=name, press_id=press_id)
        return redirect('/book_list/')

    press_data = Press.objects.all()
    return render(request, 'add_book.html', {'press_list': press_data})


# 添加出版社
def add_press(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Press.objects.create(press_name=name)
        return redirect('/press_list/')

    return render(request, 'add_press.html')


# 编辑作者
def edit_author(request):
    edit_id = request.GET.get('id')
    edit_obj = Author.objects.get(id=edit_id)
    if request.method == 'POST':
        new_name = request.POST.get('author_name')
        new_ids = request.POST.getlist('book_ids')

        # 修改信息
        edit_obj.author_name = new_name
        edit_obj.save()

        # 修改书籍选中的信息
        edit_obj.books.set(new_ids)
        return redirect('/author_list/')

    # 查询所有书籍，并绑定select下拉框
    book_data = Book.objects.all()
    return render(request, 'edit_author.html', {'author': edit_obj, 'book_list': book_data})


# 编辑书籍
def edit_book(request):
    book_id = request.GET.get('id')
    book_obj = Book.objects.get(id=book_id)

    if request.method == 'POST':
        name = request.POST.get('book_name')
        press_id = request.POST.get('press_id')
        # 修改书籍信息
        book_obj.book_name = name
        book_obj.press_id = press_id
        # 保存到数据库
        book_obj.save()
        # 跳转列表页面
        return redirect('/book_list/')

    press_data = Press.objects.all()
    return render(request, 'edit_book.html', {'book': book_obj, 'press_list': press_data})


# 编辑出版社
def edit_press(request):
    if request.method == 'POST':
        new_id = request.POST.get('id')
        # 获取值
        name = request.POST.get('name')
        # 修改值
        new_obj = Press.objects.get(id=new_id)
        new_obj.press_name = name
        new_obj.save()
        return redirect('/press_list/')
    else:
        press_id = request.GET.get('id')
        # 查询值并且赋值给控件
        ret = Press.objects.get(id=press_id)
        return render(request, 'edit_press.html', {'press': ret})


# 删除出版社
def delete_press(request):
    press_id = request.GET.get('id')
    Press.objects.filter(id=press_id).delete()
    return redirect('/press_list/')


# 删除书籍
def delete_book(request):
    book_id = request.GET.get('id')
    Book.objects.filter(id=book_id).delete()
    return redirect('/book_list/')


# 删除作者
def delete_author(request):
    author_id = request.GET.get('id')
    Author.objects.filter(id=author_id).delete()
    return redirect('/author_list/')
