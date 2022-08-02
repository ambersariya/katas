# password validation

Kata from https://katalyst.codurance.com/password-validation

Design and implement a software that validates a password applying TDD.

The password will be introduced by the user (as an argument of the method) and should return if the password is valid or not.

A valid password should meet the following requirements:

Have more than 8 characters
Contains a capital letter
Contains a lowercase
Contains a number
Contains an underscore

--

We want a method that answers if the password is valid or not.
We don't want to know the reason when the password is invalid (the return value is a boolean)
Design and implement software that can adapt to different password validation rules TDD and focus on the OOP principles.

Let's pretend that now we want to create another type of password validations because on our app we need different type of passwords, such as:

Validation 2:

Have more than 6 characters
Contains a capital letter
Contains a lowercase
Contains a number
Validation 3:

Have more than 16 characters
Contains a capital letter
Contains a lowercase
Contains an underscore
In this iteration, we should try to identify a good abstraction and try to work on OOP principles as well as on design patterns like Builder and Factory

Use object calisthenics.

Now we can know if a password is valid or not, but we cannot understand why, in this iteration, we should be able to return a list of errors for each invalid password, so we could know why the password it's not valid.

Identify how maintainable it's the code that you've built so far, and how it adapts to change, this iteration could change depending on the programming language that you use.

Up untill this point we've been able to create a list of validation rules and validate the password passes all the validation rules, but now we want a new password with the same rules but allowing to fail only one of them.

Validation 4

Have more than 8 characters
Contains a capital letter
Contains a number
Contains an underscore
Examples:

Have more than 8 characters ✅
Contains a capital letter ✅
Contains a number ✅
Contains an underscore ❌
This password it's a valid password

This will help to enforce encapsulation for the lists of rules and have a better design for validation strategies [preventing us from using inheritance], this also could help us work on the Strategy pattern.

Test Driven DevelopmentObject Oriented DesignDesign Patterns
Psst!
Katalyst is in beta and we'd love your feedback.
Email us at katalyst@codurance.com and let us know what you think.
Are you looking for autonomy, mastery and purpose in your career? We are looking for people that share the same values of pragmatism, professionalism and transparency that we do.

Learn more
Codurance Logo
Software is our passion.

We are software craftspeople. We build well-crafted software for our clients, we help developers to get better at their craft through training, coaching and mentoring, and we help companies get better at delivering software.

Company Registration No: 8712584
