#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name,missing-docstring
"""
gamelocker.strings

A collection of mappings between strings returned by the API
and their common names.
Currently Vainglory-specific only.
"""


# this is quite of a hack.
class Stats(dict):
    """A hybrid between `dict` and `object`
       that types :class:`LazyObject`'s to strings."""
    def __typeit(self, obj):
        if isinstance(obj, (tuple, list)):
            l = []
            for o in obj:
                l.append(self.__typeit(o))
            return l
        if isinstance(obj, dict):
            return Stats(obj)
        if isinstance(obj, str):
            return LazyObject(obj)
        return obj

    def __get(self, name):
        # name = LazyObject(name).pretty() # TODO prettify itemUses
        if name in self:
            return self.__typeit(self[name])
        else:
            raise AttributeError("No such attribute: " + name)

    def __getattr__(self, name):
        return self.__get(name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    @property
    def items(self):
        return self.__get("items")

class LazyObject(str):
    """Can be both :class:`Hero` or :class:`Item`."""
    def pretty(self):
        for cls in (Hero, Item):
            prettystr = cls(self).pretty()
            if prettystr != self:
                return prettystr
        return self


class Hero(str):
    heroes = {
        "*Adagio*": "Adagio",
        "*Alpha*": "Alpha",
        "*Ardan*": "Ardan",
        "*Baron*": "Baron",
        "*Blackfeather*": "Blackfeather",
        "*Catherine*": "Catherine",
        "*Celeste*": "Celeste",
        "*Flicker*": "Flicker",
        "*Fortress*": "Fortress",
        "*Glaive*": "Glaive",
        "*Gwen*": "Gwen",
        "*Hero009*": "Krul",
        "*Hero010*": "Skaarf",
        "*Hero016*": "Rona",
        "*Idris*": "Idris",
        "*Joule*": "Joule",
        "*Kestrel*": "Kestrel",
        "*Koshka*": "Koshka",
        "*Lance*": "Lance",
        "*Lyra*": "Lyra",
        "*Ozo*": "Ozo",
        "*Petal*": "Petal",
        "*Phinn*": "Phinn",
        "*Reim*": "Reim",
        "*Ringo*": "Ringo",
        "*Samuel*": "Samuel",
        "*SAW*": "SAW",
        "*Sayoc*": "Taka",
        "*Skye*": "Skye",
        "*Vox*": "Vox"
    }

    def pretty(self):
        if self in self.heroes:
            return self.heroes[self]
        return self


class Item(str):
    items = {
        "Aftershock": "Aftershock",
        "Armor2": "Coat of Plates",
        "Armor3": "Metal Jacket",
        "Armor Shredder": "Bonesaw",
        "Atlas Pauldron": "Atlas Pauldron",
        "AttackSpeed1": "Swift Shooter",
        "AttackSpeed2": "Blazing Salvo",
        "BarbedNeedle": "Barbed Needle",
        "Boots1": "Sprint Boots",
        "Boots2": "Travel Boots",
        "Boots3": "Journey Boots",
        "BreakingPoint": "Breaking Point",
        "Broken Myth": "Broken Myth",
        "Clockwork": "Clockwork",
        "Cogwheel": "Chronograph",
        "Contraption": "Contraption",
        "Cooldown1": "Hourglass",
        "Critical": "Tyrant's Monocle",
        "Crucible": "Crucible",
        "Crystal1": "Crystal Bit",
        "Crystal2": "Eclipse Prism",
        "Crystal3": "Shatterglass",
        "Crystal Matrix": "Alternating Current",
        "Echo": "Echo",
        "EveOfHarvest": "Eve of Harvest",
        "Flare": "Flare",
        "Flaregun": "Flare Gun",
        "Fountain of Renewal": "Fountain of Renewal",
        "Frostburn": "Frostburn",
        "Halcyon Chargers": "Halcyon Chargers",
        "Health2": "Dragonheart",
        "Heavy Prism": "Heavy Prism",
        "Heavy Steel": "Heavy Steel",
        "IronguardContract": "Ironguard Contract",
        "Lifewell": "Lifespring",
        "Light Armor": "Light Armor",
        "Light Shield": "Light Shield",
        "LuckyStrike": "Lucky Strike",
        "Minion Candy": "Minion Candy",
        "MinionsFoot": "Minion's Foot",
        "Mulled Wine": "Halcyon Potion",
        "NullwaveGauntlet": "Nullwave Gauntlet",
        "Oakheart": "Oakheart",
        "PiercingShard": "Piercing Shard",
        "PiercingSpear": "Piercing Spear",
        "PoisonedShiv": "Poisoned Shiv",
        "Protector Contract": "Protector Contract",
        "Reflex Block": "Reflex Block",
        "Scout Trap": "Scout Trap",
        "Serpent Mask": "Serpent Mask",
        "Shield 2": "Kinetic Shield",
        "Shiversteel": "Shiversteel",
        "Six Sins": "Six Sins",
        "SlumberingHusk": "Slumbering Husk",
        "Steam Battery": "Energy Battery",
        "Stormcrown": "Stormcrown",
        "StormguardBanner": "Stormguard Banner",
        "Tension Bow": "Tension Bow",
        "Tornado Trigger": "Tornado Trigger",
        "Void Battery": "Void Battery",
        "War Treads": "War Treads",
        "Weapon3": "Sorrowblade",
        "Weapon Blade": "Weapon Blade"
    }

    item_ids = {
        "*1000_Item_HalcyonPotion*": "Halcyon Potion",
        "*1002_Item_WeaponBlade*": "Weapon Blade",
        "*1003_Item_CrystalBit*": "Crystal Bit",
        "*1004_Item_SwiftShooter*": "Swift Shooter",
        "*1005_Item_SixSins*": "Six Sins",
        "*1009_Item_EclipsePrism*": "Eclipse Prism",
        "*1010_Item_BlazingSalvo*": " Blazing Salvo",
        "*1012_Item_Sorrowblade*": "Sorrowblade",
        "*1013_Item_Shatterglass*": "Shatterglass",
        "*1014_Item_TornadoTrigger*": "Tornado Trigger",
        "*1015_Item_Oakheart*": "Oakheart",
        "*1016_Item_Dragonheart*": "Dragonheart",
        "*1017_Item_LightArmor*": "Light Armor",
        "*1022_Item_CoatOfPlates*": "Coat of Plates",
        "*1024_Item_MetalJacket*": "Metal Jacket",
        "*1025_Item_EnergyBattery*": "Energy Battery",
        "*1026_Item_Hourglass*": "Hourglass",
        "*1027_Item_VoidBattery*": "Void Battery",
        "*1028_Item_Chronograph*": "Chronograph",
        "*1029_Item_Clockwork*": "Clockwork",
        "*1030_Item_SprintBoots*": "Sprint Boots",
        "*1032_Item_TravelBoots*": "Travel Boots",
        "*1034_Item_SerpentMask*": "Serpent Mask",
        "*1035_Item_TensionBow*": "Tension Bow",
        "*1038_Item_Flare*": "Flare",
        "*1039_Item_Bonesaw*": "Bonesaw",
        "*1041_Item_MinionCandy*": "Minion Candy",
        "*1042_Item_Shiversteel*": "Shiversteel",
        "*1043_Item_ReflexBlock*": "Reflex Block",
        "*1044_Item_Frostburn*": "Frostburn",
        "*1045_Item_FountainOfRenewal*": "Fountain of Renewal",
        "*1046_Item_Crucible*": "Crucible",
        "*1047_Item_JourneyBoots*": "Journey Boots",
        "*1049_Item_TyrantsMonocle*": "Tyrant's Monocle",
        "*1050_Item_Aftershock*": "Aftershock",
        "*1052_Item_WeaponInfusion*": "Weapon Infusion",
        "*1053_Item_CrystalInfusion*": "Crystal Infusion",
        "*1054_Item_ScoutTrap*": "Scout Trap",
        "*1055_Item_BrokenMyth*": "Broken Myth",
        "*1056_Item_WarTreads*": "War Treads",
        "*1057_Item_AtlasPauldron*": "Atlas Pauldron",
        "*1059_Item_BookOfEulogies*": "Book of Eulogies",
        "*1060_Item_BarbedNeedle*": "Barbed Needle",
        "*1061_Item_LightShield*": "Light Shield",
        "*1062_Item_KineticShield*": "Kinetic Shield",
        "*1063_Item_Aegis*": "Aegis",
        "*1064_Item_Lifespring*": "Lifespring",
        "*1065_Item_HeavySteel*": "Heavy Steel",
        "*1066_Item_PiercingSpear*": "Piercing Spear",
        "*1067_Item_BreakingPoint*": "Breaking Point",
        "*1068_Item_LuckyStrike*": "Lucky Strike",
        "*1069_Item_AlternatingCurrent*": "Alternating Current",
        "*1070_Item_PiercingShard*": "Piercing Shard",
        "*1071_Item_EveOfHarvest*": "Eve of Harvest",
        "*1072_Item_HeavyPrism*": "Heavy Prism",
        "*1073_Item_IronguardContract*": "Ironguard Contract",
        "*1074_Item_StormguardBanner*": "Stormguard Banner",
        "*1079_Item_Contraption*": "Contraption",
        "*1080_Item_MinionsFoot*": "Minion's Foot",
        "*1084_Item_ProtectorContract*": "Protector Contract",
        "*1087_Item_HalcyonChargers*": "Halcyon Chargers",
        "*1088_Item_Flaregun*": "Flare Gun",
        "*1090_Item_Stormcrown*": "Stormcrown",
        "*1092_Item_PoisonedShiv*": "Poisoned Shiv",
        "*1095_Item_NullwaveGauntlet*": "Nullwave Gauntlet",
        "*1097_Item_Echo*": "Echo",
        "*1105_Item_SlumberingHusk*": "Slumbering Husk"
    }

    def pretty(self):
        if self in self.items:
            return self.items[self]
        if self in self.item_ids:
            return self.item_ids[self]
        return self
