# Kata Airways

## Pilots Scheduling Roster

Put on your aviator shades and buckle up for a wild ride as we embark on a mission to schedule the rosters of our
fearless pilots at **Kata Airways**! With flights soaring high and the need to ensure our pilots have some R&R, we need
a top-notch system that can keep up with the demand. Get ready to write some code that'll make scheduling a breeze,
follow the rules and keep our pilots flying happy!

The program should have the following functionality:

- Show the schedule of each pilot
- Allow pilots to request time off
- Approve or deny time off requests for pilots

### Constraints

The program should also have the following rules:

1. Each pilot must have at least one day off in every seven-day period.
2. Each pilot may fly no more than 100 hours in a calendar month.
3. Each pilot must have at least nine hours of rest between flight duties.
4. Each pilot is qualified to switch between the roles of Co-Pilot and Captain.
5. The airline operates flights between the following airports: London (LHR), Los Angeles (LAX), New York (JFK), Paris (
   CDG), Tokyo (HND), Munich (MUC), Rio de Janeiro (GIG), Athens (ATH), Sydney (SYD), and Dubai (DXB).
   a. Flights cannot have the same departure and arrival airport.
6. All flights are on time and there are no delays or cancelled
7. Only one flight per day is allowed to a destination airport
8. The airline has a sufficient number of pilots for all destinations to ensure adequate staffing

You can start by writing test cases for the different functionalities of the system, such as pilots being able to view
their schedule, application being able to approve time off requests, etc.

### Examples

TODO: rules are controversial, and we need to revisit and create one solid example showing adherence to rules for rest &
time-off.

```
-- Week 1 --

Day 1: Off
Day 2: Flight LHR (2022-01-01T14:00:00Z) to SYD (2022-01-01T18:50:00Z), Duration 21h45m
Day 3: Flight SYD (2022-01-01T11:40:00Z) to LHR (2022-01-01T16:30:00Z), Duration 21h45m
Day 4: Off
Day 5: Off
Day 6: Off
Day 7: Off

Total Flight Time / Week: 43h30m
Accumulated Hours: 43h30m
Monthly Hours Remaining: 56h30m

-- Week 2 --

Day 1: Off
Day 2: Off
Day 3: Off
Day 4: Off
Day 7: Flight LHR (2022-01-01T14:00:00Z) to HND (2022-01-01T18:50:00Z), Duration 21h45m
Day 6: Flight HND (2022-01-01T11:40:00Z) to LHR (2022-01-01T16:30:00Z), Duration 21h45m
Day 7: Off

Total Flight Time / Week: 43h30m
Accumulated Hours: 87h00
Monthly Hours Remaining: 13h00m

-- Week 3 --

Day 1: Off
Day 2: Flight LHR (2022-01-01T14:00:00Z) to BER (2022-01-01T18:50:00Z), Duration 1h50m
Flight BER (2022-01-01T11:40:00Z) to LHR (2022-01-01T16:30:00Z), Duration 1h50m
Day 3: Off
Day 4: Flight LDH (2022-01-01T11:40:00Z) to CDG (2022-01-01T16:30:00Z), Duration 1h15m
 Flight CDG (2022-01-01T11:40:00Z) to LDH (2022-01-01T16:30:00Z), Duration 1h15m
Day 5: Flight LDH (2022-01-01T11:40:00Z) to CDG (2022-01-01T16:30:00Z), Duration 1h15m
 Flight CDG (2022-01-01T11:40:00Z) to LDH (2022-01-01T16:30:00Z), Duration 1h15m
Day 6: Off
Day 7: Off

Total Flight Time / Week: 8h40m
Accumulated Hours: 95h40m
Monthly Hours Remaining: 13h00m

-- Week 4 --

Day 1: Flight LDH (2022-01-01T11:40:00Z) to CDG (2022-01-01T16:30:00Z), Duration 1h50m
 Flight CDG (2022-01-01T11:40:00Z) to LDH (2022-01-01T16:30:00Z), Duration 1h50m
Day 2: Off
Day 3: Off
Day 4: Off
Day 5: Off
Day 6: Off
Day 7: Off

Total Flight Time / Week: 3h 40
Accumulated Hours: 99h20m
Monthly Hours Remaining: 40m
```

### Requesting Days Off

