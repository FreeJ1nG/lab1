from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
  return render(
    request,
    "wishlist.html",
    {
      'list_barang': BarangWishlist.objects.all(),
      'nama': "Andrew Jeremy"
    }
  )