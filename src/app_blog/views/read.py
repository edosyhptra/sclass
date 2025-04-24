from django.shortcuts import render
from app_blog.utility import query, dictfetchall

def view(request, id):
    if request.method == 'GET':
        # Mengambil data blog berdasarkan ID
        post = query("SELECT * FROM blog_post WHERE id = %s", [id])
        if post:
            # Jika blog ditemukan, tampilkan halaman detail
            return render(request, 'app_blog/read.html', {'post': post[0]})
       
    # Jika blog tidak ditemukan, redirect ke halaman notfound
    return render(request, 'app_blog/notfound.html')