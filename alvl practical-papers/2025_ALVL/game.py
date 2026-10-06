# Task 2.1
class Room:
    def __init__(self, north_exit, east_exit, south_exit, west_exit):
        self.north_exit = north_exit
        self.east_exit = east_exit
        self.south_exit = south_exit
        self.west_exit = west_exit
    
    def get_exit(self, ch):
        if ch == 'N':
            return self.north_exit
        if ch == 'S':
            return self.south_exit
        
        if ch == 'E':
            return self.east_exit
        
        if ch == 'W':
            return self.west_exit
        
class Start(Room):
    def __init__(self, north_exit, east_exit, south_exit, west_exit, start_text):
        super().__init__(north_exit, east_exit, south_exit, west_exit)
        self.start_text = start_text

    def get_message(self):
        to_return = ["Start", self.start_text]
        if self.north_exit != -1:
            to_return.append('There is a door to the North')
        if self.east_exit != -1:
            to_return.append('There is a door to the East')
        if self.south_exit != -1:
            to_return.append('There is a door to the South')
        if self.west_exit != -1:
            to_return.append('There is a door to the West')        

        return to_return
    
class Finish(Room):
    def __init__(self, north_exit, east_exit, south_exit, west_exit, finish_text):
        super().__init__(north_exit, east_exit, south_exit, west_exit)
        self.finish_text = finish_text

    def get_message(self):
        return ["Finish", self.finish_text]
    
class Normal(Room):
    def __init__(self, north_exit, east_exit, south_exit, west_exit, question, answer):
        super().__init__(north_exit, east_exit, south_exit, west_exit)
        self.question = question
        self.answer = answer

    def get_question(self):
        return self.question
    
    def check_answer(self, user_answer):
        return user_answer == self.answer

    def get_message(self):
        to_return = ['Normal']
        if self.north_exit != -1:
            to_return.append('There is a door to the North')
        if self.east_exit != -1:
            to_return.append('There is a door to the East')
        if self.south_exit != -1:
            to_return.append('There is a door to the South')
        if self.west_exit != -1:
            to_return.append('There is a door to the West') 
        return to_return

# Task 2.2
def read_data():
    with open('/workspaces/exam_papers/2025_w_soln/2025_ALVL/resources/rooms.txt') as f:
        data = f.readlines()
        data = [i.strip().split(',') for i in data]

    room_list = []

    for i in data:
        room_type = i[0]
        north_room = int(i[1])
        east_room = int(i[2])
        south_room = int(i[3])
        west_room = int(i[4])
        room_text = i[5]
        if room_type == 'Start':
            room_list.append(Start(north_room,east_room,south_room,west_room,room_text))
        elif room_type == 'Finish':
            room_list.append(Finish(north_room,east_room,south_room,west_room,room_text))
        elif room_type == 'Normal':
            answer = i[6]
            room_list.append(Normal(north_room,east_room,south_room,west_room,room_text,answer))

    return room_list


for r in read_data():
    print(type(r),r.get_message())

# Task 2.3
# Write your code here
room_list = read_data()

current_room = room_list[0]
while True: 
    for tx in current_room.get_message():
        print(tx)
    if current_room.get_message()[0] == 'Finish':
        break
    elif current_room.get_message()[0] == 'Normal':
        print(current_room.get_question())
        correct_answer = False
        while not correct_answer:
            user_ans = input('Please give your answer:')
            if current_room.check_answer(user_ans):
                print('Your answer is correct.')
                break
            else:
                print('Your answer is incorrect. Please try again.')
        
    valid = False
    while not valid:
        user_exit = input('Please choose a valid exit (N,E,S,W):')
        if user_exit == 'N' and current_room.north_exit != -1:
            print(f'going to room {current_room.north_exit}')
            current_room = room_list[current_room.north_exit]
            valid = True
        elif user_exit == 'E' and current_room.east_exit != -1:
            print(f'going to room {current_room.east_exit}')
            current_room = room_list[current_room.east_exit]
            valid = True
        elif user_exit == 'S' and current_room.south_exit != -1:
            print(f'going to room {current_room.south_exit}')
            current_room = room_list[current_room.south_exit]
            valid = True
        elif user_exit == 'W' and current_room.west_exit != -1:
            print(f'going to room {current_room.west_exit}')
            current_room = room_list[current_room.west_exit]
            valid = True
        elif user_exit == 'X':
            break

    