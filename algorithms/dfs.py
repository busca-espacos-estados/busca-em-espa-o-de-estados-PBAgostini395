from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        if depth_limit < 0:
            raise ValueError("O limite de profundidade não pode ser negativo.")
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        frontier = [initial]
        visited = {initial.tiles}
        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while frontier:
            state = frontier.pop()

            if state.is_goal:
                return SearchResult(
                    solution=state,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=state.cost,
                )

            if state.cost >= self.depth_limit:
                continue

            nodes_expanded += 1

            # A inserção reversa faz a pilha visitar os movimentos na mesma
            # ordem definida por State.neighbors().
            for child in reversed(state.neighbors()):
                if child.tiles in visited:
                    continue

                visited.add(child.tiles)
                frontier.append(child)
                nodes_generated += 1

            max_frontier_size = max(max_frontier_size, len(frontier))

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
        )
