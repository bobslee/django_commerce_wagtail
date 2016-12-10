from django.shortcuts import redirect
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _

from treebeard.admin import TreeAdmin

from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup
from wagtail.contrib.modeladmin.views import CreateView, EditView, IndexView
from wagtail.wagtailadmin import messages
from wagtail.wagtailcore.models import Page

from .models import Product, ProductIndexPage, ProductPage, Category, CategoryIndexPage, CategoryPage
from .views import IndexTree

"""
Product
"""
class ProductCreateView(CreateView):
    
    def form_valid(self, form):
        instance = form.save()

        if form.data.get('create_page', False) == 'on':
            parent_page = Page.objects.type(ProductIndexPage).first()
            product_page = ProductPage(
                title = instance.title,
                image = instance.image,
            )
        
            parent_page.add_child(instance=product_page)
            instance.product_page = product_page
            instance.save()
        
        messages.success(
            self.request, self.get_success_message(instance),
            buttons=self.get_success_message_buttons(instance)
        )
        return redirect(self.get_success_url())

class ProductEditView(EditView):

    def get_page_title(self):
        return "%s %s" % (self.page_title, self.opts.verbose_name)
    
    def form_valid(self, form):
        instance = form.save()

        if form.data.get('create_page', False) == 'on':
            parent_page = Page.objects.type(ProductIndexPage).first()
            product_page = ProductPage(
                title = instance.title,
                image = instance.image,
            )
        
            parent_page.add_child(instance=product_page)
            instance.product_page = product_page
            instance.save()
        else:
            if form.data.get('image'):
                instance.product_page.image = instance.image
                instance.product_page.save()
        
        messages.success(
            self.request, self.get_success_message(instance),
            buttons=self.get_success_message_buttons(instance)
        )
        return redirect(self.get_success_url())

class ProductModelAdmin(ModelAdmin):
    model = Product
    create_view_class = ProductCreateView
    edit_view_class = ProductEditView
    menu_icon = 'fa-product-hunt'

    # TODO: add date_published (from ProductPage)
    list_display = ['title', 'image', 'sale_price', 'product_page', 'sku', 'ean']
    search_fields = ('title', 'product_page', 'sku', 'ean',)
    form_view_extra_css = [static('wagtailcommerce/css/core.css')]

"""
Category
"""
class CategoryIndexView(IndexView):

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryIndexView, self).get_context_data(*args, **kwargs)
        context.update({'cl': IndexTree(self.request, self.model, self.model_admin)})
        
        return context

class CategoryCreateView(CreateView):
    def form_valid(self, form):
        instance = form.save()

        if form.data.get('create_page', False) == 'on':
            parent_page = instance.get_parent().category_page
            category_page = CategoryPage(
                title = instance.title,
                image = instance.image,
            )
        
            parent_page.add_child(instance=category_page)
            instance.category_page = category_page
            instance.save()
        
        messages.success(
            self.request, self.get_success_message(instance),
            buttons=self.get_success_message_buttons(instance)
        )
        return redirect(self.get_success_url())

class CategoryEditView(EditView):

    def get_page_title(self):
        return "%s %s" % (self.page_title, self.opts.verbose_name)
    
    def form_valid(self, form):
        instance = form.save()

        if form.data.get('create_page', False) == 'on':
            parent_page = instance.get_parent().category_page
            category_page = CategoryPage(
                title = instance.title,
                image = instance.image,
            )
        
            parent_page.add_child(instance=category_page)
            instance.category_page = category_page
            instance.save()
        else:
            if form.data.get('image'):
                instance.category_page.image = instance.image
                instance.category_page.save()
        
        messages.success(
            self.request, self.get_success_message(instance),
            buttons=self.get_success_message_buttons(instance)
        )
        return redirect(self.get_success_url())

# TODO PR to wagtail(contrib.modeladmin)?
class TreeModelAdmin(ModelAdmin, TreeAdmin):
    """Wagtail Admin class for treebeard."""

    def get_queryset(self, request):
        return self.model.get_tree()
    
    def get_node(self, node_id):
        return self.model.objects.get(pk=node_id)
    
class CategoryModelAdmin(TreeModelAdmin):
    model = Category
    index_view_class = CategoryIndexView
    index_template_name = 'treebeard/admin/tree_change_list.html'
    
    index_view_extra_css = (
        'admin/css/base.css',
        'admin/css/changelists.css',
        'treebeard/treebeard-admin.css',
    )

    index_view_extra_js = (
        'treebeard/treebeard-admin.js'
    )
    
    create_view_class = CategoryCreateView
    edit_view_class = CategoryEditView
    menu_icon = 'fa-tag'

    # TODO: add date_published (from ProductPage)
    list_display = ['title', 'image', 'category_page']
    search_fields = ('title', 'category_page')
    form_view_extra_css = [static('wagtailcommerce/css/core.css')]

"""
Commerce Main
"""
class CommerceModelAdminGroup(ModelAdminGroup):
    menu_label = _('Commerce')
    menu_icon = 'fa-cube'
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (CategoryModelAdmin, ProductModelAdmin)
