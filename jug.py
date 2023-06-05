class Container:
    name: str = ""
    _volume: int = 0
    _current_volume: int = 0
    pour_out: int = 0

    def pour_out_liquid(self) -> int:
        if self._current_volume > 0:
            self._current_volume -= self.pour_out
            return self.pour_out
        else:
            print(f"{self.name} пуст")
            return 0

    def pour_liquid(self, volume: int) -> None:
        need_water: int = self._volume - self._current_volume - volume
        if self._current_volume < self._volume:
            self._current_volume += need_water
            if volume > need_water:
                print(f"{self.name} полон, пролито {volume - need_water}")
        else:
            print(f"{self.name} полон, пролито {volume - need_water}")

    def info(self):
        print(f"{self.name} = {self._current_volume}")


class Jug(Container):
    name: str = "Jug"
    _volume: int = 1000
    _current_volume: int = 600
    pour_out: int = 100


class Glass(Container):
    name: str = "Glass"
    _volume: int = 300
    _current_volume: int = 0
    pour_out: int = 50


def main() -> None:
    jug = Jug()
    glass = Glass()
    i = 0
    while i < 15:
        jug.info()
        glass.info()

        glass.pour_liquid(jug.pour_out_liquid())

        i += 1


if __name__ == "__main__":
    main()
