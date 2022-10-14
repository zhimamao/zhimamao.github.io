import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Tokenizer
{
    public static void main(String[] args)
    {
        Pattern p = Pattern.compile("(a|b)*abb");
        Matcher m = p.matcher(args[0]);
        if(m.matches())
            System.out.println("yes");
        else
            System.out.println("no");
    }
}