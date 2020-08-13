def rock_paper_scissors(player1, player2):
    output = 0
    if player1 == player2:
        output = 0
    elif player1 == "rock":
        if player2 == "scissors":
            output = 1
        else:
            output = 2
    elif player1 == "paper":
        if player2 == "rock":
            output = 1
        else:
            output = 2
    elif player1 == "scissors":
        if player2 == "paper":
            output = 1
        else:
            output = 2
    return output

# def rock_paper_scissors(player1, player2):
#     output = 0
#     if player1 == player2:
#         output = 0
#     elif player1 == "Rock":
#         if player2 == "Scissors":
#             output = 1
#         else:
#             output = 2
#     elif player1 == "Paper":
#         if player2 == "Rock":
#             output = 1
#         else:
#             output = 2
#     elif player1 == "Scissors":
#         if player2 == "Paper":
#             output = 1
#         else:
#             output = 2
#     return int(output)
#     pass


# def rock_paper_scissors(player1, player2):
#     output = 0
#     if player1 == "Rock":
#         if player2 == "Scissors":
#             output = 1
#         elif player2 == "Paper":
#             output = 2
#         else:
#             output = 0
#     if player1 == "Paper":
#         if player2 == "Rock":
#             output = 1
#         elif player2 == "Scissors":
#             output = 2
#         else:
#             output = 0
#     if player1 == "Scissors":
#         if player2 == "Paper":
#             output = 1
#         elif player2 == "Rock":
#             output = 2
#         else:
#             output = 0
#     return print(int(output))


# player1 = input()
# player2 = input()
# rock_paper_scissors(player1, player2)


# def rock_paper_scissors(player1, player2):
#     output = 0
#     if player1 == "rock":
#         if player2 == "scissors":
#             output = 1
#         elif player2 == "paper":
#             output = 2
#         else:
#             output = 0
#     if player1 == "paper":
#         if player2 == "rock":
#             output = 1
#         elif player2 == "scissors":
#             output = 2
#         else:
#             output = 0
#     if player1 == "scissors":
#         if player2 == "paper":
#             output = 1
#         elif player2 == "rock":
#             output = 2
#         else:
#             output = 0
#     return output
