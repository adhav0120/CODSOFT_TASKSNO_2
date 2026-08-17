# Tic-Tac-Toe AI: Game Theory & Search Algorithms

This document provides an educational overview of the concepts and algorithms used to make the Tic-Tac-Toe AI completely unbeatable.

---

## 1. The Game Tree

Tic-Tac-Toe is a **zero-sum game** of **perfect information**. Because every state of the board and all possible moves are fully known to both players, we can represent the game structure as a **Game Tree**:

- **Root Node**: The current state of the board.
- **Branches/Edges**: All legal moves a player can choose from that state.
- **Leaf Nodes**: The terminal states where the game has ended (either a player has won, lost, or the board is full, resulting in a draw).

For a complete game of Tic-Tac-Toe, the total state space is relatively small (at most $9!$ or $362,880$ nodes). However, for games like Chess ($10^{120}$) or Go ($10^{360}$), the tree is too large to fully search, requiring heuristic truncation.

---

## 2. The Minimax Algorithm

Minimax is a recursive backtracking algorithm used in game theory to determine the optimal move for a player, assuming the opponent is also playing optimally.

The two players are designated as:
- **Maximizer (AI)**: Aims to select the move that results in the highest possible score.
- **Minimizer (Human)**: Aims to select the move that results in the lowest possible score.

### How it works:
1. From the current state, the algorithm simulates all possible moves recursively until it reaches terminal leaf nodes.
2. It assigns a base utility score to each leaf node:
   - **AI Wins**: $+10$ points
   - **Human Wins**: $-10$ points
   - **Tie Game**: $0$ points
3. As the recursion backtracks up the tree:
   - If it is the **Maximizer's** turn, it passes the **maximum** child score up to the parent.
   - If it is the **Minimizer's** turn, it passes the **minimum** child score up to the parent.
4. The root node eventually receives the minimax value of all possible moves, and the AI selects the move associated with the highest value.

### Depth-Adjusted Heuristic Scoring
To ensure that the AI plays optimally and efficiently (e.g., winning as quickly as possible, or delaying a loss as long as possible), we adjust the utility scores using the search **depth**:
- **AI Wins**: `10 - depth`
  - A win at depth 1 yields a score of `9`.
  - A win at depth 3 yields a score of `7`.
  - Since $9 > 7$, the AI prefers the quicker win.
- **Human Wins**: `-10 + depth`
  - A loss at depth 1 yields a score of `-9`.
  - A loss at depth 3 yields a score of `-7`.
  - Since $-7 > -9$, the AI prefers to stall the game and delay defeat.

---

## 3. Alpha-Beta Pruning Optimization

While a pure Minimax search can easily handle Tic-Tac-Toe, it evaluates many redundant states. **Alpha-Beta Pruning** is an optimization technique that skips evaluating branches that cannot possibly affect the final minimax decision.

It maintains two values throughout the search:
- **Alpha ($\alpha$)**: The best (highest) score that the Maximizer is guaranteed to achieve so far.
- **Beta ($\beta$)**: The best (lowest) score that the Minimizer is guaranteed to achieve so far.

### Pruning Condition:
At any node, if we discover that:
$$\beta \le \alpha$$
This means that the current player can force a worse outcome for the opponent than a previously examined path. The opponent would never allow the game to proceed down this branch. Therefore, we **prune** (stop evaluating) the rest of the branch.

### Search Space Reduction:
- **Worst-Case Complexity**: $O(b^d)$ (same as standard Minimax)
- **Best-Case Complexity**: $O(b^{d/2})$ (evaluates half the depth, doubling search speed and depth capability)
where $b$ is the branching factor and $d$ is the depth of the tree.
