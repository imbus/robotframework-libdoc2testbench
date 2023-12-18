class PKGenerator:
    """A class used to generate unique primary keys for test elements.
    Only one instance should be created and used to ensure continuous
    unique pks."""

    def __init__(self, first_pk: int = 230):
        self.pk_counter = first_pk

    def get_pk(self) -> str:
        self.pk_counter += 1
        return str(self.pk_counter)
