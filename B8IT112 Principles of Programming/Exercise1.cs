using System;

namespace CA //For this asignment I'm going to use the camelCase convention
{
    class Exercise1
    {
        static void Main(string[] args)
        {
            //Creating some of the variables
            string employeeName;
            string employeeNumber;
            string weekEnding;
            decimal hoursNormal = 37.50M;
            decimal hoursWorked;
            decimal totalPay;
            decimal netPay;
            decimal totalDeductions;

            //Input of data

            Console.WriteLine("Enter Your Name:"); //Employee name will be stored in employeeName
            employeeName = (Console.ReadLine());

            Console.WriteLine("Enter Your Employee Number:"); //Employee number will be stored in employeeNumber
            employeeNumber = (Console.ReadLine());

            Console.WriteLine("Enter the Week Ending:"); //Week Ending will be stored in weekEnding
            weekEnding = (Console.ReadLine());

            Console.WriteLine("Enter the Hours Worked:"); //Entering the total of hours worked it will be saved in hoursWorked
            hoursWorked = decimal.Parse(Console.ReadLine());


            Console.WriteLine("Enter the Hourly Rate:"); //Hourly Rate being asked to be stored in hourlyRate
            decimal hourlyRate = decimal.Parse(Console.ReadLine());

            Console.WriteLine("Enter the Overtime Rate:"); //Entering the overtime rate which is 1.5 this rate is being multiplied by hourlyRate and being stored in overtimeRate
            decimal overtimeRate = decimal.Parse(Console.ReadLine()) * hourlyRate;

            Console.WriteLine("Enter the Standard Tax Rate:"); //Entering the standard tax rate and dividing it by 100
            decimal standardTaxRate = decimal.Parse(Console.ReadLine()) / 100;

            Console.WriteLine("Enter the Overtime Tax Rate"); //Entering the overtime tax rate and dividing it by 100
            decimal overtimeTaxRate = decimal.Parse(Console.ReadLine()) / 100;

            //Some calculations

            decimal hoursOvertime = hoursWorked - 37.5M; //Here we are getting how many hours Mark as in overtime worked

            totalPay = (hoursNormal * hourlyRate) + (hoursOvertime * overtimeRate); //Total pay is being calculated in other words this is the gross pay or pay before tax

            totalDeductions = (hoursNormal * hourlyRate * standardTaxRate) + (hoursOvertime * overtimeRate * overtimeTaxRate); //Here we are calculating how much of Mark salary is going to revenue

            netPay = totalPay - totalDeductions; //Finally that's the figure that Mark will see in his bank account




            //This piece of code will print out the Payslip note that it will only work with the data given in the exercise, other data introduced will change the overview of the Payslip and may not seem aligned
            Console.WriteLine("                               PAYSLIP ");
            Console.WriteLine("WEEK ENDING  {0} ", weekEnding);
            Console.WriteLine("Employee:  {0} ", employeeName);
            Console.WriteLine("Employee Number:  {0}", employeeNumber);
            Console.WriteLine("                       Earnings               Deductions ");
            Console.WriteLine("                       Hours  Rate   Total                         ");
            Console.WriteLine("Hours (normal)         {0:0.00}  {1:0.00}  {2:0.00}   Tax @ 20% {3:0.00}", hoursNormal, hourlyRate, hoursNormal * hourlyRate, hoursNormal * hourlyRate * standardTaxRate);
            Console.WriteLine("Hours (overtime)       {0:0.00}   {1:0.00}   {2:0.00}   Tax @ 50% {3:0.00}\n", hoursOvertime, overtimeRate, hoursOvertime * overtimeRate, hoursOvertime * overtimeRate * overtimeTaxRate);
            
            Console.WriteLine("                       Total pay:                      {0:0.00}", totalPay);
            Console.WriteLine("                       Total deductions:               {0:0.00}", totalDeductions);
            Console.WriteLine("                       Net pay:                        {0:0.00}", netPay);




        }
    }
}
