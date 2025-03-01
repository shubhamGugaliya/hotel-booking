import pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})
print(df)

class Hotel:
    watermark = "real estate company" #class variable
    def __init__(self,hotel_id): #instance method
        self.hotel_id = hotel_id   #instance variable
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        """Bok the hotel by changing its availability to No"""
        df.loc[df['id'] == self.hotel_id, 'available'] ="no"
        df.to_csv("hotels.csv",index=False)

    def available(self): #instance method
        """Check if the hotel is available"""
        availability = df.loc[df['id']==self.hotel_id,'available'].squeeze()
        if availability =='yes':
            return True
        else:
            return False



    @classmethod
    def get_hotel_counts(cls,data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False
class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation
        Please find your reservation data:
        Name: {self.the_customer_name}
        Hotel name : {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount*1.2



hotel1 = Hotel(hotel_id="188")#creating an instance
hotel2 = Hotel(hotel_id="134")

print(hotel1.available()) #calling instance method
print(hotel1.name) #calling instance variable

print(hotel1.watermark) #calling class variable

print(Hotel.watermark) #calling class variable

print(Hotel.get_hotel_counts(data = df)) #calling class method

ticket = ReservationTicket(customer_name="john smith  ", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())