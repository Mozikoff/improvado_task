from collections import deque


class ExchangeAlternatives:
    rates = {}
    alternatives = []

    def update_rates(self, new_rates):
        self.rates.update(new_rates)

    def show_alternatives(self, value, origin, dest):
        self.alternatives.clear()
        self.search_all_exchange_alternatives(value, origin, dest, set(), self.format_path(origin))
        for path, value in self.alternatives:
            print(path + " {:.3f}".format(value))

    def search_all_exchange_alternatives(self, value, origin, dest, visited, path):
        d = deque()
        d.extend(self.rates[origin])
        visited.add(origin)
        while d:
            cur, rate = d.popleft()
            if cur in visited:
                continue
            if cur == dest:
                self.alternatives.append((path + self.format_path(cur), value * rate))
            else:
                self.search_all_exchange_alternatives(value * rate, cur, dest, visited, path + self.format_path(cur))

    def format_path(self, cur):
        return " -> " + cur


if __name__ == "__main__":
    rates = {
        "RUB": [("USD", 0.02), ("KZT", 7)],
        "KZT": [("USD", 0.002), ("RUB", 0.142)],
        "USD": [("RUB", 50), ("KZT", 500)]
    }
    t = ExchangeAlternatives()
    t.update_rates(rates)
    t.show_alternatives(50, "RUB", "USD")
    # 1 hour (' -> RUB -> USD', 1.0)
