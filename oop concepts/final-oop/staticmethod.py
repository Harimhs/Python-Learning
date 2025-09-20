class Company:

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} is a {self.position}."
    
    @staticmethod
    def valid_data(position):
        valid_positions = ["CEO", "CTO", "CFO", "Manager", "Developer"]
        return position in valid_positions
    
company= Company("abc", "CEO")
print(company.get_info()) 
Company.valid_data("CFO")

