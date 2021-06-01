#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program determines the factorial of a number


def address(name, str_num, str_name, city, prov, post_code,
            apt_num=None):
    addresssx = name
    if apt_num is not None:
        addresssx = (addresssx + "\n" + apt_num + "-" + str_num +
                     " " + str_name + "\n" + city + " " + prov + "  "
                     + post_code)
    else:
        addresssx = (addresssx + "\n" + str_num + " " + str_name +
                     "\n" + city + " " + prov + "  " + post_code)

    return addresssx


def main():

    apt_num = None

    name = input("Please enter your name:")
    question = input("Do you live in an apartmen? yes or no: ")
    if question.upper() == "Yes" or question.upper() == "YES":
        apt_num = input("Enter your apartment number dipshit: ")
    str_num = input("Enter your street number:")
    str_name = input("Enter your street name and type: ")
    city = input("Enter your city: ")
    prov = input("Enter your province as 2 letters: ")
    post_code = input("Enter your postal code: ")

    if apt_num is not None:
        addressx = address(name.upper(), str_num.upper(),
                           str_name.upper(), city.upper(),
                           prov.upper(), post_code.upper(),
                           apt_num.upper())
    else:
        addressx = address(name.upper(), str_num.upper(),
                           str_name.upper(), city.upper(),
                           prov.upper(), post_code.upper())

    print(addressx)
    print("Thanks for playing<3")


if __name__ == "__main__":
    main()
