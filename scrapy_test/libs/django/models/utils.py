# django model constructor has pretty smart logic for mass assignment
def copy_django_model_attrs(instance_to_copy_to, class_, **kwargs):
  tmp_listing = class_(**kwargs)
  new_kwargs = dict(
    [
      (fld.name, getattr(tmp_listing, fld.name)) for fld in tmp_listing._meta.fields if
      fld.name != tmp_listing._meta.pk
    ]
  )
  for k, v in new_kwargs.items():
    setattr(instance_to_copy_to, k, v)
