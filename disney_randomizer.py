import random

# List of full-length Pixar and Disney movies
pixar_movies = [
    "Toy Story", "Toy Story 2", "Toy Story 3", "Toy Story 4",
    "A Bug’s Life",
    "Monsters, Inc.", "Monsters University",
    "Finding Nemo", "Finding Dory",
    "The Incredibles", "Incredibles 2",
    "Cars", "Cars 2", "Cars 3",
    "Ratatouille", "WALL·E", "Up", "Brave", "Inside Out",
    "The Good Dinosaur", "Coco", "Onward", "Soul", "Luca",
    "Turning Red", "Lightyear", "Elemental"
]

disney_movies = [
    "Snow White and the Seven Dwarfs", "Pinocchio", "Fantasia", "Dumbo", "Bambi",
    "Cinderella", "Cinderella II: Dreams Come True", "Cinderella III: A Twist in Time",
    "Alice in Wonderland", "Peter Pan", "Return to Never Land",
    "Lady and the Tramp", "Lady and the Tramp II: Scamp's Adventure",
    "Sleeping Beauty", "101 Dalmatians", "101 Dalmatians II: Patch’s London Adventure",
    "The Sword in the Stone", "The Jungle Book", "The Jungle Book 2", "The Aristocats",
    "Robin Hood", "The Rescuers", "The Rescuers Down Under",
    "The Fox and the Hound", "The Fox and the Hound 2", "The Black Cauldron",
    "The Great Mouse Detective", "Oliver & Company", "The Little Mermaid",
    "The Little Mermaid II: Return to the Sea", "The Little Mermaid: Ariel’s Beginning",
    "Beauty and the Beast", "Beauty and the Beast: The Enchanted Christmas", "Belle's Magical World",
    "Aladdin", "The Return of Jafar", "Aladdin and the King of Thieves",
    "The Lion King", "The Lion King II: Simba’s Pride", "The Lion King 1½",
    "Pocahontas", "Pocahontas II: Journey to a New World",
    "The Hunchback of Notre Dame", "The Hunchback of Notre Dame II", "Hercules",
    "Mulan", "Mulan II", "Tarzan", "Tarzan & Jane", "Tarzan II",
    "Fantasia 2000", "The Emperor’s New Groove", "Kronk’s New Groove",
    "Atlantis: The Lost Empire", "Atlantis: Milo’s Return",
    "Lilo & Stitch", "Stitch! The Movie", "Lilo & Stitch 2: Stitch Has a Glitch", "Leroy & Stitch",
    "Treasure Planet", "Brother Bear", "Brother Bear 2", "Home on the Range",
    "Chicken Little", "Meet the Robinsons", "Bolt", "The Princess and the Frog",
    "Tangled", "Winnie the Pooh", "Wreck-It Ralph", "Ralph Breaks the Internet",
    "Frozen", "Frozen II", "Big Hero 6", "Zootopia", "Moana",
    "Raya and the Last Dragon", "Encanto", "Strange World", "Wish"
]

# Combine both lists if you want
all_movies = pixar_movies + disney_movies

# Pick a random one
random_movie = random.choice(all_movies)

# Output it
print("🎬 Tonight’s random Disney+ pick is:")
print(f"👉 {random_movie}")
