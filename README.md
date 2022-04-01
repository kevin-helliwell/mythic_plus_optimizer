# mythic_plus_optimizer

Goal: Tells you what M+ dungeon and keystone level to complete next in order to increase your M+ rating.

Based on dungeon score data pulled from Raider.io and/or Blizzard API.

M+ Scoring Rules:

Total Score Calculation Per Dungeon:

Total score (for a given dungeon) = A*(Tyrannical High Score) + B*(Fortified High Score)

A, B determined based on whether Tyrannical or Fortified High Score for a given dungeon is higher.

For example: If your Tyrannical High Score is higher than your Fortified High Score, then A = 1 and B = 0.3333.

If the reverse is true, then A = 0.3333 and B = 1.

How Score Is Calculated Based On Completion/Keystone Level/Affixes:

Completion of a keystone dungeon awards 37.5 score at the lowest level (M+2)

Each keystone level adds an additional 7.5 score.

Each affix adds an additional 7.5 score. **Exception: Seasonal affix adds an additional 15 score.**

Time Bonus/Penalty Scoring Per Dungeon:

Up to an additional 7.5 score can be added for being up to 40% faster than the timer for a given dungeon.

Up to 15 score can be subtracted for being up to 40% slower than the timer for a given dungeon.

Dungeons completed "massively" over the timer for a given dungeon award 0 score.

Source: https://www.wowhead.com/guides/blizzard-mythic-plus-rating-score-in-game
