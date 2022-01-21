from collections import deque

# Graph is represented by a dictionary
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anju_mango', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom_mango', 'jonny']
graph['anju_mango'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_mango_seller(name):
    return name.find('mango') > -1


"""
 algorithm [Breadth first search]
    * needs a double-ended-queue for searching through
    * needs an array for already searched elements
"""


def df_search(name):
    search_queue = deque()
    searched = []

    # begin with `name` connections 'you' => [..., ...., ....]
    search_queue += graph[name]
    while search_queue:
        # pick up an element from queue
        person = search_queue.popleft()
        # check if this element already searched before
        if person not in searched:
            if person_is_mango_seller(person):
                print(person + ': is a mongo seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False


df_search('you')
