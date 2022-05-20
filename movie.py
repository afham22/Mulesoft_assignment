import sqlite3
def create_table(): #CREATE TABLE 
     c.execute('''create table Movie(movie varchar,actor varchar,actress varchar,
 director varchar,year_of_rel date,Primary Key(movie))''')
     
def insert_data():
    movie=input('Enter the Movie name:\n')
    actor=input('Enter the name of the actor:\n')
    actress=input('Enter the name of the actress:\n')
    director=input('Enter the name of the director:\n')
    year_of_rel=int(input('Enter the year of release:\n'))    
    c.execute('''insert into Movie values(?,?,?,?,?)''',
    (movie.lower(),actor.lower(),actress.lower(),director.lower(),year_of_rel))
    con.commit()
    
def search_data(attribute,search):
    (c.execute('''select * from Movie where '''+attribute+'''=?''',[search]))
    check=c.fetchall()
    if(check==[]):
        print(search+' does not match any '+attribute+' name in database')
    for i in check:
        print("------------")
        print('Movie:'+i[0])
        print('Actor:'+i[1])
        print('Actress:'+i[2])
        print('Director:'+i[3])
        print('Year of release:'+str(i[4]))
   
con=sqlite3.connect('Movie.db')
c=con.cursor()
#create_table() #run only to create database table
while True:
    print("--------Movie Database--------")
    print("1. Insert a new movie")
    print("2. Select a movie")
    print("3. Show all the movies an actor is in")
    print("4. Show all the movies an actress is in")
    print("5. Show all the movies an director as directed")
    print("6. Exit")
    choice = int(input("Enter your choice: \n"))
    if choice ==1:
        insert_data()
    elif choice ==2:
        movie=input("Enter the movie name: \n")
        search_data('movie',movie.lower())
    elif choice ==3:
        actor=input("Enter the actors name: \n")
        search_data('actor',actor.lower())
    elif choice ==4:
        actress=input("Enter the actress name: \n")
        search_data('actress',actress.lower())
    elif choice ==5:
        director=input("Enter the director name: \n")
        search_data('director',director.lower())
    elif choice ==6:
        break
c.close()
con.close()
    