John Smith wants to request time off on Day 1. The airline's policy allows a maximum of two consecutive days off, so if
John's request is approved, he will not be able to fly on Days 2 and 3.

The current schedule for John is as follows:

```
Day 1: Off 
Day 2: Flight from London to Paris 
Day 3: Flight from Paris to London # should have day off here anyway because of 2 consecutive fligts
Day 4: Flight from London to New York
```

With John's request for time off on Day 1, the schedule would look like this:

```
Day 1: Off (request approved) 
Day 2: Flight from London to Paris (denied, two consecutive days off not allowed) 
Day 3: Flight from Paris to London (denied, two consecutive days off not allowed) 
Day 4: Flight from London to New York
```

If John requests time off on Day 4, his request will be approved since there are no consecutive flights, and the
schedule would look like this:

```
Day 1: Flight from London to Paris 
Day 2: Flight from Paris to London 
Day 3: Flight from London to New York 
Day 4: Off (request approved)
```

```python
def test_should_show_a_generated_schedule_for_pilots():
    pilots = [
        Pilot("John", "Smith"),
        Pilot("Jane", "Doe"),
        Pilot("Bob", "Johnson"),
    ]

    flights = [
        Flight(
            "LAX", "JFK", "2022-01-01", "Captain",
            FlightTime(start="2022-01-01T14:00:00Z", end="2022-01-01T18:50:00Z")
        ),
        Flight(  # need to calculate rest time and update the timestamps below.
            "JFK", "LAX", "2022-01-02", "Co-pilot",
            FlightTime(start="2022-01-01T11:40:00Z", end="2022-01-01T16:30:00Z")
        ),
        Flight(
            "LHR", "SYD", "2022-01-02", "Co-pilot",
            FlightTime(start="2022-01-01T18:30:00Z", end="2022-01-02T15:45:00Z")
        ),
        Flight(  # need to calculate rest time and update the timestamps below.
            "SYD", "LHR", "2022-01-04", "Captain",
            FlightTime(start="2022-01-04T19:30:00Z", end="2022-01-05T17:15:00Z")
        ),
    ]

    flight_scheduler = FlightScheduler()
    schedule = flight_scheduler.generate_schedule(pilots, flights)

    # Check that the schedule has all the correct pilot names, flight dates, destinations and roles
    assert schedule[0].pilot_name == "John Smith"
    assert schedule[0].flight_date == "2022-01-01"
    assert schedule[0].destination == "JFK"
    assert schedule[0].role == "Captain"

    # Check that the schedule follows the rules such as each pilot having at least one day off in every 7-day period
    # and each pilot can fly no more than 100 hours in a calendar month
    assert schedule_follows_rules(schedule)
```

---

### Features

1. ~~I want to register flights so that they are available for scheduling, as an Admin
    1. ~~Cannot fly from London to London
2. ~~I want to register pilots so that I can schedule them for flights, as an Admin
3. I want to create schedule for flights and pilots, as a Scheduler Program
    1. Each pilot must have at least one day off in every 7-day period
    2. Each pilot must have at least 9 hours of rest between flight duties
    3. You cannot have 2 flights for the same route at the same time
4. I want to request time off so I can stay within my allowed flying time and get enough rest, as a Pilot
    1. I want to deny requested time off, so that Pilot's flying time does not exceed thresholds?, as the scheduler
5. I want to see schedule for me so I can plan my time accordingly, as a Pilot

### Terminology

#### Airport

#### Pilot

#### Schedule

#### FlightTime

#### Airline

> What are we trying to get out of this?
>
> - Domain driven design
> - Software architecture
> - Story writing
> - Event Storming
> - CQRS + ES
> - Use fluent assertions
> - Maybe using ADRs to capture decisions

----
Full Kata

#katalyst
#scheduling
#outside-in-tdd
#system-design
#domain-driven-design

## Pilots Scheduling Roster

Put on your aviator shades and buckle up for a wild ride as we embark on a mission to schedule the rosters of our
fearless pilots at **Kata Airways**! With flights soaring high and the need to ensure our pilots have some R&R, we need
a top-notch system that can keep up with the demand. Get ready to write some code that'll make scheduling a breeze,
follow the rules and keep our pilots flying happy!

**TASK:** The idea is to create a 4-week schedule for each pilot that they can look at and plan their life around.

