-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get a layout of the dataset
.schema
.tables

--GET a layout of the crime_scene_reports table
.schema crime_scene_reports

-- Find description of crime for dates and street.
SELECT description FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street = 'Humphrey Street' ;

-- Read the relevant interviews from the witnesses of the crime
SELECT transcript FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28;

-- Within 10 minutes of 10:15 the thief left ie look at exit number plates
-- Thief withdrew money on Leggett Street street in the morning
-- Thief took earliest flight out of fiftyville follwing day.
-- someone else purchased the ticket

-- Search for number plates exiting around 10:15
SELECT license_plate FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND (minute > 15  AND minute <25)
AND activity = "exit";

-- combine logs and people to get names and of all those who exited the bakery
SELECT name FROM people
JOIN bakery_security_logs
ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND  minute BETWEEN 15 AND 25
AND activity = "exit"
ORDER BY name;

-- locate suspects who drew cash at atm in leggart street
SELECT name FROM people
JOIN atm_transactions
ON bank_accounts.account_number = atm_transactions.account_number
JOIN bank_accounts
ON people.id = bank_accounts.person_id
WHERE transaction_type = 'withdraw'
AND year = 2021
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
ORDER BY name;

-- locate suspects on first flight out of the fiftyvile
-- get the flight id

-- join to get passport number using flight id
SELECT passport_number FROM passengers
JOIN airports ON flights.origin_airport_id = airports.id
JOIN flights ON passengers.flight_id = flights.id
WHERE city = 'Fiftyville'
AND year = 2021
AND month = 7
AND day = 29
AND hour < 9;

-- combine license, withdrawal and flight to get suspect.
SELECT name FROM people
JOIN airports ON flights.origin_airport_id = airports.id
JOIN flights ON passengers.flight_id = flights.id
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE city = 'Fiftyville'
AND year = 2021
AND month = 7
AND day = 29
AND hour < 9
ORDER BY name;


-- Find person who made call
SELECT name FROM people
JOIN phone_calls
ON phone_calls.caller = people.phone_number
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;


-- combine to find the suspect ???
-- /do not know how to sql and get BRUCE
-- Manually compare evidence shows that BRUCe is the criminal


-- find out who helped Bruce
SELECT name FROM people
JOIN phone_calls
ON phone_calls.receiver = people.phone_number
WHERE caller =
(SELECT phone_number FROM people
WHERE name = 'Bruce')
AND year = 2021
AND month = 7
AND day = 28
AND duration < 60 ;



SELECT receiver FROM phone_calls
WHERE caller =
(SELECT phone_number FROM people
WHERE name = 'Bruce')
AND year = 2021
AND month = 7
AND day = 28
AND duration < 60 ;

-- WHERE did they escape to
 SELECT city FROM airports
 JOIN flights
 ON flights.destination_airport_id = airports.id
 JOIN passengers
 ON passengers.flight_id = flights.id
 WHERE passport_number = 5773159633 ;


 SELECT passport_number FROM people
 WHERE name = 'Bruce';