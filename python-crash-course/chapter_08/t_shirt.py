def make_shirt(size, text_message):
    print(f"\nThis is t-shirt is {size} \nand the message printed on it is: {text_message}")

make_shirt("L", "'This is a t-shirt'")


def make_shirt(size, text_message):
    print(f"\nThis is t-shirt is {size} \nand the message printed on it is: {text_message}")

make_shirt(size='L', text_message= "'This is a t-shirt")

def make_shirt(size="large", text_message="I love Python"):
    print(f"\nThis is t-shirt is {size} \nand the message printed on it is: {text_message}")

make_shirt()
make_shirt(size="medium")
make_shirt("small", "Readability counts.")