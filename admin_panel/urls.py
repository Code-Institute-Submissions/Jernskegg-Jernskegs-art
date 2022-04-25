from django.urls import path
from . import views

urlpatterns = [

    # overview
    path(
        '',
        views.get_admin_panel_overview,
        name='adminpanel'
        ),

    # Request List
    path(
        'request-list',
        views.get_admin_panel_requests,
        name='request_list'
        ),

    # Purchase History
    path(
        'purchase-history',
        views.get_admin_panel_purchase_history,
        name='purchase_history'
        ),

    # Contact Inquiries
    path(
        'contact-inquiries',
        views.get_admin_panel_contact_inquiries,
        name='contact_inquiries'
        ),

    # Products
    path(
        'products',
        views.get_admin_panel_products,
        name='products'
        ),

    # Update products
    path(
        'products/update/<item_id>',
        views.update_product,
        name='update_product'
        ),
]
