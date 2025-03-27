from django.shortcuts import render, redirect
from .models import Author, Publisher, Book
from .forms import BookForm
from django.db.models import Q
def manage_books(request):
    query = request.GET.get('query', '')
    books = None

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | 
            Q(authors__first_name__icontains=query) | 
            Q(authors__last_name__icontains=query)
        ).distinct()

    return render(request, 'base.html', {'books': books, 'query': query, 'content': 'manage_books'})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        publication_date = request.POST.get('publication_date')
        authors = request.POST.getlist('authors')
        publisher_id = request.POST.get('publisher')
        
        book = Book(title=title, publication_date=publication_date)
        publisher = Publisher.objects.get(id=publisher_id)
        book.publisher = publisher
        book.save()
        
        for author_id in authors:
            author = Author.objects.get(id=author_id)
            book.authors.add(author)
        
        return redirect('manage_books')
    
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    
    return render(request, 'base.html', {
        'content': 'add_book',
        'authors': authors,
        'publishers': publishers
    })

def add_author(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        Author.objects.create(first_name=first_name, last_name=last_name, email=email)
        return redirect('manage_books')

    return render(request, 'base.html', {'content': 'add_author'})

def add_publisher(request):
    if request.method == "POST":
        name = request.POST['name']
        street_address = request.POST['street_address']
        city = request.POST['city']
        state_province = request.POST['state_province']
        country = request.POST['country']
        website = request.POST['website']
        Publisher.objects.create(name=name, street_address=street_address,
                                 city=city, state_province=state_province,
                                 country=country, website=website)
        return redirect('manage_books')

    return render(request, 'base.html', {'content': 'add_publisher'})
