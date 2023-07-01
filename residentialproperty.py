from abc import ABC, abstractmethod


class ResidentialProperty:
    """
    A class representing a residential property.
    """

    total_properties = []  # List to store all residential properties
    reference_number = 0  # Counter to assign reference numbers to properties

    def __init__(self, address: str, built_up_area: float, num_of_bedrooms: int,
                 num_of_bathrooms: int, num_of_parking_slots=1,
                 pool_avail=False, gym_avail=False):
        """
        Initializes a new ResidentialProperty object.

        Args:
            address (str): The address of the property.
            built_up_area (float): The built-up area of the property in square units.
            num_of_bedrooms (int): The number of bedrooms in the property.
            num_of_bathrooms (int): The number of bathrooms in the property.
            num_of_parking_slots (int, optional): The number of parking slots available. Defaults to 1.
            pool_avail (bool, optional): Indicates if a pool is available. Defaults to False.
            gym_avail (bool, optional): Indicates if a gym is available. Defaults to False.
        """
        
        self.__reference_number = ResidentialProperty.reference_number + 1
        self.__address = address
        self.__built_up_area = built_up_area
        self.__num_of_bedrooms = num_of_bedrooms
        self.__num_of_bathrooms = num_of_bathrooms
        self.__num_of_parking_slots = num_of_parking_slots
        self.__pool_avail = pool_avail
        self.__gym_avail = gym_avail
        self.__agent_commission_percent = 0.02
        ResidentialProperty.reference_number += 1
        ResidentialProperty.total_properties.append(self)

    def getreference_number(self):
        """
        Returns the reference number of the property.

        Returns:
            int: The reference number.
        """
        return self.__reference_number

    @property
    def Address(self):
        """
        Gets the address of the property.

        Returns:
            str: The address.
        """
        return self.__address

    @Address.setter
    def Address(self, address):
        """
        Sets the address of the property.

        Args:
            address (str): The new address.
        """
        self.__address = address

    @property
    def Built_Up_Area(self):
        """
        Gets the built-up area of the property.

        Returns:
            float: The built-up area in square units.
        """
        return self.__built_up_area

    @Built_Up_Area.setter
    def Built_Up_Area(self, built_up_area):
        """
        Sets the built-up area of the property.

        Args:
            built_up_area (float): The new built-up area in square units.
        """
        self.__built_up_area = built_up_area

    @property
    def Number_of_Bedrooms(self):
        """
        Gets the number of bedrooms in the property.

        Returns:
            int: The number of bedrooms.
        """
        return self.__num_of_bedrooms

    @Number_of_Bedrooms.setter
    def Number_of_Bedrooms(self, num_of_bedrooms):
        """
        Sets the number of bedrooms in the property.

        Args:
            num_of_bedrooms (int): The new number of bedrooms.
        """
        self.__num_of_bedrooms = num_of_bedrooms

    @property
    def Number_of_Bathrooms(self):
        """
        Gets the number of bathrooms in the property.

        Returns:
            int: The number of bathrooms.
        """
        return self.__num_of_bathrooms

    @Number_of_Bathrooms.setter
    def Number_of_Bathrooms(self, num_of_bathrooms):
        """
        Sets the number of bathrooms in the property.

        Args:
            num_of_bathrooms (int): The new number of bathrooms.
        """
        self.__num_of_bathrooms = num_of_bathrooms

    @property
    def Number_of_Parking_Slots(self):
        """
        Gets the number of parking slots available in the property.

        Returns:
            int: The number of parking slots.
        """
        return self.__num_of_parking_slots

    @Number_of_Parking_Slots.setter
    def Number_of_Parking_Slots(self, num_of_parking_slots):
        """
        Sets the number of parking slots available in the property.

        Args:
            num_of_parking_slots (int): The new number of parking slots.
        """
        self.__num_of_parking_slots = num_of_parking_slots

    @property
    def Gym_Avail(self):
        """
        Checks if a gym is available in the property.

        Returns:
            bool: True if a gym is available, False otherwise.
        """
        return self.__gym_avail

    @Gym_Avail.setter
    def Gym_Avail(self, gym_avail):
        """
        Sets the availability of a gym in the property.

        Args:
            gym_avail (bool): True if a gym is available, False otherwise.
        """
        self.__gym_avail = gym_avail

    @property
    def Pool_Avail(self):
        """
        Checks if a pool is available in the property.

        Returns:
            bool: True if a pool is available, False otherwise.
        """
        return self.__pool_avail

    @Pool_Avail.setter
    def Pool_Avail(self, pool_avail):
        """
        Sets the availability of a pool in the property.

        Args:
            pool_avail (bool): True if a pool is available, False otherwise.
        """
        self.__pool_avail = pool_avail

    @property
    def AgentCommissionPercent(self):
        """
        Gets the agent commission percentage for the property.

        Returns:
            float: The agent commission percentage.
        """
        return self.__agent_commission_percent

    @AgentCommissionPercent.setter
    def AgentCommissionPercent(self, commission_percent=None):
        """
        Sets the agent commission percentage for the property.

        Args:
            commission_percent (float, optional): The new agent commission percentage. Defaults to None.
        """
        if commission_percent:
            self.__agent_commission_percent = commission_percent

    def print_attributes(self):
        """
        Prints all the attributes of the property.
        """
        attributes = vars(self)
        print("Attributes:")
        for attr, value in attributes.items():
            print(attr, ":", value)

            
            
