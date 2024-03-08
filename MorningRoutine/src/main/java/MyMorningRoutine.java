import java.time.LocalDateTime;

public class MyMorningRoutine implements MorningRoutine {
    public void whatShouldIDoNow() {
        var currentHour = getCurrentHour();
        if (currentHour == 6) {
            System.out.println("Do exercise");
        } else if (currentHour == 7) {
            System.out.println("Read and study");
        } else if (currentHour == 8) {
            System.out.println("Have breakfast");
        } else {
            System.out.println("No activity");
        }
    }

    protected int getCurrentHour() {
        return LocalDateTime.now().getHour();
    }
}
