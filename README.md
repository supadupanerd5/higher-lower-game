# higher-lower-game
START

    DISPLAY "Welcome to the Higher/Lower Game!"
    DISPLAY "I am thinking of a number between 1 and 10."

    SET secret_number = RANDOM NUMBER BETWEEN 1 AND 10
    SET guess = 0

    WHILE guess IS NOT EQUAL TO secret_number

        DISPLAY "Guess a number between 1 and 10."
        INPUT guess

        IF guess IS LESS THAN 1 OR guess IS GREATER THAN 10 THEN
            DISPLAY "Please enter a number between 1 and 10."

        ELSE IF guess IS LESS THAN secret_number THEN
            DISPLAY "Too low! Try a higher number."

        ELSE IF guess IS GREATER THAN secret_number THEN
            DISPLAY "Too high! Try a lower number."

        ELSE
            DISPLAY "Congratulations! You guessed the correct number!"
            DISPLAY "Great job, Bella!"

        END IF

    END WHILE

    DISPLAY "Thanks for playing the Higher/Lower Game!"

END