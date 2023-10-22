class Star_Cinema:
    _hall_list = []

    def __init__(self) -> None:
        pass

    def entry_hall(self, hall):
        Star_Cinema._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)
        super().__init__()

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = []
        for _ in range(self.__rows):
            col = []
            for _ in range(self.__cols):
                col.append(0)
            self.__seats[id].append(col)

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("\nEntered Invalid Show ID!\n")
            return
        seat_map = self.__seats[show_id]

        for seat in seat_list:
            row, col = seat
            if not (0 < row < len(seat_map) + 1) or not (
                0 < col < len(seat_map[0]) + 1
            ):
                print("\nInvalid Seat\n")
                continue
            if seat_map[row - 1][col - 1] == 1:
                print("\nSeat is already booked\n")
                continue
            seat_map[row - 1][col - 1] = 1
            print("\nSuccessfully Ticket Booked\n")
            return

    def view_show_list(self):
        if len(self.__show_list) == 0:
            print("\nCurrently No Show Is Running\n")
            return
        for show in self.__show_list:
            print(f"\nShow ID:{show[0]}\tMovie:{show[1]}\tTime:{show[2]}")
        print("\n")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("\nEntered Invalid Show ID!\n")
            return
        seat_map = self.__seats[show_id]
        for i in seat_map:
            for j in i:
                print(j, end="\t")
            print("\n")


star = Star_Cinema()
star_hall = Hall(3, 5, "star")
star_hall.entry_show("jn", "Jawan", "Oct 22 2022 4:00 PM")
star_hall.entry_show("gg", "Guardian of the galaxy vol-3", "Oct 22 2022 8:00 PM")
star_hall.entry_show("dg", "Dream Girl 2", "Oct 22 2022 8:00 PM")

# print(star_hall.__dict__)

while True:
    print("1. View All Show")
    print("2. View Available Seat")
    print("3. Book Tickets")
    print("4. Exit")
    ch = int(input("ENTER OPTION: "))

    if ch == 1:
        star_hall.view_show_list()
    elif ch == 2:
        show_id = input("Enter Show ID: ")
        star_hall.view_available_seats(show_id)
    elif ch == 3:
        show_id = input("Enter Show ID: ")
        """ match = False
        for show in star_hall.__show_list:
            if show[0] == show_id:
                match = True
        if match == False:
            print("\nEntered Invalid Show ID!\n")
            continue """
        num_of_seats = int(input("Enter Number of Tickets:"))
        seats_to_book = []
        for _ in range(num_of_seats):
            row = int(input("Enter Row:"))
            col = int(input("Enter Column:"))
            star_hall.book_seats(show_id, [(row, col)])
    elif ch == 4:
        break
