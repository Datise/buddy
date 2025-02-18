## Login and Signup TM

### What are we working on? 

A login + signup system. Basic application. routes are /login and /signup. GETS return the page and POSTS trigger the signup.


### What could go wrong?
1. Forms are injectable (SQL, mass parameter assignment, url injection)
2. Account takeover from non-unique identifiers
3. Account takeover from insufficient password complexity
3. Account takeover from username + password theft over network 
3. Account is phished
5. Session key is not sufficient or changed from DEV
3. Session is not encrypted, leaking info to attacker.
3. Session's store sensitive information
4. Visibility over action issues
3. Brute force login attempts


### What are we going to do?  
- Improve form validation for uniqueness and password complexity.
- Support passkeys or yubikeys
- Support 2FA 
- ensure passwords are sufficiently hashed
- Ensure sensitive parameters are handled only in post body.
- Verify wtform injection handling. Ensure user input is escaped and tested. 
- Verify session functionality
- CodeQL for session storage. 
- Ensure HTTPS upgrade is configured 
- Insufficient logging of user attempts. 
- enforce exponential drop off of login attempts 