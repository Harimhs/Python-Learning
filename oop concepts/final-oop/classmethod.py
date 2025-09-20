class Example:
    class_var = "I am a class variable"

    @classmethod
    def modify_class_var(cls, new_value):
        cls.class_var = new_value  

    @classmethod
    def display_class_var(cls):
        print(cls.class_var)

# Accessing class variable via class method
Example.display_class_var()  # Output: I am a class variable

# Modifying class variable via class method
Example.modify_class_var("Updated class variable")
Example.display_class_var()  # Output: Updated class variable
