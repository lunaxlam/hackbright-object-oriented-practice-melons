############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        """Initialize a melon."""

        # Initialize a list to hold pairings info for each melon
        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def __repr__(self):
        """Return info about melon for MelonType() objects"""

        return f'MelonType("{self.code}", "{self.first_harvest}", "{self.color}", "{self.is_seedless}", "{self.is_bestseller}", "{self.name})'

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Return a list of current melon types."""

    # Initialize a list to store MelonType objects
    all_melon_types = []

    # Instantiate the MelonType objects
    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", False, "Unknown", "Casaba")
    crenshaw = MelonType("cren", 1996, "green", False, "Unknown", "Crenshaw")
    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")

    # Call the add_pairing method on each object to add necessary pairings to each instance's pairings attribute
    muskmelon.add_pairing("mint")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("prosciutto")
    yellow_watermelon.add_pairing("ice cream")

    # Add each MelonType object to our list
    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)

    # Because of the __repr__(), each MelonType() object will be printed as defined in the __repr__()
    return all_melon_types


def print_pairing_info(melon_types):
    """Print information about each melon type's pairings."""

    # Iterate for each MelonType() object instance
    for i, melon in enumerate(melon_types):
        print(f"{melon_types[i].name} pairs with")
        for pairing in melon_types[i].pairings:
            print(f"- {pairing}")
        print()


def make_melon_type_lookup(melon_types):
    """Take a list of MelonTypes and return a dictionary of melon type by code."""

    # Initialize an empty dictionary to store melon info
    melon_lookup = {}

    # Iterate for each MelonType() object instance
    for i, melon in enumerate(melon_types):
        # Set self.code as the key and self.name as the value
        melon_lookup[melon_types[i].code] = melon_types[i].name

    return melon_lookup


# # Call the functions
# melon = make_melon_types()
# print_pairing_info(melon)
# print(make_melon_type_lookup(melon))


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
