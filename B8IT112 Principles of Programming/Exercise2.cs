using System;

namespace CA
{
    class Exercise2
    {
        static void Main(string[] args)
        {

            string[] dataRow = new string[1]; //Declaring and initialising the array

            for (int i = 0; i < 1; i++) //Iterating over the array
            {
                Console.WriteLine("Please enter the data row");
                dataRow[i] = Convert.ToString(Console.ReadLine()); //The input will go into the array "dataRow"

                Console.WriteLine("Please enter the delimiter");

                string delimiter = Console.ReadLine(); //Creating the variable delimiter to store any character that we like to use as a delimiter

                foreach (string line in dataRow) //Using a foreach loop and creating a variable "line" to read the data from the array "dataRow"
                {
                    string[] dataValues = line.Split(delimiter); //Declaring and initialising an array to store the data, once is separated by the delimiter

                    foreach (string value in dataValues) //Using a foreach loop and creating the variable "value" to read all the data from the array "dataValues"
                    {

                        Console.WriteLine("{0}", value);

                    }

                }
            }

        }
    }
}
