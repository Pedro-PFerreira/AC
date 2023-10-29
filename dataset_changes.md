# Dataset changes

## Players

- New attr BMI = weight / height^2
- weight and height removed 
- firstseason, lastseason removed (all zeros)

## Teams + Teams_Post

- New attr winRatio = (homeW + awayW) / GP
- Removed homeW, awayW, GP
- Losses can be derived from winRatio, so removed homeL, awayL
- firstRound removed (all zeros)
