class Doctor:
    def __init__(self, first_name, surname, speciality):
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def __str__(self):
        full_name = f"{self.__first_name} {self.__surname}"
        return f"{full_name:<30}| {self.__speciality}"


class Admin:
    def view(self, a_list):
        for index, item in enumerate(a_list):
            print(f"{index + 1:3}| {item}")

    def find_index(self, index, doctors):
        if index in range(0, len(doctors)):
            return True
        else:
            return False
        

    def test_update(self, doctors):
        while True:
            print("-----Update Doctor's Details-----")
            print("ID | Full name                     | Speciality")
            self.view(doctors)

            try:
                index = int(input("Enter the ID of the doctor: ")) - 1
                doctor_exists = self.find_index(index, doctors)
                if doctor_exists:
                    break
                else:
                    print("Doctor not found")

            except ValueError:
                print("The ID entered is incorrect")
                
        #     elif op == '3':
        # while True:
        #     print("-----Update Doctor`s Details-----")
        #     print('ID |          Full name           |  Speciality')
        #     self.view(doctors)
        #     try:
        #         index = int(input('Enter the ID of the doctor: ')) - 1
        #         doctor_index=self.find_index(index,doctors)
        #         if doctor_index!=False:
            
        #             break
    
                
                
                

        print("Choose the field to be updated:")
        print("1 First name")
        print("2 Surname")
        print("3 Speciality")

        try:
            option = int(input("Input: "))

            if option == 1:
                new_first_name = input("Enter the new first name: ")
                print("Updating doctors[", doctor_exists, "]")
                doctors[index].set_first_name(new_first_name)

            elif option == 2:
                new_surname = input("Enter the new surname: ")
                doctors[index].set_surname(new_surname)

            elif option == 3:
                new_speciality = input("Enter the new speciality: ")
                doctors[index].set_speciality(new_speciality)

            else:
                print("Invalid update option")
                return

            print("\nDoctor updated successfully.")
            print("-----Updated Doctors-----")
            self.view(doctors)

        except ValueError:
            print("Please enter 1, 2, or 3.")


doctors = [
    Doctor("John", "Smith", "Internal Medicine"),
    Doctor("Jone", "Smith", "Paediatrics"),
    Doctor("Jone", "Carlos", "Cardiology")
]

admin = Admin()
admin.test_update(doctors)