from jinja2 import Template
html = """
{%-macro get_input(name, type='text', placeholder='')-%}
    <input type='{{ type }}' name='{{name}}' placeholder='{{placeholder}}'>
{%-endmacro-%}
<p>{{get_input('firstname', placeholder='Имя')}}</p>
<p>{{get_input('lastname',placeholder='Фамилия')}}</p>
<p>{{get_input('address', placeholder='Адрес')}}</p>
<p>{{get_input('tel', type='tel', placeholder='Телефон')}}</p>
<p>{{get_input('email', type='email', placeholder='Почта')}}</p>
"""
tm = Template(html)
msg = tm.render()
print(msg)