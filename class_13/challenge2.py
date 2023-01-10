import copy

meal1 = ['bread', 'cheese']
meal2 = meal1

if __name__ == "__main__":
    print(f'Original Meal 1: {meal1}')
    # Expected: ['bread', 'cheese']
    print(f'Original Meal 2: {meal2}')
    # Expected: ['bread', 'cheese']
    print("Appending Turkey to meal 1")
    meal1.append('turkey')
    print(f'New Meal 1: {meal1}')
    # Expected: ['bread', 'cheese', 'turkey']
    print(f'New Meal 2: {meal2}')
    # Expected: ['bread', 'cheese', 'turkey']
    print(id(meal1)), print(id(meal2))
    # Expected: 2356896337288, 2356896337288
    print("Instead lets do an copy by value")
    meal2 = copy.copy(meal1)
    meal1.append('Ham')
    print(f'Updated Meal 1: {meal1}')  
    # Expected: ['bread', 'cheese', 'turkey', 'ham']
    print(f'Updated Meal 2: {meal2}') 
    # Expected: ['bread', 'cheese', 'turkey']
    print(id(meal1)), print(id(meal2))