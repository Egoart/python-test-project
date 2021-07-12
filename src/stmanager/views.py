from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth import get_user_model
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from refshelf import models as refmodels
from books import models as bookmodels
from orders import models as ordermodels
from carts import models as cartmodels
from users import models as usermodel


#Edit Authors

class AuthorCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView ):
    model = refmodels.Authors
    fields = ['first_name', 'last_name', 'picture']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class AuthorUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = refmodels.Authors
    fields = ['first_name', 'last_name', 'picture']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class AuthorDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = refmodels.Authors
    success_url = reverse_lazy('refshelf:authors')

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

#Edit Genre

class GenreCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = refmodels.Genre
    fields = ['genre_name', 'genre_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class GenreUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = refmodels.Genre
    fields = ['genre_name', 'genre_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class GenreDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = refmodels.Genre
    success_url = reverse_lazy('refshelf:genres')

    def test_func(self):
        return self.request.user.profile.sale_staff == True

#Edit Publisher

class PublisherCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = refmodels.Publisher
    fields = ['publisher_name', 'publisher_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class PublisherUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = refmodels.Publisher
    fields = ['publisher_name', 'publisher_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class PublisherDelete(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = refmodels.Publisher
    success_url = reverse_lazy('refshelf:publishers')

    def test_func(self):
        return self.request.user.profile.sale_staff == True

#Edit Series

class SeriesCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = refmodels.BookSeries
    fields = ['series_name', 'series_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class SeriesUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = refmodels.BookSeries
    fields = ['series_name', 'series_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class SeriesDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = refmodels.BookSeries
    success_url = reverse_lazy('refshelf:serieses')

    def test_func(self):
        return self.request.user.profile.sale_staff == True


#Edit book

class BookCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = bookmodels.Book
    fields = '__all__'

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class BookUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = bookmodels.Book
    fields = '__all__'

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class BookDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = bookmodels.Book
    success_url = reverse_lazy('books:books')

    def test_func(self):
        return self.request.user.profile.sale_staff == True

# def resource_create(request):
#     return render(request, 'stmanager/create_res.html')



class ViewOrders(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ordermodels.Order
    template_name = 'stmanager/create_res.html'

    def test_func(self):
        return self.request.user.profile.sale_staff == True

    def get_queryset(self):
        qs = super().get_queryset()
        status_chk = self.request.GET.get('status_chk')
        print(status_chk)
        if status_chk:
            return qs.filter(order_status__contains=status_chk) 
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = usermodel.Profile.objects.all()
        return context

class UpdateOrderStatus(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ordermodels.Order
    fields = ['order_status']
    template_name = 'stmanager/order_status_form.html'

    def test_func(self):
        return self.request.user.profile.sale_staff == True


class CartItemsDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = cartmodels.Cart
    template_name='stmanager/cart_ordered.html'

    def test_func(self):
        return self.request.user.profile.sale_staff == True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = int(self.kwargs.get('pk'))
        context['order_detail'] = ordermodels.Order.objects.get(cart=cart_id)
        return context

