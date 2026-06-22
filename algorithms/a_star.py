import heapq
<<<<<<< HEAD
from itertools import count
from puzzle.base_search import BaseSearch
from puzzle.state import GOAL_STATE, State
=======
from puzzle.base_search import BaseSearch
from puzzle.state import State
>>>>>>> e3d78295ec14166dfc6fdeadf55f6ce53772a4c1
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
<<<<<<< HEAD
        """Calcula a distância de Manhattan, ignorando o espaço vazio."""
        goal_positions = {
            tile: divmod(index, 3)
            for index, tile in enumerate(GOAL_STATE)
        }
        distance = 0

        for index, tile in enumerate(state.tiles):
            if tile == 0:
                continue

            row, col = divmod(index, 3)
            goal_row, goal_col = goal_positions[tile]
            distance += abs(row - goal_row) + abs(col - goal_col)

        return distance

    def search(self, initial: State) -> SearchResult:
        tie_breaker = count()
        frontier = [(initial.cost + self.heuristic(initial), next(tie_breaker), initial)]
        best_cost = {initial.tiles: initial.cost}
        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while frontier:
            _, _, state = heapq.heappop(frontier)

            if state.cost > best_cost.get(state.tiles, state.cost):
                continue

            if state.is_goal:
                return SearchResult(
                    solution=state,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=state.cost,
                )

            nodes_expanded += 1

            for child in state.neighbors():
                known_cost = best_cost.get(child.tiles)
                if known_cost is not None and known_cost <= child.cost:
                    continue

                best_cost[child.tiles] = child.cost
                priority = child.cost + self.heuristic(child)
                heapq.heappush(
                    frontier,
                    (priority, next(tie_breaker), child),
                )
                nodes_generated += 1

            max_frontier_size = max(max_frontier_size, len(frontier))

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
        )
=======
        # TODO: implemente a heurística aqui
        raise NotImplementedError

    def search(self, initial: State) -> SearchResult:
        # TODO: implemente o A* aqui
        raise NotImplementedError
>>>>>>> e3d78295ec14166dfc6fdeadf55f6ce53772a4c1
