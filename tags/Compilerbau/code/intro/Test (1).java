// javac Test.java
// javap -c -v Test
public class Test
{
    public static void main(String[] args)
    {
        int x = 4;
        int y = 2;
        int z = 3;
        String s = "Das Ergebnis: ";
        System.out.print(s);
        System.out.println(x*(y+z));
    }
}
