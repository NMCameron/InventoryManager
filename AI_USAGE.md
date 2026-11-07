# AI Usage Report - Homework 1

## Tools Used

OpenAI GPT-6

## How AI Was Used

AI was used to assist with general troubleshooting, and verification of code and instructed to gently guide me to the correct solution.

## Example Prompts

1. "Without solving for me, is there a better way I could handle this error?" — asked about validating menu input using .isdigit() and strip()

2. "Without solving for me, why isnt this function working the way I intend it to?" — Asking for feedback on my initial load_inventory() function and how to read and separate inventory data.

3. "Why am I getting this error?" - Asking about a TypeError I overlooked when accidentally passing two values in, instead of only the required one.

## Suggestions Accepted

Using "while True" loops in add_item to catch errors real time and allow the user to re-enter the name or category if initially invalid.

## Suggestions Rejected or Modified

Many proposed changes were rejected. An example of this was instead of ending an "if statement" with a simple return, GPT suggested to end the statement by returning "True" or "False" to be used in later functions. This was ignored as I saw this as unnecessary for the scope of this project.

## Verification

All AI-asssited code fixes were implemented by hand, and examined closely before implementing. Code was also checked against the project requirements to ensure they were being met, and staying within the scope.

## Code Understanding

1. Handling user choice in main - Embarassingly enough, despite doing this quite a few times before I still mix up the order of using .isdigit() and .strip() along with forgetting the parenthesis for the functions. First we want to strip the input before checking whether or not it is a digit. If it is a digit, we cast it to an int and carry on. If it is not a digit we reject it and `continue` to try again.



# AI Usage Report - Homework 2

## Tools Used

OpenAI GPT-6

## How AI Was Used

AI was used in a similar fashion as before, in an advisory capacity. For troubleshooting, verification, and this time a little help with tests.

## How AI assisted with testing/refactoring

AI was asked to help identify what helper functions may need to be added to ensure each of the seven test conditons were met.

## Example prompt

```
Without implementing them for me, what helper functions do I need to add to be able to test my programs ability to load a file, save a file, search the inventory, remove items from the inventory, update inventory quantity, only add valid items, and get an inventory summary. 
```

## Accepted suggestions

Once thoroughly understood, helper function suggestions were accepted and implemented with verification from AI.

## Rejected suggestions

Many times, instead of creating a helper function, the agent would suggest capsys, monkeypatch, and other imports. As this was a defined limitation and made the project more complicated than necessary, these suggestions were ignored.

## Verification
Just as before, any AI code was implemented by hand, ensuring I knew what was being implemented and why. Any and every test was tested after implementation to ensure nothing broke as a result of it.