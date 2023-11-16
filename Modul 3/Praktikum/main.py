from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def movieCount(movies):
    print("Jumlah Film Berdasarkan Genre:")
    counter = {}
    for movie in movies:
        genre = movie["genre"]
        counter[genre] = counter.get(genre, 0) + 1
    return counter

def avgRating(movies):
    print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
    counter = {}
    for movie in movies:
        year = movie["year"]
        counter[year] = counter.get(year, 0) + 1

    movie_rating = reduce(
        lambda year, movie: {
            **year,
            movie["year"]: year.get(movie["year"], 0) + movie["rating"],
        },
        movies,
        {}
    )

    avg_rating = {year: movie_rating[year] / counter[year] for year in movie_rating}
    return avg_rating

def highestRating(movies, movie_key):
    print("Film dengan Rating Tertinggi:\n")
    max_rating = max(movies, key=movie_key)
    return max_rating

def getRating(movie):
    return movie["rating"]

def searchMovie(movies):
    query = input("Masukkkan judul film yang ingin dicari: ")
    query_result = filter(lambda x: x["title"].lower() == query.lower(), movies)
    if query_result:
        return list(query_result)
    else:
        return None
    
def movieData(movie):
    print("Informasi Film: ", movie["title"])
    print("Rating: ", movie["rating"])
    print("Tahun Rilis: ", movie["year"])
    print("Genre: ", movie["genre"])

def menu():
    while (0 < 1):
        print("Pilih tugas yang ingin di lakukan")
        print("1. Menghitung jumlah film berdasarkan genre")
        print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
        print("3. Menemukan film dengan rating tertinggi")
        print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
        print("5. Selesai")
        choose = input("Masukkan nomor tugas (1/2/3/4/5): ")
        if choose == "1":
            print(movieCount(movies))
        elif choose == "2":
            print(avgRating(movies))            
        elif choose == "3":
            kinoMovie = highestRating(movies, getRating)
            movieData(kinoMovie)
        elif choose == "4":
            movie_search = searchMovie(movies)
            print("\n")
            if movie_search:
                movieData(movie_search[0])
            else: 
                print("Film dengan judul tersebut tidak ditemukan.")
        elif choose == "5":
            break
        else:
            print("Invalid input\n")
        print("\n")

def main():
    menu()


if __name__ == "__main__":
    main()