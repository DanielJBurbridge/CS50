import csv
import sys
from datetime import datetime

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        print('loading... people')
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            # print(f'loaded person {people[row["id"]]["name"]}')
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        print('loading... movies')
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }
        # print(f'loaded movie {movies[row["id"]]["title"]}')

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        print('loading... connections')
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
                # print(f'loading connection {people[row["person_id"]]["name"]} -> {movies[row["movie_id"]]["title"]}')
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    while True:
        source = person_id_for_name(input("Name: "))
        if source is None:
            sys.exit("Person not found.")
        target = person_id_for_name(input("Name: "))
        if target is None:
            sys.exit("Person not found.")

        path = shortest_path(source, target)

        if path is None:
            print("Not connected.")
        else:
            degrees = len(path)
            print(f"{degrees} degrees of separation.")
            path = [(None, source)] + path
            for i in range(degrees):
                person1 = people[path[i][1]]["name"]
                person2 = people[path[i + 1][1]]["name"]
                movie = movies[path[i + 1][0]]["title"]
                print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):

    if source is None or target is None:
        print("Source or target not found.")
        return None

    frontier = QueueFrontier()
    frontier.add(Node(source, None, None))

    explored = set()

    time_started = datetime.utcnow().microsecond
    while True:
        if frontier.empty():
            return None

        node = frontier.remove()
        # print(f'Current Node being explored: {people[node.state]["name"]}')
        explored.add(node.state)
        if len(explored) % 100 == 0:
            print(f'Explored {len(explored)} connections')

        # print(node.state, target)
        if node.state == target:
            time_finished = datetime.utcnow().microsecond
            print(f'Time Taken to find connection {(time_finished - time_started).seconds} microseconds')
            return path_from_node(node)


        for (movie, person) in neighbors_for_person(node.state):
            if person not in explored and not frontier.contains_state(person):
            # print(f'From movie: {movie}, checking person: {person}')
                child = Node(person, node, movie)
                if child.state == target:
                    time_finished = datetime.utcnow().microsecond
                    print(f'Time Taken to find connection {str(time_finished - time_started) + " microseconds" if (time_finished - time_started < 1000) else (str(int(time_finished - time_started) / 1000)) + " seconds"}')
                    return path_from_node(child)
                frontier.add(child)



def path_from_node(node):

    """
    Returns a list of (movie_id, person_id) pairs that connect
    the source to the target.
    """

    path = []
    while node.parent is not None:
        path.append((node.action, node.state))
        node = node.parent

    path.reverse()
    return path

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
