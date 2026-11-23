DISPLAY "Welcome to the Higher/Lower Guessing Game!"

DISPLAY "Enter the lower bound:"
INPUT lower_bound

DISPLAY "Enter the upper bound:"
INPUT upper_bound

WHILE lower_bound >= upper_bound
    DISPLAY "Invalid range. The lower bound must be less than the upper bound."
    DISPLAY "Enter the lower bound:"
    INPUT lower_bound

    DISPLAY "Enter the upper bound:"
    INPUT upper_bound
END WHILE

SET secret_number = RANDOM NUMBER BETWEEN lower_bound AND upper_bound

DISPLAY "I am thinking of a number between", lower_bound, "and", upper_bound

DISPLAY "Enter your guess:"
INPUT guess

WHILE guess < lower_bound OR guess > upper_bound
    DISPLAY "Invalid guess. Enter a number within the selected range."
    INPUT guess
END WHILE

WHILE guess != secret_number

    IF guess < secret_number THEN
        DISPLAY "Higher! Try again."

    ELSE
        DISPLAY "Lower! Try again."
    END IF

    DISPLAY "Enter your next guess:"
    INPUT guess

    WHILE guess < lower_bound OR guess > upper_bound
        DISPLAY "Invalid guess. Enter a number within the selected range."
        INPUT guess
    END WHILE

END WHILE

DISPLAY "Congratulations! You guessed the correct number!"