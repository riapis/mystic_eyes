# Mystic Eyes
Trading Card game dengan tema fantasi.
https://mystic-eyes.adaptable.app/
#

# Tugas 2
## Pembuatan aplikasi
### A. Membuat sebuah proyek Django baru
1. Buat direktori bernama `mystic_eyes`, lalu ke command prompt melalui direktori tersebut dan jalankan `python -m venv env` untuk membuat *virtual environment*
2. Jalankan `env\Scripts\activate.bat` untuk mengaktifkan *virtual environment*
3. Buat `requirements.txt` pada direktori dan isi dengan beberapa *dependencies*
   
   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
    Untuk mengaktifkan *dependencies*, jalankan `pip install -r requirements.txt`
4.  Buat proyek django dengan menjalankan `django-admin startproject mystic_eyes .`

### B. Membuat aplikasi dengan nama `main` pada proyek tersebut
1. Jalankan `python manage.py startapp main` untuk membuat aplikasi (akan membuat direktori baru bernama `main`)
2. Buka `mystic_eyes` -> `setting.py`, temukan `INSTALLED_APPS` dan tambahkan 'main'

   ```
   INSTALLED_APPS = [
    ...,
    'main',
    ...
   ]
   ```

### C. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`
1. Buka `mystic_eyes` -> `urls.py`
2. Tambahkan rute URL untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`
   
   ```
   urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
    ]
   ```

### D. Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib
1. Buka `main` -> `models.py` dan isi dengan

   ```
   from django.db import models

   # Create your models here.
   class Product(models.Model):
       type = models.CharField(max_length=255)
       name = models.CharField(max_length=255)
       element = models.CharField(max_length=255)
       amount = models.IntegerField()
       power = models.IntegerField()
       description = models.TextField()
   ```
2. Jalankan perintah `python manage.py makemigrations` untuk membuat migrasi model
3. Jalankan perintah `python manage.py migrate` untuk menerapkan migrasi ke dalam basis data lokal

### E. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML
1. Buka `main` -> `views.py` dan isi dengan
   
   ```
   from django.shortcuts import render

    # Create your views here.
    def show_main(request):
        context = {
            'nama': 'Fari',
            'kelas': 'PBP A'
        }
    
        return render(request, "main.html", context)
   ```
2. Buka direktori `main` dan buat direktori baru bernama `tempalates`
3. Dalam direktori `templates` buat file bernama `main.html` dan isi dengan
   
   ```
   <h1>Mystic Eyes Card Holder</h1>

   <h5>Name: </h5>
   <p>{{ nama }}</p>
   <h5>Class: </h5>
   <p>{{ kelas }}</p>
   ```

### F. Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`
1. Buka direktori `main` dan buat direktori baru bernama `urls.py`
2. Isi `urls.py` dengan
   
   ```
   from django.urls import path
   from main.views import show_main
    
   app_name = 'main'
    
   urlpatterns = [
       path('', show_main, name='show_main'),
   ]
   ```

### G. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
1. *Log in* ke Adaptable dengan Github
2. Pilih *new app* -> *connect an existing repository* -> pilih repository `mystic_eyes`
3. Pilih *Python App* Template sebagai template deployment
4. Pilih *PostgreSQL* sebagai tipe basis data yang akan digunakan
5. Pada bagian Start Command masukkan perintah `python manage.py migrate && gunicorn rey_inventory.wsgi`