class House(ResidentialProperty):
    """
    A class representing a house, which is a type of residential property.
    Inherits from the ResidentialProperty class.
    """

    def __init__(self, address, built_up_area, num_of_bedrooms,
                 num_of_bathrooms, num_of_floors, plot_size, house_type,
                 num_of_parking_slots=1, pool_avail=False, gym_avail=False):
        """
        Initializes a new House object.

        Args:
            address (str): The address of the house.
            built_up_area (float): The built-up area of the house in square units.
            num_of_bedrooms (int): The number of bedrooms in the house.
            num_of_bathrooms (int): The number of bathrooms in the house.
            num_of_floors (int): The number of floors in the house.
            plot_size (float): The size of the plot in square units.
            house_type (str): The type of the house.
            num_of_parking_slots (int, optional): The number of parking slots available. Defaults to 1.
            pool_avail (bool, optional): Indicates if a pool is available. Defaults to False.
            gym_avail (bool, optional): Indicates if a gym is available. Defaults to False.
        """
        super().__init__(address, built_up_area, num_of_bedrooms,
                         num_of_bathrooms, num_of_parking_slots,
                         pool_avail, gym_avail)
        self.__num_of_floors = num_of_floors
        self.__plot_size = plot_size
        self.__house_type = house_type

    @property
    def Number_of_Floors(self):
        """
        Gets the number of floors in the house.

        Returns:
            int: The number of floors.
        """
        return self.__num_of_floors

    @Number_of_Floors.setter
    def Number_of_Floors(self, num_of_floors):
        """
        Sets the number of floors in the house.

        Args:
            num_of_floors (int): The new number of floors.
        """
        self.__num_of_floors = num_of_floors

    @property
    def Plot_Size(self):
        """
        Gets the size of the plot for the house.

        Returns:
            float: The plot size in square units.
        """
        return self.__plot_size

    @Plot_Size.setter
    def Plot_Size(self, plot_size):
        """
        Sets the size of the plot for the house.

        Args:
            plot_size (float): The new plot size in square units.
        """
        self.__plot_size = plot_size

    @property
    def House_Type(self):
        """
        Gets the type of the house.

        Returns:
            str: The house type.
        """
        return self.__house_type

    @House_Type.setter
    def House_Type(self, house_type):
        """
        Sets the type of the house.

        Args:
            house_type (str): The new house type.
        """
        self.__house_type = house_type

