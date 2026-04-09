def generate_class(self, name, traits):

    attrs = dict(traits)

    return type(name, (object,), attrs)