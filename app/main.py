class Animal:

    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        info_anim = f"Name: {self.name}," \
                    f" Health: {self.health}," \
                    f" Hidden: {self.hidden}"
        return "{" + f"{info_anim}" + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Animal) -> None:
        if isinstance(victim, Herbivore) and victim.hidden is False:
            victim.health -= 50
        if victim.health <= 0:
            Animal.alive.remove(victim)
