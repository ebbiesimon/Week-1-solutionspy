def calculate_ac_load():
    space_size = float(input("Enter the size of the space in square meters: "))
    num_people = int(input("Enter the number of people in the space: "))

    ac_load_per_person = 0.1  # Assuming 100 watts per person
    ac_load_per_area = 25  # Assuming 25 watts per square meter

    total_ac_load = (ac_load_per_person * num_people) + (ac_load_per_area * space_size)
    print(f"The estimated AC load required is {total_ac_load} watts.")

calculate_ac_load()