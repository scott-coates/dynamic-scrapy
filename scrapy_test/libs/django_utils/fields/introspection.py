# http://stackoverflow.com/questions/15339690/how-to-fix-django-south-issue-with-regards-to-localflavor-in-django-1-5
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^localflavor\.us\.models\.USStateField"])
add_introspection_rules([], ["^localflavor\.us\.models\.PhoneNumberField"])