class Apartment(ResidentialProperty):
    """
    A class representing an apartment, which is a type of residential property.
    Inherits from the ResidentialProperty class.
    """

    def __init__(self, address, built_up_area, num_of_bedrooms,
                 num_of_bathrooms, floor_num, num_of_balconies,
                 num_of_parking_slots=1, pool_avail=False, gym_avail=False):
        """
        Initializes a new Apartment object.

        Args:
            address (str): The address of the apartment.
            built_up_area (float): The built-up area of the apartment in square units.
            num_of_bedrooms (int): The number of bedrooms in the apartment.
            num_of_bathrooms (int): The number of bathrooms in the apartment.
            floor_num (int): The floor number of the apartment.
            num_of_balconies (int): The number of balconies in the apartment.
            num_of_parking_slots (int, optional): The number of parking slots available. Defaults to 1.
            pool_avail (bool, optional): Indicates if a pool is available. Defaults to False.
            gym_avail (bool, optional): Indicates if a gym is available. Defaults to False.
        """
        super().__init__(address, built_up_area, num_of_bedrooms,
                         num_of_bathrooms, num_of_parking_slots,
                         pool_avail, gym_avail)
        self.__floor_num = floor_num
        self.__num_of_balconies = num_of_balconies

    @property
    def FloorNumber(self):
        """
        Gets the floor number of the apartment.

        Returns:
            int: The floor number.
        """
        return self.__floor_num

    @FloorNumber.setter
    def FloorNumber(self, floor_num):
        """
        Sets the floor number of the apartment.

        Args:
            floor_num (int): The new floor number.
        """
        self.__floor_num = floor_num

    @property
    def NumberOfBalconies(self):
        """
        Gets the number of balconies in the apartment.

        Returns:
            int: The number of balconies.
        """
        return self.__num_of_balconies

    @NumberOfBalconies.setter
    def NumberOfBalconies(self, num_of_balconies):
        """
        Sets the number of balconies in the apartment.

        Args:
            num_of_balconies (int): The new number of balconies.
        """
        self.__num_of_balconies = num_of_balconies

        
class Rental:
    """
    A class representing a rental property.
    """

    @property
    def DepositAmount(self):
        """
        Gets the deposit amount for the rental property.

        Returns:
            float: The deposit amount.
        """
        return self.__deposit_amount

    @DepositAmount.setter
    def DepositAmount(self, deposit_amount):
        """
        Sets the deposit amount for the rental property.

        Args:
            deposit_amount (float): The deposit amount.
        """
        self.__deposit_amount = deposit_amount

    @property
    def YearlyRent(self):
        """
        Gets the yearly rent for the rental property.

        Returns:
            float: The yearly rent.
        """
        return self.__yearly_rent

    @YearlyRent.setter
    def YearlyRent(self, yearly_rent):
        """
        Sets the yearly rent for the rental property.

        Args:
            yearly_rent (float): The yearly rent.
        """
        self.__yearly_rent = yearly_rent

    @property
    def Furnished(self):
        """
        Checks if the rental property is furnished.

        Returns:
            bool: True if the property is furnished, False otherwise.
        """
        return self.__furnished

    @Furnished.setter
    def Furnished(self, furnished):
        """
        Sets the furnished status of the rental property.

        Args:
            furnished (bool): The furnished status.
        """
        self.__furnished = furnished

    @property
    def MaidRoom(self):
        """
        Checks if the rental property has a maid room.

        Returns:
            bool: True if the property has a maid room, False otherwise.
        """
        return self.__maid_room

    @MaidRoom.setter
    def MaidRoom(self, maid_room):
        """
        Sets the maid room status of the rental property.

        Args:
            maid_room (bool): The maid room status.
        """
        self.__maid_room = maid_room

    @abstractmethod
    def AgentCommissionValue(self):
        """
        Abstract method to calculate the agent commission value.
        Subclasses must implement this method.
        """
        pass

    
    