- Allow pilots to view their upcoming 4-week schedule
- ~~Allow Pilots to view the roster for a given flight~~
- Allow pilots to request time off
- ~~Allow pilots to swap shifts with other pilots~~
- Allow system to approve or deny time off requests
- ~~Send notifications to pilots when a change to their schedule is made~~

### Constraints

The program should also have the following rules:

1. **Rule 1:** Each pilot must have at least one day off in every 7-day period.
2. **Rule 2:** Each pilot can fly no more than 100 hours in a calendar month.
3. **Rule 3:** Each pilot can fly no more than 30 hours in any 7-day period.
4. **Rule 4:** Each pilot must have at least **14 hours of rest** between flight duties for both the captain and co-pilot.
6. **Rule 6:** A pilot cannot be scheduled for more than 3 consecutive flight duties as a captain.
7. **Rule 7:** A pilot cannot be scheduled for more than 5 consecutive flight duties as a co-pilot.
8. **Rule 8:** Pilots can only request time off within a certain time frame before the flight (e.g. 4 weeks)
9. **Rule 9:** Pilots can only swap shifts with other pilots who are scheduled to work on the same flight route.
10. **Rule 10:** Managers can only approve or deny time off requests within a certain time frame before the flight (e.g.
    2 weeks)
11. **Rule 11:** Managers can only view the roster for flights that are scheduled within the next 90 days.
12. **Rule 12:** The airline operates flights between the following airports:
    - London (LHR) - Base
    - Los Angeles (LAX)
    - New York (JFK)
    - Paris (CDG)
    - Tokyo (HND)
    - Munich (MUC)
    - Rio de Janeiro (GIG)
    - Athens (ATH)
    - Sydney (SYD)
    - Dubai (DXB).
    - a. Flights cannot have the same departure and arrival airport.
      **Short <= 2.5, Medium <= 4, Long >= 4**
13. **Rule 13:** All flights are on time and there are no delays or cancelled
14. **Rule 14:** Only one flight per day is allowed to a destination airport
15. **Rule 15:** The airline has a sufficient number of pilots for all destinations to ensure adequate staffing
16. **Rule 16:** Everyone is based in London

An example print out of the schedule looks like this:

##### Captain

```
Week 1:

Day 1:
Departure airport: London (LHR)
Arrival airport: New York (JFK)
Flight time: 7 hours
Rest period before flight: 14 hours

Day 2:
Departure airport: New York (JFK)
Arrival airport: Paris (CDG)
Flight time: 6 hours
Rest period before flight: 14 hours

Day 3:
Departure airport: Paris (CDG)
Arrival airport: Tokyo (HND)
Flight time: 12 hours
Rest period before flight: 14 hours

Day 4:
Off

Day 5:
Departure airport: Tokyo (HND)
Arrival airport: London (LHR)
Flight time: 11 hours
Rest period before flight: 14 hours

Day 6:
Off

Day 7:
Off

Week 2:

Day 1:
Departure airport: London (LHR)
Arrival airport: Rio de Janeiro (GIG)
Flight time: 12 hours
Rest period before flight: 14 hours

Day 2:
Departure airport: Rio de Janeiro (GIG)
Arrival airport: Dubai (DXB)
Flight time: 7 hours
Rest period before flight: 14 hours

Day 3:
Off

Day 4:
Departure airport: Dubai (DXB)
Arrival airport: Athens (ATH)
Flight time: 6 hours
Rest period before flight: 14 hours

Day 5:
Off

Day 6:
Departure airport: Athens (ATH)
Arrival airport: Munich (MUC)
Flight time: 4 hours
Rest period before flight: 14 hours

Day 7:
Off

Week 3:

Day 1:
Departure airport: Munich (MUC)
Arrival airport: Sydney (SYD)
Flight time: 16 hours
Rest period before flight: 14 hours

Day 2:
Off

Day 3:
Departure airport: Sydney (SYD)
Arrival airport: Los Angeles (LAX)
Flight time: 15 hours
Rest period before flight: 14 hours

Day 4:
Off

Day 5:
Departure airport: Los Angeles (LAX)
Arrival airport: New York (JFK)
Flight time: 5 hours
Rest period before flight: 14 hours

Day 6:
Off

Day 7:
Off

Week 4:

Day 1:
Departure airport: New York (JFK)
Arrival airport: Paris (CDG)
Flight time: 6 hours
Rest period before flight: 14 hours

Day 2:
Off

Day 3:
Departure airport: Paris (CDG)
Arrival airport: Munich (MUC)
Flight time: 7 hours
Rest period before flight: 14 hours

Day 4:
Off

Day 5:
Departure airport: Munich (MUC)
Arrival airport: Rio de Janeiro (GIG)
Flight time: 12 hours
Rest period before flight: 14 hours

Day 6:
Off

Day 7:
Off

Note: This schedule is for illustration purposes only and may not adhere to all the constraints and rules mentioned in the kata.
```

