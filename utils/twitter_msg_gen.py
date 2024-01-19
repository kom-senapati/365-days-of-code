from random import choice

code_victory_messages = [
    "Hello fellow coders! 🚀 Just conquered #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's victory: Q*",
    "Greetings coding enthusiasts! 🚀 Successfully completed #Day* in the #365DaysofCode Challenge alongside @scaler_official\n🏆 Achievement of the day: Q*",
    "Hey fellow coders! 🚀 Another triumph on #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's win: Q*",
    "Hey coding community! 🚀 Just aced #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Highlight of the day: Q*",
    "Code warriors unite! 🚀 Nailed it on #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's success: Q*",
    "Salutations to the coding realm! 🚀 Marking off #Day* in the #365DaysofCode Challenge with @scaler_official\n🏆 Notable achievement: Q*",
    "Yo coders! 🚀 Crushed #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Key accomplishment: Q*",
    "Hey coding crew! 🚀 Another milestone on #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's triumph: Q*",
    "Code on, comrades! 🚀 Successfully navigated through #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Noteworthy victory: Q*",
    "Greetings to the coding universe! 🚀 Celebrating #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's accomplishment: Q*",
    "Hey coding champs! 🚀 Triumphed on #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's achievement: Q*",
    "Greetings fellow coders! 🚀 Navigated through #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Notable win: Q*",
    "Hello coding world! 🚀 Achieved success on #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's milestone: Q*",
    "Code masters assemble! 🚀 Successfully completed #Day* in the #365DaysofCode Challenge with @scaler_official\n🏆 Victory of the day: Q*",
    "Hey coding comrades! 🚀 Another conquest on #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's triumph: Q*",
    "Salutations, fellow coders! 🚀 Marking off #Day* in the #365DaysofCode Challenge with @scaler_official\n🏆 Noteworthy accomplishment: Q*",
    "Code warriors, rejoice! 🚀 Nailed it on #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's success story: Q*",
    "Yo coders, what's up! 🚀 Crushed #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Key highlight: Q*",
    "Hey coding crewmates! 🚀 Another milestone on #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Today's triumph: Q*",
    "Code on, friends! 🚀 Successfully journeyed through #Day* of the #365DaysofCode Challenge with @scaler_official\n🏆 Notable victory: Q,*"
]

footer = "\n\nJoin the Scaler Discord community now! 🌐🚀 https://www.scaler.com/discord\n#scalerdiscord #codewithscaler #365daysofcodescaler  #365daysofcode"

day = input("\nDay > ")
question_solved = input("Question > ")

print("\nCopy and Post on Twitter :) 👇\n")

msg = (
    choice(code_victory_messages)
    .replace("Day*", f"Day{day}")
    .replace("Q*", question_solved)
    + footer
)

print(msg)
print()
