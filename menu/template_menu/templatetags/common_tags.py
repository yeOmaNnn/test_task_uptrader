from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, title):
    request = context['request']
    if len(request.path) > 1:
        node_query = lambda x: f'''SELECT {x} FROM "template_menu_menuitem"
                        WHERE "template_menu_menuitem". "url" = '{request.path}'
                        ORDER BY "template_menu_menuitem". "tree_id" ASC, "template_menu_menuitem". "parent_id" ASC, "template_menu_menuitem". "lft" ASC
                        LIMIT 1'''
        menu_items_query = f'''SELECT * FROM "template_menu_menuitem"
        WHERE ("template_menu_menuitem"."lft" >=( {node_query("lft")}) AND "template_menu_menuitem"."rght" <= ({node_query("rght")} )
        AND "template_menu_menuitem"."tree_id" =( {node_query("tree_id")}))
        ORDER BY "template_menu_menuitem"."tree_id" ASC, "template_menu_menuitem"."lft" ASC'''
        menu_items=[]
        for obj in MenuItem.objects.raw(menu_items_query):
            menu_items.append(obj)
        #menu_items = MenuItem.objects.get_queryset_descendants(queryset=MenuItem.objects.filter(url=request.path),include_self=True)
    else:
        menu_items = MenuItem.objects.all()
    return {
        "path": request.path,
        "menu_items": menu_items,
        "title": title,
    }
