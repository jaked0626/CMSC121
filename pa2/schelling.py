# This file includes programming assignment 2, Schelling Model of Housing Segregation
#
# Jake Underland, Defne Buyukyazgan
#

"""
CS121: Schelling Model of Housing Segregation

  Program for simulating a variant of Schelling's model of
  housing segregation.  This program takes six parameters:

    filename -- name of a file containing a sample city grid

    R - The radius of the neighborhood: a home at Location (k, l) is in
        the neighborhood of the home at Location (i,j) if 0 <= k < N,
        0 <= l < N, and 0 <= |i-k| + |j-l| <= R.

    similarity_satisfaction_range (lower bound and upper bound) -
         acceptable range for ratio of the number of
         homes of a similar color to the number
         of occupied homes in a neighborhood.

   patience - number of satisfactory homes that must be visited before choosing
              the last one visited.

   max_steps - the maximum number of passes to make over the city
               during a simulation.

  Sample: python3 schelling.py --grid_file=tests/a20-sample-writeup.txt --r=1
         --sim_lb=0.40 --sim_ub=0.7 --patience=3 --max_steps=1
  The sample command is shown on two lines, but should be entered on
  a single line in the linux command-line
"""

import click
import utility

def is_satisfied(grid, R, location, sim_sat_range):
    '''
    Determine whether or not the homeowner at a specific location is
    satisfied using an R-neighborhood centered around the location.
    That is, is does their similarity score fall with the specified
    range (inclusive)

    Inputs:
        grid: the grid
        R (int): neighborhood parameter
        location (int, int): a grid location
        sim_sat_range (float, float): lower bound and upper bound on
          the range (inclusive) for when the homeowner is satisfied
          with his similarity score.
    Returns: 
        satisfied (bool): True if homeowner is satisfied, False otherwise.
    '''

    # Since it does not make sense to call this function on a home
    # that is for sale, we recommend adding an assertion to verify
    # that the home is not for sale
    
    satisfied = False
    i, j = location
    S = 0
    H = 0
    assert grid[i][j] != "F"
    for k in range(i - R, i + R + 1):  # Rows within radius R 
        for l in range(j - R, j + R + 1):  # Columns within radius R 
            if 0 <= k < len(grid) and 0 <= l < len(grid):  
                # For coordinates within radius 
                # R and within range of the grid,
                # see if they meet criteria for neighbor.
                val = abs(i - k) + abs(j - l)
                if val <= R:
                    if grid[k][l] == grid[i][j]: 
                        # Same colored homes
                        S += 1
                        H += 1
                    elif grid[k][l] == "F":  
                        # Vacant homes
                        H += 0
                    else: 
                        # Different colored homes
                        H += 1
    sim_score = S / H
    if sim_sat_range[0] <= sim_score <= sim_sat_range[1]:
        satisfied = True
    return satisfied

def swap(grid, old_location, new_location):
    '''
    Given two locations in a grid, where the former is a colored house
    and the latter is unoccupied ("F"), it swaps the two and alters the
    grid. 

    Inputs: 
        grid: the grid
        old_location (int, int): a grid location
        new_location (int, int): a grid location
    '''
    # House in new location assumes color of house from old location.
    # House in old location becomes vacant.
    i, j = new_location
    k, l = old_location
    grid[i][j] = grid[k][l]
    grid[k][l] = "F"



def relocation(grid, R, location, sim_sat_range, homes_for_sale, patience):
    '''
    Puts an unsatisfied homeowner at a given location through the list 
    of homes_for_sale until the homeowner finds the ith listing that 
    falls within her satisfaction range, where i is equal to patience. 
    If she does, homeowner moves to that location, and her old home is 
    added to the front of the list of homes_for_sale.
    If she does not find a satisfactory home, she remains in her old home.
    This function modifies original grid.

    Inputs:
        grid: the grid
        R (int): neighborhood parameter
        location (int, int): a grid location
        sim_sat_range (float, float): lower bound and upper bound on
          the range (inclusive) for when the homeowner is satisfied
          with her similarity score.
        homes_for_sale (list of tuples): list of coordinates for vacant 
          houses ("F").
        patience (int): number of satisfactory houses homeowner must visit 
          before moving.
    Returns: 
        relocated (bool): True if homeowner moves homes, False otherwise.
    '''
    relocated = False
    visits = 0
    if is_satisfied(grid, R, location, sim_sat_range) == False:
        for h, new_location in enumerate(homes_for_sale):
            swap(grid, location, new_location)
            if is_satisfied(grid, R, new_location, sim_sat_range) == True:
                # Number of satisfactory houses visited increases
                visits += 1
                if visits == patience:
                    # When number of visits equals level of 
                    # patience, homeowner moves permanently. 
                    del homes_for_sale[h]
                    homes_for_sale.insert(0, location)
                    relocated = True
                    break                                       
                else:
                    # If patience does not run out, 
                    # homeowner does not move.
                    swap(grid, new_location, location)
            else: 
                # If vacant house isn't satisfactory,
                # homeowner does not move.
                swap(grid, new_location, location)
    return relocated 
 

