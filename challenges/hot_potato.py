# Functions that you have implemented in the Queue section

def enqueue(queue, new_item):
    queue.append(new_item)


def dequeue(queue):
    # We have added return here, just to return the item that is being removed
    return queue.pop(0)


def is_empty(queue):
    return len(queue) == 0


def size(queue):
    return len(queue)


# Do not change code above this line

def hot_potato_simulator(players, turns):
    hot_potato_queue = []

    for player in players:
        enqueue(hot_potato_queue, player)  # Using enqueue function add a player to the queue

    while size(hot_potato_queue) > 1:  # Using size function check how many elements are there in the queue
        print("Start", hot_potato_queue)
        for i in range(turns):
            player = dequeue(hot_potato_queue)
            enqueue(hot_potato_queue, player)  # Enqueue the next-to-last element from the queue to the end

            print(f"\tturn {i}: flip {player}:", hot_potato_queue)
        n = dequeue(hot_potato_queue)  # Dequeue the HOT POTATO player
        print(f"deque {n}:", hot_potato_queue)

        print("End", hot_potato_queue)
    return dequeue(hot_potato_queue)  # Dequeue last element from the queue (The winner)


# Do not change code below this line
players = ["Peter", "John", "Luka", "Maria", "Sophia", "Derek"]
turns = 10
print(hot_potato_simulator(players, turns))