class Sale:
    """
    A class representing a sale property.
    """

    def __init__(self, sale_price, annual_service_charge):
        """
        Initializes a Sale property.

        Args:
            sale_price (float): The sale price of the property.
            annual_service_charge (float): The annual service charge of the property.
        """
        self.__sale_price = sale_price
        self.__annual_service_charge = annual_service_charge
        self.__fixed_tax_percent = 0.04

    @property
    def SalePrice(self):
        """
        Gets the sale price of the property.

        Returns:
            float: The sale price.
        """
        return self.__sale_price

    @SalePrice.setter
    def SalePrice(self, sale_price):
        """
        Sets the sale price of the property.

        Args:
            sale_price (float): The sale price.
        """
        self.__sale_price = sale_price

    @property
    def AnnualServiceCharge(self):
        """
        Gets the annual service charge of the property.

        Returns:
            float: The annual service charge.
        """
        return self.__annual_service_charge

    @AnnualServiceCharge.setter
    def AnnualServiceCharge(self, annual_service_charge):
        """
        Sets the annual service charge of the property.

        Args:
            annual_service_charge (float): The annual service charge.
        """
        self.__annual_service_charge = annual_service_charge

    @property
    def FixedTaxPercent(self):
        """
        Gets the fixed tax percentage for the property.

        Returns:
            float: The fixed tax percentage.
        """
        return self.__fixed_tax_percent

    @FixedTaxPercent.setter
    def FixedTaxPercent(self, fixed_tax_percent):
        """
        Sets the fixed tax percentage for the property.

        Args:
            fixed_tax_percent (float): The fixed tax percentage.
        """
        self.__fixed_tax_percent = fixed_tax_percent

    @abstractmethod
    def AgentCommissionValue(self):
        """
        Abstract method to calculate the agent commission value.
        Subclasses must implement this method.
        """
        pass

    def TaxValue(self):
        """
        Calculates the tax value for the property.

        Returns:
            float: The tax value.
        """
        return self.SalePrice * self.FixedTaxPercent

    
    
class RentalApartment(Rental, Apartment):
    """
    A class representing a rental apartment.
    Inherits from both the Rental and Apartment classes.
    """

    def __init__(self, address, built_up_area, num_of_bedrooms,
                 num_of_bathrooms, floor_num, num_of_balconies,
                 num_of_parking_slots=1, pool_avail=False, gym_avail=False):
        """
        Initializes a RentalApartment.

        Args:
            address (str): The address of the apartment.
            built_up_area (float): The built-up area of the apartment.
            num_of_bedrooms (int): The number of bedrooms in the apartment.
            num_of_bathrooms (int): The number of bathrooms in the apartment.
            floor_num (int): The floor number of the apartment.
            num_of_balconies (int): The number of balconies in the apartment.
            num_of_parking_slots (int, optional): The number of parking slots. Defaults to 1.
            pool_avail (bool, optional): Whether a pool is available. Defaults to False.
            gym_avail (bool, optional): Whether a gym is available. Defaults to False.
        """
        Apartment.__init__(self, address, built_up_area, num_of_bedrooms,
                           num_of_bathrooms, floor_num, num_of_balconies,
                           num_of_parking_slots, pool_avail, gym_avail)

    def AgentCommissionValue(self):
        """
        Calculates the agent commission value for the rental apartment.

        Returns:
            float: The agent commission value.
        """
        return self.YearlyRent * self.AgentCommissionPercent


