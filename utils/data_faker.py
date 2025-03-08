from faker import Faker

class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_user(self):
        return {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.password(length=12),
            "address": self.fake.address(),
            "phone_number": self.fake.phone_number()
        }
    
    def generate_payment_details(self):
        return {
            "card_number": self.fake.credit_card_number(),
            "card_expiry": self.fake.credit_card_expire(),
            "cvv": self.fake.credit_card_security_code(),
            "billing_address": self.fake.address()
        }