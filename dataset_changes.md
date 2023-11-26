# Dataset changes

## Players

- New attr BMI = weight / height^2
- weight and height removed 
- firstseason, lastseason removed (all zeros)

## Teams + Teams_Post

- Removed homeW, awayW (sum = won) and homeL awayL (sum = lost)
- New attr winRatio = (won + confW) / (GP + confW + confL)
- Removed won, GP, confW, confL
- Losses can be derived from winRatio, so removed lost
- semis, finals and firstRound transformed into booleans

## Coaches

- New attr coachWinRatio = won / (won + lost) and postCoachWinRatio = post_wins / (post_wins + post_losses)
- Removed won, lost, post_wins, post_losses

# Awards

- 

