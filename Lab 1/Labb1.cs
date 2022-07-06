using System;

namespace Labb1
{
    class Program   //Klassens namn 
    {
        static void Main(string[] args) //Main metoden som körs
        {
            Child c = new Child();  //Klassen child blir c och lägger till i klassen
            c.SetName("Garen");  //Set namn
            c.SetLastName("Damacia"); //Set efternamn
            GrandChild gc = new GrandChild("Lux");
            gc.SetLastName("Kaisa");
            GrandChild gc2 = new GrandChild("Lucian");
            GrandChild p = gc + gc2;
            Console.WriteLine(p.GetName());
        }
    }
}