import os

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':

    # put your desired phone number into the string!

    phone_number = input("Enter your Friend's Phone Number with country code e.g +923001001010: ")
    print("\nEntered Number is: ",phone_number)
    words = get_words('miracle.txt')
    for word in words:
        send_message(phone_number, word)