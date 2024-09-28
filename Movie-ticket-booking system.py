def initialize_seat_matrix():
    return [['O' for _ in range(5)] for _ in range(5)]  

def display_seat_matrix(seats):
    print("\nCurrent seat availability (O = Available, X = Booked):")
    for row in seats:
        print(' '.join(row))
    print()  
    

def select_seats(seats, num_tickets):
    selected_seats = []
    for _ in range(num_tickets):
        try:
            row = int(input("Enter seat row (1-5): ")) - 1
            col = int(input("Enter seat column (1-5): ")) - 1
            if seats[row][col] == 'O':
                seats[row][col] = 'X' 
                selected_seats.append((row + 1, col + 1))  
                print(f"Seat ({row + 1}, {col + 1}) successfully booked.")
                display_seat_matrix(seats)  
            else:
                print("Seat is already booked, please select another seat.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please select a valid seat.")
            continue
    return selected_seats

def t_movie():
    print("Which movie do you want to watch?")
    print("1. Kalki 2898 AD")
    print("2. Devara Part 1")
    print("3. Okkadu Re-Release")
    print("4. Back")
    
    try:
        movie = int(input("Choose your movie (1-4): "))
        if movie == 4:
            center()  
        else:
            theater()  
    except ValueError:
        print("Invalid input, please choose a valid option.")
        t_movie()

def theater():
    print("Which screen do you want to watch the movie on?")
    print("1. SCREEN 1")
    print("2. SCREEN 2")
    print("3. SCREEN 3")
    
    try:
        screen = int(input("Choose your screen (1-3): "))
        tickets = int(input("Number of tickets you want?: "))
        timing(screen, tickets)
    except ValueError:
        print("Invalid input, please enter valid choices.")
        theater()

def timing(screen, num_tickets):
    time1 = {
        "1": "10:00AM - 1:00PM",
        "2": "1:10PM - 4:10PM",
        "3": "4:20PM - 7:20PM",
        "4": "7:30PM - 10:30PM"
    }
    time2 = {
        "1": "10:15AM - 1:15PM",
        "2": "1:25PM - 4:25PM",
        "3": "4:35PM - 7:35PM",
        "4": "7:45PM - 10:45PM"
    }
    time3 = {
        "1": "10:30AM - 1:30PM",
        "2": "1:40PM - 4:40PM",
        "3": "4:50PM - 7:50PM",
        "4": "8:00PM - 10:45PM"
    }

    time_options = {1: time1, 2: time2, 3: time3}

    if screen in time_options:
        print("Choose your time:")
        for k, v in time_options[screen].items():
            print(f"{k}. {v}")
        try:
            time_choice = input("Select your time (1-4): ")
            if time_choice in time_options[screen]:
                print(f"Selected time: {time_options[screen][time_choice]}")
                seats = initialize_seat_matrix()  
                display_seat_matrix(seats)  
                selected_seats = select_seats(seats, num_tickets)  
                print(f"Successfully booked seats: {selected_seats}")
                print(f"Enjoy your movie at {time_options[screen][time_choice]}!")
            else:
                print("Invalid time selection. Please try again.")
                timing(screen, num_tickets)
        except KeyError:
            print("Invalid input. Please select a valid time.")
            timing(screen, num_tickets)
    else:
        print("Invalid screen choice.")
        theater()

def movie(theater_choice):
    if theater_choice in [1, 2, 3]:
        t_movie()
    elif theater_choice == 4:
        city()  
    else:
        print("Invalid choice.")
        center()

def center():
    print("Which theater do you wish to see a movie at?")
    print("1. PVR INOX")
    print("2. Asian ALLU ARJUN")
    print("3. Asian Mahesh Babu")
    print("4. Back")
    
    try:
        choice = int(input("Choose your option (1-4): "))
        movie(choice)
    except ValueError:
        print("Invalid input, please choose a valid option.")
        center()

def city():
    print("Hi, welcome to movie ticket booking!")
    print("Where do you want to watch a movie?")
    print("1. Bengaluru")
    print("2. Hyderabad")
    print("3. Chennai")
    
    try:
        place = int(input("Choose your option (1-3): "))
        if place in [1, 2, 3]:
            center()
        else:
            print("Invalid choice, please select again.")
            city()
    except ValueError:
        print("Invalid input, please enter a number.")
        city()
city() 