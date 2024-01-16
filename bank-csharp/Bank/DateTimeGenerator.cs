namespace Bank;

public abstract class DateTimeGenerator
{
    const string FORMAT_YMD = "yyyy-MM-dd";

    public virtual string Today()
    {
        return DateTime.Today.ToString(FORMAT_YMD);
    }
}