using System;

namespace CA
{
    class Exercise3
    {
        static void Main(string[] args)
        {


            int[] arr1 = new int[100]; //Declaring and initialising the array to store the integers
            int[] fr1 = new int[100]; //Declaring and initialising the array to store frecuencies of integers
            int n, i, j, count;
            

            Console.WriteLine("###################################");
            Console.WriteLine("WELCOME TO THE DBS CONSOLE");
            Console.WriteLine("###################################");
            Console.Write("Input the number of elements to be stored in the array :");
            n = Convert.ToInt32(Console.ReadLine());

            Console.Write("Input {0} elements in the array :\n", n);
            for (i = 0; i < n; i++)
            {
                Console.Write("element - {0} : ", i);
                arr1[i] = Convert.ToInt32(Console.ReadLine());
                fr1[i] = -1;
                
            }
            for (i = 0; i < n; i++)
            {
                count = 1;
                for (j = i + 1; j < n; j++)
                {                  
                    if (arr1[i] == arr1[j])//if check to compare if there is a repeated number in arr1 if there is a match increase the counter by one
                    {                      
                        count++;
                        fr1[j] = 0; //To avoid counting same element again  
                    }
                    
                }

                if (fr1[i] != 0)//When a match has happened this if check is populating the frequency array
                {                  
                    fr1[i] = count;                   
                }
              

            }

            Console.Write("\nThe frequency of all elements of the array : \n");
            for (i = 0; i < n; i++)
            {
                
                if (fr1[i] != 0)//Printing out the results
                {
                    Console.Write("{0} occurs {1} times\n", arr1[i], fr1[i]);
                }


            }


        }
    }
}
