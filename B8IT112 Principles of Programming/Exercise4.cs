using System;

namespace CA
{
    class Exercise4
    {
        static void Main(string[] args)
        {
            //Declaring some variables
            int i;
            
            int enteredMovies = 0;
            Console.WriteLine("###################################");
            Console.WriteLine("WELCOME TO THE DBS CONSOLE");
            Console.WriteLine("###################################");
            Console.WriteLine("Enter number of movies:");
            int num1 = int.Parse(Console.ReadLine());//Declaring num1 to set the lenght of array movies
            string[] movies = new string[num1];//Declaring and initialising 


            for (i = 0; i < num1; i++)//Iterating the array
            {
                Console.WriteLine("Enter movie name:");
                string movie = Console.ReadLine();

                if (movie.Equals("Exit", StringComparison.OrdinalIgnoreCase))//If check to detect "Exit" keyword
                {
                    break;
                }
                else//Iterating and populating the array
                {
                    movies[i] = movie;
                    enteredMovies++;

                }

            }

            for (i = 0; i < enteredMovies; i++)//Printing out the results
            {
                Console.WriteLine("Movie {0} is {1}", i + 1, movies[i]);
            }


        }
    }
}
