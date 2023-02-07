# A5: Legs in Air

## What Does It Do
A four-legged, four-armed robot is spawned. It tries to get unto its head using only its legs, such that its legs are in the air.

## How Did I Do It
I used a parallel hill climber optimization method to "evolve" the robots over generations. I included a simple sinusoidal pattern generator to evolve a different walking gait in the robots. I also adjusted the fitness function to allow evolution that caused the robot to land on its head

## How Can You Replicate It
1. Clone the repository.
2. Modify the ```constants.py``` folder to observe evolution after ```numberOfGenerations``` generations.
3. Run the ```search.py``` file .
   - **Alternatively** type in ```python3 search.py GUI``` into the terminal after navigating to the source folder.

## Get More Information
- [Ludobots MOOC](https://www.reddit.com/r/ludobots/wiki/finalproject/)
- [Video showing Evolution](https://www.youtube.com/watch?v=yeb4aDyHc9s&list=PLrKF7RjvM_gn4lMEKNgkdVZTz8rV0q325&index=15)
