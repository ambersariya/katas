export default class Clock {
    todayAsString(): string {
        const d = new Date();
        return d.toISOString().split("T")[0].trim().replace(/-/g, "/");
    }
}
