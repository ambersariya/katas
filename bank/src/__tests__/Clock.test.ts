import Clock from "../Clock";

describe("returns todays date as YYYY/MM/DD format", () => {
    test("test with mock of Date", () => {
        const mockDate = new Date("2021-09-30T00:00:00Z");
        jest.spyOn(global, "Date").mockImplementation(
            // @ts-ignore
            () => mockDate
        );

        let clock = new Clock();
        let date = clock.todayAsString();
        expect(date).toBe("2021/09/30");
    });
});
