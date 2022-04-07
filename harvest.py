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
        """Return info about melon for MelonType() objects."""

        return f'MelonType("{self.code}", "{self.first_harvest}", "{self.color}", "{self.is_seedless}", "{self.is_bestseller}", "{self.name}")'

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Return a list of current melon types."""

    # Initialize a list to store all MelonType objects
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
# print(melon)
# print_pairing_info(melon)
# print(make_melon_type_lookup(melon))


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape, color, harvested_from, harvester):
        """Initiialize a Melon."""

        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.harvested_from = harvested_from
        self.harvester = harvester


    def __repr__(self):
        """Return info about melon for Melon() objects."""

        return f'Melon("{self.melon_type}", "{self.shape}", "{self.color}", "{self.harvested_from}", "{self.harvester}")'
    

    def is_sellable(self, shape, color):
        """Return True if melon is sellable."""

        # If melon shape and color ratings are greater than 5
        if self.shape and self.color > 5:
            # AND if melon was not harvested from Field 3
            if self.harvested_from != 3:
                return True
        
        # In all other cases return False
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Initialize a list to store all Melon objects
    all_melons = []

    # Get melon codes as a key from make_melon_types dictionary object by calling make_melon_type_lookup and passing melon_types
    melons_by_id = make_melon_type_lookup(melon_types)

    # Instantiate the Melon objects
    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")


    # Add each Melon object to our list
    all_melons.append(melon_1)
    all_melons.append(melon_2)
    all_melons.append(melon_3)
    all_melons.append(melon_4)
    all_melons.append(melon_5)
    all_melons.append(melon_6)
    all_melons.append(melon_7)
    all_melons.append(melon_8)
    all_melons.append(melon_9)

    # Because of the __repr__(), each Melon() object will be printed as defined in the __repr__()
    return all_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Iterate through list of Melon objects
    for i, melon in enumerate(melons):
        # Call the .is_sellable method on each object instance and store result
        result = melons[i].is_sellable(melons[i].shape, melons[i].color)

        # Check condition and print out corresponding message
        if result == True:
            print(f"Harvested by {melons[i].harvester} from Field {melons[i].harvested_from} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melons[i].harvester} from Field {melons[i].harvested_from} (NOT SELLABLE)")


#Call the functions
melon = make_melon_types()
all_melons = make_melons(melon)
get_sellability_report(all_melons)
