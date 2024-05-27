from jinja2 import Template

dict = [
    {"href": "index", "page": "Главная"},
    {"href": "news", "page": "Новости"},
    {"href": "about", "page": "О компании"},
    {"href": "shop", "page": "Магазин"},
    {"href": "contacts", "page": "Контакты"}
]

page = """
<ul>
{% for li in dict -%}
<li href='/{{li.href}}' {%if li.page=="Главная"-%}  class='active'{%-endif-%}>{{li.page}}</li>
{%endfor-%}
</ul>
"""
web = Template(page)
viewer = web.render(dict=dict)
print(viewer)
