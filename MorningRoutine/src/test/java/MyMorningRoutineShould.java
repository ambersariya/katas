import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MyMorningRoutineShould {
    private final PrintStream standardOut = System.out;
    private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();
    private static int currentHour;

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(outputStreamCaptor));
    }

    @AfterEach
    public void tearDown() {
        System.setOut(standardOut);
    }

    @Test
    void print_no_activity_when_hour_is_zero() {
        var myMorningRoutine = new TestableMyMorningRoutine();
        currentHour = 0;
        myMorningRoutine.whatShouldIDoNow();
        assertEquals("No activity", getPrintedOutput());
    }

    @Test
    void print_Do_exercise_when_hour_is_six() {
        var myMorningRoutine = new TestableMyMorningRoutine();
        currentHour = 6;
        myMorningRoutine.whatShouldIDoNow();
        assertEquals("Do exercise", getPrintedOutput());
    }

    @Test
    void print_Read_and_study_when_hour_is_seven() {
        var myMorningRoutine = new TestableMyMorningRoutine();
        currentHour = 7;
        myMorningRoutine.whatShouldIDoNow();
        assertEquals("Read and study", getPrintedOutput());
    }

    private String getPrintedOutput() {
        return outputStreamCaptor.toString().trim();
    }

    @Test
    void print_Have_breakfast_when_hour_is_eight() {
        var myMorningRoutine = new TestableMyMorningRoutine();
        currentHour = 8;
        myMorningRoutine.whatShouldIDoNow();
        assertEquals("Have breakfast", getPrintedOutput());
    }

    private static class TestableMyMorningRoutine extends MyMorningRoutine {
        @Override
        protected int getCurrentHour() {
            return currentHour;
        }
    }
}