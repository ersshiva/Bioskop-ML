from load_data import load_data

f1 = "../dataset/ratings.dat"
f2 = "../dataset/users.dat"
f3 = "../dataset/movies.dat"
l1 = load_data(f1, f2, f3)

l1.initialize_mdb()
l1.initialize_rdb()
l1.initialize_udb()