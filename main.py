# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры

# Цель: Цель этого домашнего задания - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования. Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.

# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod


class Weapon(ABC):
    """
    Абстрактный базовый класс для оружия.
    Определяет интерфейс для всех видов оружия.
    """

    @abstractmethod
    def attack(self, target):
        """
        Абстрактный метод для атаки по цели.

        :param target: объект, по которому наносится атака (экземпляр класса Monster)
        """
        pass

    @property
    @abstractmethod
    def name(self):
        """
        Абстрактное свойство для получения названия оружия.
        """
        pass

    @property
    @abstractmethod
    def damage(self):
        """
        Абстрактное свойство для получения урона, наносимого оружием.
        """
        pass


class Sword(Weapon):
    """
    Класс для оружия 'Меч'.
    """

    def __init__(self):
        self._damage = 25
        self._name = "Меч"

    @property
    def name(self):
        """Название оружия."""
        return self._name

    @property
    def damage(self):
        """Урон оружия."""
        return self._damage

    def attack(self, target):
        """
        Атака мечом по цели.
        """
        print("Атакую мечом!")
        target.take_damage(self.damage)


class Bow(Weapon):
    """
    Класс для оружия 'Лук'.
    """

    def __init__(self):
        self._damage = 15
        self._name = "Лук"

    @property
    def name(self):
        """Название оружия."""
        return self._name

    @property
    def damage(self):
        """Урон оружия."""
        return self._damage

    def attack(self, target):
        """
        Атака луком по цели.
        """
        print("Атакую луком!")
        target.take_damage(self.damage)


class Spear(Weapon):
    """
    Класс для оружия 'Копье'.
    """

    def __init__(self):
        self._damage = 20
        self._name = "Копье"

    @property
    def name(self):
        """Название оружия."""
        return self._name

    @property
    def damage(self):
        """Урон оружия."""
        return self._damage

    def attack(self, target):
        """
        Атака копьем по цели.
        """
        print("Атакую копьем!")
        target.take_damage(self.damage)


class Fighter:
    """
    Класс, представляющий бойца.
    Может менять оружие и атаковать монстра.
    """

    def __init__(self):
        self.weapon = None

    def change_weapon(self, weapon):
        """
        Смена оружия у бойца.

        :param weapon: объект класса Weapon
        """
        self.weapon = weapon
        print("Оружие изменено на", weapon.name)

    def attack(self, target):
        """
        Атака по цели с использованием текущего оружия.

        :param target: объект класса Monster
        """
        if self.weapon is None:
            print("Нет оружия для атаки!")
        else:
            self.weapon.attack(target)


class Monster:
    """
    Класс, представляющий монстра.
    Имеет очки жизни (hit_points) и может получать урон.
    """

    def __init__(self, hit_points):
        """
        :param hit_points: начальное количество очков жизни монстра
        """
        self.hit_points = hit_points

    def take_damage(self, damage):
        """
        Получение урона монстром.

        :param damage: количество урона
        """
        self.hit_points -= damage
        print(f"Монстр получил {damage} урона! Осталось жизней: {self.hit_points}")
        if self.hit_points <= 0:
            print("Монстр побежден!")


# Демонстрация работы игры
monster = Monster(100)
fighter = Fighter()
fighter.change_weapon(Sword())
fighter.attack(monster)
fighter.change_weapon(Bow())
fighter.attack(monster)
fighter.change_weapon(Spear())
fighter.attack(monster)
