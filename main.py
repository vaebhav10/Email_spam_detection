from src.preprocess import clean_text
from src.predict import predict

i=0
while True:
    if i%10 == 0 :
        print("To exit the program type 'exit'")
    i+=1
    text = input('Enter your Text/Email: ')
    text = clean_text(text)
    if text.lower()=='exit':
        print("Are you sure ? \nThis will close the program")
        request = input("Type 'yes' to confirm :")
        if request == 'yes':
            break
    print ('verdict: ', predict(text))
    print()