class RentalHouse(Rental, House):
    """
    A class representing a rental house.
    Inherits from both the Rental and House classes.
    """

    def __init__(self, address, built_up_area, num_of_bedrooms,
                 num_of_bathrooms, num_of_floors, plot_size, house_type,
                 num_of_parking_slots=1, pool_avail=False, gym_avail=False):
        """
        Initializes a RentalHouse.

        Args:
            address (str): The address of the house.
            built_up_area (float): The built-up area of the house.
            num_of_bedrooms (int): The number of bedrooms in the house.
            num_of_bathrooms (int): The number of bathrooms in the house.
            num_of_floors (int): The number of floors in the house.
            plot_size (float): The plot size of the house.
            house_type (str): The type of house.
            num_of_parking_slots (int, optional): The number of parking slots. Defaults to 1.
            pool_avail (bool, optional): Whether a pool is available. Defaults to False.
            gym_avail (bool, optional): Whether a gym is available. Defaults to False.
        """
        House.__init__(self, address, built_up_area, num_of_bedrooms,
                       num_of_bathrooms, num_of_floors, plot_size, house_type,
                       num_of_parking_slots, pool_avail, gym_avail)

    def AgentCommissionValue(self):
        """
        Calculates the agent commission value for the rental house.

        Returns:
            float: The agent commission value.
        """
        return self.YearlyRent * self.AgentCommissionPercent


class SaleApartment(Sale, Apartment):
    """
    A class representing a sale apartment.
    Inherits from both the Sale and Apartment classes.
    """

    def __init__(self, address, built_up_area, num_of_bedrooms,
                 num_of_bathrooms, floor_num, num_of_balconies,
                 sale_price, annual_service_charge, num_of_parking_slots=1,
                 pool_avail=False, gym_avail=False):
        """
        Initializes a SaleApartment.

        Args:
            address (str): The address of the apartment.
            built_up_area (float): The built-up area of the apartment.
            num_of_bedrooms (int): The number of bedrooms in the apartment.
            num_of_bathrooms (int): The number of bathrooms in the apartment.
            floor_num (int): The floor number of the apartment.
            num_of_balconies (int): The number of balconies in the apartment.
            sale_price (float): The sale price of the apartment.
            annual_service_charge (float): The annual service charge of the apartment.
            num_of_parking_slots (int, optional): The number of parking slots. Defaults to 1.
            pool_avail (bool, optional): Whether a pool is available. Defaults to False.
            gym_avail (bool, optional): Whether a gym is available. Defaults to False.
        """
        Apartment.__init__(self, address, built_up_area, num_of_bedrooms,
                           num_of_bathrooms, floor_num, num_of_balconies,
                           num_of_parking_slots, pool_avail, gym_avail)
        Sale.__init__(self, sale_price, annual_service_charge)

    def AgentCommissionValue(self):
        """
        Calculates the agent commission value for the sale apartment.

        Returns:
            float: The agent commission value.
        """
        return self.SalePrice * self.AgentCommissionPercent


class SaleHouse(Sale, House):
    """
    A class representing a sale house.
    Inherits from both the Sale and House classes.
    """

    def __init__(self, address, built_up_area, num_of_bedrooms,
                 num_of_bathrooms, num_of_floors, plot_size, house_type,
                 sale_price, annual_service_charge, num_of_parking_slots=1,
                 pool_avail=False, gym_avail=False):
        """
        Initializes a SaleHouse.

        Args:
            address (str): The address of the house.
            built_up_area (float): The built-up area of the house.
            num_of_bedrooms (int): The number of bedrooms in the house.
            num_of_bathrooms (int): The number of bathrooms in the house.
            num_of_floors (int): The number of floors in the house.
            plot_size (float): The plot size of the house.
            house_type (str): The type of house.
            sale_price (float): The sale price of the house.
            annual_service_charge (float): The annual service charge of the house.
            num_of_parking_slots (int, optional): The number of parking slots. Defaults to 1.
            pool_avail (bool, optional): Whether a pool is available. Defaults to False.
            gym_avail (bool, optional): Whether a gym is available. Defaults to False.
        """
        House.__init__(self, address, built_up_area, num_of_bedrooms,
                       num_of_bathrooms, num_of_floors, plot_size, house_type,
                       num_of_parking_slots, pool_avail, gym_avail)
        Sale.__init__(self, sale_price, annual_service_charge)

    def AgentCommissionValue(self):
        """
        Calculates the agent commission value for the sale house.

        Returns:
            float: The agent commission value.
        """
        return self.SalePrice * self.AgentCommissionPercent