def simulate_a_wave(grid, R, sim_sat_range, homes_for_sale, patience, color):
    '''
    Simulates a wave for homeowners of specified color. Wave goes through
    grid and runs relocation function on all homeowners of that color.

    Inputs:
        grid: the grid
        R (int): neighborhood parameter
        sim_sat_range (float, float): lower bound and upper bound on
          the range (inclusive) for when the homeowner is satisfied
          with her similarity score.
        homes_for_sale (list of tuples): list of coordinates for vacant 
          houses ("F").
        patience (int): number of satisfactory houses homeowner must visit 
          before moving.
        color (string): "M" for a Maroon wave and "B" for a Blue wave.
    Returns: 
        wave_moves (int): Number of relocations that occur in the wave.
    '''
    wave_moves = 0
    for k, _ in enumerate(grid): 
        for l, _ in enumerate(grid):
            if grid[k][l] == color:
                # Make sure the wave is focusing on
                # homeowners of a certain color.
                location = (k, l)
                if relocation(grid, R, location, sim_sat_range, homes_for_sale, patience) == True:
                    # Recall that relocation yields a boolean that
                    # tracks whether the homeowner moved or not.
                    wave_moves += 1
    return wave_moves



def simulate_a_step(grid, R, sim_sat_range, homes_for_sale, patience):
    '''
    Simulates a step. Runs Maroon wave and Blue wave consecutively.

    Inputs:
        grid: the grid
        R (int): neighborhood parameter
        sim_sat_range (float, float): lower bound and upper bound on
          the range (inclusive) for when the homeowner is satisfied
          with her similarity score.
        homes_for_sale (list of tuples): list of coordinates for vacant 
          houses ("F").
        patience (int): number of satisfactory houses homeowner must visit 
          before moving.
    Returns: 
        step_moves (int): Number of relocations that occur in the step.
    '''
    # Recall that simulate_a_wave yields number of moves in a wave
    wave_moves_M = simulate_a_wave(grid, R, sim_sat_range, homes_for_sale, patience, "M")
    wave_moves_B = simulate_a_wave(grid, R, sim_sat_range, homes_for_sale, patience, "B")
    step_moves = wave_moves_M + wave_moves_B
    return step_moves






def do_simulation(grid, R, sim_sat_range, patience, max_steps, homes_for_sale):
    '''
    Do a full simulation.

    Inputs:
        grid (list of lists of strings): the grid
        R (int): neighborhood parameter
        sim_sat_range (float, float): lower bound and upper bound on
          the range (inclusive) for when the homeowner is satisfied
          with his similarity score.
        max_steps (int): maximum number of steps to do
        for_sale (list of tuples): a list of locations with homes for sale

    Returns: 
        count_relocation (int): The number of relocations completed.
    ''' 
    count_relocation = 0
    for i in range(max_steps):
        relocations_per_step = simulate_a_step(grid, R, sim_sat_range, homes_for_sale, patience)
        count_relocation += relocations_per_step
        if relocations_per_step == 0:
            # Terminate function when no one relocates in a step.
            break
    return count_relocation


@click.command(name="schelling")
@click.option('--grid_file', type=click.Path(exists=True))
@click.option('--r', type=int, default=1,
              help="neighborhood radius")
@click.option('--sim_lb', type=float, default=0.40,
              help="Lower bound of similarity range")
@click.option('--sim_ub', type=float, default=0.70,
              help="Upper bound of similarity range")
@click.option('--patience', type=int, default=1, help="patience level")
@click.option('--max_steps', type=int, default=1)
def cmd(grid_file, r, sim_lb, sim_ub, patience, max_steps):
    '''
    Put it all together: do the simulation and process the results.
    '''

    if grid_file is None:
        print("No parameters specified...just loading the code")
        return

    grid = utility.read_grid(grid_file)
    for_sale = utility.find_homes_for_sale(grid)
    sim_sat_range = (sim_lb, sim_ub)


    if len(grid) < 20:
        print("Initial state of city:")
        for row in grid:
            print(row)
        print()

    num_relocations = do_simulation(grid, r, sim_sat_range, patience,
                                    max_steps, for_sale)

    if len(grid) < 20:
        print("Final state of the city:")
        for row in grid:
            print(row)
        print()

    print("Total number of relocations done: " + str(num_relocations))

if __name__ == "__main__":
    cmd() # pylint: disable=no-value-for-parameter