##### Co-Pilot

```code

Day 1: Off
Day 2: Flight LHR (2022-01-01T14:00:00Z) to SYD (2022-01-01T18:50:00Z), Duration 21h45m
Day 3: Flight SYD (2022-01-01T11:40:00Z) to LHR (2022-01-01T16:30:00Z), Duration 21h45m
Day 4: Off
Day 5: Off
Day 6: Off
Day 7: Off

Total Flight Time / Week: 43h30m
Accumulated Hours: 43h30m
Monthly Hours Remaining: 56h30m

-- Week 2 --

Day 1: Off
Day 2: Off
Day 3: Off
Day 4: Off
Day 7: Flight LHR (2022-01-01T14:00:00Z) to HND (2022-01-01T18:50:00Z), Duration 21h45m
Day 6: Flight HND (2022-01-01T11:40:00Z) to LHR (2022-01-01T16:30:00Z), Duration 21h45m
Day 7: Off

Total Flight Time / Week: 43h30m
Accumulated Hours: 87h00
Monthly Hours Remaining: 13h00m

-- Week 3 --

Day 1: Off
Day 2: Flight LHR (2022-01-01T14:00:00Z) to BER (2022-01-01T18:50:00Z), Duration 1h50m
Flight BER (2022-01-01T11:40:00Z) to LHR (2022-01-01T16:30:00Z), Duration 1h50m
Day 3: Off
Day 4: Flight LDH (2022-01-01T11:40:00Z) to CDG (2022-01-01T16:30:00Z), Duration 1h15m
 Flight CDG (2022-01-01T11:40:00Z) to LDH (2022-01-01T16:30:00Z), Duration 1h15m
Day 5: Flight LDH (2022-01-01T11:40:00Z) to CDG (2022-01-01T16:30:00Z), Duration 1h15m
 Flight CDG (2022-01-01T11:40:00Z) to LDH (2022-01-01T16:30:00Z), Duration 1h15m
Day 6: Off
Day 7: Off

Total Flight Time / Week: 8h40m
Accumulated Hours: 95h40m
Monthly Hours Remaining: 13h00m

-- Week 4 --

Day 1: Flight LDH (2022-01-01T11:40:00Z) to CDG (2022-01-01T16:30:00Z), Duration 1h50m
 Flight CDG (2022-01-01T11:40:00Z) to LDH (2022-01-01T16:30:00Z), Duration 1h50m
Day 2: Off
Day 3: Off
Day 4: Off
Day 5: Off
Day 6: Off
Day 7: Off

Total Flight Time / Week: 3h 40
Accumulated Hours: 99h20m
Monthly Hours Remaining: 40m
```

Tasklist:

- Reduce the big flight sectors
- Maybe have a base for the airline, this will help reduce the complexity?
    - For example, everyone being based in London

```python
def test_should_show_a_generated_schedule_for_pilots():
    # Given a set of pilots and flights
    pilots = [
        Pilot("John", "Smith", "Captain"),
        Pilot("Jane", "Doe", "Co-Pilot"),
        Pilot("Bob", "Johnson", "Co-Pilot"),
    ]

    flights = [
        Flight("LAX", "JFK", "2022-01-01", "Captain"),
        Flight("JFK", "LAX", "2022-01-02", "Co-pilot"),
        Flight("LAX", "JFK", "2022-01-03", "Captain"),
        Flight("JFK", "LAX", "2022-01-04", "Co-pilot"),
    ]

    # When I generate a schedule
    flight_scheduler = FlightScheduler()
    schedule = flight_scheduler.generate_schedule(pilots, flights)

    # Then the schedule should adhere to all of the above rules
    assert schedule_adheres_to_rules(schedule)
```