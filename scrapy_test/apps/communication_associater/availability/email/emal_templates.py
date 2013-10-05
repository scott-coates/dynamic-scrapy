import textwrap

subject_template = "{{ address }} Apartment"
body_template = textwrap.dedent("""\
Hi{% if contact %} {{ contact }}{% endif %},

I saw your listing on {{ source }} for an apartment at {{ address }} \
({% if bedroom_count %}{{bedroom_count|floatformat }} BR{% else %}studio{% endif %} \
for ${{ price|floatformat:\"-2\" }}). \
I'm interested in this apartment. Is it still available? If so, when can I see it? Can you tell me anything else
about the place?

Thanks,
{{ signature }}

{{ availability_identifier }}
""")
