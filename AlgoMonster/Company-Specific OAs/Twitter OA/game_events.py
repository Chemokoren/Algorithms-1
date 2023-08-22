"""
(OA) 2021 | Game Events

Two teams are playing a game of football (or soccer if you're from America). After the game, you 
collected a list of events that happened during this game from the judge.

There are four types of events that can happen in a football game: Goal(G), Yellow Card(Y), 
Red Card(R), and Substitution(S). 
The first three events (G, Y, R) are formatted as player time event while the fourth event is 
formatted as player1 time event player2.

A football game has two halves, each 45 minutes long, with a bit of extra time to make up for time 
lost when the game has to pause due to various events. As such, the time field will either be 
represented by an integer (which represents the number of minutes into the game) or time+extra 
(which represents extra minutes granted at the end of each half). For example, 45+3 represents 3 
extra minutes after the first half, which, chronologically speaking, is before the second half.

Unfortunately, the judge messed up the order of the events that happened. All you have is two event
lists in a random order, each representing the events that happened for each team. Your job is to 
merge the two lists into a single list of events and sort them chronologically. For each event in the
merged list, add the team name before the event, followed by a space. 

In case two events happens at the same minute, sort them by event type G, Y, R, S, then by team name,
then by player name (in order, if applicable).

Note: A player's name and a team's name may consist of any alphanumeric characters (A-Z, a-z, 0-9), 
underscore (_), dash (-), and space. For simplicity, no other characters are allowed (sorry X Æ A-12,
we tried our best). No two consecutive characters can be space, either. While numeric characters are 
allowed in names, they are not allowed to be separated from other types of characters and form a word
consisting of only numeric characters. That is, for any substring of a name consisting of only 
numeric digits, either the character before or after the substring (if one exist) must be non-space.

We want to prevent ambiguous inputs like John 36 S Doe 42 G, which could mean either John is 
substituted by Doe 42 G at the 36th minute, or John 36 S Doe scored a goal at the 42nd minute.

For event, the letter corresponds to the event is used (i.e. either G, Y, R, S). The inputs are 
guaranteed to be valid. You do not have to check whether a sequence of football events make sense or
not. That is the judge's job, not yours. You merely need to sort the events according to the order
described above.

Parameters

    team1: A string representing the name of the first team.
    team2: A string representing the name of the second team.
    events1: A list of strings representing the events happened for the first team.
    events2: A list of strings representing the events happened for the second team.

Result

    A list of strings representing the all the events that happened during the game, sorted according
    to the rules described above.

Examples
Example 1:

Input:

team1 = "Home Team"

team2 = "GuestTeam"

events1 = ["Tom 46 Y", "Bob 90+2 G", "John Doe 12 G"]

events1 = ["Alice 24 G", "Alice 45+1 Y", "Jane 80 S xX_N00BSl4y3r_Xx"]

Output: [ "Home Team John Doe 12 G", "GuestTeam Alice 24 G", "GuestTeam Alice 45+1 Y",
 "Home Team Tom 46 Y", "GuestTeam Jane 80 S xX_N00BSl4y3r_Xx", "Home Team Bob 90+2 G" ]

Restrictions

    0 <= len(events1), len(events2) <= 20
    1 <= len(team1), len(team2) <= 50
    1 <= len(player_name) <= 50
    The time of the first half is 1~45 plus extra time, and the time of the second half is 46~90, 
    plus extra time.


"""

from typing import List

def sort_events(team1: str, team2: str, events1: List[str], events2: List[str]) -> List[str]:
    return []

if __name__ == '__main__':
    team1 = input()
    team2 = input()
    events1 = [input() for _ in range(int(input()))]
    events2 = [input() for _ in range(int(input()))]
    res = sort_events(team1, team2, events1, events2)
    for line in res:
        print(line)