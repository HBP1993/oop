from re import A
import AutomotiveShopClass as a

def main():
    
    service_dict = {}
    name = input("Enter customer name: ")
    address = input("Enter Address: ")
    phone = input("Enter customer phone: ")
    customer_info = a.Customer(name, address, phone)

    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    car_info = a.Car(make, model, year)

    pcharges = int(input("Enter parts charges: "))
    lcharges = int(input("Enter labor charges: "))
    taxrate = float(input("Enter salestax rate: "))
    service_quote = a.ServiceQuote(pcharges, lcharges, taxrate)

    service_dict[customer_info.get_name()] = [
        customer_info.get_address(),
        customer_info.get_phone(),
        car_info.get_make(),
        car_info.get_model(),
        car_info.get_year(),
        service_quote.get_lcharges(),
        service_quote.get_pcharges(),
        service_quote.get_salestax(),
        service_quote.get_totalcharges(),
    ]

    print("Tax charges:  ", (service_quote.get_salestax()))
    print("Total charges:  ", (service_quote.get_totalcharges()))


main()