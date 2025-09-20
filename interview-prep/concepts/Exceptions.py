try:
    result = 2/0

except:
    print("An error occurred bro!")

finally:
    print("This is the finally block bro!")

try:
    raise Exception("Something went wrong bro!")
except Exception as e:
    print(f"An error occurred: {e}")