from django.contrib import admin

from .models import Category, Topping, Wrapper, IceCream

admin.site.empty_value_display = 'Не задано'

class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'output_order'
    )
    list_editable = (
        'slug',
        'output_order'
    )
    list_display_links=('title',)
    inlines = (
        IceCreamInline,
    )

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'output_order'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
        'output_order'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream, IceCreamAdmin)
