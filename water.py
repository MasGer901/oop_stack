class Container:
    def __init__(self, name: str, volume: int, current_volume: int, pour_out: int = 100) -> None:
        self.__name = name
        self.__volume = volume
        self.current_volume = current_volume
        self.pour_out = pour_out

    def pour_out_liquid(self) -> int:
        if self.current_volume > 0:
            self.current_volume -= self.pour_out
            return self.pour_out
        else:
            print(f"{self.__name} пуст")
            return 0

    def pour_liquid(self, volume: int) -> None:
        need_water: int = self.__volume - self.current_volume - volume
        if self.current_volume < self.__volume:
            self.current_volume += need_water
            if volume > need_water:
                print(f"{self.__name} полон, пролито {volume - need_water}")
        else:
            print(f"{self.__name} полон, пролито {volume - need_water}")

    def info(self):
        print(f"{self.__name} = {self.current_volume}")


def main() -> None:
    jug = Container(name="Jug", volume=1000, current_volume=1000)
    glass = Container(name="Glass", volume=200, current_volume=0, pour_out=50)
    i = 0
    while i < 15:
        jug.info()
        glass.info()

        glass.pour_liquid(jug.pour_out_liquid())

        i += 1


if __name__ == "main":
    main()