## Bagan request client ke web aplikasi berbasis Django
![Bagan](https://i.imgur.com/gQcZoQP.png)
Saat klien mengakses situs berbasi django, browser akan mengirimkan HHTP request ke `urls.py` untuk di handle. `urls.py` akan menghubungkan URL dengan view yang sesuai dengan `views.py`. `views.py` akan mengambil data dari `models.py` dan mengirimkannya ke `templates` untuk merendel tampilan yang nantinya akn dikembalikan ke klien untuk menjadi userinterface.

## Alasan menggunakan *virtual environment* dan apa yang terjadi jika tidak menggunakan *virtual environment* 
*Virtual environment* berfungsi untuk mengelola dependensi dan paket Python untuk proyek Anda secara terpisah dari sistem Python global. Hal ini dapat menghindari konflik jika kita bekerja pada dua proyek dengan versi berbeda, tetapi dari paket yang sama.

Jika kita tidak menggunakan *virtual environment*, sebenarnya kita tetap bisa membuat aplikasi web berbasis django. Namun risiko terjadinya konflik akan sangat besar.

## MVC, MVT, MVVM
1. MVC (Model View Controller)
   * Model: mengatur cara data disimpan, diambil, dan diperbarui
   * View: menggambarkan tampilan dan berinteraksi dengan pengguna
   * Controller: menerima input dari pengguna dan mengoordinasikan tindakan yang diperlukan oleh Model dan View (penghubung antara Model dan View)
2. MVT (Model View Template)
   * Model: mengatur cara data disimpan, diambil, dan diperbarui
   * View: menggambarkan tampilan dan berinteraksi dengan pengguna
   * Template: komponen tambahan yang digunakan untuk merender tampilan
3. MVVM (Model View ViewModel)
   * Model:  mengatur cara data disimpan, diambil, dan diperbarui
   * View: menggambarkan tampilan dan berinteraksi dengan pengguna
   * ViewModel: mengubah data dari Model menjadi format yang dapat digunakan oleh View, dan juga menerima tindakan pengguna dari View dan meneruskannya ke Model

Perbedaan  MVC, MVT, MVVM:
Perbedaan utama ketiganya adalah dalam cara komponen-komponen tersebut berinteraksi, MVC menggunakan Controller untuk mengoordinasikan Model dan View, MVT menggunakan Template untuk mengatur presentasi tampilan, dan MVVM menggunakan ViewModel sebagai perantara View dan Model.

#
# Tugas 3
## `POST` vs `GET` dalam django
<table>
  <tr>
    <th>POST</th>
    <th>GET</th>
  </tr>
  <tr>
    <td>Data/value tidak terlihat di URL</td>
    <td>Data/value terlihat di URL</td>
  </tr>
  <tr>
    <td>Tidak ada batasan ukuran untuk data yang dapat dikirimkan</td>
    <td>Terdapat batasan ukuran URL yang dapat ditangani oleh server</td>
  </tr>
  <tr>
  <td>Untuk request yang dapat mengubah data di server</td>
  <td>Untuk request yang tidak mengubah data di server</td>
  </tr>
</table>

## Perbedaan XML, JSON, dan HTML dalam pengiriman data
1. XML
   * Dapat mendefinisikan struktur data secara bebas, sehingga XML lebih kompleks dibanding JSON dan HTML
   * Digunakan secara luas untuk pertukaran data antara sistem yang berbeda dan konfigurasi file
2. JSON
   * Struktur data lebih sederhana dan strukturnya terdiri dari pasangan nama-nilai
   * Umumnya digunakan untuk pertukaran data antar aplikasi web
3. HTML
   * Digunakan untuk membuat tampilan halaman web dan mengorganisir kontennya

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Karena JSON memiliki banyak keunggulan yang diantaranya:
1. JSON memiliki format yang sangat ringkas dan ringan
2. Menggunakan sintaks yang mudah dibaca dan ditulis oleh manusia
3. Hampir semua bahasa pemrograman modern memiliki dukungan untuk mengurai dan membuat JSON

## Pengimplementasian *checklist*
### A. Membuat input `form` untuk menambahkan objek model pada app sebelumnya
1. Membuat `forms.py` di direktori `main` dan isi dengan
   
   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["type", "name", "element", "amount", "power", "description"]
   ```
2. Buka folder `main` -> `views.py` dan tambahkan
   beberapa import

   ```
   from django.http import HttpResponseRedirect
   from main.forms import ProductForm
   from django.urls import reverse
   ```
   dan fungsi `add_card`

   ```
   def add_card(request):
       form = ProductForm(request.POST or None)
   
       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
   
       context = {'form': form}
       return render(request, "add_card.html", context)
   ```
3. Mengubah fungsi `show_main` menjadi

   ```
   def show_main(request):
       products = Product.objects.all()
   
       context = {
           'name': 'Fari', # Nama kamu
           'class': 'PBP A', # Kelas PBP kamu
           'products': products
       }
   
       return render(request, "main.html", context)
   ```
4. Buka `main` -> `urls.py`
   import fungsi `add_card`
   
   ```
   from main.views import show_main, add_card
   ```
   dan tambahkan *path url* ke dalam `urlpatterns`

   ```
   urlpatterns = [
       ...
       path('add-card', add_card, name='add_card'),
       ...
   ] 
   ```
# 5. HTML

### B. Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by ID*, dan JSON *by ID*
1. Buka `main` -> `views.py` dan tambahkan beberapa import

   ```
   from django.http import HttpResponse
   from django.core import serializers
   ```
2. Menambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id`

   ```
   def show_xml(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   
   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   
   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

### C. Membuat routing URL untuk masing - masing `views` yang telah ditambahkan pada poin 2
1. Buka `main` -> `urls.py` dan tambahkan ke 4 fungsi yang telah dibuat

   ```
   from main.views import show_main, add_card, show_xml, show_json, show_xml_by_id, show_json_by_id 
   ```
2. tambahkan masing - masing *path url* ke dalam `urlpatterns`

   ```
   urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'), # XML
    path('json/', show_json, name='show_json'), # JSON
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), # XML by ID
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), # JSON by ID
    ...
   ]
   ```
   
## *screenshot* dari hasil akses URL
